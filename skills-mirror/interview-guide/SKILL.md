---
name: interview-guide
description: Generate structured, bias-reducing interview guide from JD with per-role panel assignment and jurisdiction-compliant forbidden-question register. Drafting and triage aid, not HR or employment-law
  advice.
argument-hint: --jd FILE --jurisdiction CODE [--panel-roles LIST] [--video] [update path/to/guide.md]
user-invocable: true
metadata:
  author: Product Org OS
  version: 1.0.0
  category: talent-acquisition
  skill_type: task-capability
  owner: recruiter
  primary_consumers:
  - ext-hr
  sensitive: true
inherits_pack: hr-ai-governance
---
# /interview-guide

## Purpose

`/interview-guide` produces a structured, bias-reducing interview guide derived from a role's job description. It generates per-competency question banks (behavioral preferred, hypothetical only with justification), per-question rubrics with strong/adequate/weak anchors, panel-role question assignment, a calibration and scoring protocol, a jurisdiction-specific forbidden-question register, and a proxy-laden rapport scanner that flags well-intentioned questions which leak protected-class signals. It is a **drafting and triage aid**, not HR advice, not employment-law advice, and not a candidate-scoring system.

**Design thesis (one sentence).** Structured interviews raise predictive validity AND reduce bias simultaneously; unstructured interviews have near-zero predictive validity and actively produce bias. This skill operationalizes structured interviewing, which is the single highest-leverage bias reducer in hiring that a product organization can install without inventing new methodology (Schmidt & Hunter 1998 meta-analysis; Levashina et al. 2014 structured interview review; EEOC structured-interview technical assistance — all public findings).

What it IS: a structured first pass that produces an interview guide a hiring manager, recruiter, and panel can review, calibrate on, and use, with every evaluation dimension grounded in the specific JD's essential functions, and every legally risky question flagged before the panel ever sees it.

What it is NOT: an Automated Employment Decision Tool (AEDT) under NYC Local Law 144 (it generates a guide, not a candidate score), a candidate scorecard, a resume screener, a reference-check template, a compensation discussion script, or a substitute for employment counsel on jurisdiction-specific forbidden-question edge cases.

This skill is governed by `hr-ai-governance` pack v1.0.1. Every guide generation run inherits the proxy register (Section 3.2), the audit log schema (Section 4.1), the AEDT neutral-source-faithful-language bright line (Section 6.2 #8), and the jurisdiction matrix (Section 8.1) from the pack. See the Pack Inheritance section below for the exact dependency map.

---

## When to Use

Invoke `/interview-guide` when you need to:

- Open a brand-new role's interview process and need a JD-derived guide that starts from structured questions rather than a lifted template
- Calibrate an interview panel before a loop (distribute questions so three panel members don't all ask the same behavioral question three times)
- Audit an existing interview process for bias (proxy-laden rapport questions, illegal questions, missing rubrics, hypothetical-heavy questioning)
- Expand an established process into a new jurisdiction (salary-history ban, Ban-the-Box, Illinois Video Interview Act) and need the forbidden-question register re-checked
- Refresh a guide because the JD materially changed (e.g., `/job-description-generator` updated the essential functions)

## When NOT to Use

Do NOT use `/interview-guide` when:

- You need to score, rank, or compare candidates — out of scope; scoring is individual-reviewer discretion at the structured debrief, not a skill output
- You need a **technical skill assessment** (coding exercise, case study, take-home work sample) — out of scope; see a dedicated technical-assessment skill (future)
- You need a **reference check** template — different workflow; reference checks have their own legal gates
- You need **candidate communication** templates (rejection, offer, interview scheduling) — out of scope
- You need a **behavioral assessment of existing employees** for promotion, discipline, or PIP — different workflow with different legal exposure; route to @performance-specialist
- You need **compensation conversation** framing — see `/comp-benchmark`
- You need a **legal opinion** on whether a specific question is enforceable under a specific state's employment law — out of scope; engage `@employment-counsel`

The skill deliberately sits DOWNSTREAM of `/job-description-generator` (the JD defines the evaluation dimensions the guide evaluates) and UPSTREAM of the panel interview itself (the guide is calibration material the panel uses; it is not a candidate score).

---

## Modes

### Create (default)

Generate a fresh interview guide from a JD, jurisdiction, and panel roles.

```
/interview-guide --jd Legionis/Product/jd-customer-success-lead.md --jurisdiction US-DE --panel-roles "hiring-manager,peer,cross-functional,hr"
/interview-guide --jd jds/senior-backend-engineer.md --jurisdiction US-IL --panel-roles "hiring-manager,peer,skip-level,hr" --video
```

### Update

Refresh an existing guide. Pass the path to the current guide file.

```
/interview-guide update Legionis/Product/interview-guide-customer-success-lead.md --jurisdiction US-NYC
```

Update mode re-runs the forbidden-question register (jurisdiction-specific), re-runs the proxy-laden rapport scanner, re-checks panel-role distribution balance, and produces a diff-aware findings list (new findings marked `[NEW]`, previously-surfaced-and-now-resolved findings marked `~~strikethrough~~`).

### Check

Scan an externally-drafted interview guide (one a hiring manager wrote on their own) without regenerating it. Produces findings only, no rewrite.

```
/interview-guide check path/to/manager-draft-guide.md --jurisdiction US-CA
```

---

## Required Inputs

The skill MUST collect the following before producing output. If any required input is missing, it asks the user rather than guessing.

| Input | Required | Example |
|---|---|---|
| JD file | Yes | `Legionis/Product/jd-customer-success-lead.md` (ideally output of `/job-description-generator`) |
| Jurisdiction | Yes | `US-DE`, `US-NYC`, `US-CA`, `US-CO`, `US-WA`, `US-IL`, `US-MA`, `EU-DE`, `UK`, `IL` |
| Panel roles | Yes | Comma-separated list from the canonical set: `hiring-manager`, `peer`, `cross-functional`, `skip-level`, `hr` |
| Video-interview flag | If applicable | `--video` — triggers Illinois Video Interview Act flow if jurisdiction is `US-IL` or any IL-resident candidates |
| Prior guide (Update/Check) | Yes in Update/Check mode | `Legionis/Product/interview-guide-customer-success-lead.md` |

**Jurisdiction is never defaulted.** If the user does not supply it, the skill asks. The jurisdiction determines which forbidden-question rules apply (salary history ban, Ban-the-Box, Illinois Video Interview Act, Colorado AI Act, EU AI Act, etc.), the applicable framework under `hr-ai-governance` Section 8.1, and which specific runtime warnings the output must carry.

**The JD is never summarized or inferred.** The skill reads the JD and derives competencies from the essential functions. If the JD has no essential functions, the skill refuses to proceed and asks the user to run `/job-description-generator` first. A guide derived from inferred competencies is not grounded in the role and cannot be defended as structured.

---

## Output Structure

Every `/interview-guide` output conforms to `sensitive-skill-guardrails.md` Section 3. Structure is non-negotiable.

### 1. Disclaimer + UPL Guardrail Block (top)

```
> ⚠️ **Not HR or employment-law advice.** This output is a drafting and triage aid generated by a product-organization skill, not HR counsel or employment counsel. No attorney-client relationship is created by its production or use. Jurisdiction-specific questions on forbidden-question rules, pre-conditional-offer limitations, video-interview consent and analysis, pregnancy / disability / national-origin protections, or enforceability require review by a licensed employment attorney in the relevant jurisdiction and by a qualified HR professional. Do not rely on this output as the sole basis for interviewing, evaluating, or hiring any candidate.
>
> **Jurisdiction Assumed:** {jurisdiction from the required input}. If your jurisdiction differs, treat every finding below as a hypothesis to verify with local counsel.
```

### 2. Guide Metadata block

A small labeled block under the disclaimer with:

- **Role**: role name (from the JD)
- **Source JD**: path to the JD file the guide was derived from
- **Jurisdiction**: as input (no default)
- **Panel Roles**: as input (canonical set)
- **Video Interview**: yes/no (if yes, Illinois Video Interview Act addendum is generated when IL applies)
- **Pack Inheritance**: `hr-ai-governance v{version}` (read at runtime)
- **Generation Timestamp**: ISO 8601 UTC
- **Governance Pack Version**: `hr-ai-governance v1.0.1+`
- **Behavioral : Hypothetical Ratio**: ratio as generated (target ≥ 3:1)

### 3. Competency List (from the JD)

A numbered list of the competencies the guide evaluates, each mapped back to a specific essential function in the JD. The skill does NOT invent competencies. If the JD has 6 essential functions, the guide has 4-8 competencies (some essential functions collapse into one competency; some single functions produce two competencies — e.g., "Run QBRs" produces both "executive-communication" and "account-strategy"). The mapping is explicit.

### 4. Question Bank (per competency)

For each competency, a block containing:

- **Competency name** and the JD essential function(s) it maps to
- **2-4 behavioral questions** — each phrased as "Tell me about a time when you..." grounded in a specific observable activity
- **0-1 hypothetical question** — only if the behavioral questions alone cannot probe a specific situation the role requires and the candidate would not plausibly have encountered. If present, the rationale for the hypothetical is stated inline.
- **Rubric** for each question with three anchors:
  - **Strong answer**: specific situation, specific candidate action, specific outcome with numbers or named artifacts
  - **Adequate answer**: specific situation and candidate action but vague outcome, OR specific action+outcome but situation is normalized
  - **Weak answer**: abstract, second-person ("we did X"), no specific situation, or visibly rehearsed
- **Standardized follow-up pattern**: the probe sequence the interviewer uses regardless of the candidate's answer (e.g., "What was your specific contribution?" → "How did you measure the outcome?" → "What would you do differently?")
- **Anti-pattern list**: answers that sound good but don't indicate the competency (e.g., "I led a team transformation" without specifics is the classic anti-pattern; it pattern-matches as strong but contains zero evaluable signal)

### 5. Panel Assignment Matrix

A table showing which questions belong to which panel role, with a distribution check. Panel role boundaries follow a standard division of labor:

| Panel Role | What they own |
|---|---|
| **Hiring manager** | Role-critical competencies derived from essential functions (the 1-2 competencies most central to the role) |
| **Peer** | Collaboration signals, day-to-day working behaviors, how the candidate handles disagreement and feedback |
| **Cross-functional** | Stakeholder management, communication across domains, handling of competing priorities |
| **Skip-level** | Strategic alignment, judgment under ambiguity, values alignment at the leadership level (if the role warrants it) |
| **HR** | Values fit (observable, not "culture fit"), compliance-neutral questions, candidate experience and questions from the candidate |

The **distribution check**: no single panel role asks more than 40% of the total questions in the guide. If one role exceeds 40%, the skill flags a P1 `panel-distribution-imbalance` finding and suggests redistribution. The 40% threshold exists because a single-role dominance pattern usually means the panel is not actually structured — it's a hiring manager interview with three witnesses.

### 6. Calibration Protocol

A three-stage protocol, non-negotiable:

1. **Pre-interview rubric share** — all panel members receive the rubric BEFORE the interview. Not after. Not during. Reviewers who see the rubric only after they interview are cargo-cult structured interviewing; their scores are retrospectively-rationalized first impressions.
2. **Independent scoring** — panel members score their own questions individually and record their scores in a private field BEFORE any debrief discussion. Groupthink is the single largest threat to structured-interview validity; the first panel member to speak anchors everyone else. Independent scoring breaks the anchor.
3. **Structured debrief** — a standard template for aggregating scores, flagging divergence (cases where two panel members scored the same candidate >2 anchor steps apart on the same competency, indicating either a rubric ambiguity or a bias signal), and recording the hire / no-hire / additional-interview decision with explicit rationale.

The protocol also records the **debrief template** fields the skill emits: per-competency aggregated score, divergence flag, overall hire/no-hire, rationale, dissenting opinions (named).

### 7. Forbidden Question Register (standard baseline + jurisdiction-specific)

A two-part list. The **standard federal baseline** applies everywhere in the US. The **jurisdiction-specific additions** are added on top, per Section 10 below.

Standard federal baseline (never legal in any US jurisdiction):

- Age / date of birth / year of school graduation
- National origin / citizenship (beyond work authorization confirmation)
- Religion / religious practices / dietary preferences
- Marital status / spouse / family plans / pregnancy / intent to have children
- Disability (any form) pre-conditional-offer — ADA
- Sexual orientation / gender identity
- Political affiliation / union membership — NLRA Section 7 (strict liability; any surfacing is direct evidence of discrimination)
- Housing / homeownership / commute details that proxy class
- Genetic information / family medical history — GINA (strict liability)

Each entry has a brief one-line rationale and a **correct alternative** where one exists. For example: "age / date of birth" → no correct alternative; **do not ask**. "Citizenship" → the only legal question is "Are you authorized to work in {country} without employer sponsorship, now and in the foreseeable future?"

### 8. Proxy-Laden Rapport Scanner Findings

Rapport-building questions are the single most common vector for well-intentioned bias leakage. A hiring manager who asks "where did you grow up" is not trying to discriminate — but the question elicits national-origin, age, and socioeconomic-class signals the hiring manager cannot un-see once given.

The scanner runs over every question in the generated guide (including any examples in the calibration protocol) and flags proxy-laden patterns. Output table:

| # | Question | Proxy | Protected Class Leaked | Severity | Neutral Alternative | Verdict |
|---|---|---|---|---|---|---|

Categories the scanner catches:
- `"where did you grow up"` / `"where are you from"` / `"what's your background"` → national origin, age, socioeconomic class
- `"tell me about your family"` / `"are you married"` / `"do you have kids"` → family status, gender
- `"what do you do on weekends"` / `"what are your hobbies"` (open-ended) → religion, disability, family status (this one is subtle; it's flagged P2 with a suggestion to scope to work-adjacent)
- `"where did you go to school"` as rapport (not as qualification) → age, socioeconomic class, national origin
- `"what do your parents do"` / `"how did you get into this field"` (if phrased to elicit family background) → socioeconomic class
- `"tell me about yourself"` (without structure) → open door to protected-class disclosure the candidate may make; the skill does not ban this but flags it P2 with a suggested structure ("Walk me through your last three years professionally")

### 9. Video-Interview Addendum (if `--video` flag or jurisdiction requires)

If the video-interview flag is set OR the jurisdiction is `US-IL` and video is plausible, the skill generates an addendum covering:

- **Candidate disclosure**: the exact notice text the candidate must receive before the interview, per Illinois Video Interview Act (820 ILCS 42/). Disclosure must cover: the use of video, any AI-assisted analysis, the candidate's right to refuse video.
- **Candidate consent**: how consent is recorded. Verbal is not sufficient under IL; written (electronic) is required.
- **Analysis limits**: what AI-assisted analysis is and is NOT permitted. Facial expression analysis is prohibited under some readings of IL law and is categorically flagged as P0 regardless of jurisdiction.
- **Deletion timelines**: IL requires deletion within 30 days of candidate request. The addendum records the deletion-request channel.
- **Accessibility**: video interviews must have an accessible alternative (phone or in-person) available on request, per ADA and EU AI Act Annex III accessibility obligations.

If video is flagged but jurisdiction is NOT `US-IL`, the addendum still generates (video-interview hygiene is good practice everywhere) but is noted as "best-practice, not statutory in this jurisdiction."

### 10. Jurisdiction-Specific Additions

Per the jurisdiction loaded from `hr-ai-governance` Section 8.1, the skill layers additional forbidden-question rules or process requirements on top of the standard baseline:

- **US-NYC / US-CA / US-MA / US-CO / US-WA / US-CT / US-HI / US-RI / US-MD / US-DC and others**: salary history ban — the skill adds "What is your current/prior compensation?" to the forbidden list and suggests the legal alternative: "What compensation range are you targeting for this role?"
- **Ban-the-Box states** (37+ US states + NYC Fair Chance Act + numerous municipal ordinances): criminal history questions are forbidden pre-conditional-offer. The skill adds a conditional-offer gate: criminal history questions may only appear in a post-offer flow, which is a different skill entirely.
- **US-IL (Illinois)**: Illinois Video Interview Act requirements (see Section 9). Also Illinois HB 3773 IHRA amendment (effective Jan 1, 2026) — if the interview process includes any AI-assisted scoring, analysis, or decision support, the AI tool itself is subject to HB 3773 obligations; this skill generates the guide, not the scoring system, so it notes the requirement and routes AI-scoring questions to @employment-counsel.
- **US-CO (Colorado)**: Colorado AI Act (SB 24-205, effective Feb 1, 2026) — if AI scoring is used downstream, pre-use consequential-decision notice is required. This skill notes the obligation and routes to @employment-counsel.
- **EU / UK**: GDPR Article 22 (automated decision-making) and EU AI Act Annex III point 4 (recruitment / selection) — high-risk system obligations attach to any scoring automation. Also, questions about pregnancy and family plans are forbidden under the Pregnant Workers Directive and UK Equality Act 2010 regardless of the federal US baseline.
- **IL (Israel)**: national-origin-adjacent questions (country of origin, religion, IDF service details) are flagged per Israeli Equal Employment Opportunity Law; IDF service may only be asked as "military service: yes/no" without country, unit, or duration, mirroring `hr-ai-governance` Section 3.2 proxy register.
- **All US**: PDA (Pregnancy Discrimination Act) and ADA forbid pregnancy, family, and disability questions. These are already in the standard baseline but the jurisdiction-additions section restates them for completeness.

### 11. `## Findings` (numbered)

Every flagged item from Steps 5-10 above gets a numbered finding in a unified findings list:

- **Finding #** / **Category** (proxy-laden-rapport, forbidden-question, hypothetical-without-justification, panel-distribution-imbalance, missing-rubric, missing-calibration, video-interview-compliance-gap, jurisdiction-specific)
- **What** — specific question, section, or structural gap
- **Why it matters** — the risk, implication, or bias mechanism
- **Severity** — P0 / P1 / P2
- **Suggested next step** — address / accept-with-risk / reject-as-hypothetical
- **Citation** — pointer to `hr-ai-governance` section, EEOC guidance, Schmidt & Hunter 1998, Gaucher et al., or jurisdiction statute

### 12. `## Reviewer Checklist`

Ten mandatory sign-off items before the guide is acted upon:

- [ ] Jurisdiction confirmed against role location and candidate residency
- [ ] JD verified as the source and reviewed for competency derivation accuracy
- [ ] Every question mapped to a competency and a rubric
- [ ] Behavioral-to-hypothetical ratio ≥ 3:1 (justify exceptions inline)
- [ ] Panel distribution reviewed; no single role > 40% of questions
- [ ] Forbidden question register reviewed against jurisdiction and candidate profile
- [ ] Proxy-laden rapport scanner findings addressed or explicitly accepted
- [ ] Calibration protocol confirmed: pre-interview rubric share scheduled, independent scoring mechanism in place, debrief template loaded
- [ ] Video-interview addendum reviewed (if applicable) including consent + analysis-limits + deletion timeline
- [ ] Employment counsel engaged for items in "Cannot Assess Without" that apply to this role or jurisdiction

### 13. `## Cannot Assess Without Licensed Counsel or Specialist`

Minimum 5 items:

- **Actual candidate interaction** — the guide pre-calibrates the rubric, but individual candidate answers require human judgment the skill cannot substitute for
- **Technical skill validation** — coding exercises, case studies, take-home work samples, architecture reviews — all out of scope; the guide evaluates behaviors, not technical proficiency
- **Reference checks** — different workflow with different legal exposure (consent gates, jurisdiction-specific defamation law)
- **Culture-add judgment** — the guide surfaces observable values-fit questions, but the hiring panel's collective judgment on culture-add is individual and not a skill output
- **Candidate-specific follow-ups** — deeper probes triggered by something the candidate said are context-dependent and require interviewer discretion
- **Jurisdictional edge cases** — any forbidden-question call that turns on a specific statute interpretation (e.g., whether a particular "acceptable use of criminal history" exception applies in a post-conditional-offer context in NYC) requires employment counsel
- **AI-assisted candidate scoring** — if the deployer is using any AI tool to score, rank, or recommend candidates, that tool is subject to its own governance (`hr-ai-governance` Section 6 AEDT wall); this skill does not generate scoring systems

### 14. Audit Log Entry

Emitted per `hr-ai-governance` Section 4.1 schema, with the fields relevant to this skill:

- `run_id`, `timestamp`, `skill_name` (`interview-guide`), `skill_version`, `governance_pack_version`
- `jurisdiction`
- `inputs_hash` — SHA-256 of the canonicalized input object (JD path + hash, jurisdiction, panel roles, video flag). NEVER raw candidate data — this skill doesn't see candidate data at guide-generation time.
- `input_type: interview_notes` (closest available enum value; the real type is `interview_guide`, recorded in `notes`)
- `proxies_detected` — from the proxy-laden rapport scanner, each flagged question becomes a proxies_detected entry
- `redactions_applied` — N/A for this skill (this is a generation skill, not an extraction skill)
- `hitl_reviewer` — authenticated identity of the hiring manager or recruiter who will review the guide before the panel sees it
- `hitl_decision`, `hitl_timestamp`, `hitl_rationale` — populated at HITL gate
- `downstream_action` — e.g., `published-to-panel`, `held-for-revision`, `routed-to-counsel`
- `signoff_path: standard`
- `retention_expiry` — computed from jurisdiction per Section 4.3

The skill refuses to run if the deployer's auth system cannot supply an authenticated `hitl_reviewer`.

---

## Method

The skill's generation flow is a 7-step pipeline. Order matters because later steps depend on earlier ones.

### Step 1 — Derive Competency List from JD Essential Functions

Read the JD (path required as input). Extract the essential functions list. For each essential function, derive one or more competencies. A competency is a named observable capability, not an abstract trait:

- **Good competency**: `executive-stakeholder-communication` (derived from "Run quarterly business reviews with top-decile accounts")
- **Bad competency**: `strong-communication` (abstract; does not pass the rubric-anchorable test)

The skill produces 4-8 competencies total. If the JD has fewer than 3 essential functions, the skill refuses and routes to `/job-description-generator` first — a JD with fewer than 3 essential functions is too thin to support a structured interview process.

### Step 2 — Generate Behavioral + Hypothetical Questions per Competency

For each competency, the skill generates:

- **2-4 behavioral questions** — phrased as "Tell me about a time when you..." followed by a specific observable activity the competency implies. Behavioral questions have higher predictive validity than hypothetical per the structured-interview literature (Schmidt & Hunter 1998 meta-analysis put structured behavioral interviews at r ≈ 0.51 vs. r ≈ 0.14 for unstructured interviews).
- **0-1 hypothetical question** — only if the competency requires probing a scenario the candidate is statistically unlikely to have encountered (e.g., "This role is the first of its kind — how would you approach the first 90 days?"). If no such scenario exists, the competency gets zero hypotheticals. A hypothetical without a justification line is automatically downgraded or removed.

The generated behavioral-to-hypothetical ratio must be **≥ 3:1 overall**. If it falls below, the skill flags it P1 and asks the user to justify the lower ratio (typical justification: the role has no direct precedent in any candidate's background).

### Step 3 — Build Rubric per Question (Strong / Adequate / Weak Anchors)

For each question, the skill writes three rubric anchors grounded in the expected answer shape:

- **Strong answer**: specific situation, specific candidate action, specific outcome with numbers or named artifacts
- **Adequate answer**: specific situation and candidate action but vague outcome, OR specific action+outcome but situation is normalized or hypothetical
- **Weak answer**: abstract, second-person ("we did X"), no specific situation, or visibly rehearsed (uses phrases like "in general I tend to...")

The rubric does NOT include the interviewer's "gut feel" — that is precisely what structured interviewing is designed to eliminate. If a rubric anchor cannot be stated without hedging ("this feels like a strong answer if..."), the question is not anchorable and the skill either rewrites the question or removes it.

### Step 4 — Assign Questions to Panel Roles

Using the panel roles the user supplied, the skill assigns each question to the role most appropriate for owning it:

- Hiring manager owns role-critical competencies (the 1-2 most central to the JD)
- Peer owns collaboration and day-to-day working behaviors
- Cross-functional owns stakeholder management across domains
- Skip-level owns strategic alignment and judgment under ambiguity (only if the role warrants a skip-level slot)
- HR owns values fit (observable), candidate questions, and compliance-neutral items

The skill runs the **40% distribution check**. If any single role exceeds 40% of the total questions, the skill flags the imbalance and suggests redistribution. If the user's supplied panel role list is small (e.g., just hiring-manager + peer), the 40% check is relaxed proportionally — with two roles, the threshold rises to 60% for either role, because a two-person panel cannot distribute evenly below that.

### Step 5 — Apply Forbidden-Question Register per Jurisdiction

Pull the standard federal baseline. Layer the jurisdiction-specific additions from `hr-ai-governance` Section 8.1. For each layer, the skill:

1. Scans the generated questions for any forbidden pattern (e.g., "Are you a US citizen?" → citizenship question → forbidden baseline)
2. Flags any found forbidden questions as P0 `forbidden-question` findings
3. Surfaces the legal alternative where one exists (e.g., "Are you authorized to work in {country} without employer sponsorship?")
4. For jurisdictions with salary-history ban: scans for "What is your current compensation?" and equivalents; surfaces "What compensation range are you targeting?" as the legal alternative
5. For Ban-the-Box jurisdictions: scans for criminal-history questions; if found, moves them to a separate post-conditional-offer flow and notes the gate
6. Emits the full forbidden-question register in the output so the panel sees both the forbidden list AND the jurisdiction layer

The register is informational output — its value is forcing the panel to see, in writing, which questions cannot be asked. Panels that don't see the register in advance tend to ask the forbidden questions anyway, usually during the rapport-building minutes.

### Step 6 — Scan Questions for Proxy-Laden Language (inherit `hr-ai-governance` Section 3.2)

Pull the proxy register from `hr-ai-governance` Section 3.2. For each question in the generated guide (including any hiring-manager rapport examples, skip-level questions, and HR values questions), the skill runs a proxy-pattern scan:

- Name of place ("where did you grow up") → national origin + age + SES
- Family terms ("tell me about your family") → family status + gender
- Open-ended hobbies → religion + disability + family status
- School-as-identity ("where did you go to school" used as rapport not qualification) → age + SES + national origin
- Parents' professions → SES + national origin
- Open self-description ("tell me about yourself" without structure) → open door to protected-class disclosure

Each flagged question gets a finding row (Section 8 output). The scanner is deliberately over-inclusive: it flags well-intentioned questions because the whole point of the scanner is to catch questions the panel would never self-censor. A P2 flag for "tell me about yourself" is not an accusation of bias — it is a nudge to structure the opener.

### Step 7 — Generate Calibration + Scoring + Debrief Structure

Assemble the protocol (Section 6 output). The skill:

1. Generates the pre-interview rubric share package (a one-page summary per panel member showing their questions + rubrics + anti-patterns)
2. Specifies the independent-scoring mechanism (scoring field per question, recorded before any panel discussion)
3. Generates the debrief template (per-competency aggregated score, divergence flag, overall decision, rationale, dissenting opinions field)
4. Adds the HITL gate hook — the guide cannot move from "draft" to "published-to-panel" without a recruiter or hiring manager sign-off per `hr-ai-governance` Section 10

---

## Quality Gates

The skill performs a 10-item self-check BEFORE emitting output. If any check fails, the output does not publish — it produces a structural finding instead, asking the user to fix the gap.

1. Every question has a named competency mapping back to a specific JD essential function
2. Every question has a strong/adequate/weak rubric
3. Behavioral-to-hypothetical ratio ≥ 3:1 (or justified exception inline)
4. Panel distribution: no single role asks > 40% of total questions (or > 60% in a 2-role panel, proportional for ≥ 3 roles)
5. Forbidden-question register applied per jurisdiction — zero forbidden questions in the final draft
6. Proxy-laden rapport scanner run — findings emitted
7. Calibration protocol includes pre-interview rubric share (not just a post-interview debrief)
8. Independent-scoring step exists in the calibration protocol
9. Structured debrief template present with divergence flag
10. Video-interview addendum present if `US-IL` jurisdiction or `--video` flag

These 10 checks are the quality gates. They run every invocation. There is no "express mode" that skips them.

---

## Pack Inheritance

This skill inherits the following from `hr-ai-governance` pack v1.0.1. Each dependency is a contract between the skill and the pack; if the pack updates, the skill re-validates against the updated version on next run.

| Section | What the skill inherits |
|---|---|
| **3.2 non-obvious proxy register** | The proxy-laden rapport scanner is seeded from the pack's Section 3.2 proxy list. Any proxy added to Section 3.2 automatically becomes a new rapport-scanner trigger in the next run. The skill does NOT author its own proxy list. |
| **4.1 audit log schema** | Every guide generation run emits a log record conforming to the canonical schema. `inputs_hash`, `jurisdiction`, `hitl_reviewer`, `signoff_path`, and `retention_expiry` are computed per the pack's rules. |
| **6.2 bright line #8 (neutral source-faithful language)** | This skill is NOT an AEDT — it generates a guide, not a candidate score. But the neutral-source-faithful-language bright line still applies: the skill does NOT add qualitative modifiers to the rubric anchors or the anti-pattern descriptions on its own authority. "significant," "substantial," "extensive," "strong" (as a model-inserted qualifier on the rubric text) etc. are banned. If the rubric anchor requires a modifier, the anchor is rewritten to describe the observable behavior instead. |
| **8.1 jurisdiction matrix** | Forbidden-question rules, video-interview-act obligations, salary-history bans, Ban-the-Box coverage, Colorado AI Act and Illinois HB 3773 gates, EU AI Act Annex III applicability, and GDPR Art. 22 considerations are all pulled from Section 8.1. The skill does NOT hard-code jurisdiction rules. |
| **10 HITL enforcement** | Gate placement per Section 10.3: HITL gate sits before the generated interview guide is sent to the panel. The recruiter or hiring manager is the reviewer. Illegal-question linter results and proxy-laden rapport scanner findings are shown inline at the gate. |
| **11.1 review cadence** | Subsequent-similar 72-hour substantive review under the Employment Counsel SLA. This is NOT first-of-type — the pack and `/resume-summarizer` carry first-of-type status. This skill inherits the established pack pattern. |

This skill is **NOT an AEDT**. It produces a guide, not a candidate decision. The AEDT wall from `hr-ai-governance` Section 6 applies by inheritance only — no novel AEDT surface is added. The skill cannot score candidates, rank candidates, or make hiring decisions. Any downstream use of AI scoring on candidate responses is out of scope and subject to the skill's own governance (see Cannot Assess Without).

---

## Delegation Patterns Available

### Default: Pattern 1 Consultation

When a specific element of the guide needs specialist input, the skill spawns a consultation per `delegation-protocol.md` Pattern 1:

| Trigger | Spawn |
|---|---|
| Jurisdictional forbidden-question edge cases (e.g., "Can I ask about a specific certification that correlates with age in {jurisdiction}?") | 👔 Employment Counsel |
| Salary conversation framing (where to place it in the interview loop, how to phrase range-targeting questions in post-salary-history-ban jurisdictions) | 💵 Compensation Analyst |
| Panel calibration methodology (divergence thresholds, training patterns for new panel members, scoring bias audits) | 📊 People Analyst |
| Illinois Video Interview Act interpretation (consent form language, deletion-request channel design, analysis-limit specifics) | 👔 Employment Counsel |
| Ban-the-Box post-conditional-offer flow (gating criminal-history questions) | 👔 Employment Counsel |
| Pregnancy / caregiver / disability accommodation-disclosure during interview | 👔 Employment Counsel + 🧑‍🤝‍🧑 CHRO |

Consultations are attributed in the findings section: "I consulted 👔 Employment Counsel, who noted that in {jurisdiction}, pre-conditional-offer criminal history questions are prohibited by {statute} and the safe alternative is to move the question to the post-offer flow." Ownership of the interview guide stays with Recruiter.

### Adversarial Review

NOT applicable at this version. Adversarial Review (Pattern 5) is reserved for near-final deliverables with high-stakes, uncapped exposure (enterprise contracts, M&A documents, pricing commitments). An interview guide draft going to a human hiring panel is neither near-final nor uncapped-exposure — it is a draft that a human reviewer revises and the panel then uses with individual discretion.

If a specific guide becomes high-stakes (e.g., a senior executive search with public press attention, a role in a regulated industry with additional forbidden-question statutes, or a role in a jurisdiction with active litigation risk), the hiring manager can request `/interview-guide --escalate-adversarial` which routes to `@employment-counsel` for a Pattern 5 review BEFORE the panel sees the guide. This is a manual escalation, not automatic.

---

## ROI Framing

ROI for `/interview-guide` is reported as **"time saved on drafting and triage of a structured, bias-reducing interview guide"** — NEVER "time saved on HR review" or "time saved on employment-law review."

HR blended rate: $150/hr per `feedback_roi_rates.md`. Default $150/hr for a Phase 4A HR triage involving JD-to-competency derivation + behavioral question generation with rubrics + panel assignment + forbidden-question register + proxy-laden rapport scan + calibration protocol.

Time-saved baseline: a careful, structured, bias-scanned interview guide that starts from the JD, generates rubric-anchored behavioral questions, assigns them across the panel, runs the forbidden-question register, and produces a calibration protocol is **~3-4 hours** of manual drafting and triage time for a recruiter working with a hiring manager. Simpler refreshes (Update mode on an existing guide after a JD tweak) are ~1-1.5 hours baseline. Complex cases (multi-jurisdictional posting, regulated industry, video-interview requirements, executive search) are 5+ hours baseline.

The ROI tracks ONLY the time the skill saves on drafting the structured artifact, not the substantive HR or legal review time. The panel calibration, the actual interviews, and the debrief all happen in full and are owned by humans.

Example ROI line for a standard guide generation:

```
⏱️ ~3 hrs saved on drafting and triage in 55s, 17k tkns ~$1.0 cost, Value ~$450
```

---

## Attribution and Maintenance

**Owner**: 🎯 Recruiter. The skill's drafting, scanner, and panel-assignment logic is Recruiter's accountability.

**Consumers** (skills / gateways that invoke this skill):

- `ext-hr` — HR team gateway, primary user

New consumers require a frontmatter update and a one-line note in the consuming gateway's or skill's dependency list.

**Authoring**: First-principles. This skill was authored from scratch during Phase 4A as the third HR skill under the `hr-ai-governance` pack (after `/comp-benchmark` and `/job-description-generator`). Structured-interview methodology is grounded in public academic literature:

- **Schmidt, F. L., & Hunter, J. E. (1998)**. "The Validity and Utility of Selection Methods in Personnel Psychology: Practical and Theoretical Implications of 85 Years of Research Findings." *Psychological Bulletin*, 124(2), 262-274. Meta-analysis establishing structured-interview validity at r ≈ 0.51 vs. unstructured at r ≈ 0.14.
- **Levashina, J., Hartwell, C. J., Morgeson, F. P., & Campion, M. A. (2014)**. "The Structured Employment Interview: Narrative and Quantitative Review of the Research Literature." *Personnel Psychology*, 67(1), 241-293. Confirmation and extension of Schmidt & Hunter with 2000s-era meta-analytic data.
- **EEOC structured-interview technical assistance** — public guidance on structured interviewing as a bias-reduction mechanism under Title VII and ADEA. Last verified: 2026-04-11.
- **Gaucher, Friesen, and Kay (2011)** — gendered-language research previously cited by `/job-description-generator`; informs the rubric-language neutrality check.
- **Illinois Artificial Intelligence Video Interview Act (820 ILCS 42/)** — statute referenced in the video-interview addendum.
- **EEOC Uniform Guidelines on Employee Selection Procedures (1978)** — adverse-impact baseline; applies to any selection procedure including structured interviews.

No content was lifted from vendor interview-guide tools (Gem, Greenhouse, Lever, Ashby, SmartRecruiters, Textio, etc.). The question banks, rubric anchors, and panel-assignment logic are derived first-principles from the JD input plus the structured-interview literature.

**Dependency on the pack**: The skill reads from `hr-ai-governance` at every invocation. When the pack's Section 3.2 proxy register, Section 4.1 audit log schema, Section 6.2 bright line #8, or Section 8.1 jurisdiction matrix is updated, the skill picks up the new content on the next run. The pack version is recorded in every audit log entry.

**Updates**: Via the two-pass publication gate defined in `sensitive-skill-guardrails.md` Section 4. Pass 1 (scaffolding check) — 📋 Director of HR, 15 minutes, binary GO / REWORK. Pass 2 (substantive check) — 👔 Employment Counsel, **72-hour subsequent-similar SLA** (this is NOT first-of-type; the pack, `/resume-summarizer`, and `/job-description-generator` carry the first-of-type burden).

Minor edits (typos, formatting, proxy-list additions sourced from the pack's Section 3.2 updates) can bypass Pass 2. Any edit touching: severity thresholds, forbidden-question register structure, rubric-anchor taxonomy, panel-distribution threshold (40% / 60%), calibration protocol requirements, or the HITL gate placement — requires a full Pass 2 substantive review by Employment Counsel.

**Changelog**: Maintained at the bottom of this file.

---

## Example Invocation

```
User: /interview-guide --jd Legionis/Product/jd-customer-success-lead.md --jurisdiction US-DE --panel-roles "hiring-manager,peer,cross-functional,hr"

/interview-guide v1.0.0 — loading:
  - JD: Legionis/Product/jd-customer-success-lead.md (6 essential functions; source: /job-description-generator output)
  - Jurisdiction: US-DE (no salary-history ban, no Ban-the-Box complication, standard federal baseline)
  - Panel roles: hiring-manager, peer, cross-functional, hr
  - Video flag: no
  - Governance pack: hr-ai-governance v1.0.1

Running pipeline:
  Step 1: Competency derivation (6 essential functions → 5 competencies)
  Step 2: Question generation (14 behavioral + 2 hypothetical, ratio 7:1)
  Step 3: Rubric construction (16 questions × 3 anchors = 48 rubric anchors)
  Step 4: Panel assignment (hiring-manager 5, peer 4, cross-functional 4, hr 3 — distribution within 40% threshold)
  Step 5: Forbidden-question register applied (standard federal baseline only for US-DE)
  Step 6: Proxy-laden rapport scanner (3 planted proxy questions in test input; all 3 caught)
  Step 7: Calibration + scoring + debrief structure generated

Producing output at:
  Legionis/Product/interview-guide-birth-test-2026-04-11.md

10/10 quality gates passed.

⏱️ ~3 hrs saved on drafting and triage in 55s, 17k tkns ~$1.0 cost, Value ~$450
```

---

## Changelog

- **1.0.0 (2026-04-11)** — Initial authoring. First-principles during Phase 4A as the third HR skill under the `hr-ai-governance` pack (after `/comp-benchmark` and `/job-description-generator`). Authored by 🎯 Recruiter. Methodology grounded in Schmidt & Hunter 1998 meta-analysis, Levashina et al. 2014 structured-interview review, and EEOC structured-interview technical assistance (all public). Question-bank taxonomy, rubric-anchor pattern, panel-assignment boundaries, forbidden-question register, and proxy-laden rapport scanner derived first-principles. Subsequent-similar 72-hour Pass 2 review under Employment Counsel SLA. Scaffolding review by 📋 Director of HR. Birth-tested against a Legionis Customer Success Lead role (see `Legionis/Product/interview-guide-birth-test-2026-04-11.md`).
