# Service Extraction Plan Example

## Candidate

Notification delivery.

## Why It Can Split

- different throughput profile
- retry and queue semantics
- lower direct coupling to user-facing request latency
- clear interface boundary

## Why It Should Not Split Yet

- if ownership is still the same
- if deployment overhead exceeds current benefit
- if contracts are still changing weekly
