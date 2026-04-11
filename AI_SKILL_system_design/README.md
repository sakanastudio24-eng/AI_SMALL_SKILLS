# AI_SKILL_system_design

## Purpose
Design scalable systems with clear services, data ownership, and realistic operational tradeoffs.

## Use When
- designing backend services
- planning API and data flow
- evaluating queues, workers, or caching
- writing technical design docs
- deciding v1 vs scale-up architecture

## Do Not Use When
- doing page-level frontend design
- organizing git commits
- reviewing auth callback implementation details

## Inputs Needed
- core use case
- traffic and latency assumptions
- read and write patterns
- storage or consistency requirements
- failure and scaling concerns

## Steps
1. Clarify requirements, scale assumptions, and critical paths.
2. Define services, storage, async jobs, and dependencies.
3. Model data ownership and request flow.
4. Identify realistic bottlenecks and failure modes.
5. Recommend a practical v1 and future scale path.

## Output
- system design plan
- service and data flow guidance
- bottleneck and failure analysis
- scale-up checklist

## Constraints
- start with the smallest correct architecture
- add queues and caching only when justified
- define source of truth explicitly
- design idempotency for retried writes and jobs

## Related Skills
- AI_SKILL_architecture
- AI_SKILL_auth
- AI_SKILL_github_commits
