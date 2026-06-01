---
name: AI_SKILL_expo_placeholder_integration_workflow
description: Guide Expo placeholder integration work across temporary screens, navigation wiring, mock data, auth stubs, and future replacement boundaries. Use when users need to hook unfinished mobile flows into an Expo app without pretending the real backend or final UX already exists.
---

# AI_SKILL_expo_placeholder_integration_workflow

## Overview

Use this skill when a mobile flow needs to exist before the real implementation is ready. The goal is to integrate placeholders in a way that keeps navigation, state, and future replacement clean instead of scattering hardcoded temp logic through the app.

## Execute Workflow

1. Define the placeholder purpose.
- State what is temporary, what it is standing in for, and what user flow must still work.
- Separate visual placeholder work from temporary data or auth behavior.

2. Isolate placeholder boundaries.
- Keep placeholder screens, mock state, and temporary API assumptions easy to remove.
- Avoid leaking placeholder logic into shared production abstractions.

3. Wire the flow realistically.
- Connect navigation, loading, empty, and error states as if the feature were real.
- Use clear temporary copy and state markers where needed.

4. Plan the replacement path.
- Note what will later be replaced by live data, real auth, or final UI.
- Keep contracts narrow so the swap does not require wide app rewrites.

5. Protect mobile quality.
- Ensure device sizing, back navigation, and transition behavior still work.
- Avoid shipping placeholders that silently break user expectations.

## Output Requirements

Always include:

1. Placeholder surface breakdown.
2. Temporary versus future boundary.
3. Navigation and state notes.
4. Replacement plan.
5. QA or shipping caveats.
