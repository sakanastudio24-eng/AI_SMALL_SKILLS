# Design For Testability

Use this reference when the task touches dependency seams, side effects, pure logic, mocks, fixtures, or hard-to-test modules.

## Dependency Injection

External dependencies must enter through explicit boundaries:

- database adapters
- API clients
- clocks
- ID generators
- storage
- queues
- notifications
- feature flags
- environment configuration

Rules:

- Inject dependencies at meaningful system boundaries.
- Avoid service locators and hidden globals.
- Do not inject every trivial pure utility.
- Make production and test implementations satisfy the same contract.
- Keep high-level domain code from constructing low-level infrastructure directly.

Prefer:

```text
policy/orchestrator -> port/interface <- adapter
```

Avoid:

```text
policy imports SQL client, env vars, HTTP client, logger, and vendor SDK directly
```

## Pure Functions

Prefer pure functions for validation, normalization, mapping, policy decisions, state derivation, diagnostic classification, response parsing, and formatting.

A function is not pure if it reads time, environment, network, random state, cache, database, mutable globals, or the filesystem.

## Side Effects

Side effects must be explicit, isolated, named, bounded, and testable. Perform writes, network calls, notification sends, and environment reads at the outer edge of the system.

## Separation Of Concerns

Separate:

- domain decisions
- orchestration
- persistence
- transport
- UI rendering
- state projection
- diagnostics
- authorization
- formatting

A UI component should not independently decide database authority. A database function should not produce presentation copy unless that is an explicit contract.

## Test Seam Check

Before implementation, answer:

- Which pure decisions can be tested without infrastructure?
- Which adapter contracts need controlled real parsing or transport tests?
- Which dependencies must be injected?
- Which dependencies are stable enough to call directly?
- What side effects can fail after a partial success?
