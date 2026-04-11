# Request Flow Example

## Checkout Confirmation Flow

1. Client submits checkout confirmation request.
2. API validates auth, request shape, and idempotency key.
3. Order service writes the transactional update.
4. Outbox or async job records follow-up work.
5. Worker sends receipt and updates read-optimized views.
6. Client receives confirmed status without waiting on non-critical side effects.
