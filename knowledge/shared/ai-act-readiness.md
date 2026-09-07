# AI Act Readiness Pack — V2V scaffolding for EU AI Act (Regulation (EU) 2024/1689) high-risk system + GPAI obligations

**Version**: 1.1.0
**Owner**: compliance-officer (primary) + general-counsel (substantive co-owner)
**Last updated**: 2026-06-06 (Q2 delta refresh — Digital Omnibus timeline disaggregation; see §15)
**Consumers**: `/ai-regulatory-audit`, `/compliance-audit` (when --framework=eu-ai-act), `/ai-control-audit`, `compliance-officer`, `general-counsel`, `privacy-counsel`, `ai-architect`
**Sidecar**: ``compliance-frameworks.md`` (effective-date staging, regulator status)
**Sources**: ``compliance-frameworks.md`` (canonical EUR-Lex URLs, EDPB + AI Office guidance)
**Sensitive**: false (this pack is reference material; user-facing outputs derived from it are sensitive — see Section 2)
**Re-verification cadence**: quarterly (next: 2026-08-18; mandatory re-read on 2026-08-02 **GPAI** enforcement landing, AND on formal adoption / Official Journal publication of the Digital Omnibus high-risk timeline amendments — provisional agreement 2026-05-07, formal adoption expected ahead of 2026-08-02; see §15)

---

**Adapted from**:
- EU AI Act (Regulation (EU) 2024/1689) — primary source, official OJEU publication
- EU AI Act "Digital Omnibus" amendment (provisional agreement Council + Parliament + Commission, 2026-05-07; part of "Omnibus VII"; NOT yet formally adopted / published in the Official Journal as of 2026-06-06) — disaggregates the high-risk obligation timeline (see §15)
- GDPR (Regulation (EU) 2016/679) — primary source, official OJEU publication (for Article 22 + Article 35 overlap)
- Anthropic claude-for-legal plugin (released 2026-05-12, github.com/anthropics/claude-for-legal) — adapted for **EU AI Act statute coverage and Article-by-Article evidence-mapping pattern**; substantively re-authored against EU statutes. **The Findings + Reviewer Checklist + Cannot Assess Without scaffolding shape is V2V's own from `sensitive-skill-guardrails.md` §3 (active since 2026-04-11), pre-dating the Anthropic plugin release — NOT inherited from claude-for-legal.**

**Source licence**:
- EU statutes (Regulation 2024/1689, Regulation 2016/679) are public sources; no license restriction on reference and summary
- Digital Omnibus amendment proposal + provisional-agreement reporting are public sources (EU Commission digital-strategy library + law-firm/policy alerts); no license restriction on reference and summary
- Anthropic claude-for-legal per its release terms (publicly documented patterns, no formal OSS license)

**Digital Omnibus sources** (see §15):
- EU Commission Digital Omnibus AI Regulation proposal — digital-strategy.ec.europa.eu/en/library/digital-omnibus-ai-regulation-proposal
- Gibson Dunn, "EU AI Act Omnibus Agreement: Postponed High-Risk Deadlines and Other Key Changes" — gibsondunn.com/eu-ai-act-omnibus-agreement-postponed-high-risk-deadlines-and-other-key-changes/
- Covington Global Policy Watch, "EU AI Act Update: Timeline Relief, Targeted Simplification, and New Prohibitions" — globalpolicywatch.com/2026/05/eu-ai-act-update-timeline-relief-targeted-simplification-and-new-prohibitions/
- White & Case, "EU Agrees Digital Omnibus Deal to Simplify AI Rules" — whitecase.com/insight-alert/eu-agrees-digital-omnibus-deal-simplify-ai-rules

**V2V refinements**:
- Per-pack structural scaffolding per `sensitive-skill-guardrails.md` §3 (disclaimer + jurisdiction + findings + reviewer checklist + cannot-assess-without) propagated to every downstream skill output derived from this pack
- Two-pass publication gate per `sensitive-skill-guardrails.md` §4 (Director-level scaffolding pass 48h SLA + General Counsel substantive pass 5-business-day first-of-type SLA, with parallelism per M29)
- ROI framing as "drafting and triage" per `roi-display.md` (NOT "review acceleration" per the Prohibited Phrasings enumeration)
- Linked to V2V phase model: Decisions phase carries the risk-tier classification one-way-door; Commitments phase carries the Article 9 risk management system + Article 17 quality management system + post-market monitoring under Article 72
- Unified GDPR Article 35 DPIA + AI Act Article 27 FRIA scaffolding (single assessment, dual evidence)
- Cross-mapped to existing `compliance-frameworks.md` control-to-obligation matrix (§3 of that pack) so AI control IDs trace to AI Act Articles without reauthoring

---

## 1. Purpose and framing

### What this pack covers

The structural scaffolding for assessing a product's readiness against the **EU AI Act (Regulation (EU) 2024/1689)** — risk-tier classification, high-risk system obligations (Articles 8-15), General-Purpose AI (GPAI) model obligations (Articles 53 + 55), transparency obligations (Article 52), Fundamental Rights Impact Assessment (Article 27), conformity assessment paths (Annex VI vs Annex VII), and effective-date staging through 2028-08-02 (per the Digital Omnibus disaggregation — see §10 and §15; provisional agreement 2026-05-07, not yet formally adopted).

The pack feeds three downstream skills with a shared reference vocabulary:
- `/ai-regulatory-audit` — AI system governance posture across applicable frameworks, with EU AI Act as the most concrete obligation source
- `/compliance-audit --framework=eu-ai-act` — control-by-control readiness gap against AI Act high-risk + GPAI obligations
- `/ai-control-audit` — technical AI control taxonomy traced to specific AI Act Article evidence requirements

### What this pack does NOT cover

- Member State implementing measures (each EU Member State sets national designations under Articles 70-74; the pack flags the obligation, the skill defers to local counsel)
- Specific notified body identification (notified body landscape evolves; defer to current EU Commission notified body database)
- Interpretive positions on novel application questions (the AI Act is new; many application boundaries are unsettled and require EU counsel)
- Case law and enforcement actions (none yet at the depth needed for stable citation; covered in `compliance-frameworks.md` sidecar as they emerge)
- AI Office guidance not yet published (the EU AI Office issues structured guidance progressively; future guidance updates land in the sidecar)
- Sector-specific overlays (medical device AI under MDR/IVDR, financial-services AI under DORA, automotive AI under UNECE — each requires sectoral specialist review)

### Authoring discipline

- Pointer references to Article numbers, Annex numbers, recital numbers — no statute text reproduction
- Date-sensitive content (effective dates, AI Office guidance status, enforcement actions) lives in the `compliance-frameworks.md` sidecar
- No law firm citations; sources are the OJEU text, EU Commission AI Office publications, and EDPB guidance (for GDPR overlap)
- Interpretive determinations explicitly deferred to licensed EU counsel and named in `## Cannot Assess Without` of every downstream skill output

---

## 2. Sensitive-skill applicability

This pack is consumed by **sensitive skills** per `.claude/rules/sensitive-skill-guardrails.md`. The pack itself is reference material and not sensitive output. **But every V2V skill that produces AI Act readiness output is sensitive** and MUST apply the full scaffolding per `sensitive-skill-guardrails.md` Section 3:

1. **Disclaimer + UPL guardrail block** at top of output (verbatim, with `{jurisdiction}` filled in)
2. **Jurisdiction Assumed** field (default: EU; declare if otherwise)
3. **`## Findings`** — numbered, each with What / Why it matters / Severity (P0/P1/P2) / Suggested next step
4. **`## Reviewer Checklist`** — explicit human sign-off items including jurisdiction confirmation, material facts verified, P0 findings addressed, EU counsel engaged for `## Cannot Assess Without` items
5. **`## Cannot Assess Without {licensed EU counsel}`** — explicit enumeration of determinations the skill deliberately did not opine on

ROI framing for sensitive skills consuming this pack: **"drafting and triage"** — NEVER "review acceleration," "counsel time saved," or equivalent UPL-adjacent phrasing.

Publication gate (per `sensitive-skill-guardrails.md` §4): every new sensitive skill consuming this pack requires Pass 1 (Director of Legal Affairs, 48h SLA) + Pass 2 (General Counsel, first-of-type 5-business-day SLA, subsequent 72h). Pass 2 GO target for the Q2 sensitive-skill batch: 2026-06-30 (M10), with parallelism per M29.

---

## 3. Jurisdictional scope

**Primary jurisdiction**: European Union. The Regulation applies in EU Member States with Member State implementing measures (designation of national competent authorities, market surveillance authorities, and notifying authorities under Articles 70 + 74).

**Extraterritorial scope** (Article 2):
- Providers placing AI systems on the EU market or putting them into service in the EU, regardless of where the provider is established
- Providers and deployers of AI systems where the output is used in the EU, regardless of where the system is operated
- Importers and distributors of AI systems in the EU
- Product manufacturers placing AI systems on the market under their own name together with their products
- Authorized representatives of providers not established in the EU
- Affected persons located in the EU

**Practical consequence**: a non-EU SaaS provider whose system produces output used inside the EU is in scope. The "where is the inference running" test is insufficient; the "where is the output used" test governs.

**Out of scope** (Article 2 carve-outs, partial list):
- AI systems for exclusively military, defense, or national security purposes
- Public authorities of third countries and international organizations under specific cooperation frameworks
- Scientific research and development purposes (with conditions)
- Personal non-professional use by natural persons
- Free and open-source AI components (with specific conditions; see Article 2(12) — narrow carve-out, does not extend to high-risk or GPAI deployment contexts)

**Landing dates (disaggregated per Digital Omnibus — provisional agreement 2026-05-07, not yet formally adopted; see §15)**:
- **2026-08-02** — **GPAI** enforcement landing (Commission begins enforcing Articles 51-56; GPAI obligations themselves have been in force since 2025-08-02). This date is UNCHANGED by the Digital Omnibus.
- **2027-12-02** — stand-alone **high-risk** (Annex III) obligations (Articles 8-15), governance (Title III), and most other high-risk provisions enter into application. **Moved from 2026-08-02 (16-month deferral)** by the Digital Omnibus.
- **2028-08-02** — Annex I product-embedded high-risk obligations (moved from 2027-08-02).

The load-bearing dates for this pack are therefore now **two**: 2026-08-02 for GPAI, and 2027-12-02 for stand-alone high-risk Annex III systems. Treat the high-risk dates as **agreed but not yet formally published** until Official Journal publication.

---

## 4. Risk-tier classification framework — the first one-way door

The risk-tier classification is the **first one-way door** in every AI Act readiness assessment. Misclassification cascades through every downstream obligation. Per the May 2026 board-level framing produced by `general-counsel` during P0.4, classification determinations that are non-obvious require EU counsel review before the assessment proceeds.

### 4.1 Prohibited practices (Article 5)

AI practices that are categorically banned. **In force since 2025-02-02.** Categories (non-exhaustive summary; see Article 5 for full text):

- Subliminal techniques beyond a person's consciousness or purposefully manipulative techniques that materially distort behavior and cause significant harm
- Exploitation of vulnerabilities of specific groups (age, disability, social/economic situation) to materially distort behavior and cause significant harm
- Social scoring by public authorities or on their behalf leading to detrimental or unfavorable treatment in social contexts disconnected from the data-collection context, or that is disproportionate
- Real-time remote biometric identification in publicly accessible spaces for law enforcement, with narrow exceptions (specific targeted searches for victims of crimes, prevention of specific substantial threats, identification of suspects in serious crimes — each subject to authorization)
- Risk assessment of natural persons to predict criminal offending based solely on profiling or personality traits
- Untargeted scraping of facial images from the internet or CCTV to build/expand facial recognition databases
- Inferring emotions in workplaces and education institutions, except for medical or safety reasons
- Biometric categorization to infer race, political opinions, trade union membership, religious or philosophical beliefs, sex life, or sexual orientation
- Predictive policing based solely on profiling or personality traits

**Consequence of prohibited classification**: the practice is unlawful in the EU regardless of consent, contract, or commercial justification. Fines up to €35M or 7% of worldwide annual turnover (Article 99(3)).

### 4.2 High-risk systems (Article 6 + Annex I + Annex III)

Two routes to high-risk classification:

**Route A — Article 6(1) (Annex I products)**: AI systems used as safety components of products, or AI systems that are themselves products, falling under EU harmonized product safety law listed in Annex I (machinery, toys, recreational craft, lifts, equipment for explosive atmospheres, radio equipment, pressure equipment, cableways, personal protective equipment, gas appliances, medical devices, in-vitro diagnostic medical devices, civil aviation, two- or three-wheeled vehicles, agricultural vehicles, marine equipment, interoperability of rail system, motor vehicles and trailers).

**Route B — Article 6(2) (Annex III domains)**: AI systems used in eight listed sensitive domains:
1. Biometrics (real-time/post remote biometric ID; biometric categorization by sensitive attributes; emotion recognition outside Article 5 prohibitions)
2. Critical infrastructure (digital infrastructure, road traffic, supply of water/gas/heating/electricity — as safety components)
3. Education and vocational training (admissions, assessment, monitoring of prohibited behavior during tests)
4. Employment, workers' management, access to self-employment (recruitment/selection, decisions affecting terms of work, promotion/termination, task allocation, performance/behavior monitoring/evaluation)
5. Access to and enjoyment of essential private services and essential public services and benefits (credit scoring/creditworthiness assessment except for fraud detection, risk assessment/pricing for life/health insurance, emergency response triage)
6. Law enforcement (risk assessment of victims/offending, evidence reliability evaluation, profiling/predictive policing within Article 5 boundaries, crime analytics)
7. Migration, asylum, border control (risk assessment of natural persons, examination of applications, detection/recognition/identification at borders)
8. Administration of justice and democratic processes (judicial decision-support, influencing elections/referenda outcomes or voting behavior)

**Article 6(3) carve-out**: Annex III systems can be classified as **not high-risk** if they do not pose significant risk of harm to health/safety/fundamental rights, and meet at least one of: narrow procedural task; improvement of result of previously completed human activity; detection of decision-making patterns without replacing/influencing human assessment; preparatory task. This carve-out **does not apply** to systems performing profiling of natural persons. Provider must document the assessment. **This determination requires EU counsel — the Article 6(3) carve-out is the most litigation-likely boundary in the entire Act.**

### 4.3 Limited-risk / transparency obligations (Article 52)

AI systems with specific transparency obligations regardless of risk tier:

- **Article 52(1)**: AI systems intended to interact directly with natural persons must inform users they are interacting with an AI (unless obvious from context, or for law enforcement under specific conditions)
- **Article 52(2)**: Providers of AI systems generating synthetic audio/image/video/text content (including deepfakes) must ensure outputs are marked in a machine-readable format and detectable as artificially generated/manipulated
- **Article 52(3)**: Deployers of emotion-recognition or biometric-categorization systems must inform exposed natural persons of the system's operation and process personal data in compliance with GDPR
- **Article 52(4)**: Deployers of AI generating/manipulating image/audio/video content constituting deepfakes must disclose artificial generation (with exceptions for evidently artistic/satirical/creative work)

### 4.4 Minimal-risk (default)

AI systems not falling into any of the above categories carry no specific AI Act obligations beyond:
- The general accountability and risk-management principles applicable across the regulation
- Voluntary application of codes of conduct (Article 95)
- Compliance with any other applicable law (GDPR, sectoral safety law, etc.)

---

## 5. High-risk system obligations (Articles 8-15)

For systems classified high-risk under Article 6 (Annex I or Annex III), the following obligations attach. **In force from 2027-12-02** for most stand-alone (Annex III) systems — moved from 2026-08-02 by the Digital Omnibus (16-month deferral; provisional agreement 2026-05-07, not yet formally adopted); **2028-08-02** for Annex I products requiring third-party conformity assessment under sectoral product law (moved from 2027-08-02). See §10 and §15.

### 5.1 Article 8 — Compliance with the requirements

The accountability umbrella article. High-risk system providers must ensure the system complies with Articles 9-15 across its lifecycle, with all elements documented in a coherent compliance system. **Evidence required**: integrated compliance documentation set demonstrating Article 9-15 satisfaction. **Maps to `compliance-frameworks.md` §3 rows 22 + 24 (change management and re-conformity)**. **Pass 1 note**: scaffolding must show all 7 sub-obligations (Articles 9-15) traceable to evidence. **Pass 2 note**: General Counsel verifies the Article 6(3) carve-out has been substantively assessed if Annex III system is classified out.

### 5.2 Article 9 — Risk management system

A continuous, iterative risk management system established and documented for the system's lifecycle. Must identify and analyze known and reasonably foreseeable risks; estimate and evaluate risks emerging from intended use and reasonably foreseeable misuse; evaluate other risks from post-market monitoring data; adopt risk management measures targeted at residual risk acceptable. **Evidence required**: risk register, risk assessment methodology, residual risk acceptance criteria, lifecycle update procedure. **Maps to `compliance-frameworks.md` §3 rows 1-7 (model provenance + pre-deployment evaluation)**. **Pass 1 note**: scaffolding must include "reasonably foreseeable misuse" as a distinct risk category — frequent omission. **Pass 2 note**: General Counsel verifies the Article 9(9) carve-out for sectoral integration is properly invoked when applicable (e.g., MDR integration for medical AI).

### 5.3 Article 10 — Data and data governance

Training, validation, and testing data must be subject to data governance and management practices appropriate for the intended purpose. Must be relevant, sufficiently representative, free of errors and complete to the best extent possible, and address possible biases. Special category data (GDPR Article 9) processing for bias detection/correction permitted under strict conditions. **Evidence required**: training data documentation (dataset datasheets), data governance procedure, bias assessment report, data quality testing results. **Maps to `compliance-frameworks.md` §3 rows 1 + 6 (provenance + bias)**. **Pass 1 note**: scaffolding must require subgroup performance evaluation (not just aggregate metrics). **Pass 2 note**: General Counsel coordinates with Privacy Counsel on Article 10(5) special category data conditions (lawfulness under GDPR Article 9(2) basis required).

### 5.4 Article 11 — Technical documentation (with Annex IV)

Technical documentation drawn up before placing on market and kept up to date. Annex IV specifies the documentation contents: general description (intended purpose, version, hardware, software, deployment forms), detailed description (development process, training methodologies, datasets, validation procedures, system architecture, computational resources, design choices), description of the monitoring/functioning/control of the system, performance metrics, risk management system documentation, post-market monitoring plan, changes log, harmonized standards applied, EU declaration of conformity, post-market monitoring system. **Evidence required**: Annex IV-conformant technical documentation file. **Maps to `compliance-frameworks.md` §3 row 2 (model card + version history)**. **Pass 1 note**: scaffolding must enumerate all Annex IV sub-sections — partial documentation fails conformity. **Pass 2 note**: General Counsel verifies trade-secret redactions are properly framed under Article 78 confidentiality protections.

### 5.5 Article 12 — Record-keeping (automatic logging)

The system must enable automatic recording of events ("logs") over its lifetime. Logs must enable identification of situations resulting in risk under Article 79(1) or substantial modification; facilitate post-market monitoring; enable monitoring of operation by deployers under Article 26(5). **Evidence required**: logging architecture documentation, log retention policy (typically minimum 6 months unless sectoral law requires longer), log access controls, log integrity protections. **Maps to `compliance-frameworks.md` §3 row 14 (decision logging)**. **Pass 1 note**: scaffolding must address log integrity (not just retention). **Pass 2 note**: General Counsel coordinates with Privacy Counsel on GDPR retention conflicts.

### 5.6 Article 13 — Transparency and provision of information to deployers

The system must be designed and developed to enable deployers to interpret outputs and use the system appropriately. Instructions for use must include provider identity, system characteristics, capabilities and limitations, level of accuracy/robustness/cybersecurity, known/foreseeable circumstances posing risk, technical capabilities relevant to explainability, hardware/software specifications, computational resources, expected lifetime, maintenance/care measures including software updates. **Evidence required**: instructions for use document, deployer onboarding materials, performance limit documentation. **Pass 1 note**: scaffolding must include "circumstances of foreseeable misuse" disclosure to deployers. **Pass 2 note**: General Counsel verifies any disclaimer of liability does not contradict Article 25 provider obligations.

### 5.7 Article 14 — Human oversight

The system must be designed and developed to be effectively overseen by natural persons during use. Oversight measures must enable persons assigned the oversight to understand capacities and limitations, monitor operation for anomalies/dysfunctions/unexpected performance, avoid automation bias, correctly interpret outputs, decide not to use the output or override/reverse it, intervene to interrupt operation through stop button or similar procedure. **Evidence required**: human oversight design documentation, oversight training program, automation bias mitigation procedure, intervention procedure. **Maps to `compliance-frameworks.md` §3 row 11 (HITL for consequential actions)**. **Pass 1 note**: scaffolding must distinguish "oversight by persons in operation" from "oversight by natural persons" (Article 14(2) — at least two natural persons for certain biometric ID systems). **Pass 2 note**: General Counsel verifies the oversight design is operationally feasible for the deployer (not theatrical).

### 5.8 Article 15 — Accuracy, robustness, and cybersecurity

Achieve appropriate levels of accuracy, robustness, and cybersecurity, and perform consistently throughout the lifecycle. Accuracy levels and relevant metrics must be declared in instructions for use. Robustness must address errors, faults, inconsistencies, including resilience to attempts to alter use, output, or performance through unauthorized third-party exploitation. Systems that continue to learn after placing on market must be developed to eliminate or reduce risk of biased outputs influencing input for future operations (feedback loops). Cybersecurity must address AI-specific vulnerabilities including data poisoning, model poisoning, adversarial examples, model evasion, confidentiality attacks. **Evidence required**: accuracy test reports against declared metrics, adversarial robustness test results, cybersecurity assessment including AI-specific threat model, feedback loop bias mitigation documentation. **Maps to `compliance-frameworks.md` §3 rows 5 + 9 (accuracy + prompt injection defense)**. **Pass 1 note**: scaffolding must enumerate AI-specific cybersecurity threats (data poisoning, model evasion, adversarial examples) — generic cybersecurity assessment insufficient. **Pass 2 note**: General Counsel verifies post-market learning systems have feedback-loop bias controls if applicable.

---

## 6. GPAI obligations (Chapter V — Articles 51-56)

General-Purpose AI (GPAI) models carry distinct obligations from high-risk systems, with a separate timeline. **In force since 2025-08-02; Commission enforcement begins 2026-08-02.** The Digital Omnibus (provisional agreement 2026-05-07) did **NOT** change the GPAI timeline — the 2026-08-02 GPAI enforcement anchor stands. Only the stand-alone high-risk (Annex III → 2027-12-02) and Annex I product-embedded high-risk (→ 2028-08-02) timelines moved. See §15.

### 6.1 Article 53 — All GPAI model providers

Every GPAI model provider must:
- Draw up and keep up to date technical documentation including training/testing process and evaluation results (specified in Annex XI)
- Draw up and make available information and documentation to providers of AI systems intending to integrate the GPAI model (specified in Annex XII)
- Put in place a policy to comply with EU copyright law, including identifying and complying with rights reservations under Directive (EU) 2019/790 Article 4(3) (TDM opt-out)
- Draw up and make publicly available a sufficiently detailed summary of training content (template to be provided by AI Office)

**Evidence required**: Annex XI technical documentation, Annex XII downstream-provider documentation, copyright policy + TDM opt-out compliance procedure, public training data summary.

**Open-source carve-out (Article 53(2))**: providers of GPAI models released under free and open-source license that makes parameters, including weights, architecture, and model usage information publicly available, are exempted from the documentation obligations under Article 53(1)(a) + (b) — **but not** from the copyright policy and training-data-summary obligations. The carve-out also **does not apply** to GPAI models with systemic risk.

### 6.2 Article 55 — GPAI models with systemic risk

In addition to Article 53 obligations, providers of GPAI models meeting the systemic risk threshold under Article 51 must:
- Perform model evaluation including adversarial testing to identify and mitigate systemic risks
- Assess and mitigate possible systemic risks at Union level
- Track, document, and report serious incidents and possible corrective measures to AI Office and national competent authorities without undue delay
- Ensure adequate cybersecurity protection for the model and physical infrastructure

**Evidence required**: model evaluation reports, systemic risk assessment, adversarial test results, incident reporting procedure, cybersecurity assessment.

**Systemic risk threshold (Article 51)**: a GPAI model is presumed to have systemic risk if cumulative compute used for training exceeds 10^25 FLOPs, or if designated by the Commission based on capability/reach criteria.

---

## 7. GDPR overlap (Articles 22 + 35)

The EU AI Act does not replace GDPR. For AI systems processing personal data of EU residents, both apply.

### 7.1 GDPR Article 22 — automated individual decision-making

Article 22 prohibits decisions based solely on automated processing (including profiling) producing legal effects or similarly significant effects, with exceptions for contract necessity, EU/Member State law authorization, or explicit consent. Where exceptions apply, data subject has rights to obtain human intervention, express their point of view, and contest the decision.

**Overlap with AI Act**:
- AI Act Article 14 (human oversight) shares evidence with GDPR Article 22(3) (right to human intervention)
- AI Act Article 13 (transparency to deployers) shares evidence with GDPR Article 13/14 (information to data subjects) — but the AI Act obligation flows to deployers, the GDPR obligation flows to data subjects; **they are not interchangeable**
- AI Act high-risk classification for Annex III employment systems aligns with GDPR Article 22 employment decision applicability

### 7.2 GDPR Article 35 — Data Protection Impact Assessment (DPIA)

DPIA required for processing likely to result in high risk to data subjects. AI systems in Annex III domains processing personal data nearly always require DPIA.

**Overlap with AI Act Article 9 (risk management)**:
- Shared evidence: risk identification, risk assessment methodology, mitigation measures
- **DPIA does NOT substitute for Article 9 risk management** — Article 9 is broader (covers safety + fundamental rights + technical robustness, not only personal data risk)
- Article 9 risk management does not substitute for DPIA — DPIA is data-subject-centric, Article 9 is system-centric

**V2V scaffolding recommendation**: run a unified assessment that satisfies both, with two outputs (DPIA document for supervisory authorities; Article 9 risk management dossier for market surveillance authorities). Coordinate with `privacy-counsel` as co-author. See `privacy-frameworks.md` for the DPIA methodology layer.

---

## 8. FRIA — Fundamental Rights Impact Assessment (Article 27)

The AI Act introduces a **Fundamental Rights Impact Assessment** for high-risk systems deployed by certain operators:
- **Public bodies and entities providing public services** deploying high-risk AI systems
- **Private deployers** deploying high-risk systems for credit scoring/creditworthiness, risk assessment/pricing for life/health insurance, or emergency response triage (specific Annex III subdomains under Article 27(1))

**Required FRIA contents (Article 27(1))**:
- Deployer processes in which the system will be used
- Period of time and frequency of use
- Categories of natural persons and groups likely to be affected
- Specific risks of harm likely to impact those categories
- Measures for human oversight in line with instructions for use
- Measures to be taken in case of risk materialization, including internal governance and complaint mechanisms

**V2V scaffolding recommendation**: unify FRIA + GDPR Article 35 DPIA in a single assessment with three outputs:
- DPIA (data subject focus) → submitted to DPA on request
- FRIA (fundamental rights focus) → submitted to market surveillance authority on request
- Article 9 risk management dossier (system safety + robustness focus) → in technical documentation file

This three-output unification is a **V2V refinement**; the AI Act and GDPR do not mandate unification, but their evidence overlap makes it the operationally efficient choice. Coordinate authoring: `compliance-officer` leads system-side; `privacy-counsel` leads data-subject-side; `general-counsel` reviews fundamental-rights framing.

---

## 9. Enforcement geometry

### 9.1 Authorities

- **AI Office** (within EU Commission) — exclusive competence for GPAI oversight under Title IX Chapter III; supervises GPAI provider compliance, can request information, conduct evaluations, impose fines
- **Member State competent authorities** — designated under Article 70; supervise non-GPAI obligations within their jurisdiction
- **Market surveillance authorities** — Member State designated; conduct market surveillance, can require corrective action and withdrawal
- **Notifying authorities** — Member State designated; oversee notified bodies conducting third-party conformity assessment
- **European Artificial Intelligence Board** (Article 65) — coordination across Member States
- **Advisory Forum and Scientific Panel** — provide technical/stakeholder input

### 9.2 Fine ceilings (Article 99)

- **€35M or 7% of worldwide annual turnover** (whichever higher) — Article 5 prohibited practices violations
- **€15M or 3% of worldwide annual turnover** (whichever higher) — non-compliance with operator obligations (Articles 8-15, 16, 22, 23, 24, 25, 26, 27, 28, 50) and most GPAI obligations
- **€7.5M or 1% of worldwide annual turnover** (whichever higher) — supplying incorrect, incomplete, or misleading information to notified bodies and authorities

**SME and startup proportionality (Article 99(6))**: fine ceilings for SMEs and startups are the *lower* of the percentage and the absolute amount, not the higher. This is a meaningful proportionality carve-out for early-stage organizations.

### 9.3 Other enforcement instruments

- Mandatory corrective action and withdrawal under Article 79 (serious risk to health/safety/fundamental rights)
- Conformity assessment certificate withdrawal by notified body
- Public disclosure of non-compliance findings
- Criminal liability under Member State law where the Regulation is implemented through criminal provisions

---

## 10. Effective-date staging

The AI Act applies progressively. Key dates:

| Date | What enters into application |
|---|---|
| **2024-08-01** | Entry into force (the Regulation is law from this date; most provisions deferred per below) |
| **2025-02-02** | Article 5 prohibited practices in force; AI literacy obligations (Article 4) in force |
| **2025-08-02** | GPAI obligations (Chapter V — Articles 51-56) in force; governance provisions (Title III Chapter 1-2-3) in force; penalties (Article 99-101) operational for GPAI |
| **2026-08-02** | **GPAI enforcement begins** — Commission enforcement of GPAI obligations (Articles 51-56) starts. **UNCHANGED by the Digital Omnibus.** NOTE: high-risk Annex III obligations were originally tied to this date but have MOVED to 2027-12-02 (see below). |
| **2026-12-02** (NEW) | **Two new prohibitions added by the Digital Omnibus** enter into force: (1) non-consensual intimate imagery generation, (2) CSAM (child sexual abuse material) generation. Also: **watermarking grace period** for systems placed on the market before 2026-08-02 extended to this date (Article 50 transparency/marking). Provisional agreement 2026-05-07, not yet formally adopted. |
| **2027-12-02** (MOVED from 2026-08-02) | **Stand-alone high-risk system obligations (Annex III, Articles 8-15) enter into application** — 16-month deferral by the Digital Omnibus; conformity assessment obligations (Articles 43-50), post-market monitoring (Article 72), serious incident reporting (Article 73), and remaining penalties for high-risk operational from this date. Provisional agreement 2026-05-07, not yet formally adopted. |
| **2028-08-02** (MOVED from 2027-08-02) | Annex I product-embedded high-risk obligations in force (medical devices, machinery, etc. — systems where AI is integrated into products already covered by sectoral product safety law requiring third-party conformity assessment). Moved by the Digital Omnibus. |
| **Ongoing** | Codes of practice for GPAI (Article 56) — developed in 2025-2026; not statutory deadline but practical compliance milestone for GPAI providers |

**Two load-bearing dates now govern this pack** (post-Digital-Omnibus disaggregation): **2026-08-02 for GPAI enforcement** (unchanged) and **2027-12-02 for stand-alone high-risk Annex III obligations** (moved). The high-risk dates are **agreed but not yet formally published** (provisional agreement 2026-05-07; formal adoption / Official Journal publication expected ahead of 2026-08-02). Verify against the Official Journal before relying on the high-risk dates as settled law. See §15.

---

## 11. Conformity assessment paths

High-risk systems undergo conformity assessment **before placing on market or putting into service** (Article 43).

### 11.1 Annex VI — Internal control

The default path for most Annex III high-risk systems. Provider performs the assessment internally against the Article 8-15 requirements, drawing up the EU declaration of conformity, and affixing the CE marking. No third-party body involvement. Evidence package retained for 10 years post placing on market.

### 11.2 Annex VII — Third-party assessment by notified body

Required for:
- Certain Annex III biometric identification systems (Annex III point 1(a) — real-time remote biometric identification and post-remote biometric identification for law enforcement)
- All Annex I product systems where the underlying sectoral product safety law requires third-party assessment (medical devices, machinery, etc. — assessment integrated into the existing sectoral procedure)

The notified body issues an EU technical documentation assessment certificate; the provider affixes CE marking after positive assessment.

### 11.3 Substantial modifications

Substantial modifications to a placed-on-market high-risk system trigger re-conformity assessment (Article 43(4)). The threshold for "substantial" is defined by Article 3(23) — modification affecting compliance with Articles 8-15 not foreseen by the initial assessment, OR change in intended purpose. For continuous-learning systems, pre-determined changes within the original conformity assessment are NOT substantial modifications (Article 43(4) carve-out).

### 11.4 CE marking and EU declaration of conformity

CE marking on the high-risk AI system or its documentation (Article 48). EU declaration of conformity drawn up by the provider per Annex V (Article 47). Both retained for 10 years post placing on market.

### 11.5 Post-market monitoring (Article 72)

Providers must establish and document a post-market monitoring system proportionate to the nature of the AI technologies and risks. Collects/analyzes data on performance throughout the lifetime, evaluates continuous compliance with Articles 8-15. **Evidence required**: post-market monitoring plan (Article 72(3)), monitoring data records, evaluation reports, corrective action records.

---

## 12. Standard structural scaffolding for downstream skills

Every V2V skill producing AI Act readiness output MUST conform to this structure. Skills cannot omit sections. Skills MAY add domain-specific sections (e.g., a medical-AI skill adds MDR overlay).

### 12.1 Required output sections

```markdown
> ⚠️ **Not legal advice.** [Full disclaimer block per sensitive-skill-guardrails.md §3.1]
>
> **Jurisdiction Assumed:** {EU | EU + national: [Member State] | EU + extraterritorial via Article 2 [basis]}

## Risk-Tier Classification

[Article 5 / Article 6 + Annex I / Article 6 + Annex III / Article 52 transparency / minimal-risk — with rationale]
[If Annex III Article 6(3) carve-out invoked — flag for EU counsel review explicitly]

## Findings

### Finding 1
**What**: [specific gap or readiness state observation]
**Why it matters**: [obligation impact, fine exposure, market access impact]
**Severity**: P0 / P1 / P2
**Suggested next step**: [what the human reviewer should do]
**Article reference**: [specific AI Act Article(s) — e.g., Article 9(2)(b)]

[...repeat for each finding...]

## Reviewer Checklist

- [ ] Jurisdiction confirmed (EU + Member States in scope identified)
- [ ] Risk-tier classification verified by EU counsel (especially if Article 6(3) carve-out invoked)
- [ ] Material facts about system architecture, deployment, and user interaction verified against current product state
- [ ] All P0 findings addressed in technical documentation or accepted as risk with documented reasoning
- [ ] EU counsel engaged for items listed in "Cannot Assess Without"
- [ ] Article 9 risk management dossier exists or is in active drafting
- [ ] Annex IV technical documentation file structure exists or is in active drafting
- [ ] DPIA (GDPR Article 35) and FRIA (AI Act Article 27) coordination confirmed if applicable
- [ ] Conformity assessment path (Annex VI vs Annex VII) determined and confirmed by counsel
- [ ] Post-market monitoring plan (Article 72) drafted or in active development

## Cannot Assess Without Licensed EU Counsel

- The settled effective date for stand-alone high-risk (Annex III) obligations — the Digital Omnibus moved it from 2026-08-02 to **2027-12-02** by provisional agreement (2026-05-07), but this is **agreed and not yet formally adopted / published in the Official Journal**; counsel + the OJ govern the settled date (see §15)
- Article 6(3) carve-out determinations for Annex III systems (the most litigation-likely boundary)
- Member State implementing measure variations (national designations under Articles 70 + 74)
- Sectoral overlay determinations (MDR, IVDR, DORA, MiFID II, UNECE — when AI system is integrated into sectorally regulated product)
- Open-source carve-out applicability for GPAI providers (Article 53(2) conditions)
- Systemic-risk designation by Commission outside the 10^25 FLOPs presumption (Article 51)
- Trade-secret redaction strategy for Article 11 + Annex IV technical documentation (Article 78 confidentiality interaction)
- GDPR Article 9 lawful basis for special-category-data processing for bias detection under AI Act Article 10(5)
- Liability allocation between provider, deployer, importer, distributor under Articles 25-27 in multi-actor deployment
- Enforcement strategy and engagement posture with AI Office, market surveillance authorities, and Member State competent authorities

## Reviewer Sign-Off

- Reviewer name + role: ________________
- Pass 1 (scaffolding) verdict: GO / REWORK — by Director of Legal Affairs
- Pass 2 (substantive) verdict: GO / GO WITH CHANGES / REWORK — by General Counsel
- Date: ________________
```

### 12.2 ROI framing

Every sensitive skill consuming this pack frames ROI as **"time saved on drafting and triage"** — never "review acceleration," "counsel time saved," or equivalent UPL-adjacent phrasing.

---

## 2026-06 Delta Update — Digital Omnibus (as of 2026-06-06)

> **Status: provisional agreement, NOT yet formally adopted.** The changes below reflect the EU AI Act "Digital Omnibus" amendment (part of "Omnibus VII"), on which the Council, Parliament, and Commission reached **provisional political agreement on 2026-05-07**. Formal adoption and Official Journal publication are expected "in the coming weeks" ahead of 2026-08-02. Until OJ publication, treat every high-risk date below as **agreed but not yet settled law** and verify against the Official Journal before relying on it. If formal adoption changes details, this section requires a future update.

This section is referenced throughout the pack as **§15** (the in-line date corrections above point here for the full rationale and sources).

### What changed

| Obligation | Old anchor | New anchor | Status |
|---|---|---|---|
| **GPAI obligations (Articles 51-56)** | In force since 2025-08-02; Commission enforcement begins **2026-08-02** | **UNCHANGED** — still 2026-08-02 enforcement | In force (obligations); enforcement date unchanged |
| **Stand-alone high-risk (Annex III) obligations (Articles 8-15)** | 2026-08-02 | **2027-12-02** (16-month deferral) | Provisional |
| **Annex I product-embedded high-risk obligations** | 2027-08-02 | **2028-08-02** | Provisional |
| **NEW prohibition: non-consensual intimate imagery generation** | — | **2026-12-02** | Provisional |
| **NEW prohibition: CSAM generation** | — | **2026-12-02** | Provisional |
| **Watermarking grace period** (pre-2026-08-02 systems, Article 50 marking) | — | extended to **2026-12-02** | Provisional |

### The load-bearing nuance (do not collapse)

The single most important correction: **the old "2026-08-02 for everything high-risk + GPAI" anchor is now wrong and must be disaggregated.**

- **GPAI = 2026-08-02 enforcement, UNCHANGED.** Wherever the pack ties GPAI (Articles 51-56 / 53 / 55) to an Aug-2-2026 enforcement landing, that is still correct. Keep it.
- **Stand-alone high-risk (Annex III) = 2027-12-02, MOVED.** Wherever the pack ties high-risk Annex III obligations (Articles 8-15, 43-50, 72, 73) to Aug-2-2026, that is now stale and has been corrected in §3, §5, §6, and §10.
- **Annex I product-embedded high-risk = 2028-08-02, MOVED** (from 2027-08-02). Corrected in §1, §5, §10.

### Two new prohibitions (2026-12-02)

The Digital Omnibus adds two new prohibited practices under the Article 5 family, effective **2026-12-02**: (1) generation of **non-consensual intimate imagery**, and (2) generation of **child sexual abuse material (CSAM)**. Skills assessing prohibited-practice exposure (§4.1) must flag these two new categories for systems with generative-content capabilities. As with all Article 5 prohibitions, the consequence is unlawfulness regardless of consent or commercial justification, with the highest fine tier (€35M / 7% — Article 99(3)).

### Watermarking grace period (2026-12-02)

The transparency/marking obligation for synthetic content (Article 50 / Article 52(2)) now carries an extended **grace period to 2026-12-02** for AI systems placed on the market before 2026-08-02. Systems shipped after that line should not assume grandfathering.

### Sources

- EU Commission Digital Omnibus AI Regulation proposal — https://digital-strategy.ec.europa.eu/en/library/digital-omnibus-ai-regulation-proposal
- Gibson Dunn — https://www.gibsondunn.com/eu-ai-act-omnibus-agreement-postponed-high-risk-deadlines-and-other-key-changes/
- Covington Global Policy Watch — https://www.globalpolicywatch.com/2026/05/eu-ai-act-update-timeline-relief-targeted-simplification-and-new-prohibitions/
- White & Case — https://www.whitecase.com/insight-alert/eu-agrees-digital-omnibus-deal-simplify-ai-rules

### Reviewer flag (sensitive-skill scaffolding)

Because this is a **provisional agreement**, any downstream skill output that states a high-risk effective date MUST carry the caveat "agreed but not yet formally published (Digital Omnibus, provisional agreement 2026-05-07)" and defer to licensed EU counsel + the Official Journal for the settled date. This is added to the `## Cannot Assess Without` enumeration (§12.1).

---

## 13. Cross-references

- `compliance-frameworks.md` §2.8 (EU AI Act pointer reference) — structural overview without obligation depth; this pack is the depth layer
- `compliance-frameworks.md` §3 (control-to-obligation mapping) — AI control IDs trace to AI Act Articles; this pack provides the Article-side depth
- `compliance-frameworks.md` §5.1 (EU AI Act + GDPR overlap) — high-level overlap framing
- `privacy-frameworks.md` — DPIA methodology for GDPR Article 35 coordination
- `hr-ai-governance.md` — when AI Act Annex III point 4 (employment) is in scope; FCRA + NYC AEDT + Texas TRAIGA cross-jurisdictional layer
- `sensitive-skill-guardrails.md` — the scaffolding spec for downstream skill outputs
- `source-attribution.md` — the attribution rule applied to this pack
- `roi-display.md` — the ROI framing rule for sensitive skill consumers

---

## 14. Operating principle

> "Risk-tier classification is the first one-way door. Get it wrong and every downstream obligation, every evidence package, every conformity assessment is wrong with it. The pack's job is to make the classification visible, to make the Article 6(3) carve-out visible, and to make 'this needs EU counsel' visible — not to substitute for the counsel determination itself."
