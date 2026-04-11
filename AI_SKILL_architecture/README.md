# AI_SKILL_architecture

## Purpose
Shape codebase boundaries and ownership so systems stay maintainable as they grow.

## Use When
- reviewing module boundaries
- deciding whether to split services
- cleaning up shared library ownership
- planning refactors across large code areas
- reducing coupling and circular dependencies

## Do Not Use When
- doing endpoint-level API implementation
- solving page-level UI issues
- making infra-only deployment tweaks

## Steps
1. Map current modules, owners, and dependency direction.
2. Identify boundary failures and high-churn areas.
3. Decide what should stay together vs split apart.
4. Define a target shape with explicit ownership.
5. Plan an incremental migration path.

## Constraints
- prefer modular monoliths over service sprawl by default
- do not split systems only for conceptual purity
- keep shared modules narrow and stable
- optimize for change safety, not diagram aesthetics

## Related Skills
- AI_SKILL_system_design
- AI_SKILL_github_commits
