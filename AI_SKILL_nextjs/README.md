# AI_SKILL_nextjs

## Canonical ID
`AI_SKILL_nextjs`

## Status
active

## Category
next.js

## Repo Status
linked

## Repo URL
https://github.com/sakanastudio24-eng/AI_SMALL_SKILLS

## Folder Path
`AI_SKILL_nextjs/`

## Created
April 10, 2026

## Last Updated
April 10, 2026

## Purpose
Guide Next.js implementation across app router structure, server and client boundaries, route handlers, data flow, auth callbacks, rendering decisions, and performance-safe patterns.

## Use When
- creating or restructuring routes
- building pages, layouts, and nested flows
- deciding server vs client component boundaries
- adding route handlers or backend-touching logic
- wiring auth callbacks in a Next.js app
- reviewing startup, loading, or rendering issues
- organizing scalable Next.js project structure

## Do Not Use When
- building mobile-only workflows
- designing browser extension-only runtime behavior
- making framework-agnostic architecture decisions with no Next.js impact

## Inputs Needed
- feature or route goal
- route location
- page or component involved
- data requirements
- auth requirements
- rendering needs
- state needs
- performance concerns

## Steps
1. Identify the route, layout, or handler involved.
2. Decide what belongs in server components, client components, and route handlers.
3. Keep data fetching close to the appropriate server boundary when possible.
4. Separate UI structure from backend-touching logic.
5. Review loading, error, empty, and redirect states.
6. Verify auth and callback behavior if sessions or protected routes are involved.
7. Check whether the structure stays modular and scalable.
8. Review performance impact before shipping.

## Output
- Next.js implementation plan
- route and component structure guidance
- server/client boundary recommendation
- route-handler guidance
- rendering and flow checklist

## Constraints
- do not use client components when server components are enough
- avoid mixing too many concerns in a single route or page
- keep auth callbacks and protected flows explicit
- prefer clean app router structure over quick hacks
- preserve modular system design

## Related Skills
- `AI_SKILL_web`
- `AI_SKILL_auth`
- `AI_SKILL_architecture`
- `AI_SKILL_system_design`

## Notes
This skill is especially important for InkVein and other Next.js-based products where routing, auth, and structure are core to the build.
