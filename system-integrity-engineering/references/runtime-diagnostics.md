# Runtime Diagnostics

Use this reference when failures are vague, logs are unsafe, runtime behavior is hard to diagnose, or product support needs stable failure codes.

## Diagnostic Goal

A system is not complete when normal product failures require reading raw infrastructure logs.

Create bounded helpers that classify failures into stable codes. Use codebase-appropriate names equivalent to:

- `validateSelection`
- `classifyFailure`
- `describeFailure`
- `isCurrentTransition`
- `createSafeDiagnosticContext`

## A Useful Diagnostic Explains

- what failed
- which boundary failed
- why information cannot be displayed
- whether a mutation occurred
- whether selection was preserved
- safe next action
- whether retry is safe
- whether refresh is appropriate
- whether user support or engineering review is required

## Safe Diagnostic Fields

Diagnostics may include:

- safe request ID
- route
- release SHA
- bounded outcome code
- HTTP status
- booleans about resolution stages
- elapsed time
- one-way reference fingerprints

Diagnostics must not include:

- credentials
- secrets
- cookies
- auth tokens
- raw private IDs
- private content
- notes
- evidence
- request bodies
- unrestricted response bodies

## User-Facing Wording

Do not only say:

```text
Invalid contract
Unavailable
Something went wrong
Action failed
```

when a more exact safe reason is known.

Prefer stable safe language:

```text
The review could not be opened because the server no longer confirms your access to this case.
```

## Closeout Requirement

When changing diagnostics, report:

- stable code added or reused
- sensitive fields excluded
- user-facing message behavior
- where operators can correlate the failure safely
