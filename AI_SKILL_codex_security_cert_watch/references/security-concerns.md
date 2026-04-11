# Security Concerns for AI/App Bots

Last reviewed: 2026-02-20

## Core "Do-Not-Cross" Lines

1. Do not misrepresent the system as human or hide that automation is being used.
2. Do not make unsubstantiated claims about AI accuracy, legal/medical capability, or detection performance.
3. Do not process personal data without valid notice, lawful basis, and user rights handling.
4. Do not automate high-impact decisions without human review and a dispute path.
5. Do not deploy manipulative behavior that exploits vulnerable users.
6. Do not expose secrets, internal data, or user data through prompt injection and tool misuse.
7. Do not enable exam fraud, unauthorized material use, or policy-violating test assistance.

## High-Risk Failure Modes

- Prompt injection leading to data exfiltration.
- Retrieval leakage from unscoped documents or over-broad connectors.
- Tool abuse (shell/web/actions) without allowlists and confirmation gates.
- Hallucinated compliance claims ("certified," "accredited," "lawful") without evidence.
- Outdated certification advice when version/retirement dates changed.

## Operational Controls

1. Require source-backed assertions for dates, versions, and policy statements.
2. Prefer primary sources: official cert vendors, regulators, standards bodies.
3. Add confidence labels when advice is inferred.
4. Keep an update cadence for volatile content (monthly or before major recommendations).
5. Maintain an audit trail of cited sources and review date.

## Regulatory and Framework References

- FTC AI claims and deception enforcement: https://www.ftc.gov/news-events/topics/artificial-intelligence
- CCPA/CPRA overview (California OAG): https://oag.ca.gov/privacy/ccpa
- COPPA rule guidance (FTC): https://www.ftc.gov/business-guidance/privacy-security/childrens-privacy
- EU AI Act text: https://eur-lex.europa.eu/eli/reg/2024/1689/oj/eng
- NIST AI RMF playbook: https://www.nist.gov/itl/ai-risk-management-framework/nist-ai-rmf-playbook
- OWASP Top 10 for LLM Applications: https://owasp.org/www-project-top-10-for-large-language-model-applications/

