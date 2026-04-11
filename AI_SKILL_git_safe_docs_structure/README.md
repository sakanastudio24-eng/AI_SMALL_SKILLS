# AI_SKILL_git_safe_docs_structure

## Purpose
Handle documentation and repository-structure changes safely with low-risk git workflow and reviewable history.

## Use When
- reorganizing docs folders
- changing documentation structure
- updating open-source repo docs safely
- planning docs-related branch and PR workflow
- preventing risky file-structure edits

## Do Not Use When
- building unrelated product features
- doing non-docs architecture design
- making endpoint or auth changes unrelated to docs structure

## Inputs Needed
- docs change scope
- repo size or complexity
- current branch state
- target structure pattern
- migration or redirect concerns for moved paths

## Steps
1. Classify the docs or structure change scope.
2. Run preflight safety checks.
3. Choose the correct structure profile.
4. Implement minimal safe commits.
5. Prepare before/after review notes for the PR.

## Output
- docs change plan
- safe git workflow guidance
- structure recommendation
- migration checklist

## Constraints
- never commit secrets or env files
- separate content edits from mass moves when possible
- use tracked renames for moved files
- destructive structure changes require manual review before shipping

## Related Skills
- AI_SKILL_github_commits
- AI_SKILL_architecture
- AI_SKILL_web
