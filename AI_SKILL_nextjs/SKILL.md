---
name: AI_SKILL_nextjs
description: Guide Next.js implementation across app router structure, server and client boundaries, route handlers, data flow, auth callbacks, rendering decisions, and performance-safe patterns. Use when users ask about Next.js routes, app router structure, auth callbacks, rendering behavior, or server/client boundaries.
---

# AI_SKILL_nextjs

## Overview

Use this skill for Next.js work involving the app router, server/client separation, route handlers, auth callbacks, rendering choices, and performance-safe project structure.

## Execute Workflow

1. Identify the route, layout, or handler involved.
- Locate the feature in the app router tree.
- Clarify whether the task touches pages, layouts, route handlers, server actions, or auth callbacks.

2. Define server and client boundaries.
- Keep server work on the server when possible.
- Use client components only when browser APIs, interactivity, or client state actually require them.

3. Place data flow correctly.
- Fetch data near the correct server boundary.
- Separate backend-touching logic from UI composition.

4. Review runtime states.
- Define loading, error, empty, redirect, and auth boundary behavior.
- Check protected routes and callback paths explicitly.

5. Validate structure and performance.
- Keep routes modular, layouts intentional, and route handlers narrow.
- Avoid mixing too many responsibilities in one page or route.

## Output Requirements

Always include:

1. Route and file-structure guidance.
2. Server/client boundary recommendation.
3. Data-flow and handler guidance.
4. Auth or callback guidance when relevant.
5. Rendering and performance notes.
