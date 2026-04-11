---
name: AI_SKILL_web
description: Build, review, and improve web pages and web apps with strong UX, clear information architecture, responsive behavior, and practical frontend execution. Use when users ask for website design, landing pages, UI cleanup, frontend implementation plans, or web UX audits.
---

# AI_SKILL_web

## Overview

Use this skill for practical web work: page structure, UX cleanup, responsive layout decisions, component planning, and frontend implementation guidance. Prefer concrete page recommendations over generic visual advice.

## Execute Workflow

1. Classify the surface.
- Identify the surface type:
  - `marketing`: landing page, waitlist page, product site
  - `application`: dashboard, workflow screen, CRUD surface
  - `account`: auth, onboarding, billing, settings
  - `content`: docs, resource page, help center
- State the primary action and at most two secondary actions.
- Identify whether the task is net-new design, cleanup of an existing UI, or implementation from an existing design/system.

2. Gather the constraints.
- Confirm audience, device expectations, existing design system, and technical stack.
- Note whether the page must preserve an established brand, typography system, or component library.
- Identify the real bottleneck: weak hierarchy, confusing flow, low trust, clutter, poor mobile behavior, or implementation inconsistency.

3. Build the information hierarchy.
- Define the main headline, support content, proof, and CTA order.
- Reduce each page to:
  - entry point
  - value explanation
  - proof or system feedback
  - action area
- Remove low-signal sections before adding more UI.
- For app screens, prefer task flow clarity over marketing-style section stacking.

4. Design for actual usage.
- Account for desktop and mobile behavior.
- Specify the states that matter:
  - loading
  - empty
  - success
  - validation or error
  - disabled
- Prefer simple navigation, clear spacing, obvious affordances, and visible state changes over decorative complexity.

5. Implement with product discipline.
- Preserve the existing design system when one exists.
- If none exists, define a small set of repeatable patterns for spacing, typography, surfaces, and actions.
- Keep interaction rules explicit:
  - one dominant CTA per viewport
  - consistent button hierarchy
  - stable navigation placement
  - predictable form validation
- Prefer reusable sections/components instead of one-off bespoke blocks.

6. Review the result.
- Check readability, CTA clarity, responsive behavior, empty states, and accessibility basics.
- Flag vague copy, weak hierarchy, inconsistent component usage, inaccessible contrast, and unclear action labels.
- Treat “too many equally important elements” as a primary design failure.

## Apply Review Rules

- Marketing pages:
  - Headline must state what the product does.
  - CTA must be visible without hunting.
  - Trust proof must appear before the user is asked for commitment.
- App screens:
  - The main workflow must be obvious in under one screen.
  - Filters, actions, and results must be visually separated.
  - Empty and error states must explain the next action.
- Forms:
  - Labels must outperform placeholders.
  - Validation must be attached to fields.
  - Destructive actions must be visually distinct.
- Navigation:
  - Avoid duplicate routes or overlapping labels.
  - Use stable IA; do not move key actions between breakpoints unless necessary.

## Output Requirements

Always include:

1. The primary user goal for the page or flow.
2. The intended content hierarchy.
3. The key UX problem being solved.
4. Mobile and desktop considerations.
5. Specific UI/component recommendations when proposing changes.
6. State handling requirements.
7. Concrete implementation guidance rather than generic design language.
