# HR AI Governance Pack

**Version**: 1.0
**Type**: knowledge-pack (sensitive)
**Primary Users**: @chro, @hr-dir, @recruiter, @people-analyst, @employment-counsel
**Status**: Q2-1.B authored 2026-05-18 (V2V Q2 2026 regulatory TRIO, pack 2 of 3)

---

**Adapted from**:
- EU AI Act (Regulation (EU) 2024/1689) — Article 6 risk classification + Annex III(4) employment, workers management, and access to self-employment + Annex III(7) education and vocational training. Published Official Journal of the European Union 2024-07-12; high-risk obligations enforcement landing 2026-08-02.
- NYC Local Law 144 of 2021 (Automated Employment Decision Tools — AEDT) + DCWP Final Rule (§5-300 et seq., NYC Rules Title 6, Chapter 5, Subchapter T). In force 2023-07-05; enforcement actions visible from 2025-2026.
- Texas TRAIGA (Texas Responsible Artificial Intelligence Governance Act, H.B. 149, 89th Legislature R.S.). Signed 2025; in force 2026-01-01.
- Colorado SB 24-205 (Consumer Protections for Artificial Intelligence). Originally scheduled 2026-02-01; **postponed to 2027-01-01 by S.B. 26-189 (signed May 2026)**. Rule-making in progress at the Colorado AG office; provisional substantive content only.
- Fair Credit Reporting Act (15 U.S.C. § 1681 et seq.) — pre-adverse-action procedural regime. **Eightfold AI class action filed 2026-01-20 in California state court (Superior Court of California, Santa Clara County)**, naming Eightfold AI Inc. as defendant and Microsoft Corporation + PayPal Inc. as employer-customers whose use of Eightfold's AI candidate-scoring outputs gave rise to plaintiff class.
- Illinois Artificial Intelligence Video Interview Act (820 ILCS 42/) — in force since 2020; Illinois H.B. 3773 (Pay Transparency + AI in Employment) extending 2026.
- California SB 1162 (pay transparency, in force 2023-01-01); California ICRAA (Investigative Consumer Reporting Agencies Act, Cal. Civ. Code § 1786 et seq.); California CCRAA (Consumer Credit Reporting Agencies Act, Cal. Civ. Code § 1785 et seq.).
- GDPR (Regulation (EU) 2016/679) Article 22 (automated individual decision-making) + Article 35 (DPIA). EU Pay Transparency Directive 2023/970 — **cross-referenced only**; full V2V `eu-pay-transparency.md` deferred per D12 to Q3 2026.
- UK Data Protection Act 2018 + UK ICO guidance "AI and data protection" (updated 2024).
- ISO/IEC 42001:2023 — AI Management Systems Standard, Annex A controls (specifically A.6 internal organization, A.7 resources, A.8 impact assessment, A.9 lifecycle, A.10 third-party).
- Anthropic HR Plugin (released 2026-02-24, claude.com/plugins/human-resources) — adapted for **substantive HR-AI content patterns and jurisdiction taxonomy coverage** (per `source-attribution.md` §"Edge Case — Anthropic Vertical Plugins"; technical-doc attribution only, no marketing surface). **The Findings + Reviewer Checklist + Cannot Assess Without scaffolding shape is V2V's own from `sensitive-skill-guardrails.md` §3 (active since 2026-04-11) — NOT inherited from the Anthropic HR Plugin.**

**License**:
- All statutes (EU AI Act, NYC LL144, Texas TRAIGA, Colorado SB 24-205 / SB 26-189, FCRA, Illinois AIVIA, GDPR, UK DPA, California Civil Code) are public sources, no license restriction on reference or summary.
- ISO/IEC 42001:2023 is a commercial standard published by ISO/IEC; cited by section reference only, full text requires ISO subscription.
- Anthropic HR Plugin per Anthropic plugin release terms (no formal OSS license; publicly documented patterns).

**V2V refinements**:
- Per-pack structural scaffolding per `sensitive-skill-guardrails.md` §3 (especially §3.5.1 FCRA enumeration requirement, authored 2026-04-29).
- Two-pass publication gate (Pass 1 scaffolding 48h SLA, Pass 2 substantive first-of-type 5 business days) per §4.
- ROI framing as "drafting and triage" per `roi-display.md` Prohibited Phrasings enumeration.
- Title VII / FCRA independence framing per `sensitive-skill-guardrails.md` §1.4 (the two regimes are structurally independent — a fair model can still create FCRA exposure).
- Cross-jurisdictional matrix: US federal + 27 EU member states + UK + 9 named US states with active AI-in-employment statutes or enforcement.
- Explicit Colorado postponement correction (the prior 2026-03-29 V2V baseline assumed February 2026 enforcement; the correct date is January 1, 2027 per S.B. 26-189).
- Cross-pack integration: pairs with `ai-act-readiness.md` (Q2-1.A) for EU AI Act high-risk HR overlap; pairs with `privacy-frameworks.md` for GDPR Article 22 + UK DPA overlap; pairs with `employment-law.md` for Title VII / ADA / ADEA underlying substantive law.

---

## 1. Purpose

This pack is the V2V scaffolding for AI use in HR workflows. Any V2V OS or Extension Teams skill that produces, evaluates, or relies on AI-generated employment decisions, candidate scoring, performance signals, or workforce analytics outputs MUST consume this pack and apply its scaffolding before publishing.

**Coverage**: FCRA + Title VII + EU AI Act high-risk HR + NYC AEDT + Texas TRAIGA + Colorado SB 24-205 (2027 effective) + Illinois AIVIA + ISO/IEC 42001 HR-applicable controls + GDPR Article 22 + UK DPA 2018.

**Out of scope (covered by sibling packs)**:
- Generic employment-law substance (Title VII disparate impact theory, ADA, ADEA, FMLA, wage-and-hour) → `employment-law.md`
- Generic EU AI Act readiness for non-HR high-risk systems → `ai-act-readiness.md` (Q2-1.A)
- EU Pay Transparency Directive substance → `eu-pay-transparency.md` (deferred to Q3 2026 per D12)
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
| **Colorado AI Act** | Colorado | **Postponed to 2027-01-01** (was 2026-02-01) | Colo. Rev. Stat. § 6-1-1701 et seq. (SB 24-205 as amended by SB 26-189) |
| **Illinois AIVIA** | Illinois | In force since 2020-01-01 | 820 ILCS 42/ |
| **Illinois H.B. 3773** | Illinois | Pay transparency + AI in employment, 2026 effective | 820 ILCS 112/ |
| **California SB 1162** | California | In force 2023-01-01 (pay transparency) | Cal. Lab. Code § 432.3 |
| **California ICRAA** | California | In force since 1975 | Cal. Civ. Code § 1786 et seq. |
| **California CCRAA** | California | In force since 1975 | Cal. Civ. Code § 1785 et seq. |
| **EU AI Act (high-risk HR)** | EU 27 + EEA | **Enforcement landing 2026-08-02** for high-risk obligations | Reg. (EU) 2024/1689, Art. 6 + Annex III(4) + Annex III(7) |
| **GDPR Article 22** | EU 27 + EEA | In force since 2018-05-25 | Reg. (EU) 2016/679, Art. 22 + Art. 35 |
| **EU Pay Transparency** | EU 27 | Member State transposition by 2026-06-07 | Directive (EU) 2023/970 (cross-ref only — see `eu-pay-transparency.md` Q3 deferral) |
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

## 7. Colorado AI Act (SB 24-205) — POSTPONED

### 7.1 Explicit Correction of Prior V2V Baseline

The 2026-03-29 V2V baseline assumed Colorado AI Act enforcement at February 1, 2026. **That date is incorrect.** S.B. 26-189, signed by Governor Polis in May 2026, postponed the operative date to **January 1, 2027**. The Colorado Attorney General's office is conducting rule-making and stakeholder consultation through the deferral window.

This pack treats Colorado as a **Q4 2026 / Q1 2027 active concern**, not a Q2 2026 enforcement reality. V2V skills consuming this pack should NOT include Colorado in current-state compliance assertions; should include Colorado in roadmap / readiness assertions with the 2027-01-01 effective date.

### 7.2 Substantive Content (Provisional)

The current text of SB 24-205 (as amended by SB 26-189) covers:

- "High-risk artificial intelligence systems" used in consequential decisions including employment, education, financial services, healthcare, housing, insurance, and legal services.
- **Developer obligations**: documentation of training data, foreseeable risks, intended use, and known limitations; disclosure to deployers.
- **Deployer obligations**: impact assessment before deployment + annually thereafter; notice to consumers; right to appeal an adverse consequential decision; right to correct inaccurate personal data feeding the system.
- **Algorithmic discrimination duty**: deployers and developers have a duty of reasonable care to avoid algorithmic discrimination.
- **Enforcement**: Colorado AG; civil penalties; no private right of action.

Final substantive content is subject to rule-making during the deferral period and may change before 2027-01-01. Authors should re-verify against the current statute before any Colorado-affecting output.

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

Numbered findings, each with **What** + **Why it matters** + **Severity (P0/P1/P2)** + **Suggested next step**. Findings must address (as applicable) each operative regime — Title VII, FCRA, AEDT, TRAIGA, Colorado (post-2027), EU AI Act high-risk, GDPR Art. 22, ISO 42001 — independently.

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

Authors may add jurisdiction-specific bullets (EU AI Act Article 27 FRIA scope, GDPR Article 22 contractual-necessity defense, Colorado SB 24-205 post-2027 obligations) but may NOT remove the listed FCRA bullets.

### 13.5 ROI Framing

Per `roi-display.md` Sensitive Skill ROI Framing rule: "time saved on drafting and triage" — NEVER "time saved on HR review" or "time saved on legal review."

### 13.6 Delegation Pattern

Downstream skills must cite the operative delegation pattern from `delegation-protocol.md`:

- **Pattern 1 Consultation** — default for skills consulting Employment Counsel on a single question.
- **Pattern 3 Review** — Employment Counsel reviews the HR-AI output before action.
- **Pattern 5 Adversarial Review** — for high-stakes, near-final HR-AI outputs (e.g., AEDT bias audit reports, EU AI Act FRIA submissions). Tiebreaker: @general-counsel + @chro.

## 14. Operating Principle

> "Title VII reaches outcomes. FCRA reaches procedure. AI Act reaches lifecycle. AEDT reaches audit. They are independent regimes. A fair model with bad procedure is still exposure. A compliant procedure with a discriminatory model is still exposure. Scaffolding makes the multi-regime analysis impossible to skip."

---

**Pack version**: 1.0 — Q2-1.B authored 2026-05-18 (@chro lead author, @hr-dir + @employment-counsel cross-reviewed)
**Next review trigger**: Colorado SB 24-205 rule-making conclusion (expected Q4 2026); EU AI Act Article 113 enforcement landing 2026-08-02; ongoing Eightfold AI class action developments.
