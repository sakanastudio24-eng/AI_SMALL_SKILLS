# Task Recipes

Use these recipes to turn broad design-system requests into concrete work.

## `new-system`

Use when the user wants to create a system from scratch.

Recommended sequence:

1. capture product scope and users
2. define principles and accessibility target
3. define foundations
4. define token architecture
5. pick the first 5 to 10 shared components
6. document contribution and governance basics
7. deliver starter code/docs structure

Minimum useful deliverables:

- foundations brief
- token naming map
- component inventory
- repo structure
- first implementation target

## `system-refresh`

Use when the user already has styles/components but they are inconsistent.

Recommended sequence:

1. inventory existing tokens, utilities, and components
2. group duplicates and near-duplicates
3. separate keep, merge, deprecate, and replace decisions
4. define migration order by surface area and risk
5. implement one normalization pass first

Minimum useful deliverables:

- inconsistency report
- normalized token plan
- component deprecation table
- migration sequence

## `product-adoption`

Use when the system exists and the user wants to apply it to a page or feature.

Recommended sequence:

1. map the screen to existing tokens and components
2. identify true gaps versus local one-offs
3. add missing component states only if they generalize
4. implement the page using system primitives
5. document any new reusable additions

Minimum useful deliverables:

- adoption plan for the target page/feature
- list of reused system pieces
- list of justified additions
- code changes

## `system-audit`

Use when the user wants to know whether a design system is healthy.

Audit dimensions:

- foundations completeness
- token quality
- component consistency
- accessibility coverage
- documentation quality
- governance and release discipline

Minimum useful deliverables:

- prioritized findings
- severity or impact ranking
- missing artifacts
- next 3 to 5 fixes

## Prioritization Rule

When choosing what to do first, prefer work that improves:

1. high-reuse primitives
2. accessibility correctness
3. token consistency
4. documentation discoverability
5. migration clarity

Do not spend early cycles on decorative pattern libraries before the token and component base is stable.
