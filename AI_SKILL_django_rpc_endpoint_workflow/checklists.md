# Django RPC Endpoint Checklist

## Contract Checklist
- [ ] Endpoint action is explicit
- [ ] Method matches the action semantics
- [ ] Request payload is validated
- [ ] Response contract is clear
- [ ] Error shape is predictable

## Security Checklist
- [ ] Auth is enforced server-side
- [ ] Role or ownership checks are explicit
- [ ] Sensitive side effects are logged appropriately
- [ ] Idempotency was considered for retries
- [ ] Unsafe fallback behavior is avoided

## Architecture Checklist
- [ ] View logic stays thin
- [ ] Business logic lives in a service or dedicated function
- [ ] Serializer or schema responsibilities are clear
- [ ] Endpoint does not combine unrelated operations
- [ ] Retest path is documented
