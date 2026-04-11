---
name: endpoint-health-auditor
description: Audit endpoint and subdomain health, TLS validity, and health-check coverage for APIs/services. Use when users ask to test if servers are responding, identify missing health endpoints, diagnose unhealthy dependencies, or generate remediation steps for non-responding services.
---

# Endpoint Health Auditor

## Overview

Run deterministic endpoint checks and produce an actionable report for users and AI agents. Detect DNS/connectivity failures, TLS certificate issues, missing health routes, and unhealthy HTTP responses.

## Workflow

1. Collect targets.
- Accept subdomains, base URLs, or explicit endpoint URLs.
- Prefer HTTPS targets when possible.

2. Run the checker script.
- Execute `scripts/check_endpoints.py` with `--target` and/or `--targets-file`.
- Use `--json-out` when downstream automation needs machine-readable output.

3. Classify results.
- `healthy`: at least one health endpoint returns 2xx.
- `health_endpoint_missing`: host responds but common health routes are missing.
- `unhealthy`: endpoint responds with 5xx or explicit failing payload.
- `tls_invalid_or_expiring`: certificate cannot be validated or expires soon.
- `not_responding`: DNS, timeout, or connection failure.

4. Recommend next actions.
- For missing health routes, propose standard liveness/readiness endpoints.
- For transport failures, separate DNS/TLS/network/app-layer causes.
- For unhealthy dependencies, list failing checks and escalate owners.

5. Validate setup against current best practices.
- Use `references/health-endpoint-setup.md` for probe design and security boundaries.
- Re-check official docs for version-sensitive platform behavior.

## Commands

Check specific targets:
```bash
python3 scripts/check_endpoints.py \
  --target https://api.example.com \
  --target https://auth.example.com \
  --json-out /tmp/endpoint-health.json
```

Check from file:
```bash
python3 scripts/check_endpoints.py \
  --targets-file references/example-targets.txt \
  --timeout 6
```

## Output Requirements

Always include:

1. A one-line status summary per target.
2. Explicit list of missing/non-responding endpoints.
3. Root-cause bucket (`dns`, `tls`, `network`, `http`, `app`).
4. A concrete next step for each failing target.
5. Source-backed guidance when recommending endpoint conventions.

## References

- Health endpoint standards and platform conventions: `references/health-endpoint-setup.md`
- Target list template: `references/example-targets.txt`
