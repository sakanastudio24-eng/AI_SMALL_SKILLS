#!/usr/bin/env python3
"""Endpoint and subdomain health auditor.

Checks DNS resolution, TLS certificate validity, and common health endpoints.
Outputs an actionable report and optional JSON payload for automation.
"""

from __future__ import annotations

import argparse
import json
import socket
import ssl
import sys
import time
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from typing import Iterable
from urllib.error import HTTPError, URLError
from urllib.parse import urlparse, urlunparse
from urllib.request import Request, urlopen

DEFAULT_HEALTH_PATHS = [
    "/health",
    "/healthz",
    "/readyz",
    "/livez",
    "/status",
    "/actuator/health",
    "/actuator/health/readiness",
    "/actuator/health/liveness",
]

NON_HEALTHY_KEYWORDS = ["down", "unhealthy", "fail", "error"]
UA = "AI_SKILL_endpoint_health_auditor/1.0"


@dataclass
class EndpointCheck:
    url: str
    status: int | None = None
    latency_ms: int | None = None
    error: str | None = None
    body_preview: str | None = None
    healthy: bool = False


@dataclass
class TargetReport:
    target: str
    normalized_target: str
    dns_ok: bool = False
    dns_error: str | None = None
    tls_checked: bool = False
    tls_ok: bool | None = None
    tls_error: str | None = None
    tls_expires_utc: str | None = None
    tls_days_remaining: int | None = None
    state: str = "unknown"
    reason: str = ""
    next_step: str = ""
    checks: list[EndpointCheck] = field(default_factory=list)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Check endpoint/subdomain health, TLS validity, and missing health routes."
        )
    )
    parser.add_argument(
        "--target",
        action="append",
        default=[],
        help="Target host or URL (repeatable), e.g. api.example.com or https://api.example.com",
    )
    parser.add_argument(
        "--targets-file",
        help="Path to file with one target per line; '#' comments are ignored.",
    )
    parser.add_argument(
        "--paths",
        default=",".join(DEFAULT_HEALTH_PATHS),
        help="Comma-separated health paths to test.",
    )
    parser.add_argument(
        "--timeout",
        type=float,
        default=5.0,
        help="Per-request timeout in seconds (default: 5).",
    )
    parser.add_argument(
        "--warn-days",
        type=int,
        default=21,
        help="TLS expiry warning threshold in days (default: 21).",
    )
    parser.add_argument(
        "--json-out",
        help="Write structured report to a JSON file.",
    )
    return parser.parse_args()


def load_targets(cli_targets: list[str], file_path: str | None) -> list[str]:
    raw: list[str] = list(cli_targets)
    if file_path:
        with open(file_path, "r", encoding="utf-8") as handle:
            for line in handle:
                item = line.strip()
                if not item or item.startswith("#"):
                    continue
                raw.append(item)
    unique = list(dict.fromkeys(raw))
    return unique


def parse_paths(value: str) -> list[str]:
    paths: list[str] = []
    for part in value.split(","):
        token = part.strip()
        if not token:
            continue
        if not token.startswith("/"):
            token = "/" + token
        paths.append(token)
    deduped = list(dict.fromkeys(paths))
    return deduped or list(DEFAULT_HEALTH_PATHS)


def normalize_url(target: str) -> str:
    text = target.strip()
    if "://" not in text:
        text = "https://" + text
    parsed = urlparse(text)
    if not parsed.netloc and parsed.path:
        # Handle malformed values like "https:example.com".
        parsed = urlparse("https://" + parsed.path)
    scheme = parsed.scheme or "https"
    netloc = parsed.netloc
    path = parsed.path or "/"
    return urlunparse((scheme, netloc, path, "", parsed.query, ""))


def host_port(parsed) -> tuple[str, int]:
    host = parsed.hostname or ""
    if parsed.port:
        return host, parsed.port
    if parsed.scheme == "https":
        return host, 443
    return host, 80


def dns_check(host: str) -> tuple[bool, str | None]:
    try:
        socket.getaddrinfo(host, None)
        return True, None
    except OSError as exc:
        return False, str(exc)


def tls_check(host: str, port: int, timeout: float) -> tuple[bool, str | None, str | None, int | None]:
    if port != 443:
        return True, None, None, None
    context = ssl.create_default_context()
    try:
        with socket.create_connection((host, port), timeout=timeout) as sock:
            with context.wrap_socket(sock, server_hostname=host) as tls_sock:
                cert = tls_sock.getpeercert()
        expiry_raw = cert.get("notAfter")
        if not expiry_raw:
            return False, "TLS certificate missing notAfter", None, None
        expiry = datetime.strptime(expiry_raw, "%b %d %H:%M:%S %Y %Z").replace(
            tzinfo=timezone.utc
        )
        days_left = int((expiry - datetime.now(timezone.utc)).total_seconds() // 86400)
        return True, None, expiry.isoformat(), days_left
    except Exception as exc:  # noqa: BLE001
        return False, str(exc), None, None


def candidate_urls(parsed, health_paths: list[str]) -> list[str]:
    base_prefix = parsed.path.rstrip("/")
    scheme = parsed.scheme
    netloc = parsed.netloc
    candidates: list[str] = []

    # Explicit endpoint provided.
    if parsed.path not in ("", "/") and parsed.path in health_paths:
        candidates.append(urlunparse((scheme, netloc, parsed.path, "", parsed.query, "")))
        return candidates

    # Prefix-aware checks for deployments behind path-based routing.
    prefixes = [""]
    if base_prefix and base_prefix != "/":
        prefixes.insert(0, base_prefix)

    for prefix in prefixes:
        for hp in health_paths:
            path = f"{prefix}{hp}" if prefix else hp
            candidates.append(urlunparse((scheme, netloc, path, "", "", "")))

    # If user supplied an explicit non-health path, test it too.
    if parsed.path not in ("", "/") and parsed.path not in health_paths:
        candidates.insert(0, urlunparse((scheme, netloc, parsed.path, "", parsed.query, "")))

    return list(dict.fromkeys(candidates))


def is_healthy_http(status: int, body_preview: str) -> bool:
    if status < 200 or status >= 300:
        return False
    lowered = (body_preview or "").lower()
    return not any(word in lowered for word in NON_HEALTHY_KEYWORDS)


def fetch_url(url: str, timeout: float) -> EndpointCheck:
    start = time.perf_counter()
    req = Request(
        url,
        method="GET",
        headers={
            "User-Agent": UA,
            "Accept": "application/json,text/plain,*/*",
        },
    )
    try:
        with urlopen(req, timeout=timeout) as response:
            body = response.read(400).decode("utf-8", errors="replace").strip()
            latency = int((time.perf_counter() - start) * 1000)
            status = int(response.status)
            return EndpointCheck(
                url=url,
                status=status,
                latency_ms=latency,
                body_preview=body,
                healthy=is_healthy_http(status, body),
            )
    except HTTPError as exc:
        latency = int((time.perf_counter() - start) * 1000)
        body = ""
        try:
            body = exc.read(300).decode("utf-8", errors="replace").strip()
        except Exception:  # noqa: BLE001
            body = ""
        return EndpointCheck(
            url=url,
            status=exc.code,
            latency_ms=latency,
            error=f"HTTP {exc.code}",
            body_preview=body,
            healthy=False,
        )
    except URLError as exc:
        latency = int((time.perf_counter() - start) * 1000)
        return EndpointCheck(
            url=url,
            latency_ms=latency,
            error=f"URL error: {exc.reason}",
        )
    except Exception as exc:  # noqa: BLE001
        latency = int((time.perf_counter() - start) * 1000)
        return EndpointCheck(
            url=url,
            latency_ms=latency,
            error=f"{type(exc).__name__}: {exc}",
        )


def classify(report: TargetReport, warn_days: int) -> None:
    statuses = [c.status for c in report.checks if c.status is not None]
    healthy_hits = [c for c in report.checks if c.healthy]

    if not report.dns_ok:
        report.state = "not_responding"
        report.reason = "DNS resolution failed"
        report.next_step = "Check DNS record, host spelling, and authoritative zone."
        return

    if report.tls_checked and report.tls_ok is False:
        report.state = "tls_invalid_or_expiring"
        report.reason = "TLS validation failed"
        report.next_step = "Fix certificate chain/hostname and re-run checks."
        return

    if healthy_hits:
        if (
            report.tls_checked
            and report.tls_days_remaining is not None
            and report.tls_days_remaining <= warn_days
        ):
            report.state = "tls_invalid_or_expiring"
            report.reason = f"Endpoint healthy but certificate expires in {report.tls_days_remaining} day(s)"
            report.next_step = "Renew certificate, deploy, and verify full chain."
            return
        report.state = "healthy"
        report.reason = f"Healthy response from {healthy_hits[0].url}"
        report.next_step = "Keep this in monitoring and alert on latency/status regressions."
        return

    if statuses:
        if all(code in {404, 405, 501} for code in statuses):
            report.state = "health_endpoint_missing"
            report.reason = "Host responds but common health endpoints are missing"
            report.next_step = (
                "Add liveness and readiness endpoints (for example /livez and /readyz) "
                "and wire them into probes/load balancer checks."
            )
            return
        if any(code >= 500 for code in statuses):
            report.state = "unhealthy"
            report.reason = "Health endpoint returned server-side failures"
            report.next_step = "Inspect service logs and dependency checks; fail readiness until recovered."
            return
        report.state = "unhealthy"
        report.reason = "Endpoint reachable but not healthy"
        report.next_step = "Review response semantics and ensure healthy path returns 200 with minimal payload."
        return

    report.state = "not_responding"
    report.reason = "No HTTP response from tested endpoints"
    report.next_step = "Check network routing, firewall/security groups, ingress, and process uptime."


def run_audit(target: str, health_paths: list[str], timeout: float, warn_days: int) -> TargetReport:
    normalized = normalize_url(target)
    parsed = urlparse(normalized)
    host, port = host_port(parsed)

    report = TargetReport(
        target=target,
        normalized_target=normalized,
    )

    dns_ok, dns_error = dns_check(host)
    report.dns_ok = dns_ok
    report.dns_error = dns_error

    if parsed.scheme == "https":
        report.tls_checked = True
        tls_ok, tls_error, tls_expiry, tls_days = tls_check(host, port, timeout)
        report.tls_ok = tls_ok
        report.tls_error = tls_error
        report.tls_expires_utc = tls_expiry
        report.tls_days_remaining = tls_days

    if report.dns_ok:
        for url in candidate_urls(parsed, health_paths):
            report.checks.append(fetch_url(url, timeout=timeout))

    classify(report, warn_days=warn_days)
    return report


def print_report(reports: Iterable[TargetReport]) -> None:
    reports = list(reports)
    counts: dict[str, int] = {}
    for report in reports:
        counts[report.state] = counts.get(report.state, 0) + 1

    print("Endpoint Health Audit")
    print("====================")
    print(f"Generated at: {datetime.now(timezone.utc).isoformat()}")
    print(f"Targets: {len(reports)}")
    print()
    for state in sorted(counts):
        print(f"- {state}: {counts[state]}")
    print()

    for report in reports:
        print(f"[{report.state}] {report.target}")
        print(f"  reason: {report.reason}")
        print(f"  next:   {report.next_step}")
        if report.dns_error:
            print(f"  dns:    {report.dns_error}")
        if report.tls_checked:
            if report.tls_error:
                print(f"  tls:    {report.tls_error}")
            else:
                print(
                    f"  tls:    ok, expires={report.tls_expires_utc}, days_remaining={report.tls_days_remaining}"
                )
        for check in report.checks:
            status_text = str(check.status) if check.status is not None else "-"
            latency_text = f"{check.latency_ms}ms" if check.latency_ms is not None else "-"
            health_mark = "healthy" if check.healthy else "no"
            err = check.error or ""
            print(f"  check:  {check.url} -> status={status_text} latency={latency_text} healthy={health_mark} {err}".rstrip())
        print()


def main() -> int:
    args = parse_args()
    targets = load_targets(args.target, args.targets_file)
    if not targets:
        print("No targets provided. Use --target or --targets-file.", file=sys.stderr)
        return 2

    paths = parse_paths(args.paths)
    reports = [
        run_audit(target=t, health_paths=paths, timeout=args.timeout, warn_days=args.warn_days)
        for t in targets
    ]
    print_report(reports)

    if args.json_out:
        payload = {
            "generated_at_utc": datetime.now(timezone.utc).isoformat(),
            "health_paths_tested": paths,
            "reports": [asdict(r) for r in reports],
        }
        with open(args.json_out, "w", encoding="utf-8") as handle:
            json.dump(payload, handle, indent=2)
            handle.write("\n")
        print(f"Saved JSON report to {args.json_out}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
