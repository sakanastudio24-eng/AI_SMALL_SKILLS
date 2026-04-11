# AI_SKILL_github_commits

## Purpose
Organize repository changes into clean commits with messages and history that are easy to review and revert.

## Use When
- splitting mixed diffs into reviewable commits
- improving commit messages
- separating refactors from fixes
- preparing branches for pull requests
- deciding what should stay unstaged

## Do Not Use When
- changing product architecture
- implementing UI behavior
- designing backend systems

## Steps
1. Inspect the diff and classify the kinds of changes.
2. Group files by intent.
3. Keep unrelated work and noisy artifacts out of the commit.
4. Write clear commit messages for each group.
5. Check whether the branch tells a clean PR story.

## Constraints
- keep one intent per commit
- keep lockfiles with their dependency change
- keep generated output out unless required
- do not sweep unrelated user changes into a commit

## Related Skills
- AI_SKILL_architecture
- AI_SKILL_auth
