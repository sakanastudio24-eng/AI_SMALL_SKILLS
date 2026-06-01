# AI_SKILL_django_rpc_endpoint_workflow

## Canonical ID
`AI_SKILL_django_rpc_endpoint_workflow`

## Status
active

## Category
django / backend api

## Repo Status
linked

## GitHub Repo
`sakanastudio24-eng/AI_SMALL_SKILLS`

## Repo URL
https://github.com/sakanastudio24-eng/AI_SMALL_SKILLS

## Folder Path
`AI_SKILL_django_rpc_endpoint_workflow/`

## Primary Source
https://github.com/sakanastudio24-eng/AI_SMALL_SKILLS/tree/main/AI_SKILL_django_rpc_endpoint_workflow

## Skill File URL
https://github.com/sakanastudio24-eng/AI_SMALL_SKILLS/blob/main/AI_SKILL_django_rpc_endpoint_workflow/SKILL.md

## Created
May 31, 2026

## Last Updated
May 31, 2026

## Purpose
Guide Django RPC-style endpoint work across route design, input validation, auth checks, service boundaries, action semantics, and response contracts.

## Use When
- planning a Django action endpoint
- reviewing RPC-style API handlers
- deciding between CRUD and action routes
- wiring serializers and services for backend actions
- checking auth and ownership on state-changing endpoints

## Do Not Use When
- building purely frontend workflows
- designing framework-agnostic APIs with no Django context
- solving database policy issues outside endpoint behavior

## Inputs Needed
- endpoint goal
- request payload
- auth and role requirements
- side effects
- expected response
- related model or service boundaries

## Steps
1. Classify the endpoint action and decide whether RPC is appropriate.
2. Define method, route, input contract, and output contract.
3. Separate view-level validation from service-level logic.
4. Enforce auth, role, and ownership rules.
5. Plan idempotency, failure handling, and retest behavior.

## Output
- route recommendation
- request and response contract
- auth and permission guidance
- service-boundary recommendation
- failure-mode checklist

## Constraints
- do not hide broad business logic inside the view
- action routes should be explicit and narrow
- state-changing endpoints require server-side permission checks
- avoid combining unrelated actions in one RPC call

## Related Skills
- `AI_SKILL_architecture`
- `AI_SKILL_auth`
- `AI_SKILL_system_design`
