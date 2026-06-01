# AI_SKILL_expo_placeholder_integration_workflow

## Canonical ID
`AI_SKILL_expo_placeholder_integration_workflow`

## Status
active

## Category
expo / mobile placeholder integration

## Repo Status
linked

## GitHub Repo
`sakanastudio24-eng/AI_SMALL_SKILLS`

## Repo URL
https://github.com/sakanastudio24-eng/AI_SMALL_SKILLS

## Folder Path
`AI_SKILL_expo_placeholder_integration_workflow/`

## Primary Source
https://github.com/sakanastudio24-eng/AI_SMALL_SKILLS/tree/main/AI_SKILL_expo_placeholder_integration_workflow

## Skill File URL
https://github.com/sakanastudio24-eng/AI_SMALL_SKILLS/blob/main/AI_SKILL_expo_placeholder_integration_workflow/SKILL.md

## Created
May 31, 2026

## Last Updated
May 31, 2026

## Purpose
Guide temporary Expo placeholder integration across screens, navigation, mock data, auth stubs, and future replacement boundaries without creating avoidable mobile debt.

## Use When
- wiring an unfinished mobile feature into Expo
- adding placeholder screens or flows
- using mock data before backend readiness
- keeping temporary auth or loading states isolated
- planning a future swap from placeholder to real implementation

## Do Not Use When
- building the final production implementation directly
- solving general React Native architecture outside placeholder work
- handling website-only temporary UI

## Inputs Needed
- placeholder feature goal
- affected screens
- navigation path
- temporary data or auth assumptions
- expected replacement source
- shipping or demo constraints

## Steps
1. Define what the placeholder stands in for.
2. Isolate temporary screens, state, and mock assumptions.
3. Wire navigation and states realistically.
4. Define what will later be replaced and how.
5. Validate mobile behavior and shipping caveats.

## Output
- placeholder integration plan
- boundary guidance
- navigation and state notes
- replacement plan
- QA caveats

## Constraints
- placeholder logic should be easy to remove
- do not spread temp state through shared production layers
- user-facing temp behavior should still feel intentional
- back navigation and device behavior should remain correct

## Related Skills
- `AI_SKILL_mobile_workflows_react_native`
- `AI_SKILL_web`
- `AI_SKILL_auth`
