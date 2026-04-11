---
name: AI_SKILL_system_design
description: Design scalable software systems with clear service boundaries, data flow, reliability tradeoffs, and operational constraints. Use when users ask for system design, backend architecture, API/platform planning, scaling strategy, or technical design docs.
---

# AI_SKILL_system_design

## Overview

Use this skill for end-to-end system design work: services, data models, queues, APIs, scaling, reliability, and tradeoff analysis. Prefer a practical v1 that matches the stated scale over premature distributed complexity.

## Execute Workflow

1. Define the problem.
- Clarify users, core use cases, throughput expectations, latency sensitivity, and consistency needs.
- Separate hard requirements from nice-to-have scale assumptions.
- Capture:
  - read/write ratio
  - peak traffic expectations
  - data retention needs
  - latency targets
  - failure tolerance
  - compliance/security constraints

2. Design the major components.
- Identify clients, APIs, core services, storage layers, async jobs, and external dependencies.
- Prefer explicit boundaries and simple data flow.
- Start with the smallest architecture that can correctly serve the core path.

3. Model data and state.
- Define the key entities, write/read paths, and ownership of source-of-truth data.
- Call out caching, indexing, or event-driven updates only where they materially help.
- Separate transactional state from derived/read-optimized state.

4. Evaluate non-functional requirements.
- Address reliability, security, observability, failure handling, and deployment concerns.
- Include bottlenecks and fallback behavior.
- Specify the top two or three realistic bottlenecks rather than listing every possible one.

5. Recommend a practical version.
- Start with a design that is correct for the current scale.
- Note what changes later if usage or complexity increases.

## Apply Design Rules

- Start monolithic unless there is a clear need for independent scaling, failure isolation, or team separation.
- Use async jobs for slow, retryable, or user-non-blocking work.
- Use queues only when retries, buffering, or fan-out are real requirements.
- Add caching only after identifying a read bottleneck, latency hotspot, or expensive recomputation path.
- Event-driven patterns are justified when multiple consumers need the same state change or when coupling must be reduced.
- Be explicit about source of truth for each entity.
- Design idempotency for retries on payments, webhooks, job processors, and externally triggered writes.

## Output Format

Use this structure when the user wants a full design:

1. Requirements and assumptions.
2. Major components.
3. Critical request/data flows.
4. Data model and storage choices.
5. Bottlenecks and failure handling.
6. V1 recommendation.
7. Scale-up path.

## Output Requirements

Always include:

1. Core requirements and assumptions.
2. Main components and their responsibilities.
3. Data flow for critical paths.
4. Data ownership and storage choices.
5. Bottlenecks, tradeoffs, and failure points.
6. Security and observability considerations.
7. A sensible v1 design before scale-up extensions.
