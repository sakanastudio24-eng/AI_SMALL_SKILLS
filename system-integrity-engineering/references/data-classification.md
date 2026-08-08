# Data Classification

Use this reference when touching fields, logs, API responses, UI exposure, storage, test fixtures, AI prompts, tool calls, diagnostics, or exports.

## Restricted

Highest-risk data. Examples:

- passwords
- API secrets
- encryption keys
- session tokens
- recovery secrets
- private signing material
- raw credentials
- highly sensitive identity or security evidence

Rules:

- Never expose to browser code unless intrinsically required.
- Never log.
- Never place in prompts or diagnostic output.
- Never commit.
- Use dedicated secret storage.
- Use synthetic fixtures.

## Confidential

Nonpublic sensitive data. Examples:

- private user content
- personal information
- internal moderation evidence
- staff notes
- private communications
- business-sensitive records
- unpublished financial or legal material

Rules:

- Use minimum necessary access.
- Redact diagnostics.
- Control storage and retention.
- Avoid public fixtures.
- Avoid unrestricted AI or tool exposure.

## Internal

Nonpublic operational or engineering information. Examples:

- architecture notes
- safe internal identifiers
- release metadata
- internal process documentation
- non-sensitive staff references
- development diagnostics

Rules:

- Keep within appropriate project access.
- Do not expose publicly by accident.
- Use in bounded internal engineering workflows.

## Public

Explicitly approved for public disclosure. Examples:

- public profile fields
- published documentation
- public API responses
- approved marketing content

Public must be intentional. Database visibility does not automatically make data public.

## Classification Behavior

- Use the highest applicable classification.
- Unknown user/security data defaults to at least Confidential.
- Unknown operational data defaults to at least Internal.
- Derived data inherits source sensitivity unless proven otherwise.
- Masking a value does not automatically lower classification.
- A safe reference is Public or Internal only when a contract explicitly makes it so.

Use `templates/data-classification-matrix.md` when classification is consequential.
