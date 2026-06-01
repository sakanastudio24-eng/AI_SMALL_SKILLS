---
name: AI_SKILL_hosted_manual_test_sheet_workflow
description: Guide hosted manual QA sheet planning, execution, and upkeep across test cases, environments, ownership, result tracking, and bug follow-up. Use when users ask about creating or running shared manual test sheets for hosted products or staged releases.
---

# AI_SKILL_hosted_manual_test_sheet_workflow

## Overview

Use this skill for shared manual QA sheets that track what to test, where to test it, who owns the check, and what happened. The focus is operational clarity: a hosted product should have a repeatable manual pass, not a vague checklist.

## Execute Workflow

1. Define the hosted test surface.
- Identify environment, release scope, and critical user journeys.
- Separate smoke checks from broader exploratory tests.

2. Structure the sheet.
- Capture test case name, steps, expected result, actual result, owner, environment, and status.
- Keep each row or entry action-oriented and reproducible.

3. Cover realistic hosted states.
- Include auth, empty state, happy path, failure path, permissions, and environment-specific checks.
- Account for staging-only configuration differences.

4. Track outcomes cleanly.
- Record pass/fail/block reasons.
- Link bugs or follow-up work directly to the failing case.

5. Keep the sheet maintainable.
- Remove stale cases, split overgrown sheets, and preserve release-critical checks.
- Avoid turning the sheet into an unowned archive.

## Output Requirements

Always include:

1. Test sheet structure.
2. Required columns or fields.
3. Release or environment coverage guidance.
4. Bug follow-up rules.
5. Ongoing maintenance notes.
