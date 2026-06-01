---
name: AI_SKILL_django_rpc_endpoint_workflow
description: Guide Django RPC-style endpoint design, implementation, and review across views, serializers, auth, validation, service boundaries, and response contracts. Use when users ask about Django API endpoints that behave like actions or RPC calls rather than plain CRUD resources.
---

# AI_SKILL_django_rpc_endpoint_workflow

## Overview

Use this skill for Django endpoints that trigger explicit actions, workflows, or backend operations. The focus is on keeping RPC-style routes safe, explicit, validated, and maintainable without collapsing business logic into the view layer.

## Execute Workflow

1. Classify the endpoint action.
- State the user action, side effect, and expected response shape.
- Decide whether RPC is appropriate or whether a resource-oriented route would be cleaner.

2. Define the contract.
- Specify method, input payload, auth rules, error cases, and output structure.
- Keep action names explicit and avoid ambiguous "do everything" handlers.

3. Separate transport from business logic.
- Keep validation, permission checks, and orchestration clear in the view layer.
- Move core business logic into services or dedicated functions.

4. Protect state changes.
- Enforce auth and ownership checks server-side.
- Handle idempotency, retries, and partial failure behavior intentionally.

5. Validate the endpoint story.
- Ensure the route, serializer, service call, logging, and response shape tell a clean action-oriented story.
- Avoid mixing unrelated operations into one RPC call.

## Output Requirements

Always include:

1. Route and method recommendation.
2. Input and output contract.
3. Auth and permission checks.
4. Service-boundary guidance.
5. Failure and retest notes.
