# Example Systems And Reusable Patterns

Use these examples as pattern libraries for structure and decision-making, not as UI templates to copy.

## Open Design Systems

Source: https://www.designsystems.com/open-design-systems/

Use this as a discovery index when the user wants precedents from public systems. It is useful for:

- comparing documentation structures
- seeing how open systems separate foundations, components, and governance
- finding examples beyond the usual handful of popular systems

## GitHub Brand Toolkit

Source: https://brand.github.com/guides/getting-started

Borrow from this when the task has a strong brand-expression angle. Useful takeaways:

- keep brand foundations explicit
- separate graphic elements from product components
- define how assets and marks are used before building UI rules around them

## Atlassian Design System

Source: https://atlassian.design/get-started/design/atlassians

Borrow from this when the task needs a mature product-system structure. Useful takeaways:

- connect foundations, components, and content guidelines
- use shared libraries and common tooling between design and engineering
- document behavior and accessibility, not just visual appearance

## Lightning Design System 2

Source: https://www.lightningdesignsystem.com/2e1ef8501/p/85bd85-lightning-design-system-2

Borrow from this when the system must scale across many apps or teams. Useful takeaways:

- design tokens need to be first-class artifacts
- component blueprints should include enterprise-grade states and behaviors
- accessibility and consistency must be built into the system layer

## Backstage Design Language System

Source: https://backstage.io/docs/dls/design/

Borrow from this when the team wants an open, collaborative operating model. Useful takeaways:

- build the system iteratively instead of waiting for a perfect v1
- keep the process transparent across design and engineering
- pair the system with living docs and examples

## Material 3

Source: https://m3.material.io/

Borrow from this when you need a strong foundations baseline. Useful takeaways:

- foundations should cover color, type, shape, layout, motion, and interaction
- system decisions should scale across components instead of being decided ad hoc
- accessibility and adaptable theming belong near the core model

## Sakana Studio Design-system Repo

Source: https://github.com/sakanastudio24-eng/Design-system

Use this as a maturity-check example, not as a substantive system reference yet.

Snapshot verified on March 15, 2026:

- public GitHub repository
- default branch: `main`
- repository metadata shows no description and effectively no implementation footprint yet
- root contents currently expose only `LICENSE`

Practical takeaway:

- verify that a linked design-system repo actually contains foundations, tokens, components, docs, or governance material before treating it as a research source
- when a repo is this early, use it as a prompt for what is missing from a real design-system baseline rather than as a pattern to imitate

## Cross-System Patterns To Reuse

Across these systems, the repeatable structure is:

1. Principles and foundations.
2. Tokens or other reusable style primitives.
3. Component and pattern library.
4. Usage guidance and examples.
5. Governance, contribution, and rollout.

If the user asks for "a design system," make sure all five layers are considered even if the final deliverable only implements part of them.
