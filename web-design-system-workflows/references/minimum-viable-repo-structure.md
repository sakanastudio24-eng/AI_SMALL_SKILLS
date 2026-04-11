# Minimum Viable Repo Structure

Use this when the user asks how a design-system repo or package should be organized.

## Default Shape

This is a practical baseline for a web design-system repo or package set:

```text
design-system/
├── foundations/
│   ├── principles.md
│   ├── color.md
│   ├── typography.md
│   ├── spacing.md
│   ├── layout.md
│   └── motion.md
├── tokens/
│   ├── base.json
│   ├── semantic.json
│   ├── themes/
│   │   ├── light.json
│   │   └── dark.json
│   ├── css/
│   │   └── variables.css
│   └── README.md
├── components/
│   ├── primitives/
│   ├── navigation/
│   ├── forms/
│   ├── feedback/
│   └── data-display/
├── patterns/
│   ├── auth/
│   ├── dashboards/
│   ├── settings/
│   └── empty-error-loading/
├── docs/
│   ├── getting-started.md
│   ├── contribution.md
│   ├── accessibility.md
│   ├── migration.md
│   └── release-policy.md
└── governance/
    ├── ownership.md
    ├── naming.md
    ├── review-checklist.md
    └── deprecations.md
```

## If The System Lives Inside A Product Repo

Use a narrower layout:

```text
src/
├── styles/
│   ├── tokens.css
│   ├── themes.css
│   └── globals.css
├── design-system/
│   ├── foundations/
│   ├── components/
│   ├── patterns/
│   └── docs/
└── app/
```

Prefer this when:

- the team has one product, not a shared multi-product platform
- the design system is still evolving with the product
- extracting a separate package would add overhead without reuse

## Token Layer Guidance

Keep token layers explicit:

1. `base`: raw scales and references such as color ramps, spacing steps, radii.
2. `semantic`: meaning-based aliases such as `surface-primary`, `text-danger`, `border-muted`.
3. `theme overrides`: light, dark, brand, density, or white-label overrides.
4. `component tokens`: only for highly reused components with stable anatomy.

Avoid:

- storing only one flat token file
- naming tokens after hex colors
- mixing semantic and component tokens arbitrarily

## Component Package Guidance

At minimum, each reusable component should have:

- implementation file
- tests if the repo uses them
- story/example
- usage documentation
- accessibility notes

Do not let stories become the only documentation source if the system serves multiple teams. Keep written docs for discoverability and governance.

## What Must Exist Before Calling It A Design System

Minimum baseline:

- foundations documentation
- reusable tokens
- a small set of shared components
- usage guidance
- ownership/governance notes

If one or more of those are missing, describe it accurately as a UI library, token set, component collection, or brand guide instead of overstating maturity.
