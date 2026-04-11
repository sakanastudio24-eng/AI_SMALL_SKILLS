# Health Endpoint Setup and Best Practices

Last reviewed: 2026-02-21

## What "Proper" Health Endpoints Should Provide

1. Separate liveness from readiness.
2. Keep responses machine-readable and fast.
3. Return clear HTTP semantics:
- `200` when healthy/ready.
- `503` when not ready for traffic.
4. Avoid leaking internal dependency details on public endpoints.
5. Use the same probe paths in orchestrator and load balancer configs.

## Platform Conventions (Source-Backed)

### Kubernetes

- Kubernetes defines probe types for `liveness`, `readiness`, and `startup`.
- Docs explicitly call out each probe type and expected use.
- Source: https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/

### ASP.NET Core

- Official docs show separate endpoints like `/healthz/ready` and `/healthz/live`.
- Readiness can include dependencies; liveness can be a lightweight self-check.
- Source: https://learn.microsoft.com/en-us/aspnet/core/host-and-deploy/health-checks

### Spring Boot Actuator

- Standard health endpoint is `/actuator/health`.
- Kubernetes probe groups are available at `/actuator/health/liveness` and `/actuator/health/readiness`.
- Detailed health info is restricted by config (`show-details` default is `never`).
- Source: https://docs.spring.io/spring-boot/reference/actuator/endpoints.html

### AWS Application Load Balancer

- Health checks use a configured `HealthCheckPath` for HTTP/HTTPS targets.
- Default health check path is `/`.
- Default success matcher is HTTP `200`.
- Source: https://docs.aws.amazon.com/elasticloadbalancing/latest/application/target-group-health-checks.html

### Google Cloud Load Balancing

- HTTP/HTTPS health checks require a request path.
- Default path is `/`.
- Expected HTTP response code for healthy backend is `200`.
- Source: https://cloud.google.com/load-balancing/docs/health-check-concepts

## Response Shape Guidance

No finalized RFC currently governs a universal health JSON schema. The API Health Check draft is widely referenced but expired.

- Draft fields include top-level `status` and optional `checks`.
- Source: https://datatracker.ietf.org/doc/html/draft-inadarei-api-health-check-06

Practical recommendation:

1. Keep public response minimal (`{"status":"pass"}`).
2. Put detailed dependency checks behind auth/internal networks.
3. Keep field names stable so automation can parse consistently.

## Quick Starter Endpoint Set

Use this baseline unless platform conventions require different paths:

- `/livez` -> process is alive.
- `/readyz` -> service is ready for traffic and dependencies.
- `/health` -> optional aggregate summary for humans/tools.

## Common Failure Mapping

- `404/405` on all health paths: endpoint likely missing.
- `5xx` on readiness: dependency failure or misconfigured check.
- Timeout/connection refused: routing/ingress/service process issue.
- TLS verify failures: invalid chain/SAN/expiry.

