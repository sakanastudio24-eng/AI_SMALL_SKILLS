---
name: AI_SKILL_architecture
description: Review and shape software architecture for maintainability, boundaries, module ownership, and long-term change safety. Use when users ask for architecture reviews, codebase structure guidance, refactoring boundaries, or service/module decomposition.
---

# AI_SKILL_architecture

## Overview

Use this skill when the main question is how a codebase should be structured, split, or evolved over time. Focus on maintainability, ownership, dependency direction, and change safety rather than abstract idealism.

## Execute Workflow

1. Classify the architecture problem.
- Determine whether the task is:
  - `module-boundary cleanup`
  - `monolith restructuring`
  - `service extraction`
  - `frontend architecture cleanup`
  - `shared library/platform split`
- Identify the triggering pain:
  - slow changes
  - circular dependencies
  - unclear ownership
  - duplicated logic
  - deployment coupling
  - test fragility

2. Map the current structure.
- Identify modules, services, shared utilities, data boundaries, and cross-cutting concerns.
- Separate current reality from intended architecture.
- List the highest-churn areas and the highest-risk shared dependencies.

3. Evaluate boundaries.
- Look for leaking abstractions, circular dependencies, mixed responsibilities, and weak ownership lines.
- Prefer seams that reduce future change cost.
- Distinguish:
  - domain logic
  - integration logic
  - UI or transport logic
  - infrastructure concerns

4. Apply boundary rules.
- Keep code together when it changes together.
- Split code when it has different owners, scaling needs, release cadence, or failure domains.
- Do not extract a service only to gain conceptual purity.
- Prefer a modular monolith over service sprawl unless there is a clear operational reason to split.
- Shared modules must be stable and narrow; avoid dumping volatile business logic into `shared`.

5. Propose a target shape.
- Define the module or service boundaries.
- State what should stay together, what should split, and what should become shared infrastructure.
- Specify dependency direction explicitly.
- Name the ownership model for each major boundary.

6. Plan migration pragmatically.
- Recommend incremental moves, not idealized rewrites.
- Prefer steps that improve testability, ownership, and deploy safety.
- Migrations should usually follow:
  - isolate interfaces
  - move reads
  - move writes
  - move ownership and tests
  - remove dead paths

7. Validate tradeoffs.
- Call out complexity, runtime coupling, team ownership, and operational cost.
- Explicitly note when a simpler architecture is better than a more abstract one.

## Smells To Flag

- Modules importing through side doors instead of public interfaces.
- “Shared” packages with business logic from multiple domains.
- Services that cannot be deployed or tested independently despite being split.
- Controllers/components that contain orchestration, validation, persistence, and formatting in one place.
- Data ownership that depends on tribal knowledge rather than code boundaries.

## Output Requirements

Always include:

1. The current architectural pain points.
2. The current boundary failures or dependency problems.
3. The proposed boundaries or ownership lines.
4. The dependency direction of the target shape.
5. The main tradeoffs of the recommended structure.
6. An incremental migration path.
7. Risks if the current structure remains unchanged.
