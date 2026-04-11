# Security Boundary Example

## Scenario

An AI agent can open support tickets, read logs, and propose infra changes.

## Guardrails

- no production secret retrieval without human approval
- no destructive infra actions without explicit confirmation
- audit logs required for privileged operations
- treat generated remediation as untrusted until reviewed
