# Reliability And Performance

Use this reference for timeouts, retries, caching, pagination, backpressure, rate limits, repeated calls, performance bugs, and resource cleanup.

## Reliability Review

Check:

- timeout ownership
- bounded retries
- retryable versus non-retryable errors
- cache ownership
- cache invalidation
- deduplication
- pagination
- loading behavior
- cancellation
- backpressure
- rate limits
- request waterfalls
- repeated authorization calls
- failure loops
- memory and resource cleanup

## Retry And Idempotency

Consequential mutations must define:

- idempotency key ownership
- replay result
- conflicting replay result
- transaction boundary
- lock order
- concurrent winner
- rollback behavior
- exactly-once versus at-least-once expectations
- duplicate history protection
- duplicate notification protection

Never automatically retry a mutation after an uncertain result unless the operation is idempotent and the replay behavior is defined.

## Caching Rules

- Do not cache authoritative mutable security decisions unless the contract explicitly allows it.
- Stale caches must fail safely.
- Cache invalidation must have a named owner.
- Performance work must preserve contract correctness.

## Performance Rules

Do not optimize blindly. Measure or identify a concrete pressure point before restructuring code. Prefer removing request waterfalls or repeated boundary calls before adding broad caching.

## Closeout

Report:

- pressure point or failure loop addressed
- timeout/retry behavior
- cache safety
- remaining production measurement gap
