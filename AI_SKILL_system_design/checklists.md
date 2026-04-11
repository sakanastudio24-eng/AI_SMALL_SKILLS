# System Design Checklist

## Pre-ship
- [ ] Core request flow is defined
- [ ] Source of truth is explicit
- [ ] Bottlenecks are realistic
- [ ] Failure handling is defined
- [ ] Idempotency exists for retried writes or jobs

## Edge Cases
- [ ] Dependency outage
- [ ] Duplicate job delivery
- [ ] Read hotspot
- [ ] Partial write failure
- [ ] Queue backlog or retry storm
