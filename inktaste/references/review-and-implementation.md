# Review and Implementation Contract

Use this file for every InkTaste audit or implementation.

## Section Workflow

1. Define one logical section and its user goal.
2. Inspect task rules and only relevant source.
3. Inspect current screenshots or real-device evidence when available.
4. Map navigation, component state, API/request behavior, and backend/source authority.
5. Run the ten-second test from `core-laws.md`.
6. Classify findings as BLOCKER, STRUCTURAL, PERFORMANCE, ACCESSIBILITY, POLISH, or INFO.
7. Research purpose-matched patterns when reference evidence will improve the decision.
8. Propose the smallest coherent structural repair.
9. Implement only when the user requested implementation and the task contract permits edits.
10. Run focused checks, then proportionate regressions.
11. Request manual/device proof only for boundaries local automation cannot prove.
12. Record only genuinely remaining polish work.

## Authority and State Law

Do not invent client authority.

Before changing lifecycle- or security-sensitive controls, identify:

- authoritative state owner;
- derived server and client projections;
- mutation authority;
- actor/ownership/capability checks;
- stale-response protection;
- terminal and read-only states;
- denial and conflict behavior.

The UI may project available actions, but the backend must authorize mutations at action time. Never repair a correct 403, 404, or 409 by weakening backend authority. Prevent predictable invalid controls while preserving server enforcement.

Protect against late async overwrite:

```text
request A starts
selection/state changes
request B returns
request A returns late
```

Use the project's established request identity, sequence token, cancellation, selected-reference comparison, or reducer-owned transition pattern. Do not add polling or retries without evidence and contract support.

## Request and Render Performance Law

Inspect where practical:

- repeated identical requests;
- hidden tabs fetching data;
- unnecessary fetch-on-render or fetch-on-focus;
- stale async overwrite;
- request fan-out and waterfalls;
- repeated media fetches;
- unnecessary large-list reads;
- expensive transforms on each render;
- request storms or retry loops;
- avoidable rerenders caused by state ownership;
- blocking secondary work;
- duplicated data retrieval;
- loading that discards usable content.

Optimize only when evidence identifies a pressure point. Prefer removing duplicate boundary calls and waterfalls before broad caching. Do not cache mutable security decisions unless the source contract explicitly permits it. Do not perform speculative architecture rewrites merely because an optimization is possible.

## Behavior Review

Inspect loading with and without usable content, empty state, success feedback, local validation, backend denial/conflict, valid recovery, stale or switched-object behavior, long and missing real data, supported offline/background behavior, screen-reader order, and selected/disabled/read-only/destructive states.

Do not add fake data to make layout evidence look complete.

## Media Presentation

When the section includes media, inspect aspect-ratio durability, preview/play affordances, poster or placeholder behavior, local loading and failure states, accessibility labels, and repeated fetch behavior. Reuse controlled access for private media; do not expose storage paths or internal identifiers merely to improve presentation. Make image, video, processing, unavailable, and removed states honest and visually distinct.

## Required Output

Return:

1. Screen purpose.
2. Current hierarchy.
3. Current interaction grammar.
4. Current API/request behavior.
5. Mobbin references researched.
6. Principles that apply.
7. Principles that do not apply.
8. Structural problems.
9. Performance problems.
10. Accessibility issues.
11. Minimal repair plan.
12. Files expected or actually changed.
13. Authority boundaries to preserve.
14. Validation plan and evidence level.
15. Remaining final-polish-only work.

For implementation closeout, also state git status and proposed commit when relevant. Never commit, push, migrate, deploy, or install dependencies without explicit permission or an applicable task contract.

## Completion Gate

Confirm the section purpose/location, one primary action, interaction grammar, honest state/loading/errors/feedback, invalid-action prevention, server-owned authority, navigation escape/context, real-data durability, accessibility basics, evidence-based performance findings, absence of fake/dead UI, and a genuinely polish-only remainder.
