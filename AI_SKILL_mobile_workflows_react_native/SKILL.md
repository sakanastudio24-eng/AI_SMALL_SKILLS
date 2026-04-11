---
name: AI_SKILL_mobile_workflows_react_native
description: Guide React Native mobile workflows across screen planning, navigation, state flow, auth handling, animation decisions, device constraints, testing, and shipping readiness. Use when users ask about React Native screens, mobile navigation, auth on mobile, device behavior, or adapting web product flows to mobile.
---

# AI_SKILL_mobile_workflows_react_native

## Overview

Use this skill for React Native mobile planning and implementation guidance across screen structure, navigation, shared state, device constraints, and shipping quality.

## Execute Workflow

1. Define the mobile flow.
- Map the user journey screen by screen.
- Identify where state is local to the screen, shared in-app, or backend-driven.

2. Choose navigation and interaction patterns.
- Fit the flow to stack, tabs, drawers, modal sheets, or nested navigation only when needed.
- Treat gestures, transitions, and touch targets as part of the product flow.

3. Plan operational states.
- Define loading, empty, offline, success, and failure states.
- Check realistic device-size behavior instead of assuming a compressed web layout will work.

4. Validate auth and platform behavior.
- Review session persistence, app resume behavior, and iOS/Android differences where relevant.
- Check deep links, onboarding transitions, and interrupted auth flows.

5. Review shipping quality.
- Ensure the flow is usable on real devices.
- Keep animation supportive, navigation clear, and screen purpose obvious.

## Output Requirements

Always include:

1. Screen breakdown.
2. Navigation recommendation.
3. State-handling guidance.
4. Mobile QA notes.
5. Platform/device edge cases.
