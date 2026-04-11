# System Design Checklists

## Requirements

- define primary users
- define critical read and write paths
- define traffic assumptions
- define latency and consistency needs
- define retention and compliance constraints

## Design Review

- source of truth is explicit
- bottlenecks are realistic
- async jobs are used for slow or retryable work
- queue semantics are justified
- caching is tied to a real read or latency need
- failure handling is defined for critical paths

## Reliability

- idempotency exists for retried writes
- observability covers errors and latency
- fallback behavior exists for dependency failure
- operational ownership is clear
