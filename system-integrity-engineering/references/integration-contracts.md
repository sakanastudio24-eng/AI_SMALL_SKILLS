# Integration Contracts

Use this reference for APIs, RPCs, webhooks, queues, SDKs, browser extension bridges, server actions, database functions, or any consequential boundary between systems.

## Required Contract Fields

Every integration contract must define:

- producer
- consumer
- request shape
- response shape
- version or compatibility policy
- data classification
- authority source
- idempotency behavior
- timeout
- retry rules
- cancellation behavior
- stale behavior
- conflict behavior
- observability
- safe diagnostics
- realistic tests

## Intent Versus Projection

Distinguish:

- intent command
- read projection
- authoritative mutation
- authoritative detail
- user-facing state
- diagnostic feedback

A read projection may describe current state. It must not select a consequential mutation when the real state can change before execution.

Prefer high-level intent:

```text
Review this case
```

over stale frontend branching:

```text
claim -> take over -> renew -> open
```

## Contract Drift Checks

Reject integrations when:

- request and response shapes are implied by examples only
- frontend enums duplicate backend enums without validation
- one side treats optional fields as required
- errors are raw vendor errors with unstable meaning
- retries can duplicate writes
- observability leaks private data
- tests mock the boundary that the change claims to prove

## Minimal Contract Output

When documenting a boundary, include:

```text
Boundary:
Producer:
Consumer:
Command/query:
Authority:
Data classification:
Success:
Known failures:
Retry/idempotency:
Diagnostics:
Proof level:
```
