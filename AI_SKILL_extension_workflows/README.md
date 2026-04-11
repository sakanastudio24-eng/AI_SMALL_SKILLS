# AI_SKILL_extension_workflows

## Canonical ID
`AI_SKILL_extension_workflows`

## Status
active

## Category
browser extension

## Repo Status
linked

## Repo URL
https://github.com/sakanastudio24-eng/AI_SMALL_SKILLS

## Folder Path
`AI_SKILL_extension_workflows/`

## Created
April 10, 2026

## Last Updated
April 10, 2026

## Purpose
Guide browser extension work from planning through implementation, debugging, permissions review, UI injection, runtime behavior, and shipping checks.

## Use When
- planning a Chrome extension feature
- deciding extension architecture
- building popup, options, background, or content script flows
- injecting UI into webpages
- debugging extension runtime issues
- reviewing permissions before shipping
- connecting extension behavior to a website or web account system

## Do Not Use When
- building normal website-only features
- designing mobile app flows
- making unrelated backend architecture decisions

## Inputs Needed
- extension goal
- surface involved (popup, content script, background, options, devtools, etc.)
- data source
- permissions required
- whether auth is local-first or web-connected
- expected user flow

## Steps
1. Define the extension surface involved.
2. Identify what runs in content script, background, popup, and web app.
3. Minimize required permissions.
4. Map data flow and source of truth.
5. Define UI behavior for idle, loading, success, error, and disconnected states.
6. Check runtime edge cases across tabs, refreshes, and restricted pages.
7. Review security and privacy implications.
8. Confirm the feature can ship without breaking the host page.

## Output
- extension implementation plan
- surface breakdown
- permission review
- runtime checklist
- UI state checklist
- ship-readiness notes

## Constraints
- permissions should be minimal
- do not overconnect the extension to backend systems too early
- avoid fragile DOM assumptions when injecting UI
- treat the extension as an observer/tool unless the product explicitly requires deeper integration
- keep account sync optional unless already defined as source-of-truth behavior

## Related Skills
- `AI_SKILL_web`
- `AI_SKILL_architecture`
- `AI_SKILL_system_design`
- `AI_SKILL_auth`

## Notes
Best suited for Metis-style extension products and future utility overlays.
