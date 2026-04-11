# GitHub Commits Checklists

## Commit Review

- identify behavior changes
- identify refactors
- identify formatting-only edits
- identify dependency changes
- identify generated artifacts
- identify unrelated user changes

## Grouping Rules

- one coherent intent per commit
- lockfile stays with dependency change
- rename-only commit can be separate if it improves review clarity
- broad formatting should not hide behavior changes
- generated output stays out unless required

## PR Readiness

- history tells a clean story
- tests match the behavior changes
- risky areas are called out
- follow-up work is noted explicitly
