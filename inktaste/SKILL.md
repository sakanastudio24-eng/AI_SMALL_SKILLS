---
name: inktaste
description: InkVein's reusable UI/UX judgment and implementation standard for auditing or structurally improving a functionally correct screen or user-facing section. Use for InkVein hierarchy, location clarity, navigation, affordances, information architecture, state visibility, loading/error/feedback/recovery, drafts, accessibility, real-data durability, media presentation, request/render performance, source-authoritative UI behavior, dead or fake controls, container overuse, truncation, consistency, and Mobbin-informed research. Stop before broad final color, motion, or decorative polish.
---

# InkTaste

Turn a functionally correct InkVein screen into a structurally coherent one. Leave the remaining work mostly to color, fine spacing, typography finishing, motion, micro-interactions, icon refinement, and bounded performance refinement.

## Priority Order

Apply this order:

```text
Correct behavior
-> clear location
-> strong hierarchy
-> obvious interaction
-> honest feedback
-> recoverability
-> accessibility
-> visual refinement
```

Use this V1 acceptance test:

> Could someone who has never used InkVein correctly predict what will happen before they tap each visible control?

If not, prefer a clearer label, familiar affordance, stronger hierarchy, visible state, fewer competing choices, removal of unnecessary UI, or another structural correction.

## Scope One Section

Review one logical user-facing section at a time. Do not redesign the whole application in one pass. Do not introduce Calendar or another adjacent product feature unless the user explicitly scopes it.

Before editing:

1. Inspect the applicable task contract and project rules.
2. Inspect the section source, current screenshots/device evidence, navigation path, component state, API calls, and relevant backend/source contracts.
3. State the screen purpose and authoritative state owner.
4. Read `references/core-laws.md` completely.
5. Read `references/review-and-implementation.md` completely.
6. Read `references/research-and-inkvein-directions.md` when working on InkVein-specific structure or doing reference research.
7. Ask Zech one concise question only when source inspection leaves a genuine ambiguity or product decision. Do not ask what source can answer.

## Review Then Implement

Follow this sequence:

```text
inspect source
-> inspect actual evidence
-> map request/render and authority behavior
-> identify structural UX problems
-> research purpose-matched patterns
-> propose the smallest coherent direction
-> implement only the scoped section
-> run local validation
-> obtain manual proof when required
-> record polish-only remainder
```

Do not redesign from screenshots alone. Do not invent client authority, weaken a correct denial, create fake controls or values, or rewrite architecture speculatively for possible performance gains.

## Interaction Grammar

Use distinct treatments:

- Status: badge or plain label; normally not pressable.
- Navigation: row/card with a clear destination affordance, usually a chevron.
- Primary action: obvious button.
- Boolean: switch.
- Single selection: radio, selected tab, or segmented control.
- Multi-selection: checkbox or clearly selected tokens.
- More: ellipsis/menu.
- Information: plain readable content.
- Destructive: explicit destructive treatment with proportional confirmation.

Same appearance must mean the same behavior. Different behavior needs different treatment. Status must not compete with action.

## Evidence Discipline

Classify each finding as exactly one of:

- `BLOCKER`: incorrect or unusable interaction.
- `STRUCTURAL`: hierarchy, navigation, state, or affordance issue to fix before final polish.
- `PERFORMANCE`: evidenced request, render, or loading issue.
- `ACCESSIBILITY`: usability or accessibility concern.
- `POLISH`: color, fine spacing, animation, or micro-visual refinement.
- `INFO`: intentional current behavior.

Do not call source inspection runtime proof. Distinguish static, automated, local runtime, hosted, and real-device evidence. If Mobbin or device evidence is unavailable, say so rather than implying it was inspected.

## Completion Boundary

Finish InkTaste only when location, hierarchy, navigation, interaction grammar, state, feedback, recoverability, accessibility basics, real-data durability, authority behavior, and evidenced request/render behavior are coherent.

Stop before broad final-polish work. If final polish still requires major screen restructuring, InkTaste is not complete.

Use the required output contract in `references/review-and-implementation.md`.
