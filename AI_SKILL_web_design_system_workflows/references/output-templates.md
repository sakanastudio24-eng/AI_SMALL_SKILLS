# Output Templates

Use these response shapes when the user wants actionable design-system output, not just analysis.

## `new-system` Template

Use this when proposing a new design system.

```text
Goal
- What the system is for and who it serves

Foundations
- Principles
- Accessibility target
- Core foundations to define first

Token Strategy
- Token layers
- Naming rules
- Theme strategy

First Component Set
- 5 to 10 components to build first
- Why these come first

Docs And Governance
- What docs must exist
- Ownership and contribution model

Initial Deliverables
- What gets produced now
- What can wait
```

## `system-refresh` Template

Use this when the system exists but is inconsistent.

```text
Current Problems
- Duplicate patterns
- Token drift
- Accessibility or documentation gaps

Keep / Merge / Deprecate
- What remains
- What gets normalized
- What should be retired

Migration Plan
- Lowest-risk first changes
- Breaking changes later

Immediate Deliverable
- One cleanup pass with the highest leverage
```

## `product-adoption` Template

Use this when adapting a page or feature to an existing system.

```text
Target Surface
- The page, flow, or component set being updated

Reuse
- Existing tokens/components to apply

Gaps
- Missing states, variants, or patterns

Implementation Plan
- What changes in code
- What should become reusable system assets

Acceptance Bar
- Visual consistency
- Accessibility
- Responsive behavior
```

## `system-audit` Template

Use this when reviewing a design system.

```text
Findings
- Highest-severity issues first

Missing Artifacts
- Foundations, tokens, components, docs, or governance gaps

Risk
- Product inconsistency
- Accessibility exposure
- Migration friction

Recommended Next Steps
- Top 3 to 5 fixes in priority order
```

## Formatting Rule

Prefer short sections with direct decisions, concrete deliverables, and clear priorities. Avoid turning design-system responses into trend commentary or generic inspiration lists.
