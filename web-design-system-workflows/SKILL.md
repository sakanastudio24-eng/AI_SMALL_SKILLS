---
name: web-design-system-workflows
description: Create, audit, document, implement, and evolve web design systems for websites and apps. Use when users ask to build a design system, turn brand rules into tokens and components, align design and code, choose a foundations architecture, or apply an existing system consistently in web design.
---

# Web Design System Workflows

Use this skill for design-system work that spans visual foundations, tokens, components, documentation, and adoption in frontend codebases.

## Classify The Request

Start by placing the task in one of these buckets:

- `new-system`: create a system from brand/product inputs.
- `system-refresh`: modernize an inconsistent or outdated system.
- `product-adoption`: apply an existing system to pages, flows, or components.
- `system-audit`: identify gaps in tokens, accessibility, docs, or governance.

Then choose the smallest output that will move the work forward. Do not default to a full design-system rebuild when the real need is a token pass, a component cleanup, or a rollout plan.

## Core Workflow

1. Define scope and consumers.
- Identify products, brands, platforms, frameworks, and owners.
- Confirm the target outputs: foundations, tokens, component library, documentation, or rollout plan.
- Ask whether the system must support multiple themes, brands, densities, or dark mode.

2. Capture the foundations before touching components.
- Define principles, accessibility bar, color, typography, spacing, layout, radius, elevation, motion, iconography, and content tone.
- Treat brand examples as constraints and inspiration, not as a permission slip to copy UI details blindly.
- When the repo already has styling primitives, reuse and normalize them instead of replacing everything.

3. Create the token model.
- Prefer a layered token structure:
  - base/reference tokens
  - semantic tokens
  - component tokens only where reuse justifies them
- Default web outputs:
  - CSS custom properties
  - token JSON or similar source-of-truth format
  - TypeScript typings/constants when the stack benefits from them
- Do not hardcode brand hex values or spacing numbers directly inside component implementations unless the repo clearly does not use tokens.

4. Design the component architecture.
- Separate primitives, composed components, page patterns, and templates.
- Define states, variants, responsiveness, interaction behavior, loading/empty/error states, and accessibility expectations.
- Prefer composable APIs and restrained prop surfaces over one-off variants that solve only a single screen.

5. Ship code and documentation together.
- Keep the implementation paired with usage guidance.
- Document:
  - what the component is for
  - when to use it
  - when not to use it
  - anatomy
  - variants and states
  - accessibility notes
  - code examples
- If Figma is part of the workflow, use the `figma` or `figma-implement-design` skill in the same turn when URLs or node IDs are present.

6. Add governance.
- Define ownership, review path, contribution rules, naming rules, versioning, and deprecation strategy.
- Prioritize high-reuse components first.
- Treat migration guidance as part of the system, not as optional cleanup.

## Task Recipes

Load `references/task-recipes.md` when you need a more concrete path for one of the four request buckets.

- For `new-system`, produce principles, foundations, tokens, first components, docs IA, and repo structure.
- For `system-refresh`, identify breakpoints between what should be normalized, deprecated, or preserved.
- For `product-adoption`, adapt existing pages/components to the system instead of rebuilding the system itself.
- For `system-audit`, score gaps and prioritize fixes by user impact and reuse.

## Output Rules

Always return a concrete deliverable, not just theory. Choose the smallest useful package for the request:

- foundations brief
- token schema and naming plan
- component inventory
- documentation IA
- rollout/migration plan
- production code for tokens/components/pages
- audit report with prioritized gaps

For implementation tasks, include:

1. Foundations decisions.
2. Token decisions.
3. Component/API decisions.
4. Accessibility constraints.
5. Documentation or adoption notes.

When the user asks how to organize the work in code, load `references/minimum-viable-repo-structure.md` and propose a concrete file/folder layout instead of speaking abstractly.

When the user needs a plan, audit, or design-system brief, load `references/output-templates.md` and reuse the closest response shape instead of inventing a new format.

## Heuristics

- Tokens first, components second, page examples third.
- Semantic names beat visual names.
- Separate brand identity from reusable product mechanics.
- Build for consistency without making every screen look generic.
- A design system is not a component dump; it needs rules, examples, and governance.
- Do not introduce unnecessary abstractions if the product only needs a narrow system.

## Load References As Needed

- Web examples and reusable patterns: `references/examples-and-patterns.md`
- Practical delivery checklist: `references/implementation-checklist.md`
- Minimum viable repo and file layout: `references/minimum-viable-repo-structure.md`
- Task-specific execution paths: `references/task-recipes.md`
- Reusable answer structures: `references/output-templates.md`

Load only the relevant reference sections for the task at hand.
