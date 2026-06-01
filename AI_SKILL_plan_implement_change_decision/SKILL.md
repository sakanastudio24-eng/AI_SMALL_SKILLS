---
name: AI_SKILL_plan_implement_change_decision
description: Guide whether work should stay at plan level, move to implementation, or be handled as a scoped change request. Use when users are deciding between brainstorming, detailed planning, implementation, refactor requests, or follow-up changes on work already in motion.
---

# AI_SKILL_plan_implement_change_decision

## Overview

Use this skill to classify ambiguous requests into the right execution mode before work starts or changes direction. The goal is to avoid planning when the user wants action, avoid coding when the request is still unresolved, and avoid mixed-scope changes that hide the real decision.

## Execute Workflow

1. Identify the current request mode.
- Decide whether the user is asking for planning, implementation, review, or a change to prior work.
- Look for signals that the request is blocked on product decisions versus ready for execution.

2. Check whether the spec is stable enough to build.
- If success criteria, scope, or tradeoffs are still unstable, keep the work in plan mode.
- If the request is narrow and executable, move directly to implementation.

3. Separate net-new work from change requests.
- Distinguish “build this” from “modify the thing you already made.”
- For changes, restate the delta clearly before execution.

4. Make the execution decision explicit.
- State whether the next action should be `plan`, `implement`, `review`, or `revise`.
- Note any assumptions that make the choice safe.

5. Protect against mode drift.
- Do not mix architecture planning, coding, and review in one blurred response.
- If the request spans multiple modes, sequence them intentionally.

## Output Requirements

Always include:

1. Chosen mode.
2. Why that mode is correct.
3. Any blocked decisions or assumptions.
4. The immediate next step.
5. Scope guardrails for the current turn.
