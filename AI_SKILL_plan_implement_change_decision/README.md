# AI_SKILL_plan_implement_change_decision

## Canonical ID
`AI_SKILL_plan_implement_change_decision`

## Status
active

## Category
planning / execution control

## Repo Status
linked

## GitHub Repo
`sakanastudio24-eng/AI_SMALL_SKILLS`

## Repo URL
https://github.com/sakanastudio24-eng/AI_SMALL_SKILLS

## Folder Path
`AI_SKILL_plan_implement_change_decision/`

## Primary Source
https://github.com/sakanastudio24-eng/AI_SMALL_SKILLS/tree/main/AI_SKILL_plan_implement_change_decision

## Skill File URL
https://github.com/sakanastudio24-eng/AI_SMALL_SKILLS/blob/main/AI_SKILL_plan_implement_change_decision/SKILL.md

## Created
May 31, 2026

## Last Updated
May 31, 2026

## Purpose
Guide whether a request should stay in planning, move into implementation, be handled as a review, or be treated as a targeted change request on existing work.

## Use When
- deciding whether work is ready to build
- separating brainstorming from execution
- handling “change this” requests on prior work
- clarifying whether a user wants review versus implementation
- preventing mode drift in multi-part requests

## Do Not Use When
- implementing a specific product feature directly
- doing framework-specific technical design
- reviewing security or auth issues without a mode-choice problem

## Inputs Needed
- user request
- current project state
- whether prior work already exists
- decision blockers or missing constraints
- expected output for this turn

## Steps
1. Identify whether the request is plan, implement, review, or revise.
2. Check whether scope and success criteria are stable enough to execute.
3. Separate net-new work from change requests.
4. State the correct mode explicitly.
5. Define the immediate next step and guardrails.

## Output
- chosen work mode
- reasoning for the mode choice
- blocked decisions or assumptions
- next-step recommendation
- scope boundaries for the turn

## Constraints
- do not mix planning and implementation carelessly
- do not treat unresolved scope as implementation-ready
- change requests should restate the delta clearly
- review requests should default to finding risks first

## Related Skills
- `AI_SKILL_architecture`
- `AI_SKILL_github_commits`
- `AI_SKILL_system_design`
