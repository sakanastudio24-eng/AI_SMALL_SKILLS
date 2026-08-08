# Migrations And Compatibility

Use this reference for schema changes, data migrations, storage policies, database functions, API contract changes, old-client compatibility, and deployment ordering.

## Migration Rules

Require:

- forward-only migrations unless the project explicitly allows otherwise
- no rewriting already-applied migrations
- schema and application compatibility order
- old-client compatibility where needed
- data backfill strategy
- rollback or forward-repair strategy
- idempotent deployment behavior
- production-safe diagnostics
- migration parity verification
- runtime proof when SQL behavior matters

A migration source-text test is not runtime migration proof.

Do not create a migration until the exact schema or data-contract defect is proven.

## Compatibility Order

For additive changes, prefer:

1. Add backward-compatible schema or API support.
2. Deploy code that can read old and new shapes.
3. Backfill data if needed.
4. Switch writers.
5. Remove old behavior only after verified compatibility window.

## Review Questions

- Is the migration already applied anywhere?
- Can old code survive the new schema?
- Can new code survive old data?
- What happens if deployment stops between schema and app changes?
- Is the rollback a true rollback or a forward repair?
- Which hosted smoke step proves runtime behavior?

## SQL Proof

When SQL behavior matters, prefer real database proof over text assertions. If real proof is unavailable, state the remaining gap plainly.
