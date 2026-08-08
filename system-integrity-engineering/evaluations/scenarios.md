# Evaluation Scenarios

Use these prompts to pilot whether the skill changes agent behavior without leaking expected answers.

## Scenario 1 - Stale Frontend Authority

```text
Use $system-integrity-engineering at /path/to/system-integrity-engineering. Review a feature where the frontend receives availableActions from an API and then decides whether to call /claim, /take-over, or /renew based on the cached list. The backend endpoints each check login but trust the action selected by the frontend. Produce the design risks and the smallest repair plan.
```

## Scenario 2 - Over-Mocked Integration

```text
Use $system-integrity-engineering at /path/to/system-integrity-engineering. A PR says payment webhook processing is fully tested, but tests mock signature verification, database writes, and notification publishing. Review the test evidence claim and propose a realistic verification plan.
```

## Scenario 3 - Fragile Refactor

```text
Use $system-integrity-engineering at /path/to/system-integrity-engineering. A large service class mixes validation, SQL access, email sending, retry logic, and UI-facing error text. Plan a behavior-preserving refactor that can be shipped incrementally.
```

## Scenario 4 - Migration Compatibility

```text
Use $system-integrity-engineering at /path/to/system-integrity-engineering. A team wants to rename a required database column and update the app in one deployment. Identify compatibility risks, rollout order, and proof requirements.
```
