# 🤖 AI SKILLS / CODEX WORKFLOWS

## 🧠 HOW TO READ THIS PAGE

Each skill in this repo is a controlled workflow.

That means every skill should define:

- A clear purpose
- Hard rules and guardrails
- Ordered steps or checks
- What not to break while doing the work
- Any script, reference, or validation path that keeps the workflow safe

This page rewrites the repo's skills into that format so they are easy to scan, review, and extend.

---

## 💸 1. Cost / Pricing / FinOps

### 🔧 Skill: Code Price Optimization

**Purpose**  
Diagnose software, cloud, and API spend, then produce a ranked optimization plan with clear tradeoffs.

**Rules**

- Focus on unit economics before broad cost-cutting
- Collect company size, workload type, budget ceiling, and regional constraints first
- Re-check live vendor pricing before stating exact numbers
- Include compliance boundaries such as PCI, HIPAA, SOC 2, FedRAMP, or residency rules
- Reject shortcuts that lower reliability or violate policy boundaries

**Steps**

1. Gather the optimization profile
2. Run the diagnostic script
3. Map the result to the repo playbooks
4. Validate against current standards and provider pricing
5. Deliver ranked actions plus a 90-day rollout plan
6. Add a `Do / Avoid / Measure` section

**Checks**

- Report pressure points clearly
- Rank actions by expected savings direction and operational impact
- Include region-placement constraints when relevant
- Track metrics such as `cost/1M requests`, `cost/active user`, and `egress/request`

**Repo Source**

- `Price-optomization/code-price-optimization/SKILL.md`
- Script: `Price-optomization/code-price-optimization/scripts/diagnose_cost_plan.py`

---

### 🔧 Skill: Extension Price Diagnosis

**Purpose**  
Operate and extend the Price Diagnosis Chrome extension without breaking scan flow, scoring, or recommendation behavior.

**Rules**

- Confirm the local Python API is running before debugging extension behavior
- Keep extension build output present in `extension/dist`
- Preserve confidence-based confirmation for uncertain stack fields
- Keep the weighted scoring model intact unless the user asks to change it
- Do not present a final diagnosis when critical stack fields remain unresolved

**Steps**

1. Verify local services and build artifacts
2. Run the active-tab scan flow
3. Confirm inference confidence and user-confirmation logic
4. Run the diagnosis flow end to end
5. Validate recommendation cards and rollout sections
6. Recheck policy-boundary handling

**Checks**

- Stack inference returns `confidence` and `requiresUserConfirm`
- Score weighting remains `0.40 unit + 0.35 efficiency + 0.25 governance`
- Partial-data flows still return a score with reduced confidence
- Recommendation cards show title, why, savings direction, risk, and actions

**Repo Source**

- `Price-chrome-extention/extension-price-diagnosis-skill/SKILL.md`
- Script: `Price-chrome-extention/extension-price-diagnosis-skill/scripts/run_local_diagnosis.sh`

---

## 🔐 2. Security / Certification / Guardrails

### 🔧 Skill: Codex Security Cert Watch

**Purpose**  
Answer certification and AI security-boundary questions with source-backed, current guidance.

**Rules**

- Separate stable guidance from date-sensitive claims
- Treat exam versions, retirement dates, pricing, and renewal policies as time-sensitive
- Prefer official provider pages over summaries
- Mark inferred guidance versus directly confirmed facts
- Include anti-fraud and exam-policy reminders when users ask for shortcuts

**Steps**

1. Clarify whether the ask is about cert mapping, current exam changes, security concerns, or a learning path
2. Identify the target role when missing
3. Verify freshness for unstable facts
4. Build the answer in three blocks: security concerns, certification landscape, recommended path
5. Flag confidence and source quality
6. Add operational guardrails

**Checks**

- Include an `As of <date>` status line
- Keep official URLs first
- Avoid unsupported claims about accreditation, pass rates, or compliance

**Repo Source**

- `codex-security-cert-watch/SKILL.md`
- References:
  - `codex-security-cert-watch/references/security-concerns.md`
  - `codex-security-cert-watch/references/certification-catalog.md`

---

## 🔍 3. Debugging / Reliability / Service Health

### 🔧 Skill: Endpoint Health Auditor

**Purpose**  
Audit API and service endpoints for DNS, TLS, response health, and missing health-check coverage.

**Rules**

- Prefer HTTPS targets when possible
- Run deterministic checks before guessing root cause
- Separate DNS, TLS, network, HTTP, and app-layer failures
- Recommend standard liveness/readiness endpoints when health routes are missing
- Re-check official platform docs if behavior may be version-sensitive

**Steps**

1. Collect target domains or URLs
2. Run the checker script
3. Classify results into health buckets
4. Recommend the next action for each failing target
5. Validate advice against health endpoint best practices

**Checks**

- Label targets as `healthy`, `health_endpoint_missing`, `unhealthy`, `tls_invalid_or_expiring`, or `not_responding`
- Include one-line status per target
- Include explicit failing endpoint list
- Include a root-cause bucket and one concrete next step for each failure

**Repo Source**

- `endpoint-health-auditor/SKILL.md`
- Script: `endpoint-health-auditor/scripts/check_endpoints.py`

---

## 🧹 4. Docs / Structure / Git-Safe Changes

### 🔧 Skill: Git Safe Docs Structure

**Purpose**  
Plan and execute documentation and repository-structure changes with low risk, clean history, and predictable review.

**Rules**

- Classify work as `docs-only`, `docs+structure`, or `architecture-scale`
- Run preflight checks before editing
- Separate content edits from mass file moves when possible
- Use atomic, reviewable commits
- Never commit secrets, env files, private keys, or customer exports

**Steps**

1. Classify scope
2. Run the docs preflight script
3. Choose the correct structure profile
4. Implement minimal safe commits
5. Validate with `git status --short` and `git diff --stat`
6. Prepare PR notes with intent, impact, and before/after structure

**Git Discipline**

- Prefer additive updates over destructive rewrites
- Use `git mv` for tracked renames
- Keep one canonical location per concept
- Use conventional commits for docs and structure work
- Create a feature branch when starting from `main` or `master`

**Repo Source**

- `git-safe-docs-structure/SKILL.md`
- Script: `git-safe-docs-structure/scripts/git_docs_preflight.sh`
- References:
  - `git-safe-docs-structure/references/structure-small.md`
  - `git-safe-docs-structure/references/structure-medium.md`
  - `git-safe-docs-structure/references/structure-complex.md`

---

## 🎨 5. UI / Frontend / Design System

### 🔧 Skill: Web Design System Workflows

**Purpose**  
Create, audit, implement, document, and evolve web design systems without turning the work into a vague component dump.

**Rules**

- Classify the request before choosing the deliverable
- Do not default to a full redesign if a token pass or adoption plan is enough
- Capture foundations before touching components
- Prefer layered token models over hardcoded component values
- Ship code and documentation together
- Add governance, contribution rules, and migration guidance

**Steps**

1. Classify the task as `new-system`, `system-refresh`, `product-adoption`, or `system-audit`
2. Define scope, consumers, and target outputs
3. Capture foundations: color, type, spacing, layout, motion, accessibility
4. Create the token model
5. Design component architecture and variants
6. Ship implementation plus documentation
7. Add governance and rollout guidance

**Checks**

- Tokens first, components second, page examples third
- Semantic names beat visual names
- Accessibility constraints are explicit
- Deliver a concrete artifact: foundations brief, token schema, inventory, docs IA, rollout plan, audit, or production code

**Repo Source**

- `web-design-system-workflows/SKILL.md`
- References:
  - `web-design-system-workflows/references/task-recipes.md`
  - `web-design-system-workflows/references/output-templates.md`
  - `web-design-system-workflows/references/minimum-viable-repo-structure.md`

---

## 📱 6. Mobile / App Delivery / Platform Engineering

### 🔧 Skill: General Mobile Workflows

**Purpose**  
Deliver mobile features and releases across React Native, Expo, Swift, Kotlin, and Kotlin Multiplatform with platform-correct tradeoffs and release guardrails.

**Rules**

- Define platform split before implementation
- Choose the narrowest architecture that fits the feature
- Build the smallest vertical slice first
- Integrate push, auth, deep links, analytics, and secure storage incrementally
- Enforce performance, security, and release gates before ship
- Keep mobile-specific guidance explicit instead of giving generic product advice

**Steps**

1. Define scope and platform split
2. Choose architecture path
3. Build the smallest vertical slice
4. Integrate platform services
5. Validate performance and reliability
6. Run security and release gates
7. Tune feed performance and retention loops when applicable

**Checks**

- Recommend the correct stack path with tradeoffs
- Include platform-specific checkpoints
- Include integration checklist for auth, storage, push, deep links, analytics, and CI/CD
- Include build-pass and release checklists
- Apply mobile security controls before merge and store submission

**Repo Source**

- `Mobile-Optomization-workflows/general-mobile-workflows/SKILL.md`
- References:
  - `Mobile-Optomization-workflows/general-mobile-workflows/references/react-native-expo.md`
  - `Mobile-Optomization-workflows/general-mobile-workflows/references/gradle-build-pass-notes.md`
  - `Mobile-Optomization-workflows/general-mobile-workflows/references/mobile-security.md`

---

## 🧭 7. What This Repo Actually Covers

This repo already has strong workflow coverage for:

- Cost and pricing diagnosis
- Chrome-extension-specific diagnostic flows
- Security certification guidance and AI risk boundaries
- Endpoint and service-health auditing
- Git-safe docs and file-structure work
- Web design system planning and implementation
- Mobile delivery, release, and platform architecture

What it does **not** yet have as standalone skills:

- Generic feature builder
- Auth flow debugger
- Pure backend endpoint builder
- General-purpose refactor controller
- Safe commit generator outside docs/structure work

Those would be the next logical additions if you want this repo to match the broader skill taxonomy you outlined.
