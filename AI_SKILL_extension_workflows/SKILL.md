---
name: AI_SKILL_extension_workflows
description: Guide browser extension work from planning through implementation, debugging, permissions review, UI injection, runtime behavior, and shipping checks. Use when users ask about popup flows, content scripts, background/service workers, extension architecture, permission reviews, or extension-to-web integration.
---

# AI_SKILL_extension_workflows

## Overview

Use this skill for browser extension work that spans popup UI, content scripts, background logic, permissions, injection behavior, runtime messaging, and extension-to-web coordination.

## Execute Workflow

1. Define the extension surface.
- Identify whether the work lives in popup, options, content script, background/service worker, devtools, or a companion web app.
- State the user-facing goal and what must persist across refreshes or tabs.

2. Map runtime boundaries.
- Separate what runs on the page, in the extension runtime, and on the backend.
- Define the source of truth for user state, sync state, and page-observed state.

3. Minimize permissions.
- Use the smallest permission set that supports the feature.
- Prefer optional permissions or host scoping when possible.

4. Plan UI and runtime states.
- Define idle, loading, success, error, disconnected, and permission-denied states.
- Account for restricted pages, tab switches, refreshes, and stale DOM assumptions.

5. Validate security and shipping risk.
- Check host-page stability, privacy implications, auth coupling, and message-passing boundaries.
- Treat injection logic and extension-web bridging as high-risk areas that require manual review.

## Output Requirements

Always include:

1. Extension surface breakdown.
2. Permission review.
3. Runtime/state checklist.
4. Injection or popup guidance.
5. Shipping notes and edge cases.
