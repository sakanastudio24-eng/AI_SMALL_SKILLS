---
name: system-integrity-engineering
description: Preserve real system behavior while designing architecture, implementing features, integrating APIs/data flows, refactoring, repairing defects, debugging production failures, designing tests, reviewing PRs, planning migrations, authorization, reliability, performance, or system-quality work. Use for consequential engineering changes across frontend, backend, data, state, auth, infrastructure, or tests. Do not trigger a large workflow for trivial comments, wording, renames, formatting, or one-line documentation corrections.
---

# System Integrity Engineering

Use this skill to keep generated engineering work connected to the real system: explicit contracts, authoritative state, safe data handling, realistic tests, and bounded changes.

For meaningful work, start with one short execution line:

```text
Recommended execution: GPT-5.5 High - cross-layer implementation with known architecture.
```

Adjust the model/reasoning only when `references/model-and-token-routing.md` says the task is Low, Medium, or GPT-5.6-worthy.

## First Decision

If the task is only a typo, comment, formatting change, simple rename, or one-line documentation correction, do not run the integrity workflow. Make the small change and close out normally.

Otherwise:

1. Scope the smallest subsystem that can answer the user request.
2. Choose exactly one primary mode below.
3. Load only the reference files needed for that mode.
4. Identify the source of truth, external boundaries, data classification, and test evidence level before claiming completion.
5. Preserve existing behavior unless the user explicitly asked to change it.

## Modes

### Baseline

Use when first entering a project, inherited subsystem, or risky area. Produce only the baseline needed for current work:

- system and ownership map
- dependency seams
- authoritative data sources
- integration boundaries
- data classifications
- runtime failure paths
- test-evidence realism
- highest-risk coupling
- prioritized repair order

Do not perform a full repository audit when a bounded subsystem baseline is enough. After a baseline exists, update only changed facts.

### Design

Use before implementing a new foundation or cross-system capability. Define user-visible behavior, source of truth, state ownership, contracts, dependencies, data classification, authorization, failure behavior, observability, test strategy, compatibility, and rollout.

### Implementation

Use when adding behavior through established contracts and extension seams. Do not redesign unrelated systems. Keep business rules in the authoritative layer, not duplicated across UI, API, and persistence.

### Repair

Use for defects and production failures. Trace the actual failing path and find the first factual disagreement. Prefer the smallest repair that restores the intended contract. Do not add speculative migrations or duplicate business rules.

### Refactor

Use when preserving behavior while improving responsibility boundaries, coupling, testability, readability, replaceability, or runtime diagnostics. Do not mix a large feature with a broad structural rewrite unless technically inseparable.

### Enhancement

Use when adding new behavior to an existing system. Prefer extension points, strategies, handlers, adapters, or focused policies when justified by real variation. Do not create speculative plugin systems for one implementation.

### Review

Use for PR or diff review. Evaluate whether the change preserves contract promises, real system behavior, data boundaries, authority, diagnostics, compatibility, and realistic testing.

## Reference Routing

- For dependency injection, pure functions, seams, and side effects, read `references/design-for-testability.md`.
- For SOLID, module boundaries, and abstraction discipline, read `references/solid-and-modularity.md`.
- For APIs, RPC, queues, webhooks, SDKs, or multi-system handoffs, read `references/integration-contracts.md`.
- For workflows, state machines, stale UI, source-of-truth, or frontend/backend authority, read `references/state-and-authority.md`.
- For production failures, error wording, logging, and safe diagnostic context, read `references/runtime-diagnostics.md`.
- For test plans, proof claims, mocks, hosted/manual proof, and closeout wording, read `references/testing-evidence.md`.
- For fields, logs, API responses, fixtures, prompts, or tool exposure, read `references/data-classification.md`.
- For auth, authorization, ownership, roles, privileged functions, or object access, read `references/security-and-authorization.md`.
- For database/schema changes, migrations, old clients, or compatibility order, read `references/migrations-and-compatibility.md`.
- For timeouts, retries, caching, pagination, rate limits, or performance work, read `references/reliability-and-performance.md`.
- For choosing model/reasoning level and preserving context, read `references/model-and-token-routing.md`.
- For rejecting disconnected or overbuilt AI-generated code, read `references/anti-slop-rules.md`.

## Templates

Use templates only when they reduce ambiguity in the current work:

- `templates/system-baseline.md`
- `templates/integration-contract.md`
- `templates/failure-state-matrix.md`
- `templates/test-evidence-matrix.md`
- `templates/data-classification-matrix.md`
- `templates/repair-plan.md`
- `templates/implementation-closeout.md`

## Definition Of Done

For consequential work, do not mark complete until applicable gates are addressed:

- Behavior: intended user journey works, including loading, success, stale, conflict, failure, and retry states.
- Design: responsibility boundaries are coherent, dependencies are explicit, and extension points are justified.
- Authority: source of truth is explicit, frontend visibility is not authorization, and stale projections do not select mutations.
- Data: fields are classified, outputs are minimized, logs are safe, and sensitive fixtures are synthetic.
- Tests: evidence level is stated, PASS wording is truthful, and missing realistic boundaries are explicit.
- Runtime: meaningful failures have stable diagnostics and safe correlation references.
- Operations: migration/deployment order, rollback or forward repair, and hosted smoke steps are known where applicable.
- Compatibility: existing behavior remains green and direct routes or older clients are considered where relevant.

## Output Format

For substantial tasks, return a compact structure:

1. Recommended execution level.
2. Current behavior and goal.
3. System boundary.
4. Data classification.
5. Design or repair decision.
6. Files/components involved.
7. Test-evidence plan.
8. Runtime diagnostics.
9. Validation.
10. Remaining hosted proof.
11. PASS/BLOCKED.
