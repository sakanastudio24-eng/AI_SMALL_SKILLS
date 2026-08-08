# Expected Behavior

Use this as an evaluator checklist after piloting the skill.

## Must Do

- Choose a bounded mode instead of launching a full audit by default.
- Identify source of truth and authority boundaries.
- Reject frontend visibility as authorization proof.
- Distinguish read projections from authoritative mutation commands.
- Classify sensitive data before logging, exposing, or using fixtures.
- State test evidence level and what PASS does or does not prove.
- Prefer smallest contract-restoring repair for defects.
- Preserve existing behavior during refactors.
- Avoid broad speculative abstractions.
- Mention hosted/manual proof gaps when real environment behavior matters.

## Must Not Do

- Recommend GPT-5.6 only because a task is long.
- Treat mocked tests as full integration proof.
- Duplicate business rules across frontend, backend, and SQL.
- Add hidden side effects to pure-looking functions.
- Propose migrations before proving the schema defect.
- Mix a large behavior change with a broad refactor unless inseparable.
- Output large boilerplate matrices when a compact answer is enough.

## Success Signal

The agent should produce a compact, evidence-aware plan or review that points to the first consequential disagreement, not a generic architecture essay.
