# HR AI Governance Pack

**Version**: 1.0
**Type**: knowledge-pack (sensitive)
**Primary Users**: `chro`, `hr-dir`, `recruiter`, `people-analyst`, `employment-counsel`
**Status**: Q2-1.B authored 2026-05-18 (V2V Q2 2026 regulatory TRIO, pack 2 of 3)

---

**Adapted from**:
- EU AI Act (Regulation (EU) 2024/1689) — Article 6 risk classification + Annex III(4) employment, workers management, and access to self-employment + Annex III(7) education and vocational training. Published Official Journal of the European Union 2024-07-12; high-risk obligations enforcement landing 2026-08-02.
- NYC Local Law 144 of 2021 (Automated Employment Decision Tools — AEDT) + DCWP Final Rule (§5-300 et seq., NYC Rules Title 6, Chapter 5, Subchapter T). In force 2023-07-05; enforcement actions visible from 2025-2026.
- Texas TRAIGA (Texas Responsible Artificial Intelligence Governance Act, H.B. 149, 89th Legislature R.S.). Signed 2025; in force 2026-01-01.
- Colorado AI legislation: SB 24-205 (Consumer Protections for Artificial Intelligence) was **repealed and replaced** — not postponed — by **SB 25-189** (passed 2026-05-12, signed by the Governor 2026-05-14, effective 2027-01-01). SB 25-189 abandons the "high-risk AI system" / algorithmic-discrimination construct of SB 24-205 and substitutes a disclosure-based "automated decision-making technology (ADMT)" regime. (Note: some law-firm alerts format the bill number as "SB26-189"; the substance is firm.)
- 2026-06-06 delta sources: Norton Rose Fulbright (nortonrosefulbright.com/en-us/knowledge/publications/18733d31/colorado-enacts-revised-ai-law); Troutman Pepper Locke privacy blog (troutmanprivacy.com/2026/05/colorado-legislature-passes-bill-to-repeal-and-replace-colorado-ai-act/); Government Technology (govtech.com/artificial-intelligence/colorado-passes-bill-amending-current-ai-legislation); Duane Morris class-action blog on Mobley v. Workday (blogs.duanemorris.com/classactiondefense/2026/06/02/...); Akin Gump AI Law & Regulation Tracker (akingump.com/en/insights/ai-law-and-regulation-tracker/...mobley-v-workday-inc); Ogletree Deakins on EU Pay Transparency deadline (ogletree.com/insights-resources/blog-posts/european-commission-confirms...); L&E Global EU Pay Transparency status (leglobal.law/2026/05/27/european-union-pay-transparency-directive-europe-nears-the-deadline-but-most-member-states-are-not-ready/).
- Fair Credit Reporting Act (15 U.S.C. § 1681 et seq.) — pre-adverse-action procedural regime. **Eightfold AI class action filed 2026-01-20 in California state court (Superior Court of California, Santa Clara County)**, naming Eightfold AI Inc. as defendant and Microsoft Corporation + PayPal Inc. as employer-customers whose use of Eightfold's AI candidate-scoring outputs gave rise to plaintiff class.
- Illinois Artificial Intelligence Video Interview Act (820 ILCS 42/) — in force since 2020; Illinois H.B. 3773 (Pay Transparency + AI in Employment) extending 2026.
- California SB 1162 (pay transparency, in force 2023-01-01); California ICRAA (Investigative Consumer Reporting Agencies Act, Cal. Civ. Code § 1786 et seq.); California CCRAA (Consumer Credit Reporting Agencies Act, Cal. Civ. Code § 1785 et seq.).
- GDPR (Regulation (EU) 2016/679) Article 22 (automated individual decision-making) + Article 35 (DPIA). EU Pay Transparency Directive 2023/970 — **cross-referenced only**; full V2V the deferred EU pay-transparency pack deferred per D12 to Q3 2026.
- UK Data Protection Act 2018 + UK ICO guidance "AI and data protection" (updated 2024).
- ISO/IEC 42001:2023 — AI Management Systems Standard, Annex A controls (specifically A.6 internal organization, A.7 resources, A.8 impact assessment, A.9 lifecycle, A.10 third-party).
- Anthropic HR Plugin (released 2026-02-24, claude.com/plugins/human-resources) — adapted for **substantive HR-AI content patterns and jurisdiction taxonomy coverage** (per `source-attribution.md` §"Edge Case — Anthropic Vertical Plugins"; technical-doc attribution only, no marketing surface). **The Findings + Reviewer Checklist + Cannot Assess Without scaffolding shape is V2V's own from `sensitive-skill-guardrails.md` §3 (active since 2026-04-11) — NOT inherited from the Anthropic HR Plugin.**

**Source licence**:
- All statutes (EU AI Act, NYC LL144, Texas TRAIGA, Colorado SB 25-189 / former SB 24-205, FCRA, Illinois AIVIA, GDPR, UK DPA, EU Pay Transparency Directive 2023/970, California Civil Code) are public sources, no license restriction on reference or summary. Mobley v. Workday court orders are public-record judicial opinions; law-firm alerts summarizing them are cited for navigation only.
- ISO/IEC 42001:2023 is a commercial standard published by ISO/IEC; cited by section reference only, full text requires ISO subscription.
- Anthropic HR Plugin per Anthropic plugin release terms (no formal OSS license; publicly documented patterns).

**V2V refinements**:
- Per-pack structural scaffolding per `sensitive-skill-guardrails.md` §3 (especially §3.5.1 FCRA enumeration requirement, authored 2026-04-29).
- Two-pass publication gate (Pass 1 scaffolding 48h SLA, Pass 2 substantive first-of-type 5 business days) per §4.
- ROI framing as "drafting and triage" per `roi-display.md` Prohibited Phrasings enumeration.
- Title VII / FCRA independence framing per `sensitive-skill-guardrails.md` §1.4 (the two regimes are structurally independent — a fair model can still create FCRA exposure).
- Cross-jurisdictional matrix: US federal + 27 EU member states + UK + 9 named US states with active AI-in-employment statutes or enforcement.
- Explicit Colorado repeal-and-replace correction (the prior baseline twice mis-stated Colorado: first as February-2026 enforcement, then as a "postponement" to 2027-01-01 via "S.B. 26-189"; the correct posture is that SB 24-205 was REPEALED AND REPLACED by SB 25-189, signed 2026-05-14, effective 2027-01-01, switching to an ADMT disclosure model). See §0 Delta Update and §7.
- 2026-06 delta integration: Mobley v. Workday March + May 2026 rulings (ADEA covers applicants; vendor-as-agent theory; AI-bias-testing-under-counsel privilege); EU Pay Transparency Directive 2023/970 transposition-deadline reality check.
- Cross-pack integration: pairs with `ai-act-readiness.md` (Q2-1.A) for EU AI Act high-risk HR overlap; pairs with `privacy-frameworks.md` for GDPR Article 22 + UK DPA overlap; pairs with `employment-law.md` for Title VII / ADA / ADEA underlying substantive law.

---

## 0. 2026-06 Delta Update (as of 2026-06-06)

This section summarizes corrections and additions verified in the 2026-06-06 refresh window. The substantive body sections (§3, §7, §11) have been corrected inline; this is the consolidated change log. This is reference content for drafting and triage, not legal advice.

### 0.1 Colorado — REPEAL-AND-REPLACE (CRITICAL correction)

The prior baseline said the Colorado AI Act (SB 24-205) was "postponed to 2027-01-01 by S.B. 26-189." **That is now wrong.** Corrected posture:

- SB 24-205 was **REPEALED AND REPLACED**, not postponed.
- The operative law is **SB 25-189**, passed 2026-05-12, **signed by the Governor 2026-05-14**, **effective 2027-01-01**.
- SB 25-189 **repeals** the SB 24-205 framework: it abandons the "high-risk AI system" + algorithmic-discrimination construct and removes the duty of care, the annual impact-assessment requirement, and the risk-management-program requirement.
- It **replaces** them with a disclosure-based regime built on "automated decision-making technology (ADMT)," with limited consumer rights (notice, access, correction, and human review on adverse outcomes). Enforcement is AG-exclusive; there is no private right of action.
- Bill-number formatting note: some law-firm alerts render the bill as "SB26-189." Use **SB 25-189**; the substance (repeal-and-replace, ADMT/disclosure model, 2027-01-01 effective) is firm regardless of the formatting variance.
- Sources: Norton Rose Fulbright; Troutman Pepper Locke; Government Technology (full URLs in the attribution block).

### 0.2 Mobley v. Workday — two 2026 rulings (pairs with the Eightfold/FCRA content in §4)

- **2026-03-06** (Judge Rita Lin, N.D. Cal.): the ADEA covers job **applicants**, not just employees, rejecting Workday's dismissal argument. This sits on top of the prior surviving theory that an AI-hiring vendor can be liable as the employer's **agent**.
- **2026-05-29** (Magistrate Judge Beeler, discovery order): Workday's AI bias-testing data is **attorney-client privileged** (counsel curated it); Workday lacked Rule 34 "control" over its customers' applicant data; but EEO-1 / OFCCP documents are discoverable.
- **Practical takeaway**: structure AI bias-testing **under counsel** to preserve privilege. The vendor-as-"agent" theory and the ADEA-covers-applicants theory are both surviving litigation, so AI-hiring vendors and their employer-customers should treat both as live exposure.
- Sources: Duane Morris class-action blog (2026-06-02); Akin Gump AI Law & Regulation Tracker.

### 0.3 EU Pay Transparency Directive (2023/970) — deadline holds, compliance reality is patchy

- The **2026-06-07 transposition deadline HOLDS** (European Commission confirmed; no extension).
- BUT as of late May 2026, most member states are NOT transposed: only ~2 (Italy, Slovakia) had comprehensive legislation; ~10 had draft bills; ~11 had nothing public. Netherlands and Denmark are publicly targeting ~2027-01-01; Sweden paused. Many states are now technically in breach / facing infringement risk.
- Nuance for downstream skills: the deadline is fixed, but operative compliance is **jurisdiction-by-jurisdiction**, not "EU-wide as of June 7." Pay-equity/comp skills (`/comp-benchmark`, etc.) should treat EU pay transparency obligations as live in transposed states and as imminent (but not yet locally enacted) elsewhere — verify the specific member state. The full V2V the deferred EU pay-transparency pack pack remains deferred per D12; this is a cross-reference only.
- Sources: Ogletree Deakins (Commission deadline confirmation); L&E Global (member-state status as of 2026-05-27).

---

## 1. Purpose

This pack is the V2V scaffolding for AI use in HR workflows. Any V2V OS or Extension Teams skill that produces, evaluates, or relies on AI-generated employment decisions, candidate scoring, performance signals, or workforce analytics outputs MUST consume this pack and apply its scaffolding before publishing.

**Coverage**: FCRA + Title VII + EU AI Act high-risk HR + NYC AEDT + Texas TRAIGA + Colorado SB 25-189 (ADMT disclosure regime, 2027 effective; repealed-and-replaced SB 24-205) + Illinois AIVIA + ISO/IEC 42001 HR-applicable controls + GDPR Article 22 + UK DPA 2018.

**Out of scope (covered by sibling packs)**:
- Generic employment-law substance (Title VII disparate impact theory, ADA, ADEA, FMLA, wage-and-hour) → `employment-law.md`
- Generic EU AI Act readiness for non-HR high-risk systems → `ai-act-readiness.md` (Q2-1.A)
- EU Pay Transparency Directive substance → the deferred EU pay-transparency pack (deferred to Q3 2026 per D12)
- General privacy / GDPR substantive law beyond Article 22 → `privacy-frameworks.md`

## 2. Sensitive-Skill Applicability

This pack is bias-sensitive territory. Per `sensitive-skill-guardrails.md` §1 and §6, any V2V skill producing HR-AI output is structurally sensitive and MUST apply:

- **§3.1** Disclaimer + UPL/HR-advice block at the top of every output (HR-domain variant: "Not legal or HR advice").
- **§3.2** Jurisdiction Assumed field declared explicitly.
- **§3.3** `## Findings` section with numbered findings, P0/P1/P2 severity tags, and suggested next steps.
- **§3.4** `## Reviewer Checklist` with explicit sign-off items.
- **§3.5** `## Cannot Assess Without Licensed Counsel` section.
- **§3.5.1** Mandatory FCRA enumeration — verbatim or substantively equivalent — for any output involving candidate scoring, employment-adverse decision, or consumer-report-equivalent material.
- **§4** Two-pass publication gate. Pass 1 scaffolding: 👥 CHRO (or designate) within 48 hours. Pass 2 substantive: 👔 Employment Counsel within 5 business days for first-of-type, 72 hours thereafter.
- **§5** ROI framing as "drafting and triage" — NEVER as "review."

In-scope V2V skills (non-exhaustive): `/resume-summarizer`, `/job-description-generator`, `/interview-guide`, `/interview-synthesis`, `/comp-benchmark`, `/bias-check`, `/ai-regulatory-audit`, `/compliance-audit`. When in doubt, mark sensitive (per §2 of the rule).

## 3. Jurisdictional Scope Matrix

| Regime | Jurisdiction | Status | Operative Citation |
|---|---|---|---|
| **FCRA** | US federal | In force since 1970; AI candidate-scoring class theory novel as of 2026-01-20 (Eightfold) | 15 U.S.C. § 1681 et seq. |
| **Title VII** | US federal | In force since 1964; EEOC AI guidance updated 2023 | 42 U.S.C. § 2000e et seq. |
| **ADA** | US federal | In force since 1990; EEOC AI guidance 2022 | 42 U.S.C. § 12101 et seq. |
| **ADEA** | US federal | In force since 1967 | 29 U.S.C. § 621 et seq. |
| **GINA** | US federal | In force since 2008 | 42 U.S.C. § 2000ff et seq. |
| **EEOC AI Guidance** | US federal | 2023 technical assistance documents on AI in employment | EEOC TAD May 2023 + October 2023 |
| **NYC AEDT (LL144)** | NYC employers + non-NYC employers using AI on NYC candidates | In force 2023-07-05; DCWP enforcement visible 2025-2026 | NYC Admin Code § 20-870 et seq. |
| **Texas TRAIGA** | Texas | **In force 2026-01-01** | Tex. Bus. & Com. Code Ch. 552 (H.B. 149) |
| **Colorado AI law (SB 25-189, ADMT regime)** | Colorado | **Effective 2027-01-01** — SB 24-205 REPEALED AND REPLACED by SB 25-189 (signed 2026-05-14); switched from "high-risk AI" to ADMT disclosure model | SB 25-189 (bill-number formatting varies; some alerts say "SB26-189"). Replaces former Colo. Rev. Stat. § 6-1-1701 et seq. (SB 24-205) |
| **Connecticut Public Act 26-15 (substitute SB 5)** | Connecticut | **Enacted 2026-05-27** — primary-text pointer only; applicability, effective date, and HR-AI obligations not assessed here | Public Act No. 26-15 (substitute SB 5), Connecticut General Assembly enacted text |
| **Illinois AIVIA** | Illinois | In force since 2020-01-01 | 820 ILCS 42/ |
| **Illinois H.B. 3773** | Illinois | Pay transparency + AI in employment, 2026 effective | 820 ILCS 112/ |
| **California SB 1162** | California | In force 2023-01-01 (pay transparency) | Cal. Lab. Code § 432.3 |
| **California ICRAA** | California | In force since 1975 | Cal. Civ. Code § 1786 et seq. |
| **California CCRAA** | California | In force since 1975 | Cal. Civ. Code § 1785 et seq. |
| **EU AI Act (high-risk HR)** | EU 27 + EEA | **Enforcement landing 2026-08-02** for high-risk obligations | Reg. (EU) 2024/1689, Art. 6 + Annex III(4) + Annex III(7) |
| **GDPR Article 22** | EU 27 + EEA | In force since 2018-05-25 | Reg. (EU) 2016/679, Art. 22 + Art. 35 |
| **EU Pay Transparency** | EU 27 | Transposition deadline 2026-06-07 HOLDS, but as of late May 2026 most member states NOT yet transposed (only ~2 comprehensive); compliance is jurisdiction-by-jurisdiction (see §0.3) | Directive (EU) 2023/970 (cross-ref only — see the deferred EU pay-transparency pack Q3 deferral) |
| **UK Data Protection Act 2018** | UK | In force since 2018-05-25; ICO AI guidance updated 2024 | UK DPA 2018 |
| **ISO/IEC 42001:2023** | Voluntary standard | Published 2023-12; certifications growing 2024-2026 | ISO/IEC 42001:2023 |

Additional state layers without dedicated AI-in-employment statutes but with consumer-credit / background-check analogs that interact with AI candidate-scoring: NY, MA, MN, OK, WA. Authors of HR-AI skills must declare the operative jurisdiction per output; cross-jurisdictional outputs are permissible but the disclaimer block MUST list each operative regime.

## 4. FCRA Section (Canonical per Sensitive-Skill-Guardrails §1.4 + §3.5.1)

FCRA is independent of Title VII. A perfectly fair, non-discriminatory candidate-scoring model can still create FCRA exposure for the employer-user if the four procedural obligations are not satisfied before adverse action is taken.

### 4.1 Eightfold AI Class Theory (2026-01-20)

The Eightfold AI class action, filed 2026-01-20 in the Superior Court of California, Santa Clara County, advances a novel theory: AI candidate-scoring outputs furnished by Eightfold AI Inc. qualify as "consumer reports" under 15 U.S.C. § 1681a(d), and Eightfold therefore qualifies as a "consumer reporting agency" under § 1681a(f). Named employer-customers include Microsoft Corporation and PayPal Inc. The class theory does NOT challenge the fairness of the scoring model itself; it challenges the procedural handling of the output by Microsoft and PayPal in adverse employment actions.

The theory is novel and untested. As of this writing (2026-05-18) the case is at pleading stage. The question of whether AI candidate-scoring outputs are "consumer reports" within the meaning of FCRA is a question of first impression. But the theory is credible enough that:

1. The complaint has been allowed to proceed past initial motion practice.
2. Other plaintiff firms are reportedly building parallel actions against other AI-hiring vendors (HireVue, Pymetrics, Modern Hire).
3. Treating FCRA as live exposure for any AI-candidate-scoring skill is the only defensible posture.

### 4.2 The Four Procedural Obligations (Verbatim from §3.5.1)

| Obligation | Statutory Source | What It Requires |
|---|---|---|
| **Pre-Adverse Action Notice** | 15 U.S.C. § 1681b(b)(3)(A)(i) | Before taking adverse action based in whole or in part on a consumer report, the user must provide the consumer with notice of the intended adverse action plus a copy of the report |
| **Copy of Consumer Report** | 15 U.S.C. § 1681b(b)(3)(A)(i) | The candidate is entitled to receive a copy of the actual report used in the adverse action — not a summary, not a redacted version |
| **Summary of Rights under FCRA** | 15 U.S.C. § 1681g | Written summary of consumer rights under FCRA, in the form prescribed by the CFPB, delivered with the pre-adverse-action notice |
| **30-Day Dispute Window + Reinvestigation** | 15 U.S.C. § 1681i | The consumer has 30 days to dispute inaccuracies; the furnisher and the CRA have reinvestigation obligations within that window before adverse action may proceed |

### 4.3 State-Law Layered Obligations

- **California ICRAA** (Cal. Civ. Code § 1786 et seq.) — investigative consumer reports; layered disclosure and copy-of-report obligations beyond federal FCRA.
- **California CCRAA** (Cal. Civ. Code § 1785 et seq.) — consumer credit reports; California-specific dispute mechanisms.
- **NY, MA, IL, MN, OK, WA** — analog state regimes with disclosure and timing variations. Always verify operative state law before adverse action.

### 4.4 Cross-Reference for HR-AI Skill Authors

Every in-scope HR-AI skill's `## Cannot Assess Without Licensed Counsel` section MUST enumerate the seven bullets specified in `sensitive-skill-guardrails.md` §3.5.1. Omission is a Pass 1 (Scaffolding) failure. Authors may add additional bullets but may NOT remove the listed ones.

## 5. NYC AEDT (Local Law 144)

The most-established US state/local AI-in-employment statute. In force since 2023-07-05; DCWP (NYC Department of Consumer and Worker Protection) enforcement actions have grown 2025-2026 following a December 2025 NY State Comptroller audit that publicly named non-compliant employers.

### 5.1 Affected Employers

- NYC employers using an Automated Employment Decision Tool (AEDT) for screening NYC-based candidates or employees.
- Non-NYC employers using an AEDT to screen candidates physically located in NYC at the time of the employment decision (extraterritorial reach).

An AEDT is defined as "any computational process, derived from machine learning, statistical modeling, data analytics, or artificial intelligence, that issues simplified output, including a score, classification, or recommendation, that is used to substantially assist or replace discretionary decision-making for making employment decisions" (NYC Admin Code § 20-870).

### 5.2 Core Obligations

| Obligation | Detail | Source |
|---|---|---|
| **Independent Bias Audit** | Annual, conducted by an independent auditor; tests for disparate impact across protected categories | NYC Admin Code § 20-871(a)(1) + DCWP Final Rule §5-301 |
| **Public Bias Audit Summary** | Summary results posted on the employer's website + publicly available for at least 6 months | § 20-871(a)(2) |
| **Notice to Candidates** | At least 10 business days before AEDT use, employer must notify the candidate that an AEDT will be used + which job qualifications are being assessed | § 20-871(b) |
| **Alternative Process Option** | Candidate must be informed of the option to request an alternative selection process or accommodation (where applicable) | § 20-871(b)(3) |
| **Data Retention** | Source and type of data collected disclosed; data retention policy disclosed | § 20-871(b)(4) |

### 5.3 Adverse Impact Ratio (AIR) Methodology

The DCWP Final Rule prescribes the methodology for the bias audit's adverse impact analysis:

- Selection rate for each category divided by the selection rate of the most-selected category.
- AIR < 0.8 (the "four-fifths rule") is presumptive evidence of disparate impact.
- Intersectional analysis (e.g., Black women) is required, not optional.

The audit must cover the AEDT's outputs over the prior calendar year (or, if newly deployed, over a representative sample period defined by the auditor).

### 5.4 Enforcement Posture

DCWP enforcement has shifted from reactive complaints to proactive sweeps following the December 2025 NY State Comptroller audit. Civil penalties: up to $1,500 per violation, with each day of non-compliance counted as a separate violation. Public naming + reputational exposure is often more material than the dollar penalty.

## 6. Texas TRAIGA (Texas Responsible Artificial Intelligence Governance Act)

H.B. 149, 89th Texas Legislature, Regular Session. Signed 2025; in force 2026-01-01. Codified at Tex. Bus. & Com. Code Ch. 552.

### 6.1 Scope

TRAIGA covers "high-risk" AI systems in Texas, with employment as one of the named high-risk domains. Definitions track but do not exactly mirror the EU AI Act — Texas operators must read TRAIGA's definitions directly rather than relying on EU AI Act analogs.

### 6.2 Core Obligations

- **Notice and disclosure** to consumers (candidates, employees) when a high-risk AI system is used to make a consequential decision.
- **Opt-out provisions** for certain categories of automated decision-making.
- **Risk management program** documenting the AI system's purpose, training data, foreseeable misuse, and bias mitigations.
- **Annual impact assessment** for ongoing high-risk deployments.
- **State AG enforcement** — Texas Attorney General has primary enforcement authority. Private right of action is limited; the statute does not create a robust private cause of action for individual candidates (contrast with FCRA, which does).

### 6.3 Comparison to NYC AEDT

| Dimension | NYC AEDT | Texas TRAIGA |
|---|---|---|
| Effective date | 2023-07-05 | 2026-01-01 |
| Audit cadence | Annual bias audit, public summary | Annual impact assessment, not public |
| Notice timing | 10 business days pre-use | "Reasonable notice" before consequential decision |
| Enforcement | DCWP, $1,500/violation | Texas AG, civil penalties TBD by rule-making |
| Private right of action | Limited | Limited |
| Scope | Employment-specific (AEDT) | Multi-domain (employment, lending, housing, etc.) |

Same general shape — notice + assessment + AG-led enforcement — different specifics. A multi-state employer must comply with both regimes independently; satisfying one does not satisfy the other.

## 7. Colorado AI law — SB 24-205 REPEALED AND REPLACED by SB 25-189 (ADMT disclosure regime)

### 7.1 Explicit Correction of Prior V2V Baseline (TWO prior errors)

Two earlier baselines were wrong, in sequence:

1. The 2026-03-29 baseline assumed Colorado AI Act **enforcement at February 1, 2026** — incorrect.
2. The later baseline said the Act was **"postponed to 2027-01-01 by S.B. 26-189"** — also incorrect.

**Correct posture (verified 2026-06-06):** SB 24-205 was **REPEALED AND REPLACED**, not postponed. The operative law is **SB 25-189**, passed 2026-05-12, **signed by the Governor 2026-05-14**, **effective 2027-01-01**. (Bill-number formatting varies across sources — some law-firm alerts render it "SB26-189." Use SB 25-189; the substance is firm.)

V2V skills consuming this pack should NOT include Colorado in current-state (2026) compliance assertions, and should NOT carry forward the old SB 24-205 "high-risk AI system" / duty-of-care / annual-impact-assessment obligations as Colorado's future state. Those were repealed. Include Colorado in roadmap / readiness assertions with the **2027-01-01 effective date and the ADMT disclosure model** described below.

### 7.2 What SB 25-189 Repeals (from the former SB 24-205)

SB 25-189 abandons the SB 24-205 architecture. Specifically REMOVED:

- The "high-risk artificial intelligence system" construct and the "algorithmic discrimination" framing.
- The deployer/developer **duty of reasonable care** to avoid algorithmic discrimination.
- **Annual impact assessments** for high-risk deployments.
- The **risk-management-program** requirement.

### 7.3 What SB 25-189 Replaces It With (ADMT disclosure regime)

- A disclosure-based regime centered on **"automated decision-making technology (ADMT)"** rather than "high-risk AI."
- **Limited consumer rights**: notice that ADMT is used, access, correction, and **human review on adverse outcomes**.
- **Enforcement**: Colorado Attorney General, **exclusive** enforcement; **no private right of action**.

This is a materially lighter regime than the repealed SB 24-205 framework — closer to a disclosure/transparency model than to the EU-AI-Act-style risk-management model the original statute contemplated. Authors should re-verify against the enacted SB 25-189 text and any implementing rules before any Colorado-affecting output, since rule-making may follow.

## 8. EU AI Act High-Risk HR (Article 6 + Annex III(4) + Annex III(7))

### 8.1 Risk Classification

Under EU AI Act Article 6, an AI system is "high-risk" if it is listed in Annex III. Two Annex III entries cover HR:

- **Annex III(4)** — AI systems intended to be used for:
  - (a) Recruitment or selection of natural persons (including placing of targeted job advertisements, screening or filtering applications, evaluating candidates).
  - (b) Decisions affecting terms of work-related relationships, promotion or termination, allocation of tasks based on individual behavior or personal traits, monitoring or evaluating performance and behavior.
- **Annex III(7)** — AI systems intended to be used for:
  - (a) Determining access or admission to educational and vocational training institutions.
  - (b) Evaluating learning outcomes (including for steering future learning).
  - (c) Assessing the appropriate level of education an individual will receive.
  - (d) Monitoring and detecting prohibited behavior of students during tests.

Most HR-AI applications fall under Annex III(4). Workplace learning and development AI may also touch Annex III(7).

### 8.2 Enforcement Landing Date

**2026-08-02** is the operative date for high-risk system obligations under Article 113 of the Regulation. General-purpose AI obligations landed earlier (2025-08-02); high-risk obligations land in August 2026.

### 8.3 Core Obligations for HR-AI Providers and Deployers

Applied to HR context:

| Article | Obligation | HR Application |
|---|---|---|
| **Art. 9** | Risk management system across the AI lifecycle | Documented risk identification for foreseeable HR harms (disparate impact, false negatives, candidate gaming) |
| **Art. 10** | Data governance for training, validation, testing datasets | Demographic representativeness of training data; bias examination; sourcing legality |
| **Art. 11** | Technical documentation | Maintained throughout lifecycle; available to authorities on request |
| **Art. 12** | Automatic logging | AEDT-equivalent logging of inputs, outputs, and decisions |
| **Art. 13** | Transparency and information to deployers | Operator-facing documentation; explanation of system behavior |
| **Art. 14** | Human oversight | Meaningful human review of AI-driven employment decisions; not rubber-stamp review |
| **Art. 15** | Accuracy, robustness, cybersecurity | Performance metrics maintained over time |
| **Art. 26** | Deployer obligations | Specific obligations on the employer-customer (notice, monitoring, human oversight execution) |
| **Art. 27** | Fundamental Rights Impact Assessment (FRIA) | Required for certain deployers using high-risk AI; HR deployers often in scope |

### 8.4 Penalties

Under Article 99: up to €15 million OR 3% of global annual turnover (whichever is higher) for non-compliance with high-risk system obligations. Higher penalties for use of prohibited AI practices (Article 5) and supply-of-incorrect-information violations.

### 8.5 FRIA + DPIA Unified Assessment

EU AI Act FRIA (Article 27) and GDPR DPIA (Article 35) overlap substantially for HR-AI use cases. Best practice — cross-referenced in `ai-act-readiness.md` (Q2-1.A) — is a unified impact assessment satisfying both regimes in a single document, with clearly labeled sections meeting each statute's specific requirements.

## 9. GDPR Article 22 + Article 35 (Automated Individual Decision-Making)

### 9.1 Article 22 — Right Not to Be Subject to Solely Automated Decisions

GDPR Article 22(1) gives data subjects the right "not to be subject to a decision based solely on automated processing, including profiling, which produces legal effects concerning him or her or similarly significantly affects him or her."

For HR-AI:

- **Solely automated** is interpreted strictly. Meaningful human review breaks the "solely" element — but rubber-stamp review does not (CJEU + multiple national supervisory authority decisions reinforce this).
- **Legal or similarly significant effects** clearly includes hiring decisions, termination decisions, promotion decisions, compensation decisions. Performance ratings are at the margin and depend on consequence.
- **Exceptions** (Art. 22(2)): contractual necessity, EU/Member State law authorization, or explicit consent. HR-AI deployers commonly try to rely on "contractual necessity" but this is contested in case law; consent is often invalid in employment because of the power imbalance (Art. 7 + WP29 Opinion on consent in employment).
- **Safeguards** (Art. 22(3)): even when an exception applies, the data subject retains the right to obtain human intervention, express their point of view, and contest the decision.

### 9.2 Article 35 — DPIA Requirement

Article 35 requires a Data Protection Impact Assessment "where a type of processing in particular using new technologies, and taking into account the nature, scope, context and purposes of the processing, is likely to result in a high risk to the rights and freedoms of natural persons."

HR-AI processing almost always triggers Article 35: WP29/EDPB guidance lists "systematic and extensive evaluation based on automated processing including profiling, on which decisions are based that produce legal or similarly significant effects" as a clear DPIA trigger.

### 9.3 Cross-Reference

EU AI Act FRIA (Article 27) and GDPR DPIA (Article 35) run in parallel and overlap substantially for HR. See §8.5 above and `ai-act-readiness.md` Q2-1.A for unified assessment guidance.

## 10. ISO/IEC 42001:2023 — AI Management Systems Standard

### 10.1 HR-Applicable Controls

ISO/IEC 42001:2023 is the AI Management Systems Standard, published December 2023. It is structured analogously to ISO/IEC 27001 (information security), with management-system requirements in clauses 4-10 and applicable controls in Annex A.

HR-applicable Annex A controls:

| Control Group | Relevant Controls | HR Application |
|---|---|---|
| **A.6 Internal organization** | A.6.1.2 AI roles and responsibilities | Named accountability for HR-AI deployment (CHRO + Employment Counsel + Data Lead) |
| **A.7 Resources** | A.7.2 Training and awareness | Hiring manager + recruiter training on AI tool use and limits |
| **A.8 Impact assessment** | A.8.2 AI system impact assessment | Documented impact analysis (intersects with FRIA + DPIA) |
| **A.9 AI lifecycle** | A.9.2 AI system requirements; A.9.3 AI system design and development; A.9.4 AI system verification and validation; A.9.5 AI system deployment; A.9.6 AI system operation and monitoring | End-to-end lifecycle controls applied to HR-AI |
| **A.10 Third-party** | A.10.2 Allocation of responsibilities; A.10.4 Customers | Vendor management for HR-AI tools (HireVue, Eightfold, Pymetrics, etc.) |

### 10.2 Path to EU AI Act Compliance

ISO/IEC 42001 certification is one defensible path to demonstrating Article 9 (risk management system) compliance under the EU AI Act. The standard is not a substitute for AI Act compliance — Article 9 has specific requirements that ISO 42001 only partially addresses — but a certified ISO 42001 program is strong evidence of good-faith risk management.

### 10.3 Certification Ecosystem and Costs

Accredited certification bodies (BSI, TÜV, DNV, LRQA) launched ISO 42001 certifications in 2024. Initial certifications typically run 9-12 months, with cost in the high five figures to low six figures for mid-market organizations. Adoption is concentrated in heavily regulated industries (financial services, healthcare, defense, government contractors) and is expanding to HR-tech vendors in 2026.

## 11. Title VII / FCRA Independence Framing

Per `sensitive-skill-guardrails.md` §1.4, Title VII and FCRA are independent regimes that must be analyzed separately for any HR-AI deployment:

| Dimension | Title VII | FCRA |
|---|---|---|
| **What it reaches** | Discriminatory outcomes (disparate impact + disparate treatment) | Procedural handling of consumer-report-equivalent outputs |
| **What triggers it** | A scoring model that produces disparate impact across protected categories | An adverse employment action taken based on a consumer report |
| **Who enforces** | EEOC + private right of action + state FEP agencies | FTC + CFPB + private right of action |
| **Defense to the other** | A Title VII-compliant model does NOT defeat FCRA exposure | FCRA-compliant procedure does NOT defeat Title VII exposure |
| **Statute of limitations** | 180 / 300 days to file EEOC charge | 2 years from discovery (or 5 years from violation) |

**Implication for V2V HR-AI skills**: every output must satisfy BOTH analyses. A skill that produces a perfectly fair, non-discriminatory candidate score still creates FCRA exposure for its user if procedural obligations are not satisfied. Conversely, FCRA compliance does nothing to mitigate disparate-impact exposure under Title VII.

Skill authors must structure their `## Findings` and `## Cannot Assess Without` sections to address each regime independently. Conflating them is a Pass 2 substantive failure.

## 12. In-Scope V2V Skills

The following V2V OS and Extension Teams skills are in-scope for this pack (non-exhaustive — when in doubt, mark sensitive):

| Skill | In-scope because |
|---|---|
| `/resume-summarizer` | Produces candidate-scoring / triage output → FCRA + Title VII + AEDT/TRAIGA + AI Act high-risk |
| `/job-description-generator` | Output shapes who applies → ADEA + Title VII + AI Act transparency (if AI-generated) |
| `/interview-guide` | Structures evaluation → Title VII consistency + ADA accommodation considerations |
| `/interview-synthesis` | Synthesizes candidate signals → AEDT + AI Act human-oversight + GDPR Art. 22 |
| `/comp-benchmark` | Pay equity exposure → CA SB 1162 + IL HB 3773 + EU Pay Transparency (Q3 deferred) |
| `/bias-check` | Itself the bias-mitigation mechanism for other HR-AI skills |
| `/ai-regulatory-audit` | Itself the audit mechanism; meta-applies this pack to other skills |
| `/compliance-audit` | When scope includes HR-AI use |
| Recruiter-workflow skills | Any candidate-scoring or filtering touchpoint |
| Performance-review-AI skills | Title VII + GDPR Art. 22 + AI Act Annex III(4)(b) |
| Compensation-AI skills | Pay equity + GDPR Art. 22 |
| Talent-marketplace-AI skills | Internal mobility = "decisions affecting terms of work-related relationships" under Annex III(4)(b) |

## 13. Standard Structural Scaffolding for Downstream Skills

Downstream HR-AI skills consuming this pack MUST produce output in this shape (verbatim or substantively equivalent, with jurisdiction-specific tailoring):

### 13.1 Disclaimer Block (top of output)

```markdown
> ⚠️ **Not legal or HR advice.** This output is a drafting and triage aid generated by a product-organization skill, not counsel or qualified HR. No attorney-client or HR-advisor relationship is created by its production or use. Jurisdiction-specific questions, contested matters, and any decision with material legal, regulatory, or employment consequence require review by a licensed attorney and/or qualified HR professional in the relevant jurisdiction. Do not rely on this output as the sole basis for any legal, compliance, or employment decision.
>
> **Jurisdiction Assumed:** {jurisdiction — e.g., "U.S. federal + NY (NYC AEDT)," "EU (Germany, GDPR + EU AI Act)," "Multi-state U.S. (CA, NY, TX, IL)"}. If your jurisdiction differs, treat every finding below as a hypothesis to verify with local counsel.
```

### 13.2 `## Findings`

Numbered findings, each with **What** + **Why it matters** + **Severity (P0/P1/P2)** + **Suggested next step**. Findings must address (as applicable) each operative regime — Title VII, FCRA, AEDT, TRAIGA, Colorado SB 25-189 ADMT disclosure regime (post-2027), EU AI Act high-risk, GDPR Art. 22, ISO 42001 — independently.

### 13.3 `## Reviewer Checklist`

Items the human reviewer MUST sign off before action. At minimum:

- [ ] Operative jurisdiction confirmed and matches Disclaimer Block declaration
- [ ] Title VII disparate-impact analysis completed for the scoring model
- [ ] FCRA procedural obligations (four bullets per §3.5.1) verified in workflow
- [ ] AEDT bias audit (if NYC candidates in scope) within annual window
- [ ] TRAIGA notice + impact assessment (if Texas candidates in scope) completed
- [ ] EU AI Act Article 9-15 obligations verified (if EU candidates in scope)
- [ ] GDPR Article 22 + Article 35 DPIA in place (if EU data subjects)
- [ ] All P0 findings addressed or explicitly accepted-as-risk with documented reasoning
- [ ] Counsel engaged for items flagged in "Cannot Assess Without Licensed Counsel"

### 13.4 `## Cannot Assess Without Licensed Counsel`

For any in-scope skill per §12 above, this section MUST enumerate the seven bullets from `sensitive-skill-guardrails.md` §3.5.1 verbatim or substantively equivalent. Omission is a Pass 1 (Scaffolding) failure.

```markdown
## Cannot Assess Without Licensed Counsel
- Pre-adverse action notice obligations under 15 U.S.C. § 1681b(b)(3) — whether the employer-user has provided the consumer with notice of the intended adverse action plus a copy of the report before acting
- Copy of consumer report delivery under 15 U.S.C. § 1681b(b)(3) — whether the candidate has received the actual report used, not a summary or redacted version
- Summary of rights under FCRA per 15 U.S.C. § 1681g — whether the CFPB-prescribed summary has been delivered with the pre-adverse-action notice
- 30-day dispute window with reinvestigation obligations under 15 U.S.C. § 1681i — whether the consumer has been given the statutory 30 days to dispute, and whether the consumer reporting agency and furnisher have satisfied reinvestigation obligations before final adverse action
- Whether the skill output qualifies as a "consumer report" under 15 U.S.C. § 1681a(d) and whether the producing entity qualifies as a "consumer reporting agency" under § 1681a(f) (novel theory at issue in Eightfold AI class litigation; assessment requires counsel)
- State-law layered obligations: ICRAA / CCRAA (California), and analogs in NY, MA, IL, MN, OK, WA
- Title VII disparate-impact exposure on the underlying scoring model (parallel and independent of FCRA — see EEOC guidance on AI in employment decisions)
```

Authors may add jurisdiction-specific bullets (EU AI Act Article 27 FRIA scope, GDPR Article 22 contractual-necessity defense, Colorado SB 25-189 ADMT disclosure obligations effective 2027-01-01) but may NOT remove the listed FCRA bullets.

### 13.5 ROI Framing

Per `roi-display.md` Sensitive Skill ROI Framing rule: "time saved on drafting and triage" — NEVER "time saved on HR review" or "time saved on legal review."

### 13.6 Delegation Pattern

Downstream skills must cite the operative delegation pattern from `delegation-protocol.md`:

- **Pattern 1 Consultation** — default for skills consulting Employment Counsel on a single question.
- **Pattern 3 Review** — Employment Counsel reviews the HR-AI output before action.
- **Pattern 5 Adversarial Review** — for high-stakes, near-final HR-AI outputs (e.g., AEDT bias audit reports, EU AI Act FRIA submissions). Tiebreaker: `general-counsel` + `chro`.

## 14. Agentic Recruiting Action-Taking Governance

> **Sensitive overlay (drafting & triage aid — requires counsel review).** Added 2026-07-11 via the Capability Embed run (item B2). Passed the two-pass sensitive-skill gate: Pass-1 scaffolding `chro` = GO; Pass-2 substantive `employment-counsel` = GO WITH CHANGES (renumbering fix applied; no invented citations; all four hard conditions met). MB6-R1 non-execution posture verified TRUE as of 2026-07-11 (HR agents recommend; a human acts) — the §14.5 tripwire is the standing condition. Extends the scoring-centric compliance spine (§4 FCRA, §5 AEDT, §8 EU AI Act, §9 GDPR Art. 22) with the action-taking dimension; does not rewrite it.

> ⚠️ **Not legal or HR advice.** This output is a drafting and triage aid generated by a product-organization skill, not counsel or qualified HR. No attorney-client or HR-advisor relationship is created by its production or use. Jurisdiction-specific questions, contested matters, and any decision with material legal, regulatory, or employment consequence require review by a licensed attorney and/or qualified HR professional in the relevant jurisdiction. Do not rely on this output as the sole basis for any legal, compliance, or employment decision.
>
> **Jurisdiction Assumed:** U.S. federal + NYC (Local Law 144 / AEDT). If EU or UK candidates are in scope, GDPR Article 22 (see §14.6 and pack §9) applies and materially changes the analysis; treat every finding below as a hypothesis to verify with local counsel.

---

### 14.0 The Gap This Overlay Closes

The existing pack governs AI that **scores or classifies** a candidate — the AEDT "simplified output... score, classification, or recommendation" of NYC Admin Code § 20-870, and the candidate-scoring "consumer report" theory of the Eightfold FCRA action (pack §4.1). Today's HR-AI vendor cohort (SRC-186: Eightfold, Paradox, Findem, and similar ATS/talent-intel platforms) is moving from scoring to **agentic action**: a single system that chains multiple steps —

1. **Source** — identify and surface candidates, place or target job ads, build a slate.
2. **Screen** — filter, rank, or knock out candidates against role criteria (this is the classic AEDT/FCRA scoring step).
3. **Schedule** — book interviews, send logistics, coordinate calendars.
4. **Advance / Reject** — move a candidate forward, or reject them (including **reject-by-inaction** — see §14.4) — with reduced or no human review between the AI's output and the effect on the candidate.

The governance question is no longer only "is the score fair and is the scoring output handled procedurally per FCRA." It is now **"which of these actions may an agent take autonomously, and which require a human decision before the action fires."** That is what this overlay adds.

**Framing note (why this is not a new compliance regime).** No statute here is new. FCRA (pack §4), NYC AEDT/LL144 (pack §5, SRC-259), Title VII (pack §11), EU AI Act high-risk HR (pack §8), GDPR Art. 22 (pack §9) all already apply. What changes with agentic action is **the trigger point and the human-oversight posture** — an action-taking agent can fire an adverse action faster, more silently, and with less human deliberation than a scoring tool. The exposure was always latent in the scoring output; agentic action pulls the trigger.

---

### 14.1 Governing Principle — Non-Execution Is the Safety, Not Provenance

The safety of an agentic recruiting flow rests on **non-execution**: the agent produces **recommendations**, and a **human takes the adverse employment action**. The agent does not, by itself, reject a candidate or fire a consumer-report-equivalent adverse action.

This must be stated plainly because it is easy to reach for the wrong safeguard:

- **The Decision Provenance Standard (DPS) does NOT gate this.** DPS is a provenance / Mode-classification mechanism — it records *who authored what* and *how a decision was reached*. It is **not** the FCRA/AEDT/Title-VII adverse-action gate, and it is **not** a liability shield. Note further that per `agent-spawn-protocol.md` Phase 1.5, the Decision-Record check **excludes ET agents** (HR and Legal). HR agent outputs never become Decision Records. So there is no DR for DPS to attest here in the ordinary case — **DPS gates nothing in this flow.** (MC1)
- Any prior or future wording to the effect of "our HR agents' outputs are human-affirmed by design, therefore the human-affirmation IS the adverse-action gate" is **STRUCK**. Human affirmation of a *provenance record* is a different act from the *statutorily-required human adverse-action decision* under FCRA § 1681b(b)(3) and the *meaningful human oversight* of EU AI Act Art. 14 / GDPR Art. 22. Do not conflate them. (MC1, MC4)
- The two gates are **separate** (MC2):
  - **Provenance gate (DPS)** — applies only where a Decision Record actually exists; records authorship/mode. Cite DPS ONLY as "additional provenance where a DR exists," never as "the internal gate." (MC4)
  - **Adverse-action gate (FCRA / AEDT / Title VII / Art. 22)** — applies **always**, at the moment a human acts adversely on the agent's recommendation, regardless of whether any DR exists.

**External vs internal safety posture:**

| Deployment | What makes it safe |
|---|---|
| **External / client deployment** (V2V-authored agent shipped into a customer's recruiting stack, which has *no* V2V internal controls) | The pack **content itself must mandate the human adverse-action gate** — advance / reject / reject-by-inaction are RECOMMENDATIONS requiring a human adverse-action decision before any candidate is rejected or a consumer-report-equivalent adverse action fires (§14.2, MB6). The client cannot rely on any V2V-internal convention; the gate must be in the shipped behavior. |
| **Internal operator use** | Safety rests on **non-execution (agents recommend, a human acts) + the §14.5 tripwire** — NOT on DPS. If an internal flow is ever wired so the agent takes an autonomous employment action, the external-deployment gate applies internally too (MC3). |

---

### 14.2 The Human Adverse-Action Gate (HARD requirement — MB6)

For **external / client deployments**, the pack content MUST mandate the following, and downstream skills that produce agentic-recruiting behavior MUST implement it:

> **advance, reject, and reject-by-inaction are RECOMMENDATIONS, not executed decisions.** Before any candidate is rejected, deprioritized out of consideration, or subjected to any consumer-report-equivalent adverse action, a **human must make the adverse-action decision**. The agent may prepare, draft, queue, and recommend; it may not fire the adverse action.

This is a **hard gate**, not a best-practice suggestion. An external deployment that lets the agent autonomously reject candidates (or silently deprioritize them past the point of consideration) has:

- moved from AEDT "assist" to AEDT "replace" discretionary decision-making (§14.3, MB8), pulling in LL144 bias-audit + 10-day notice obligations; and
- created the FCRA adverse-action posture (§14.6, MB6-R2) with no human in the loop to satisfy the § 1681b(b)(3) pre-adverse-action sequence.

The gate is what keeps an agentic recruiting flow inside "AI assists a human decision" rather than "AI makes the employment decision."

---

### 14.3 Risk-Tiering the Four Actions (MB7)

The four pipeline actions are **not one undifferentiated automation surface**. They carry materially different legal triggers and must be governed separately:

| Action | Risk tier | Why | Autonomy posture |
|---|---|---|---|
| **Source** | **Low (logistics)** | Identifying/surfacing candidates and placing ads. Note: ad *targeting* can carry Title VII / ADEA exposure (discriminatory ad delivery), so "low" is not "zero" — but it is not an adverse action against an identified candidate. | Agent may act autonomously, with ad-targeting audited for protected-class skew. |
| **Schedule** | **Low (logistics)** | Booking interviews, sending calendar logistics for candidates a human has already decided to advance. Pure coordination once the advance decision is made by a human. | Agent may act autonomously. |
| **Screen** | **HIGH** | This is the classic AEDT scoring/filtering step and the FCRA "consumer-report" candidate-scoring output (pack §4, §5). Filtering/ranking/knock-out directly shapes who is considered. | Output is a recommendation; screening that *removes* a candidate is an adverse action requiring the §14.2 human gate. |
| **Advance / Reject** | **HIGH** | The adverse-action trigger for FCRA (§1681b(b)(3)), AEDT "replace" analysis (§14.3 below / MB8), Title VII disparate impact, and EU AI Act Art. 14 / GDPR Art. 22. | Recommendation only. Reject / reject-by-inaction requires the human adverse-action decision per §14.2. |

**The dividing line**: `source` + `schedule` are logistics an agent can own; `screen` + `advance/reject` are the FCRA / AEDT / Title-VII triggers and sit behind the human adverse-action gate. Do not let a downstream skill collapse all four into a single "autonomous recruiting agent" permission.

### AEDT "Replace vs Assist" analysis (MB8)

NYC LL144 (SRC-259) turns on whether the tool is used to **"substantially assist or replace discretionary decision-making"** (NYC Admin Code § 20-870). An agent that **auto-advances or auto-rejects** candidates — acting on its own screen output without a human decision — leans hard toward the **"replace"** prong: the discretionary decision (who moves forward, who is rejected) is being made by the tool, not substantially assisted. When the "replace" prong is met, the full LL144 obligation set attaches (pack §5.2):

- Annual independent **bias audit** with public summary (AIR / four-fifths analysis per pack §5.3);
- **10-business-day candidate notice** before AEDT use, with the job qualifications assessed;
- Alternative-process / accommodation notice; data-retention disclosure.

Conversely, keeping the human adverse-action gate (§14.2) in place is precisely what keeps the deployment on the **"assist"** side — the agent assists, the human decides. The gate is not only an FCRA control; it is also the fact that most cleanly keeps an agentic flow within the "assist" reading of AEDT. (This is drafting/triage analysis, not a legal conclusion — the assist/replace line is fact-specific and for counsel per §14.7.)

---

### 14.4 "Reject-by-Inaction" Is an Adverse Action (MB9)

A specific agentic failure mode must be named because it is invisible by construction:

> **Reject-by-inaction** — a queue or slate the agent **silently deprioritizes** so that a candidate is never advanced, never scheduled, and never formally "rejected," but is functionally out of consideration. No rejection email fires; no status flips to "rejected"; the candidate simply never surfaces.

**This is an adverse action.** The absence of an explicit "reject" event does not make it not-adverse:

- Under **FCRA**, the adverse action is the *effect on the candidate* (not being considered / not being hired based in whole or in part on the scoring output), not the presence of a rejection letter.
- Under **NYC AEDT**, a tool that determines who is *not* surfaced for consideration is substantially assisting-or-replacing the discretionary decision just as much as one that emits a rejection.
- Under **Title VII**, disparate impact is measured on selection *outcomes*; a silently-deprioritized cohort is a selection outcome.

Governance implication: reject-by-inaction must be treated identically to an explicit reject for the human adverse-action gate (§14.2), for AEDT audit scope (the deprioritized cohort is in the bias-audit denominator), and for FCRA procedure. Downstream skills MUST surface the deprioritized queue to the human reviewer — a candidate silently aging out of a queue is an adverse action that skipped the gate.

---

### 14.5 The Tripwire — Internal Autonomy Escalates to the External Gate (MC3)

The internal safety posture (§14.1) depends on non-execution: internally, the agent recommends and a human acts. **The tripwire**: if an internal flow is ever wired so the agent takes an **autonomous employment action** — auto-reject, auto-deprioritize-out-of-consideration, auto-advance-to-offer — then the internal deployment has become, functionally, an external-grade autonomous decision system, and **the full external-deployment human-adverse-action gate (§14.2) applies internally too**, along with the AEDT "replace" analysis (§14.3) and the FCRA procedure (§14.6). "It's just internal tooling" is not a defense once the agent is executing employment actions rather than recommending them.

---

### 14.6 FCRA Attaches the Moment a Human Acts Adversely — LIVE, Not a Footnote (MB6-R2)

The four FCRA procedural obligations (pack §4.2, per `sensitive-skill-guardrails.md` §3.5.1) are **live obligations that attach the moment a human acts adversely on the agent's recommendation** — for BOTH external and internal deployments. This is not an external-only concern and not a footnote. The instant a human rejects (or reject-by-inaction removes) a candidate based in whole or in part on the agent's screen/advance-reject output, the FCRA pre-adverse-action sequence is triggered if the output qualifies as a consumer report (the novel-but-live Eightfold theory, pack §4.1, SRC-183). The full enumeration is carried in the `### 14.10 Cannot Assess Without Licensed Counsel (agentic action-taking overlay)` section below and applies to the internal case as much as the external one.

Reuse, do not re-cite loosely: the operative litigation signals are already in the pack — **Eightfold AI class action** (filed 2026-01-20, Santa Clara County; pack §4.1) and **Mobley v. Workday** (2026-03-06 ADEA-covers-applicants + vendor-as-agent; 2026-05-29 privilege/discovery order; pack §0.2). Do not invent new case citations.

### Agentic-security cross-reference (SRC-108)

The OWASP Top 10 for Agentic Applications 2026 (SRC-108) principles of **least-agency** and **observability** map directly onto this overlay's controls: least-agency = do not grant the agent autonomous execute permission on `screen`/`advance-reject` (§14.2, §14.3); observability = the deprioritized queue and every recommendation must be logged and surfaced to the human reviewer (§14.4). This is the security framing of the same human-gate requirement.

---

### 14.7 EU / UK — GDPR Article 22 (MB10)

If EU or UK candidates are in scope, an auto-advancing/auto-rejecting agent implicates **GDPR Article 22** (pack §9): the right not to be subject to a decision **based solely on automated processing** that produces legal or similarly significant effects. Hiring and rejection decisions are squarely "similarly significant effects." An agentic flow that rejects (or reject-by-inaction removes) a candidate with no meaningful human review is a "solely automated" decision — and **rubber-stamp human review does not break the "solely" element** (pack §9.1). The human adverse-action gate (§14.2) is also what preserves the "meaningful human intervention" that Art. 22(3) and EU AI Act Art. 14 require. UK deployments: UK GDPR / DPA 2018 + ICO automated-decision-making guidance (pack §3, §9) apply in parallel.

---

### 14.8 Findings

1. **Agentic recruiting collapses four differently-regulated actions into one automation surface.**
   - **What**: Vendors (SRC-186) are shipping agents that source → screen → schedule → advance/reject in one flow. The pack currently governs scoring, not multi-step action.
   - **Why it matters**: `screen` and `advance/reject` are the FCRA/AEDT/Title-VII triggers; `source`/`schedule` are logistics. Treating them as one "autonomous recruiter" permission puts high-risk actions on the same autonomy footing as calendar booking.
   - **Severity**: P0.
   - **Suggested next step**: Adopt the §14.3 risk-tiering; require downstream skills to gate `screen`/`advance-reject` behind the human adverse-action decision while permitting autonomous `source`/`schedule`.

2. **Without an in-content human adverse-action gate, external deployments become AEDT "replace" systems.**
   - **What**: A shipped agent that autonomously rejects candidates makes the discretionary decision itself.
   - **Why it matters**: Meets the LL144 "replace discretionary decision-making" prong → annual bias audit + public summary + 10-day candidate notice attach (pack §5.2, SRC-259). External clients have no V2V-internal controls to fall back on.
   - **Severity**: P0.
   - **Suggested next step**: The pack content MUST mandate the §14.2 gate (advance/reject/reject-by-inaction = recommendations requiring a human decision). This is MB6, a hard gate.

3. **DPS must not be represented as the internal adverse-action gate.**
   - **What**: Prior framing that "human-affirmed-by-design = the gate" conflates provenance with the statutory adverse-action decision.
   - **Why it matters**: DPS records authorship/mode; it is not the FCRA/AEDT/Title-VII gate and is not a liability shield. HR agent outputs are not even Decision Records (ET agents are excluded from the Phase 1.5 DR-check), so DPS gates nothing here.
   - **Severity**: P0.
   - **Suggested next step**: Struck per §14.1 (MC1). Cite DPS only as "additional provenance where a DR exists" (MC4); keep the provenance gate and adverse-action gate separate (MC2).

4. **Reject-by-inaction is a silent adverse action that skips every gate.**
   - **What**: A deprioritized queue removes a candidate from consideration with no rejection event.
   - **Why it matters**: FCRA/AEDT/Title VII measure effect and outcome, not the presence of a rejection letter. An un-surfaced candidate is an adverse-action outcome that bypassed the human gate and is missing from the AEDT audit denominator.
   - **Severity**: P0.
   - **Suggested next step**: Treat reject-by-inaction identically to explicit reject (§14.4, MB9); require the deprioritized queue to be surfaced to the human reviewer and included in bias-audit scope.

5. **FCRA is a live obligation on the internal case, attaching when the human acts adversely.**
   - **What**: The four §3.5.1 obligations trigger the instant a human rejects based in whole or in part on the agent's output — internal or external.
   - **Why it matters**: Framing FCRA as external-only understates internal exposure. The trigger is the human's adverse action, not the deployment boundary.
   - **Severity**: P1.
   - **Suggested next step**: Keep the full FCRA enumeration on both cases (§14.6, MB6-R2); verify the § 1681b(b)(3) sequence in any workflow where a human rejects on the agent's recommendation.

6. **Internal autonomy silently escalates exposure once the agent executes rather than recommends.**
   - **What**: An internal flow wired to auto-act on employment decisions has become an external-grade autonomous system.
   - **Why it matters**: "It's internal tooling" stops being a defense the moment the agent fires employment actions.
   - **Severity**: P1.
   - **Suggested next step**: Implement the §14.5 tripwire (MC3) — internal autonomous employment actions invoke the full external gate + AEDT replace analysis + FCRA procedure.

7. **EU/UK candidates make an auto-acting agent a solely-automated decision under GDPR Art. 22.**
   - **What**: Auto-reject / reject-by-inaction with no meaningful human review is "solely automated."
   - **Why it matters**: Art. 22 gives the right not to be subject to it for decisions with significant effect (hiring/rejection qualify); rubber-stamp review does not cure it (pack §9.1).
   - **Severity**: P1 (P0 if EU/UK candidates are confirmed in scope).
   - **Suggested next step**: Apply §14.7 (MB10); the human adverse-action gate also supplies the "meaningful human intervention" Art. 22(3) / EU AI Act Art. 14 require.

---

### 14.9 Reviewer Checklist

- [ ] Operative jurisdiction confirmed and matches the Disclaimer Block (U.S. federal + NYC LL144; EU/UK flagged if candidates in scope)
- [ ] The four pipeline actions are risk-tiered per §14.3 (source/schedule = low; screen/advance-reject = high) in every downstream agentic-recruiting skill
- [ ] The §14.2 human adverse-action gate is present **in the shipped pack content** for external deployments (MB6) — not merely a V2V-internal convention
- [ ] advance / reject / **reject-by-inaction** are all treated as recommendations requiring a human adverse-action decision (§14.2, §14.4)
- [ ] The deprioritized/reject-by-inaction queue is surfaced to the human reviewer and included in AEDT bias-audit scope (§14.4)
- [ ] AEDT "replace vs assist" analysis applied; if "replace," LL144 bias-audit + 10-day notice obligations verified (§14.3, pack §5.2)
- [ ] FCRA four-obligation enumeration carried on BOTH internal and external cases (§14.6, MB6-R2); not framed as external-only
- [ ] DPS is described ONLY as "additional provenance where a DR exists," never as the internal gate (MC1/MC2/MC4); no "human-affirmed-by-design = the gate" language present
- [ ] §14.5 tripwire wired: internal autonomous employment action → full external gate applies (MC3)
- [ ] If EU/UK candidates in scope: GDPR Art. 22 + Art. 35 DPIA analysis applied (§14.7, pack §9)
- [ ] All P0 findings addressed or explicitly accepted-as-risk with documented reasoning
- [ ] Counsel engaged for items flagged in "Cannot Assess Without Licensed Counsel"

---

### 14.10 Cannot Assess Without Licensed Counsel (agentic action-taking overlay)

The following require review by a licensed attorney in the operative jurisdiction. These obligations attach the moment a human acts adversely on an agent's recommendation, on BOTH internal and external deployments (MB6-R2):

- **Pre-adverse action notice obligations under 15 U.S.C. § 1681b(b)(3)** — whether the employer-user has provided the consumer with notice of the intended adverse action plus a copy of the report before acting.
- **Copy of consumer report delivery under 15 U.S.C. § 1681b(b)(3)** — whether the candidate has received the actual report used, not a summary or redacted version.
- **Summary of rights under FCRA per 15 U.S.C. § 1681g** — whether the CFPB-prescribed summary has been delivered with the pre-adverse-action notice.
- **30-day dispute window with reinvestigation obligations under 15 U.S.C. § 1681i** — whether the consumer has been given the statutory 30 days to dispute, and whether the consumer reporting agency and furnisher have satisfied reinvestigation obligations before final adverse action.
- **Whether the agent's screen / advance-reject output qualifies as a "consumer report" under 15 U.S.C. § 1681a(d) and whether the producing entity qualifies as a "consumer reporting agency" under § 1681a(f)** — the novel theory at issue in the Eightfold AI class litigation (pack §4.1); assessment requires counsel.
- **State-law layered obligations**: ICRAA / CCRAA (California), and analogs in NY, MA, IL, MN, OK, WA.
- **Title VII disparate-impact exposure on the underlying scoring model** — parallel and independent of FCRA (pack §11); a fair model with bad adverse-action procedure is still exposure, and vice versa.
- **NYC AEDT "assist vs replace" determination for the specific deployment** (§14.3) — whether the auto-advancing/auto-rejecting design meets the "replace discretionary decision-making" prong, triggering LL144 bias-audit + 10-day candidate notice.
- **GDPR Article 22 "solely automated" determination + Article 35 DPIA** (§14.7) — for any EU/UK candidates, whether the flow is solely automated and whether human review is meaningful rather than rubber-stamp.

---

### 14.11 Source Attribution (agentic action-taking overlay)

**Adapted from**:
- NYC Local Law 144 of 2021 (AEDT) + DCWP Final Rule — "substantially assist or replace discretionary decision-making" standard (SRC-259, nyc.gov/site/dca/about/automated-employment-decision-tools.page). Primary-text pointer; re-derive holdings from the statute.
- Fair Credit Reporting Act, 15 U.S.C. § 1681 et seq., and the Eightfold AI FCRA class-action signal (SRC-183, litigation-signal pointer — no legal holding stored; re-derive from filings).
- ATS / talent-intelligence agentic vendor cohort — Eightfold, Paradox, Findem (SRC-186, vendor-docs pointer) — the source-screen-schedule-advance action pattern this overlay governs.
- OWASP Top 10 for Agentic Applications 2026 (SRC-108, genai.owasp.org) — least-agency + observability principles mapped onto the human-gate and queue-surfacing controls.

**Source licence**: All statutes (FCRA, NYC LL144) are public sources. OWASP identifiers and public guidance are cited as describes-public-method; no licensed text is reproduced. Vendor docs are proprietary, cited as pointers only.

**V2V refinements**:
- Adds the action-taking dimension (source/screen/schedule/advance-reject) as an overlay on the existing scoring-centric compliance spine (pack §4/§5/§8/§9), without rewriting it.
- Risk-tiers the four pipeline actions (§14.3) rather than treating "autonomous recruiting" as one permission.
- Names "reject-by-inaction" as an adverse action (§14.4) — a V2V-specific agentic failure mode not named in any source statute.
- Separates the provenance gate (DPS) from the adverse-action gate (FCRA/AEDT), and scopes DPS as provenance-only (§14.1, MC1/MC2/MC4).
- Adds the internal-autonomy tripwire (§14.5) escalating internal execution to the external gate.
- Applies `sensitive-skill-guardrails.md` §3 scaffolding (Findings / Reviewer Checklist / Cannot Assess Without) with the §3.5.1 FCRA enumeration.
---

## 15. Operating Principle

> "Title VII reaches outcomes. FCRA reaches procedure. AI Act reaches lifecycle. AEDT reaches audit. They are independent regimes. A fair model with bad procedure is still exposure. A compliant procedure with a discriminatory model is still exposure. Scaffolding makes the multi-regime analysis impossible to skip."

---

**Pack version**: 1.0 — Q2-1.B authored 2026-05-18 (`chro` lead author, `hr-dir` + `employment-counsel` cross-reviewed)
**Next review trigger**: Colorado SB 25-189 implementing rules (post-enactment; effective 2027-01-01); EU AI Act Article 113 enforcement landing 2026-08-02; ongoing Eightfold AI class action + Mobley v. Workday developments; EU Pay Transparency Directive 2023/970 member-state transposition progress past the 2026-06-07 deadline.
**Last delta refresh**: 2026-06-06 (Colorado repeal-and-replace correction; Mobley v. Workday March + May 2026 rulings; EU Pay Transparency deadline reality check) — see §0.
