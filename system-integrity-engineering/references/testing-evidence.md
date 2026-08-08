# Testing Evidence

Use this reference for test planning, review claims, mock-heavy suites, hosted proof, manual checks, and closeout wording.

## Evidence Levels

Level 0 - Source/static:

- text assertions
- lint
- type checks
- schema-string checks
- migration-fragment checks

Level 1 - Pure unit:

- pure domain logic without infrastructure

Level 2 - Component or framework test:

- component, controller, view, or service with fake dependencies

Level 3 - Adapter/contract test:

- real parsing or transport adapter logic against controlled responses

Level 4 - Real infrastructure integration:

- real PostgreSQL, filesystem, queue, service emulator, or similar

Level 5 - Cross-service integration:

- real connected boundaries such as API -> PostgREST -> PostgreSQL

Level 6 - Hosted or production-equivalent proof:

- deployed journey against intended environment

Level 7 - User journey/end-to-end proof:

- actual user-visible workflow and resulting authoritative state

## Truthful PASS Rules

Never call:

- source-text SQL assertions database integration
- a Django test client full-stack when downstream calls are mocked
- a test count a quality score
- mocked downstream behavior proof that a real integration works

State:

- what PASS proves
- what PASS does not prove
- which realistic boundaries are missing
- why a focused test was enough, or why a full suite was needed

## Focused Verification

Run focused tests first. Run broad suites when compatibility risk is broad. Use hosted/manual proof only when real environment behavior matters.

## Test Plan Shape

```text
Claim:
Required evidence level:
Available test:
Boundary actually exercised:
Mocked/fake pieces:
What PASS proves:
What PASS does not prove:
Remaining proof:
```
