---
name: codex-security-cert-watch
description: Maintain up-to-date cybersecurity certification guidance and security-risk guardrails for AI/app-bot workflows. Use when users ask about security certificates, certification roadmaps, renewal requirements, exam updates, policy boundaries, or key security concerns and "do-not-cross" lines for AI-enabled systems.
---

# Codex Security Cert Watch

## Overview

Use this skill to answer security-certification and AI security-boundary requests with current, source-backed guidance. Prioritize official provider pages and clearly separate stable guidance from date-sensitive claims.

## Workflow

1. Clarify the request scope.
- Identify whether the user wants certification mapping, latest exam/version changes, security concerns for AI bots, or a full learning path.
- Ask for role target (SOC, GRC, cloud security, appsec, pentest, leadership) if missing.

2. Verify freshness for unstable facts.
- Treat versions, retirement dates, exam objective updates, pricing, and renewal policies as time-sensitive.
- Check official vendor pages before answering any "latest/current/today" question.

3. Build the answer in three blocks.
- `Security concerns`: use `references/security-concerns.md`.
- `Certification landscape`: use `references/certification-catalog.md`.
- `Recommended path`: map beginner/intermediate/advanced options to the user role.

4. Flag confidence and source quality.
- Label inferred guidance versus directly confirmed facts.
- Prefer primary sources and include direct links.

5. Add operational guardrails.
- Include anti-fraud and exam-policy reminders when the user asks for shortcuts.
- Avoid unverified claims about accreditation, pass rates, or legal compliance.

## Output Format

Use this concise structure:

1. `As of <date>` status line.
2. Key security concerns (5-8 bullets).
3. Certification options by provider/domain.
4. Suggested next certs for the user goal.
5. Sources list (official URLs first).

## Reference Map

- For AI/app-bot risk boundaries and "do-not-cross" lines: `references/security-concerns.md`
- For major security certifications and official provider links: `references/certification-catalog.md`
