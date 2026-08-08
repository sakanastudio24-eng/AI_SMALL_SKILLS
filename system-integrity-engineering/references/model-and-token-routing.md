# Model And Token Routing

Use this reference when selecting model/reasoning level, managing large context, or planning long-running work.

## Recommended Execution Levels

Low:

- comments
- simple wording
- naming
- formatting
- straightforward documentation corrections
- tiny mechanical edits with no behavioral impact

Medium:

- routine repository inspection
- simple tests
- bounded menial refactors
- lint/type corrections
- familiar isolated components
- documentation maintenance
- deterministic migration of repetitive patterns

GPT-5.5 High:

- feature implementation
- debugging
- integration work
- production diagnosis
- migrations
- authorization
- concurrency
- cross-layer changes
- behavior-preserving refactors
- performance corrections

GPT-5.6 High:

- creating or materially redesigning this skill
- new foundational architecture
- ambiguous authority across several systems
- unresolved data-model design
- major concurrency foundations
- large migrations with multiple valid architectures
- situations where GPT-5.5 has repeatedly failed despite strong evidence

Do not recommend GPT-5.6 merely because a task is long.

## Token Economy

Require:

- progressive disclosure
- load only relevant reference files
- reuse verified system maps
- update deltas instead of rewriting baselines
- do not repeat confirmed facts
- distinguish current truth from historical context
- keep implementation prompts short by referencing the skill
- create concise checkpoint notes after major stages
- avoid full logs when safe outcome codes are enough
- request exact evidence instead of broad screenshots
- group related tool calls
- run focused tests first
- reserve full suites for closeout
- preserve explicit unresolved blockers

## Project Checkpoint

For long projects, maintain a small checkpoint:

```text
Current goal:
Authoritative state:
Current blocker:
Changed files:
Tests and evidence level:
Hosted status:
Next action:
```

Do not let the checkpoint become a conversation transcript.
