---
name: job-description-generator
description: Generates neutral, jurisdiction-compliant job descriptions with gender-coded language scanner, essential-vs-preferred enforcement, and comp band alignment. Drafting and triage aid, not HR or
  employment-law advice.
argument-hint: --role NAME --jurisdiction CODE [--comp-band FILE] [--essential-functions FILE] [update path/to/jd.md]
user-invocable: true
metadata:
  author: Product Org OS
  version: 1.0.0
  category: talent-acquisition
  skill_type: task-capability
  owner: recruiter
  primary_consumers:
  - ext-hr
  - interview-guide
  - comp-benchmark
  sensitive: true
co_owner: compensation-analyst
inherits_pack: hr-ai-governance
---
# /job-description-generator

## Purpose

`/job-description-generator` produces a neutral, jurisdiction-aware job description from a set of role requirements. It runs a gender-coded language scanner, a non-neutral framing scanner (age / disability / citizenship / culture-fit / degree), enforces separation of essential versus preferred requirements, checks comp-band-to-title alignment, and verifies pay-transparency compliance for the declared jurisdiction. It is a **drafting and triage aid**, not HR advice, not employment-law advice, and not a recommendation that any specific candidate is or is not qualified.

What it IS: a structured first pass that produces a JD draft a human recruiter can review, edit, and own, with every bias-adjacent choice made explicit as a finding rather than buried in the prose.

What it is NOT: an Automated Employment Decision Tool (AEDT) under NYC Local Law 144, a candidate-facing system, a resume screener, an interview guide, a compensation analysis, or a substitute for employment counsel on jurisdiction-specific pay-transparency or protected-class questions.

This skill is governed by `hr-ai-governance` pack v1.0.1. Every generation run inherits the proxy register (Section 3.2), audit log schema (Section 4.1), AEDT neutral-source-faithful-language bright line (Section 6.2 #8), and jurisdiction matrix (Section 8.1) from the pack. See the Pack Inheritance section below for the exact dependency map.

---

## When to Use

Invoke `/job-description-generator` when you need to:

- Open a brand-new role and need a JD draft that starts from neutral language rather than a lifted template
- Refresh an existing JD that was authored before pay-transparency rules landed in the deployment jurisdiction
- Check an externally-drafted JD for gender-coded language, age-coded language, or required-vs-preferred bloat before posting
- Convert a legacy JD from a jurisdiction without pay transparency to one that requires it (e.g., posting a role in NYC that was originally written for Texas)
- Validate that a JD's stated seniority ("Senior," "Lead," "Staff") is consistent with the comp band the hiring manager expects

## When NOT to Use

Do NOT use `/job-description-generator` when:

- You need to screen, summarize, rank, or score incoming resumes against the JD → use `/resume-summarizer` (explicit AEDT wall; see `hr-ai-governance` Section 6)
- You need to build the interview guide that evaluates candidates against this JD → use `/interview-guide`
- You need compensation analysis, pay-gap audit, or salary-band construction → use `/comp-benchmark`
- You need performance evaluation criteria or a PIP framework → out of scope; see `/performance-specialist` consultations
- You need org design or headcount planning — out of scope; see `@chro`
- You need a legal opinion on whether a specific JD requirement is enforceable under a specific state's employment law → out of scope; engage `@employment-counsel`

The skill deliberately sits UPSTREAM of `/interview-guide` (the JD defines the evaluation dimensions) and DOWNSTREAM of `/comp-benchmark` (the comp band feeds the JD's pay range when pay transparency applies).

---

## Modes

### Create (default)

Generate a fresh JD from scratch given role, jurisdiction, essential functions, seniority level, and (if pay transparency applies) comp band.

```
/job-description-generator --role "Customer Success Lead" --jurisdiction US-DE
/job-description-generator --role "Senior Backend Engineer" --jurisdiction US-NYC --comp-band comp-bands/backend-senior.json
```

### Update

Refresh an existing JD. Pass the path to the current JD file.

```
/job-description-generator update Legionis/Product/jd-customer-success-lead.md --jurisdiction US-NYC
```

Update mode re-runs all scanners against the current JD, preserves section structure where possible, and produces a diff-aware findings list (new findings marked `[NEW]`, previously-surfaced-and-now-resolved findings marked `~~strikethrough~~`).

### Check

Scan an externally-drafted JD (one a hiring manager wrote on their own) without regenerating it. Produces findings only, no rewrite.

```
/job-description-generator check path/to/manager-draft.md --jurisdiction US-CA
```

---

## Required Inputs

The skill MUST collect the following before producing output. If any required input is missing, it asks the user rather than guessing.

| Input | Required | Example |
|---|---|---|
| Role name / working title | Yes | "Customer Success Lead" / "Senior Backend Engineer" |
| Jurisdiction | Yes | `US-DE`, `US-NYC`, `US-CA`, `US-CO`, `US-WA`, `US-IL`, `EU-DE`, `UK`, `IL` |
| Essential functions list | Yes | ≥ 3 items describing the core job duties a person in this role MUST perform |
| Seniority level | Yes | IC2 / IC3 / IC4 / IC5 / Manager / Senior Manager / Director |
| Team context | If known | "5-person customer success org, reports to VP Customer Success, cross-functional with sales and product" |
| Comp band (min / mid / max) | Required if jurisdiction requires pay transparency | `$130,000–$170,000 base + equity` |
| Prior JD (for Update/Check) | Yes in Update/Check mode | `Legionis/Product/jd-customer-success-lead.md` |
| Work arrangement | Yes | Remote / Hybrid / On-site + timezone expectations |
| Visa sponsorship policy | If known | "Sponsorship available for H-1B transfers only" — surfaces a "Cannot Assess Without" item |

**Jurisdiction is never defaulted.** If the user does not supply it, the skill asks. The jurisdiction determines pay-transparency obligations, the applicable framework under `hr-ai-governance` Section 8.1, and which specific runtime warnings the output must carry.

**Essential functions are never inferred.** The skill does not guess what a "Customer Success Lead" does; it requires the user to supply the essential functions, because essential functions are the ADA-relevant foundation of the JD. Inferred essential functions are a disability-discrimination exposure vector.

---

## Output Structure

Every `/job-description-generator` output conforms to `sensitive-skill-guardrails.md` Section 3. Structure is non-negotiable.

### 1. Disclaimer + UPL Guardrail Block (top)

```
> ⚠️ **Not HR or employment-law advice.** This output is a drafting and triage aid generated by a product-organization skill, not HR counsel or employment counsel. No attorney-client relationship is created by its production or use. Jurisdiction-specific questions on pay transparency, protected-class signaling, essential-function framing, ADA compliance, or enforceability require review by a licensed employment attorney in the relevant jurisdiction and by a qualified HR professional. Do not rely on this output as the sole basis for posting, recruiting, interviewing, or any employment decision.
>
> **Jurisdiction Assumed:** {jurisdiction from the required input}. If your jurisdiction differs, treat every finding below as a hypothesis to verify with local counsel.
```

### 2. JD Metadata block

A small labeled block under the disclaimer with:

- **Role**: title as input
- **Jurisdiction**: as input (no default)
- **Seniority Level**: IC2 / IC3 / IC4 / IC5 / Manager / Senior Manager / Director
- **Comp Band**: min/mid/max as input, or `[not supplied — jurisdiction does not require pay transparency]`
- **Pay Transparency Required**: `yes` / `no` (derived from Section 8.1 jurisdiction matrix + Section 2 of this skill)
- **Pack Inheritance**: `hr-ai-governance v{version}` (read at runtime)
- **Generation Timestamp**: ISO 8601 UTC
- **Governance Pack Version**: `hr-ai-governance v1.0.1+`
- **Scanner Wordlist Version**: Gaucher et al. 2011 + non-obvious framing extensions (see Method Step 5)

### 3. The JD Draft

Structured sections in this order:

1. **About the role** — 2-3 sentence framing, neutral language, no qualitative modifiers added by the model on its own authority
2. **Essential functions** — numbered list, one function per item, each item expressed as an observable activity ("Lead weekly customer health reviews" not "Own customer success")
3. **Preferred qualifications** — distinct from essential functions, explicitly labeled as preferred, each with an "or equivalent experience" alternative where a degree is listed
4. **How we work** — work arrangement, timezone expectations, collaboration style (no culture-fit language; culture ADD framing)
5. **Compensation** — pay range if jurisdiction requires it; explicit statement of equity / benefits if applicable; omitted if jurisdiction does not require and user did not supply a band
6. **Equal opportunity statement** — neutral, jurisdiction-appropriate language (US → EEOC; EU → GDPR + AI Act notice; IL → PPL-appropriate)

Every line of the JD is the skill's structured extraction of the user's input. The skill does NOT add adjectives, qualitative modifiers, or unsupported claims. If the user's input does not support a line, the skill does not write the line.

### 4. `## Scanner Findings`

Every flagged term gets a row in a table with:

- **Finding #**
- **Category** — gender-coded (masculine) / gender-coded (feminine) / age-coded / disability-coded / citizenship-coded / culture-fit / degree-no-alternative / comp-band-title-mismatch / pay-transparency-missing / essential-preferred-bleed / qualitative-modifier-inserted / structural-finding
- **Term or passage**
- **Where it appears** — section of the JD
- **Severity** — P0 / P1 / P2
- **Why it matters** — the risk or implication
- **Suggested neutral alternative** — or "remove" for terms without a neutral replacement
- **Verdict** — address / accept-with-risk / reject-as-hypothetical

The scanner findings are the core bias-reduction output of the skill. They are how the hiring manager sees what the skill flagged and what it suggested. Structural findings (empty essential functions list, comp band not matching stated seniority, missing pay range in a pay-transparency jurisdiction) appear in the same table with `structural-finding` category.

### 5. `## Essential vs. Preferred Classification Report`

A two-column table showing what the skill classified as essential vs. preferred, with a one-line rationale for each. The hiring manager reviews this table before approving the JD, because the 8/8 rule (over-requiring narrows the pipeline disproportionately for groups that apply only when they meet 100% of requirements) makes this classification load-bearing. Items that appear in "essential" get a follow-up question: "Is this truly essential, or can a candidate learn it in the first 90 days?"

### 6. `## Comp Band Alignment Report`

Co-owner contribution from 💵 Compensation Analyst. If a comp band was supplied, this section records:

- The stated seniority level
- The supplied comp band (min / mid / max)
- The alignment verdict: `aligned` / `title-band-mismatch` / `cannot-assess`
- If `title-band-mismatch`: the specific conflict (e.g., "Title says 'Lead' which implies IC5+ but band midpoint is at IC3 market") and suggested resolution (adjust title OR adjust band)
- If `cannot-assess`: the reason (e.g., "No market data supplied for 'Customer Success Lead' at this seniority level in this geography — run /comp-benchmark first")

### 7. `## Pay Transparency Compliance Status`

- Jurisdiction → pay transparency rule (e.g., `US-NYC → NYC DCWP pay-transparency required`, `US-DE → no pay-transparency rule in force`)
- Status: `compliant` / `non-compliant` / `not-applicable`
- If `non-compliant`: the skill REFUSES to emit a final JD. The output is a finding, not a draft. The user must supply a comp band before the skill proceeds.

### 8. `## Reviewer Checklist`

Seven mandatory sign-off items before the JD is acted upon:

- [ ] Jurisdiction confirmed against role location and candidate residency
- [ ] Essential functions list reviewed by the hiring manager and confirmed ADA-defensible
- [ ] Every P0 scanner finding addressed or explicitly accepted-with-risk by named approver
- [ ] Essential-vs-preferred classification reviewed; any "essential" item that could be learned in 90 days reclassified as preferred
- [ ] Comp band alignment verdict reviewed (if supplied)
- [ ] Pay transparency compliance status verified against the jurisdiction
- [ ] Employment counsel engaged for items in "Cannot Assess Without" that apply to this role

### 9. `## Cannot Assess Without Licensed Counsel or Specialist`

Minimum 5 items. Examples:

- Enforceability of non-compete clauses in {jurisdiction} — out of scope; requires employment counsel
- Actual market compensation data for {role} in {geography} — requires `/comp-benchmark`
- Team composition and culture fit — out of scope; culture fit is NOT a valid preference
- Individual hiring manager preferences that are not observable job-performance criteria — out of scope; not a valid JD input
- Competitive intelligence on other active JDs in the market — out of scope
- Visa sponsorship policy and immigration law — requires employment counsel + immigration counsel
- ADA reasonable-accommodation boundaries for the essential functions — requires employment counsel for any specific candidate accommodation request

### 10. Audit Log Entry

Emitted per `hr-ai-governance` Section 4.1 schema, with the fields relevant to this skill:

- `run_id`, `timestamp`, `skill_name`, `skill_version`, `governance_pack_version`
- `jurisdiction`
- `inputs_hash` — SHA-256 of the canonicalized role-input object (role, jurisdiction, essential-functions, seniority, comp-band-hash). NEVER raw candidate data — this skill doesn't see candidate data.
- `input_type: job_description`
- `proxies_detected` — from the scanner findings, each flagged term becomes a proxies_detected entry
- `redactions_applied` — N/A for this skill (this is a generation skill, not an extraction skill)
- `hitl_reviewer` — authenticated identity of the recruiter or hiring manager who will review
- `hitl_decision`, `hitl_timestamp`, `hitl_rationale` — populated at HITL gate
- `downstream_action` — e.g., `published-to-careers-page`, `held-for-revision`
- `signoff_path: standard`
- `retention_expiry` — computed from jurisdiction per Section 4.3

The skill refuses to run if the deployer's auth system cannot supply an authenticated `hitl_reviewer`.

---

## Method

The skill's generation flow is a 7-step pipeline. Order matters because later steps depend on earlier ones.

### Step 1 — Load Jurisdiction Rules

Read the jurisdiction from the required input. Look up the applicable row in `hr-ai-governance` Section 8.1. Extract:

- Pay-transparency requirement (yes / no)
- Pay-transparency specifics (salary range required on posting, or range on request, or range in interview process)
- Protected-class signaling rules specific to the jurisdiction (e.g., CA and NY have broader protected classes than US federal baseline)
- Runtime warning block to emit (e.g., EU → Section 7.3 EU AI Act high-risk notice)
- Retention period for the audit log entry

If the jurisdiction is not in the matrix, the skill blocks and routes to @employment-counsel per Section 11.1.

### Step 2 — Accept Role Requirements; Enforce Essential-vs-Preferred Separation

Read the essential functions list. For each item:

- Is it phrased as an observable activity? (verb + object, not an abstract noun)
- Is it something the skill can verify against other inputs, or is it abstract ("must be a team player")?
- Could it be learned in the first 90 days of the role? If yes → flag as `essential-preferred-bleed`, suggest reclassification as preferred

The skill does NOT add essential functions the user did not supply. Inferred essential functions are an ADA-compliance exposure vector.

### Step 3 — Generate JD Draft with Neutral Source-Faithful Language

Write the JD sections in order. Every line is grounded in a specific user input. The skill does NOT add qualitative modifiers on its own authority (per `hr-ai-governance` Section 6.2 bright line #8). Banned model-inserted adjectives include: "significant," "substantial," "extensive," "strong," "impressive," "deep," "broad," "notable," "accomplished," "proven," and any equivalent qualitative modifier.

If the user supplied a modifier explicitly ("we need someone with significant experience"), the skill retains it verbatim and flags it as a finding ("significant" is a qualitative modifier supplied by the user; consider specifying a minimum year count instead).

### Step 4 — Run Gender-Coded Language Scanner

Wordlist source: Gaucher, Friesen, and Kay (2011), "Evidence That Gendered Wording in Job Advertisements Exists and Sustains Gender Inequality," *Journal of Personality and Social Psychology*. Public academic citation, not a vendor tool.

Masculine-coded (flagged as `gender-coded (masculine)`):
`aggressive, ambitious, analytical, assertive, athletic, autonomous, boast, challenging, competitive, confident, courageous, decide, decisive, determined, dominant, driven, fearless, forceful, greedy, headstrong, hierarchical, hostile, impulsive, independent, individualistic, intellectual, lead, leader, logic, logical, objective, opinionated, outspoken, persistent, principled, reckless, self-confident, self-reliant, self-sufficient, stubborn, superior`

Feminine-coded (flagged as `gender-coded (feminine)`):
`affectionate, cheer, collaborate, committed, communal, compassionate, connect, considerate, cooperative, dependable, emotional, empathetic, feel, flatterable, gentle, honest, interpersonal, interdependent, kind, kinship, loyal, modest, nag, nurturing, pleasant, polite, quiet, responsible, sensitive, submissive, supportive, sympathetic, tender, together, trust, trustworthy, understanding, warm, whiny, yield`

For each match, the scanner flags the term, records its location in the JD, suggests a neutral alternative (e.g., "leader" → "owns outcomes," "collaborative" → "works across functions," "aggressive" → "outcome-focused"), and sets severity based on context: P1 if the term appears in essential functions or required qualifications; P2 if it appears in the "about the role" framing.

**Balance rule**: if masculine-coded count exceeds feminine-coded count by more than 3, OR vice versa, the overall JD is flagged P0. The empirical finding (Gaucher et al.) is that lopsided language — particularly masculine-coded imbalance — measurably reduces application rates from the under-represented gender.

### Step 5 — Run Non-Neutral Framing Scanner

Beyond the gender-coded wordlist, the skill scans for:

| Category | Trigger phrases | Severity | Neutral alternative |
|---|---|---|---|
| Age-coded | "digital native," "recent graduate" (as a requirement), "young team," "energetic environment," "N+ years exactly" | P1 | "Comfortable with modern SaaS tooling" / "N+ years minimum" / omit |
| Age-coded (tenure ceiling) | "early-career," "max 5 years experience" (unless a genuine junior-only program with a legal basis) | P0 | Remove the ceiling; describe the scope instead |
| Disability-coded | "must stand 8 hours," "perfect vision required," "must lift 50 lbs" without an essential-function rationale | P0 | Remove unless tied to a named essential function; if retained, link to the specific essential function |
| Citizenship-coded | "US citizens only," "green card holders only" without ITAR / export-control or government-clearance basis | P0 | Remove unless a documented legal basis (ITAR, public-trust clearance) applies; flag for employment counsel review |
| Culture-fit | "culture fit," "work hard play hard," "family," "bro culture," "rockstar team" | P1 | Replace with "culture ADD" framing: "We value {observable behavior}" |
| Degree-no-alternative | "BA/BS required" without "or equivalent experience" | P1 | Add "or equivalent experience" — removes an unnecessary filter for career-changers |
| Qualitative modifier inserted | Model-generated "significant," "substantial," "extensive," etc. | P0 | Remove — violates `hr-ai-governance` Section 6.2 bright line #8 |
| Over-requiring | More than 8 "required" items when 4-5 are genuinely essential | P1 | Reclassify non-essential items as preferred (the 8/8 rule) |

### Step 6 — Comp Band Alignment Check (co-owner contribution)

I consulted **💵 Compensation Analyst** on the title-to-band consistency logic. The alignment check:

1. Read the stated seniority (e.g., "Senior," "Lead," "Staff," "Principal")
2. Read the supplied comp band (min / mid / max)
3. Map the seniority to an expected band range (this mapping is owned by @compensation-analyst and lives in the comp-benchmark pack; this skill consumes it as a dependency)
4. If the supplied band is > 20% below the expected range for the stated seniority → flag `title-band-mismatch` P0: "Title says {X} which implies IC{N}+ market rate; supplied band midpoint is at IC{N-1}. Either adjust the title to match the band, or adjust the band to match the title."
5. If the supplied band is > 20% above the expected range → flag `title-band-overpay` P1: "Band is above market for stated seniority. Confirm this is deliberate (retention hire, scarce skill, high-cost geography) or adjust."
6. If market data is not available for the specific role + geography → return `cannot-assess` and surface "Run /comp-benchmark first" as the suggested next step.

The alignment check is load-bearing because title inflation (calling a mid-level role "Senior" or "Lead" without the comp to match) is a well-known hiring anti-pattern that wastes recruiter cycles on candidates who will reject the offer once the band is disclosed — which, under pay-transparency laws, happens at application time, not at offer stage.

### Step 7 — Pay Transparency Compliance Check

Per the jurisdiction loaded in Step 1:

- If the jurisdiction requires pay-range-on-posting: verify a comp band was supplied; verify it appears in the Compensation section of the JD draft; verify the format matches the jurisdiction's rule (e.g., CA requires "good faith" range; NYC requires min and max).
- If the jurisdiction requires pay-range-on-request: the skill notes the obligation and advises the recruiter to have the range ready for any candidate who asks.
- If the jurisdiction does not require pay transparency: the skill does NOT require a comp band as input, BUT if a comp band is supplied, it still runs Step 6 alignment.
- If compliance status is `non-compliant`: the skill REFUSES to emit a final JD. The output becomes a finding: "Cannot generate final JD for {jurisdiction} without comp band."

---

## Quality Gates

The skill performs a 10-item self-check BEFORE emitting output. If any check fails, the output does not publish — it produces a structural finding instead, asking the user to fix the gap.

1. Jurisdiction declared in the metadata block
2. Essential functions list is non-empty and distinct from preferred
3. No masculine-coded / feminine-coded imbalance > 3 terms
4. No age-coded, disability-coded, or citizenship-coded red flags at P0
5. No culture-fit language — culture-add framing only
6. Every degree requirement has an "or equivalent experience" alternative
7. Pay range present if the jurisdiction requires pay transparency
8. Comp band (if supplied) matches the stated seniority level within the tolerance band
9. No qualitative modifiers inserted by the model on its own authority (`hr-ai-governance` Section 6.2 #8 enforcement)
10. Audit log entry generated with a valid `hitl_reviewer` identity

These 10 checks are the quality gates. They run every invocation. There is no "express mode" that skips them.

---

## Pack Inheritance

This skill inherits the following from `hr-ai-governance` pack v1.0.1. Each dependency is a contract between the skill and the pack; if the pack updates, the skill re-validates against the updated version on next run.

| Section | What the skill inherits |
|---|---|
| **3.2 non-obvious proxy register** | The scanner wordlists are seeded from the pack's standard + non-obvious proxy lists. The skill does NOT author its own proxy register. Any proxy added to Section 3.2 automatically becomes a new scanner trigger in the next run. |
| **4.1 audit log schema** | Every generation run emits a log record conforming to the canonical schema. `inputs_hash`, `jurisdiction`, `hitl_reviewer`, `signoff_path`, and `retention_expiry` are computed per the pack's rules, not per this skill. |
| **6.2 bright line #8 (neutral source-faithful language)** | The model is prohibited from inserting qualitative modifiers on its own authority. "significant," "substantial," "extensive," "strong," "impressive," "deep," "broad," "notable," "accomplished," "proven" (and semantic equivalents) are banned as model-generated additions. The skill enforces this as a quality gate (check #9) and as a scanner finding category (`qualitative-modifier-inserted`). |
| **8.1 jurisdiction matrix** | Pay-transparency obligations, retention periods, runtime warnings, and HITL requirements are all pulled from Section 8.1. The skill does NOT hard-code jurisdiction rules. |
| **10 HITL enforcement** | Gate placement per Section 10.3: HITL gate sits before the generated JD is saved or emitted for publication. The recruiter or hiring manager is the reviewer. Scanner findings are shown inline at the gate. |
| **11.1 review cadence** | Subsequent-similar 72-hour substantive review under the Employment Counsel SLA. This is NOT first-of-type — `/resume-summarizer` carries that honor. This skill inherits the established pack pattern. |

This skill is NOT an AEDT. It produces a JD draft, not a candidate decision. The AEDT wall from `hr-ai-governance` Section 6 applies by inheritance only — no novel AEDT surface is added. The skill cannot screen candidates, rank candidates, or make hiring decisions.

---

## Delegation Patterns Available

### Default: Pattern 1 Consultation

When a specific element of the JD needs specialist input, the skill spawns a consultation per `delegation-protocol.md` Pattern 1:

| Trigger | Spawn |
|---|---|
| Comp band alignment or title-to-band consistency | 💵 Compensation Analyst (co-owner; default consultation) |
| Jurisdiction-specific pay-transparency interpretation | 👔 Employment Counsel |
| ADA reasonable-accommodation boundaries for essential functions | 👔 Employment Counsel |
| Visa sponsorship policy framing | 👔 Employment Counsel (may further consult immigration counsel) |
| Non-compete or non-solicit clause inclusion in the offer | 👔 Employment Counsel |
| Culture-add language that is genuinely tied to a protected class (e.g., religious organization exemption) | 👔 Employment Counsel + 🧑‍🤝‍🧑 CHRO |

Consultations are attributed in the scanner findings section or the alignment report: "I consulted 💵 Compensation Analyst, who noted that the supplied $130-170k band is ~15% below the market midpoint for a 'Lead' title in remote-Israel + US-Eastern in Q2 2026, and recommended either retitling to 'Senior' or increasing the band." Ownership of the JD draft stays with Recruiter.

### Adversarial Review

NOT applicable at this version. Adversarial Review (Pattern 5) is reserved for near-final deliverables with high-stakes, uncapped exposure (enterprise contracts, M&A documents, pricing commitments). A JD draft is neither near-final nor uncapped-exposure at the generation stage; it is a draft going to a human reviewer who will revise and publish.

If a specific JD becomes high-stakes (e.g., a senior executive search with public press attention, or a role with ITAR/clearance requirements), the hiring manager can request `/job-description-generator --escalate-adversarial` which routes to `@employment-counsel` for a Pattern 5 review BEFORE posting. This is a manual escalation, not an automatic one.

---

## ROI Framing

ROI for `/job-description-generator` is reported as **"time saved on drafting and triage of a neutral, jurisdiction-compliant JD"** — NEVER "time saved on HR review" or "time saved on employment-law review."

HR blended rate: $150/hr per `feedback_roi_rates.md`. Default $150/hr for a Phase 4A HR triage involving a first-pass bias scan + structural draft + comp alignment check.

Time-saved baseline: a careful, bias-scanned, jurisdiction-aware JD draft that integrates comp band alignment and produces a scanner findings table is ~2-3 hours of manual drafting and triage time for a recruiter working with a hiring manager. Simpler refreshes (Update mode on an existing JD with no pay-transparency change) are ~0.75-1 hour baseline. Complex roles (novel function, multi-jurisdiction posting, regulated industry with additional counsel consultation) are 4+ hours baseline.

The ROI tracks ONLY the time the skill saves on drafting the structured artifact, not the substantive HR review time. The substantive review by the recruiter, hiring manager, and (where needed) employment counsel still happens in full.

Example ROI line for a standard JD generation:

```
⏱️ ~2.5 hrs saved on drafting and triage in 45s, 15k tkns ~$0.9 cost, Value ~$375
```

---

## Attribution and Maintenance

**Owner**: 🎯 Recruiter. The skill's drafting and scanner logic is Recruiter's accountability.

**Co-owner**: 💵 Compensation Analyst. Joint accountability on the comp band alignment logic in Method Step 6 and the Comp Band Alignment Report output section. Any change to the title-to-band tolerance thresholds, the alignment verdict taxonomy, or the `cannot-assess` routing requires sign-off from both owners.

**Consumers** (skills / gateways that invoke this skill):

- `ext-hr` — HR team gateway, primary user
- `interview-guide` — downstream skill; the JD defines the evaluation dimensions for the interview guide
- `comp-benchmark` — upstream when the user runs comp-benchmark first to get a market band, then feeds it into JD generation

New consumers require a frontmatter update and a one-line note in the consuming gateway's or skill's dependency list.

**Authoring**: First-principles. This skill was authored from scratch during Phase 4A as the first HR skill under the `hr-ai-governance` pack. Scanner wordlists are sourced from the Gaucher et al. 2011 academic paper (public, not a vendor tool). Non-obvious framing categories are sourced from the pack's Section 3.2 proxy register (not copied from Textio, Gender Decoder, Hemingway, or any vendor tool).

**Dependency on the pack**: The skill reads from `hr-ai-governance` at every invocation. When the pack's Section 3.2 proxy register, Section 4.1 audit log schema, Section 6.2 bright line #8, or Section 8.1 jurisdiction matrix is updated, the skill picks up the new content on the next run. The pack version is recorded in every audit log entry.

**Updates**: Via the two-pass publication gate defined in `sensitive-skill-guardrails.md` Section 4. Pass 1 (scaffolding check) — 📋 Director of HR, 15 minutes, binary GO / REWORK. Pass 2 (substantive check) — 👔 Employment Counsel, **72-hour subsequent-similar SLA** (this is NOT first-of-type; the pack and `/resume-summarizer` carry the first-of-type burden).

Minor edits (typos, formatting, scanner wordlist additions sourced from the pack's proxy register updates) can bypass Pass 2. Any edit touching: severity thresholds, scanner category taxonomy, comp band alignment logic, pay transparency compliance logic, or the HITL gate placement — requires a full Pass 2 substantive review by Employment Counsel.

**Changelog**: Maintained at the bottom of this file.

---

## Example Invocation

```
User: /job-description-generator --role "Customer Success Lead" --jurisdiction US-DE --comp-band "$130-170k base + equity" --essential-functions legionis/cs-lead-essential.md

/job-description-generator v1.0.0 — loading:
  - Jurisdiction: US-DE (no pay-transparency rule; comp band supplied voluntarily)
  - Governance pack: hr-ai-governance v1.0.1
  - Scanner wordlist: Gaucher et al. 2011 + non-obvious framing extensions
  - Essential functions: 6 items (from cs-lead-essential.md)
  - Seniority: Lead (IC5-equivalent per user input)
  - Comp band: $130-170k base + equity

Running pipeline:
  Step 1: Jurisdiction rules loaded (US-DE: no PT requirement; 3-year retention default)
  Step 2: Essential functions parsed (6 items; 1 flagged as essential-preferred-bleed)
  Step 3: JD draft generated (neutral source-faithful language; 0 model-inserted modifiers)
  Step 4: Gender-coded scanner (3 masculine terms flagged, 2 feminine terms flagged — within balance)
  Step 5: Non-neutral framing scanner (1 culture-fit term flagged, 0 age-coded, 0 disability-coded)
  Step 6: Comp band alignment (consulted @compensation-analyst: Lead title + $130-170k = title-band-mismatch P0)
  Step 7: Pay transparency compliance (US-DE: not-applicable; comp band displayed as optional)

Producing output at:
  Legionis/Product/job-description-generator-birth-test-2026-04-11.md

10/10 quality gates passed (after title-band-mismatch finding surfaced for hiring manager decision).

⏱️ ~2.5 hrs saved on drafting and triage in 45s, 15k tkns ~$0.9 cost, Value ~$375
```

---

## Changelog

- **1.0.0 (2026-04-11)** — Initial authoring. First-principles during Phase 4A as the first HR skill under the `hr-ai-governance` pack. Co-owned by 🎯 Recruiter (primary) and 💵 Compensation Analyst (comp band alignment). Scanner wordlists from Gaucher et al. 2011 (public academic source) + `hr-ai-governance` Section 3.2 proxy register. Subsequent-similar 72-hour Pass 2 review under Employment Counsel SLA (the pack carries first-of-type status). Scaffolding review by 📋 Director of HR. Birth-tested against a Legionis Customer Success Lead role (see `Legionis/Product/job-description-generator-birth-test-2026-04-11.md`).
