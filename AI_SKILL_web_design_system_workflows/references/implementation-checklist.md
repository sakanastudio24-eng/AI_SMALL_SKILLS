# Implementation Checklist

Use this checklist when turning design-system ideas into code and documentation.

## Discovery Inputs

- product types and target surfaces
- supported frameworks
- current UI inconsistencies
- brand constraints
- accessibility target
- theming or white-label requirements
- existing CSS, token, or component libraries

## Foundations Deliverables

- design principles
- color roles, not just palettes
- typography scale
- spacing scale
- radius and elevation rules
- layout grid and breakpoints
- motion guidance
- iconography rules

## Token Deliverables

- naming convention
- source-of-truth format
- semantic token map
- CSS variable output
- theme override strategy
- token documentation with examples

## Component Deliverables

- primitive inventory
- composed component inventory
- anatomy and slot model
- states and variants
- responsive behavior
- accessibility requirements
- code examples and usage limits

## Documentation Deliverables

- getting started guide
- foundations section
- components section
- pattern/page examples
- accessibility notes
- contribution rules
- migration notes if replacing legacy UI

## Governance Deliverables

- owners and reviewers
- release/versioning approach
- deprecation policy
- adoption metrics or success criteria
- change log expectations

## Common Failure Modes

- skipping tokens and encoding values directly in components
- naming tokens after colors instead of meaning
- shipping components without usage rules
- overloading one component with too many variants
- ignoring content and accessibility guidance
- treating documentation as an afterthought
