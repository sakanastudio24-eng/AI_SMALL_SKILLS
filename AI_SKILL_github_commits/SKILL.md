---
name: AI_SKILL_github_commits
description: Structure Git and GitHub changes into clean commits with clear messages, safe staging, and reviewable history. Use when users ask to prepare commits, split changes, improve commit messages, or organize work for pull requests.
---

# AI_SKILL_github_commits

## Overview

Use this skill when the work is not just “commit everything” but making a change history that is easy to review, revert, and understand. Optimize for reviewability, reversibility, and clean pull-request storytelling.

## Execute Workflow

1. Inspect the change set.
- Separate unrelated edits, generated files, and risky mixed-purpose changes.
- Keep user changes intact unless explicitly asked to rewrite them.
- Identify whether the diff contains:
  - behavior changes
  - refactors
  - formatting
  - dependency updates
  - docs
  - tests
  - generated artifacts

2. Group by intent.
- Prefer one commit per coherent change: feature, fix, refactor, docs, or tests.
- Avoid mixing formatting-only edits with behavior changes unless they are inseparable.
- Keep lockfile changes with the dependency change that caused them.
- Keep renames/moves separate from behavior edits when doing so improves review clarity.

3. Stage intentionally.
- Stage the minimum files needed for each commit.
- Keep noisy or unrelated work out of the commit history.
- Do not pull incidental local changes into a commit just to make the working tree clean.

4. Write the commit message.
- Use a concise subject that states what changed and why.
- Prefer messages that help a reviewer understand intent without reading the full diff first.
- Prefer patterns like:
  - `feat(auth): add session expiry handling`
  - `fix(api): reject empty webhook signatures`
  - `refactor(ui): split billing page sections by concern`
  - `docs(repo): clarify local setup steps`

5. Check GitHub readiness.
- Ensure the branch history tells a clean story.
- Call out follow-up commits, test gaps, or risky areas before opening a PR.

## Apply Commit Rules

- One intent per commit.
- Keep refactors behavior-preserving unless the user explicitly wants mixed commits.
- Keep generated code out unless it is required for the build, release, or artifact contract.
- Dependency upgrades belong in their own commit unless tightly coupled to a specific fix.
- Test additions can travel with the behavior change they validate; broad test refactors should be separate.
- Do not rewrite or discard unrelated user changes without explicit approval.

## Output Format

When organizing commits, provide:

1. Proposed commit groups.
2. Files in each group.
3. Commit message for each group.
4. Anything that should remain unstaged for now.
5. PR risks or review notes.

## Output Requirements

Always include:

1. The intended commit grouping.
2. The rationale for each grouping.
3. Any files that should stay out of the current commit.
4. Commit messages that match the grouped intent.
5. Risks from combining or splitting changes incorrectly.
6. Notes for PR readiness when relevant.
