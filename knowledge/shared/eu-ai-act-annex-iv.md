---
pack: eu-ai-act-annex-iv
consumers:
- compliance-officer
- it-security-policy
- general-counsel
- privacy-counsel
---
# EU AI Act Annex IV — Technical Documentation (V2V Knowledge Pack)

**Version**: 0.2.0-draft
**Owner**: compliance-officer (primary) + general-counsel (substantive co-owner) + it-security-policy (joint author for runtime documentation lens)
**Last updated**: 2026-06-06 (Q2 delta refresh — Digital Omnibus high-risk timeline disaggregation; see §11)
**Consumers**: `/ai-regulatory-audit`, `/compliance-audit` (when --framework=eu-ai-act), `/ai-control-audit`, `compliance-officer`, `general-counsel`, `it-security-policy`, `ai-architect`, `chief-architect`
**Sidecar**: ``compliance-frameworks.md`` (effective-date staging, AI Office guidance status)
**Sources**: ``compliance-frameworks.md`` (canonical EUR-Lex URLs, AI Office Annex IV templates as they publish)
**Sensitive**: false (reference material; user-facing outputs derived from it ARE sensitive)
**Token budget variance rationale**: D14 case (c) — regulatory-scaffolding pack required by `sensitive-skill-guardrails.md` §3 + statutory-citation density inherent to Annex IV's 9-element documentation taxonomy
**Re-verification cadence**: quarterly (next: 2026-08-18; mandatory re-read on 2026-08-02 **GPAI** enforcement landing, AND on formal adoption / Official Journal publication of the Digital Omnibus high-risk timeline amendments that moved the Annex IV / high-risk landing to 2027-12-02 — provisional agreement 2026-05-07; see §11)

---

**Adapted from**:
- EU AI Act Annex IV (Regulation (EU) 2024/1689, eur-lex.europa.eu/eli/reg/2024/1689/oj), specifically Annex IV §§1-9 and Article 11 (Technical Documentation obligations for high-risk AI systems)
- EU AI Act "Digital Omnibus" amendment (provisional agreement Council + Parliament + Commission, 2026-05-07; part of "Omnibus VII"; NOT yet formally adopted / published in the Official Journal as of 2026-06-06) — moves the stand-alone high-risk obligation timeline (to which Article 11 + Annex IV are tied) from 2026-08-02 to 2027-12-02 (see §11)

**Source licence**: EU statute + Digital Omnibus amendment proposal / provisional-agreement reporting (public access; no license restriction on reference and summary)

**Digital Omnibus sources** (see §11):
- EU Commission Digital Omnibus AI Regulation proposal — digital-strategy.ec.europa.eu/en/library/digital-omnibus-ai-regulation-proposal
- Gibson Dunn — gibsondunn.com/eu-ai-act-omnibus-agreement-postponed-high-risk-deadlines-and-other-key-changes/
- Covington Global Policy Watch — globalpolicywatch.com/2026/05/eu-ai-act-update-timeline-relief-targeted-simplification-and-new-prohibitions/
- White & Case — whitecase.com/insight-alert/eu-agrees-digital-omnibus-deal-simplify-ai-rules

**V2V refinements**:
- Translated Annex IV's 9 documentation elements into product-organization deliverable templates (PRD scope, model cards, runtime telemetry specs, change logs, incident playbooks) so a product team can map "what is owed under the statute" onto "what we already produce under V2V"
- Cross-mapped Annex IV to V2V Phase 4 (Execution) as the primary phase carrier for runtime documentation obligations, with hand-offs back to Phase 1 (Decisions) for high-risk classification gating and Phase 3 (Commitments) for risk-management-system documentation under Article 9
- Added per-pack structural scaffolding per `sensitive-skill-guardrails.md` §3 (disclaimer + jurisdiction + findings + reviewer checklist + cannot-assess-without) for every downstream skill output derived from this pack
- Added M42 Pass 2 sequencing constraint to prevent statutory-citation drift from the upstream Q2-1.A `ai-act-readiness.md` pack (which is the primary authority on Article 6 + Annex III high-risk classification)
- ROI framing as "drafting and triage" per `roi-display.md` (NEVER "review acceleration" per the Prohibited Phrasings enumeration in `roi-display.md` Sensitive Skill ROI Framing section)

**Cross-references**: Q2-1.A `ai-act-readiness.md` (PRIMARY authority on high-risk classification + Article 6/Annex III boundary + GPAI obligations); existing `compliance-frameworks.md` (control-to-obligation matrix); Q2-3.3 `csa-ai-controls-matrix.md` (sibling pack — control taxonomy); Q2-3.5 `ai-bom.md` (upstream evidence — AI Bill of Materials feeding Annex IV §2)

---

> 🕐 **Pass 2 deferred per M42**: This pack's Pass 2 substantive review is gated on Q2-1.A `ai-act-readiness.md` Pass 2 GO (target 2026-06-30) to eliminate statutory-citation drift between sibling packs. Pass 1 scaffolding gate (48h binary) applies per normal Q2-3 timing. Until Q2-1.A Pass 2 GO, content here is **DRAFT** and may revise to follow upstream Pass 2 changes — particularly on Article 6 boundary interpretation, Annex III scope, and any AI Office guidance updates landing between now and 2026-06-30.

> ⚠️ **Not legal advice.** This output is a drafting and triage aid generated by a product-organization knowledge pack, not counsel. No attorney-client relationship is created by its production or use. Jurisdiction-specific questions, contested matters, and any decision with material legal or regulatory consequences require review by a licensed EU AI Act counsel. Do not rely on this output as the sole basis for any legal, compliance, or conformity-assessment decision.
>
> **Jurisdiction Assumed:** European Union (Regulation (EU) 2024/1689 applies in EU Member States with national implementing measures under Articles 70 + 74). **UK adequacy carve-out:** the UK is not bound by Regulation 2024/1689 post-Brexit. The UK AI Authority framework (UK AI Regulation White Paper 2023 + subsequent UK AI Bill activity 2025-2026) is **NOT equivalent** to the EU AI Act. UK-deployed systems require a separate UK-jurisdiction assessment; this pack does not provide it.

---

## 1. Purpose and framing

### What this pack covers

The structural scaffolding for producing **Annex IV technical documentation** for high-risk AI systems under the **EU AI Act (Regulation (EU) 2024/1689)**. Annex IV is the operational counterpart to Article 11: Article 11 establishes the obligation to maintain technical documentation; Annex IV (§§1-9) specifies the 9 documentation elements that documentation MUST contain.

This pack translates each of the 9 elements into a V2V product-organization deliverable template, so a product team can identify which existing artefacts already satisfy which element, and which elements require net-new documentation.

The pack feeds three downstream skills with a shared documentation vocabulary:
- `/ai-regulatory-audit` — readiness check on whether Annex IV documentation exists per element, identifies gaps
- `/compliance-audit --framework=eu-ai-act` — gap analysis against Annex IV element-by-element for a specific high-risk AI system
- `/ai-control-audit` — technical control taxonomy traced to Annex IV §3 (monitoring, functioning, control) evidence requirements

### What this pack does NOT cover

- **High-risk classification itself** — Article 6 + Annex III classification is the upstream authority of Q2-1.A `ai-act-readiness.md`. This pack assumes classification is settled. If your system's high-risk status is uncertain, route to Q2-1.A first.
- **GPAI model documentation** — General-Purpose AI obligations under Articles 53 + 55 + Annex XI use a different documentation taxonomy. This pack covers Annex IV (high-risk AI systems) only.
- **Conformity assessment route selection** — Article 43 + Annex VI vs Annex VII selection is a counsel determination, deferred to `## Cannot Assess Without`.
- **Notified body interaction** — the procedural workflow with a notified body during third-party conformity assessment is operational, not documentation-shape, and belongs in `/launch-readiness` workflows.
- **AI Office template formats** — when the EU AI Office publishes structured Annex IV templates (expected progressively through 2026-2027), they supersede the deliverable templates in this pack. Status tracked in `compliance-frameworks.md` sidecar.

### Authoring discipline

- Article number + Annex number + Annex IV section-number pointer references; no statute text reproduction
- Date-sensitive content (AI Office template publications, member-state transposition notes, enforcement actions) lives in `compliance-frameworks.md` sidecar
- No law firm citations; sources are the OJEU text and EU AI Office publications
- Interpretive determinations (Article 6(3) carve-outs, conformity assessment route selection, member-state-level differences) explicitly deferred to licensed EU counsel and named in `## Cannot Assess Without` of every downstream skill output

---

## 2. Dec 2, 2027 Enforcement Anchor (high-risk / Annex IV) — MOVED from Aug 2, 2026 by the Digital Omnibus

**Why this pack is operationally live — but the deadline has MOVED.**

> ⚠️ **Date correction (Digital Omnibus, provisional agreement 2026-05-07; see §11):** The original effective-date staging (Article 113) tied most high-risk AI system obligations — including Article 11 (technical documentation) and by extension **Annex IV** — to **2026-08-02**. The Digital Omnibus amendment **moved the stand-alone high-risk (Annex III) landing to 2027-12-02** (a 16-month deferral). Since Article 11 + Annex IV obligations attach to high-risk systems, **the operative Annex IV anchor is now 2027-12-02**, NOT 2026-08-02. This is **agreed but not yet formally adopted / published in the Official Journal** (as of 2026-06-06); verify against the OJ before relying on it. The 2026-08-02 date is UNCHANGED only for **GPAI** enforcement (Articles 51-56) — which Annex IV does not govern.

For high-risk AI systems placed on the EU market or put into service in the Union on or after **2027-12-02** (the post-Digital-Omnibus high-risk landing; provisional):

- Article 11 technical documentation MUST exist before placement on the market (Article 11(1))
- Documentation MUST contain at minimum the elements set out in Annex IV (Article 11(1))
- Documentation MUST be kept up to date (Article 11(2)) — implicating Annex IV §5 change documentation
- For SMEs and start-ups: simplified Annex IV documentation per Article 11(1) third subparagraph (AI Office to publish simplified template)

For Annex I product-embedded high-risk systems, the landing is **2028-08-02** (moved from 2027-08-02 by the Digital Omnibus).

**Operational consequence**: any V2V product organization shipping a high-risk AI system into the EU market on or after **2027-12-02** (Annex III) or **2028-08-02** (Annex I) needs all 9 Annex IV elements documented and conformity-assessed (Article 43) before placement. The 16-month deferral buys runway, but Annex IV §2 (development-process + training-data documentation) and §5 (change log) cannot be reconstructed post hoc — so the discipline must still begin at inception. Documentation readiness belongs in V2V Phase 3 (Commitments) gating, not Phase 5 (Launch). Do NOT treat the deferral as permission to defer the documentation discipline; treat it as runway to build it properly.

For systems already on the market before the high-risk landing (2027-12-02 for Annex III) but materially modified after that date: Article 6(1) re-triggers; Annex IV documentation obligations attach to the modified system as if newly placed.

---

## 3. The 9 Annex IV Elements (V2V Product-Org Translation)

Each subsection states what Annex IV §N requires (pointer-citation only, no statute reproduction), then maps to the V2V deliverables that satisfy it, then names the owner-agent that produces the deliverable in a V2V product organization.

### §1 — General description of the AI system

**Annex IV requirement**: A general description of the AI system covering its intended purpose, the persons developing it, the date and version, interactions with hardware/software outside the system, versions of relevant software/firmware, deployment forms, hardware on which the system runs, product configurations, user interface description, and instructions for use.

**V2V deliverables**:
- **PRD scope section** — intended purpose, target users, deployment context (cross-ref `/prd` skill output)
- **System architecture diagram** — interactions with external hardware/software (cross-ref `chief-architect` deliverables)
- **Version manifest** — software/firmware versions, build artefacts (cross-ref Q2-3.5 `ai-bom.md` AI Bill of Materials)
- **User documentation / instructions for use** — operator-facing manual (cross-ref `kb-specialist` deliverables)

**Owner**: `product-manager` (intended purpose + user documentation) co-owned with `chief-architect` (architecture diagram) and `ai-architect` (model-system boundary).

**Translation note**: §1 maps cleanly to existing V2V artefacts. The element that is sometimes missing in product orgs is the "instructions for use" — operator-facing documentation written for a non-technical reviewer. PRD ≠ user docs.

### §2 — Detailed description of system elements and the development process

**Annex IV requirement**: Methods and steps for development including pre-trained systems used, design specifications (model architecture, intended uses, design choices and rationale, optimisation objectives), system architecture, computational resources used, data requirements (datasheets describing training methodologies, provenance, scope, characteristics, data labelling procedures, data cleaning methodologies), assessment of human oversight measures, predetermined changes documentation, validation and testing procedures and results.

**V2V deliverables**:
- **Model card** — model architecture, training methodology, design choices, optimisation objectives (cross-ref `ai-architect` model card template)
- **Training data documentation** — datasheets per training dataset, provenance, scope, labelling procedures (cross-ref Q2-3.5 `ai-bom.md` data lineage section)
- **Design rationale document** — design choices and trade-offs documented as the system was built (cross-ref V2V `/decision-record` outputs that touched the system)
- **Human oversight design** — Article 14 human oversight measures, assessment of effectiveness (cross-ref `ai-architect` deliverables)
- **Validation and testing report** — train/test/eval splits, evaluation metrics, performance against intended purpose (cross-ref `ml-engineer` + `experimentation-analyst` deliverables)

**Owner**: `ai-architect` (model + training) co-owned with `ml-engineer` (validation/testing) and `data-architect` (data lineage).

**Translation note**: §2 is the densest element. It assumes the developer maintains rigorous model card + datasheet discipline from inception. **A product org that did not produce these artefacts during development cannot reconstruct them post hoc with full fidelity.** This is where most Annex IV gaps surface. Flag in `/launch-readiness` as a non-negotiable Phase 3 deliverable.

### §3 — Detailed information on monitoring, functioning, and control

**Annex IV requirement**: Information on capabilities and limitations in performance (including degrees of accuracy for specific persons or groups), foreseeable unintended outcomes and risk sources, human oversight measures in place per Article 14, specifications on input data, and instructions for use of the system as deployed.

**V2V deliverables**:
- **Runtime telemetry specification** — what is observed, logged, and surfaced for human oversight (cross-ref `it-security-policy` runtime instrumentation standards)
- **Capabilities and limitations memo** — explicit statement of what the system does well and what it does not, including subgroup performance (cross-ref `user-researcher` + `data-analyst` joint deliverable)
- **Foreseeable misuse register** — anticipated unintended outcomes documented (cross-ref `/risk-analysis` skill output)
- **Human oversight runbook** — operational procedures for the human-in-the-loop / on-the-loop function (cross-ref `ai-architect` Article 14 design document)
- **Input data specification** — required format, validation rules, rejection criteria

**Owner**: `it-security-policy` (runtime telemetry + monitoring instrumentation) co-owned with `ai-architect` (human oversight design) and `product-manager` (capabilities/limitations user-facing framing).

**Translation note**: §3 is where the runtime documentation gap most often surfaces in product orgs. Development-time documentation (§2) tends to be richer than runtime documentation (§3). Build the telemetry spec early, not late.

### §4 — Description of the risk management system

**Annex IV requirement**: A description of the risk management system in accordance with Article 9.

**V2V deliverables**:
- **Risk register** — identified risks per Article 9(2)(a), grouped by phase (design, deployment, post-market)
- **Risk mitigation catalog** — controls and mitigations per identified risk, with effectiveness evidence
- **Article 9 process documentation** — iterative risk-management lifecycle, evaluations, review cadence

**Owner**: `compliance-officer` (risk management system documentation) co-owned with `ai-architect` (technical risk identification) and `general-counsel` (legal/regulatory risk).

**Translation note**: §4 cross-refs Article 9 (which lives in Q2-1.A `ai-act-readiness.md`). The risk management system is not a one-time deliverable; it is a continuous process. Annex IV §4 documents the process AND its current state.

### §5 — Description of changes through system's lifecycle

**Annex IV requirement**: A description of any change made to the system through its lifecycle.

**V2V deliverables**:
- **Change log** — model retraining events, deployment changes, configuration updates, dataset additions
- **Retraining provenance** — what data, what hyperparameters, what evaluation results, signed off by whom
- **Material modification register** — changes significant enough to potentially re-trigger Article 6(1) high-risk re-classification

**Owner**: `ai-architect` (technical changes) co-owned with `product-manager` (functional changes) and `compliance-officer` (material-modification determination).

**Translation note**: §5 is the documentation element most likely to be neglected in continuous-deployment AI systems. A model that retrains weekly produces 52 retraining events per year. Each requires §5 documentation. The discipline must be automated as part of the MLOps pipeline (cross-ref `ml-engineer` + `devops`); it cannot be retroactively reconstructed.

### §6 — List of harmonised standards applied

**Annex IV requirement**: A list of the harmonised standards applied in full or in part, the references of which have been published in the Official Journal of the European Union; where no such harmonised standards have been applied, a description of the solutions adopted to meet the requirements set out in Chapter III, Section 2.

**V2V deliverables**:
- **Standards compliance mapping** — which CEN-CENELEC harmonised standards have been applied (as they publish through 2026-2027), traced to Chapter III Section 2 requirements (Articles 8-15)
- **ISO 42001 AI Management System** mapping if applied (operational management standard, complementary to harmonised standards)
- **Alternative-solutions documentation** — where no harmonised standard exists, the solution adopted and its rationale

**Owner**: `compliance-officer` (standards mapping) co-owned with `it-security-policy` (technical-control mapping to standard clauses).

**Translation note**: As of 2026-05, the CEN-CENELEC harmonised standards stack for the AI Act is still in development under the EU Commission standardisation request (M/593). Early adopters will rely on §6's alternative-solutions documentation pathway. Track standards publication status in `compliance-frameworks.md` sidecar.

### §7 — Copy of the EU declaration of conformity

**Annex IV requirement**: A copy of the EU declaration of conformity referred to in Article 47.

**V2V deliverables**:
- **EU declaration of conformity** — formal document per Article 47, signed by the provider, declaring conformity with the requirements of Chapter III Section 2

**Owner**: `general-counsel` (formal declaration signature path) co-owned with `compliance-officer` (substantive conformity assertion).

**Translation note**: §7 is procedurally simple but substantively load-bearing. The signed declaration of conformity creates statutory liability for the provider. Counsel sign-off is mandatory; the V2V skill does not draft this.

### §8 — Description of the post-market monitoring plan

**Annex IV requirement**: A detailed description of the system put in place to evaluate the AI system performance in the post-market phase in accordance with Article 72, including the post-market monitoring plan referred to in Article 72(3).

**V2V deliverables**:
- **Post-market monitoring plan** — operational plan per Article 72(3) for ongoing system performance evaluation
- **Feedback loop documentation** — how user-feedback, support tickets, incident reports flow back to the development team
- **Performance-drift detection design** — telemetry + thresholds for detecting model degradation post-deployment
- **Periodic evaluation cadence** — when and how the system is re-evaluated post-deployment

**Owner**: `it-security-policy` (monitoring instrumentation + telemetry) co-owned with `support-lead` (feedback loop) and `ai-architect` (performance-drift detection).

**Translation note**: §8 + Article 72 are operationally substantial. The post-market monitoring plan is NOT a static document; it describes an ongoing operational capability. Many product orgs have ad-hoc post-deployment monitoring; Article 72 requires it to be planned, documented, and proportionate.

### §9 — Information on serious incidents

**Annex IV requirement**: A list of the relevant procedures and information referred to in Article 73 (the serious-incident-reporting obligation).

**V2V deliverables**:
- **Incident reporting playbook** — what counts as a serious incident under Article 3(49), how it is detected, who is notified internally, the Article 73 reporting timeline to market surveillance authorities
- **Serious-incident register** — historical log of reported incidents and their disposition
- **Authority notification template** — pre-drafted notification structure for Article 73 reports to the relevant Member State market surveillance authority

**Owner**: `it-security-policy` (incident detection + internal escalation) co-owned with `general-counsel` (Article 73 authority notification) and `compliance-officer` (incident-classification determination).

**Translation note**: §9 is the element most often missing in product orgs that have not previously operated under sectoral incident-reporting regimes (medical devices, financial services). The Article 73 reporting timeline (15 days for serious incidents; 2 days for widespread serious incidents or critical infrastructure) is tight. The playbook must be operational before market placement, not drafted reactively after the first incident.

---

## 4. Cross-Mapping to V2V Phase Model

| V2V Phase | Annex IV elements primarily satisfied | Primary owner-agent |
|---|---|---|
| Phase 1 (Decisions) | §1 (intended purpose declared in PRD), high-risk classification gate from Q2-1.A | `product-manager` + `compliance-officer` |
| Phase 2 (Strategy/Architecture) | §1 (architecture), §2 (design specifications, training data plan), §4 (risk management system design) | `chief-architect` + `ai-architect` |
| Phase 3 (Commitments) | §2 (validation/testing complete), §3 (runtime monitoring designed), §4 (risk-mgmt operational), §6 (standards selected), §8 (post-market plan written), §9 (incident playbook written) | `ai-architect` + `compliance-officer` + `it-security-policy` |
| Phase 4 (Execution / runtime) | §3 (live monitoring), §5 (change log accruing), §8 (post-market plan executing), §9 (incident log accruing if any) | `it-security-policy` + `ai-architect` |
| Phase 5 (Launch/conformity) | §6 (final standards mapping), §7 (declaration of conformity signed) | `general-counsel` + `compliance-officer` |
| Phase 6 (Value/learning) | §5 (material modifications documented), §8 (performance evaluation cycles) | `ai-architect` + `value-realization` |

**Pre-Phase-3 gate**: a high-risk AI system MUST have §§2, 3, 4, 8, 9 documentation drafted before Phase 3 commitment is made. Phase 5 launch requires §§6, 7 complete.

---

## 5. Findings

### Finding 1
**What**: §2 (development process + training data documentation) is the densest Annex IV element and the one most likely to be incomplete in product orgs that did not maintain model card + dataset datasheet discipline from project inception. Reconstructing §2 post hoc — particularly training data provenance and labelling procedures for datasets that have been superseded — is in many cases practically impossible with full fidelity.
**Why it matters**: Article 11(1) requires Annex IV documentation to exist before market placement. A product org that discovers in Phase 5 that it cannot fully document §2 has two options: re-do the relevant model training with discipline (months), or place the system on the market with incomplete documentation (statutory non-conformity, exposing the provider to penalties under Article 99).
**Severity**: P0
**Suggested next step**: Reviewer confirms with `ai-architect` + `ml-engineer` that model cards + dataset datasheets have been maintained from project inception. If not, surface the gap in V2V Phase 3 readiness review, before commitment locks. Mitigation options include scope-limiting the system out of high-risk classification (Article 6(3) — but), deferring market placement until §2 reconstruction completes, or accepting the documentation gap with named counsel sign-off and risk acceptance.

### Finding 2
**What**: §5 (description of changes through system's lifecycle) is incompatible with ad-hoc continuous-deployment practices. A model that retrains weekly without automated retraining-provenance capture cannot satisfy §5 retroactively; the documentation discipline must be built into the MLOps pipeline as a first-class concern, not bolted on.
**Why it matters**: Article 11(2) requires the technical documentation to be kept up to date. Failure to maintain §5 creates ongoing statutory non-conformity throughout the system's operational lifecycle, not just at market placement. Each retraining event without §5 documentation is a separate compliance gap.
**Severity**: P1
**Suggested next step**: Reviewer confirms with `ml-engineer` + `devops` that the MLOps pipeline captures retraining provenance automatically (training data version, hyperparameters, evaluation metrics, signed-off-by). If not, build the capability as a Phase 3 commitment. Defer high-risk system market placement until automated §5 capture is operational.

### Finding 3
**What**: The Article 6(3) carve-out — which excludes certain AI systems from high-risk classification despite falling under Annex III categories — is operationally the most litigation-likely boundary in the entire AI Act (per Q2-1.A `ai-act-readiness.md` framing). A product team that asserts Article 6(3) carve-out to avoid Annex IV obligations is taking a position counsel must validate; the V2V skill does not opine on whether the carve-out applies.
**Why it matters**: An incorrect Article 6(3) assertion exposes the provider to penalties under Article 99 (up to €15 million or 3% of worldwide annual turnover) plus market withdrawal under Article 79. The downside of a wrong carve-out call is asymmetric — the cost of producing Annex IV documentation defensively is much lower than the cost of a regulator-finding non-conformity after market placement.
**Severity**: P0
**Suggested next step**: Reviewer confirms that Article 6(3) carve-out (if asserted) has been validated by licensed EU AI Act counsel with a documented reasoned opinion. Per M42, this pack does NOT take a statutory position on Article 6(3) boundary; the determination is named in `## Cannot Assess Without` and deferred to counsel.

---

## 6. Reviewer Checklist
- [ ] Jurisdiction confirmed (EU; UK adequacy carve-out applied if relevant, with separate UK-jurisdiction assessment if UK deployment in scope)
- [ ] AI system classification confirmed as high-risk per Article 6 + Annex III (cross-ref Q2-1.A `ai-act-readiness.md`); if Article 6(3) carve-out asserted, counsel sign-off documented
- [ ] All 9 Annex IV elements have a named owner-agent assigned per Section 3 of this pack
- [ ] §2 (development process + training data) documentation discipline confirmed from project inception; if not, gap surfaced as P0 in Phase 3 readiness
- [ ] §5 (change log) automation confirmed in MLOps pipeline; if not, gap surfaced as P1 in Phase 3 readiness
- [ ] §8 (post-market monitoring plan) operational design complete, not just documented intent
- [ ] §9 (serious incident playbook) operational with Article 73 reporting timeline understood
- [ ] Conformity assessment route selected per Article 43 (Annex VI vs Annex VII) with counsel sign-off
- [ ] EU declaration of conformity (§7) signature path identified with counsel
- [ ] Re-verification cadence set: quarterly review of this pack + sidecar refresh; mandatory re-read on the high-risk / Annex IV enforcement landing (now **2027-12-02** for Annex III per the Digital Omnibus — moved from 2026-08-02; provisional), AND on formal adoption / Official Journal publication of the Digital Omnibus high-risk timeline amendments
- [ ] Counsel engaged for all `## Cannot Assess Without` items

## 7. Cannot Assess Without Licensed EU Counsel
- High-risk classification under Article 6 + Annex III for your specific system (cross-ref Q2-1.A — this pack assumes classification is settled upstream)
- **Article 6(3) carve-outs** — the most litigation-likely boundary in the entire Act. This pack takes no statutory position on whether your system falls within or outside Article 6(3); the determination is counsel's.
- Conformity assessment route selection under Article 43 (internal control per Annex VI vs third-party assessment per Annex VII)
- Whether your system constitutes a "substantial modification" under Article 3(23), re-triggering Article 6(1) classification and Annex IV documentation refresh
- Whether your post-market monitoring plan (Annex IV §8) satisfies Article 72(3) in detail and proportionality
- Whether a specific event constitutes a "serious incident" under Article 3(49) requiring Article 73 notification, and the applicable reporting timeline (15 days standard; 2 days for widespread serious incidents or critical infrastructure)
- Member-state-level implementation differences — Annex IV citations may differ post national transposition; each Member State designates its own market surveillance authority under Article 70
- The settled effective date for the high-risk / Annex IV landing — the Digital Omnibus moved it from 2026-08-02 to **2027-12-02** (Annex III) and from 2027-08-02 to **2028-08-02** (Annex I) by provisional agreement (2026-05-07), but this is **agreed and not yet formally adopted / published in the Official Journal**; counsel + the OJ govern the settled date (see §11)
- Treatment of legacy systems placed on the market before the high-risk landing (2027-12-02 for Annex III, per the Digital Omnibus; was 2026-08-02) but materially modified after that date
- Interaction with sectoral regimes (medical device AI under MDR/IVDR, financial-services AI under DORA, automotive AI under UNECE) where sector-specific documentation may extend or modify Annex IV obligations
- UK adequacy treatment (post-Brexit; UK AI Authority framework is NOT equivalent to the EU AI Act)
- Penalty exposure under Article 99 for documented non-conformity — counsel risk-rating required
- Privilege and confidentiality treatment of Annex IV documentation when shared with notified bodies and market surveillance authorities

---

## 8. Anti-Patterns / Common Failures

**"Documentation theater."** Producing all 9 Annex IV elements as polished documents that satisfy the auditor checkbox but do not reflect actual operational practice. Annex IV §3 (runtime monitoring) and §8 (post-market monitoring plan) in particular MUST describe operational reality, not aspirational intent. Article 72 + Article 79 give market surveillance authorities the power to verify operational reality; documentation that describes a monitoring capability that does not actually exist is statutory non-conformity, not partial compliance.

**Treating Annex IV as a launch deliverable rather than a development discipline.** §2 (development process + training data) cannot be reconstructed post-hoc. §5 (change log) cannot be back-filled for retraining events that occurred without provenance capture. §8 + §9 (post-market + incidents) are operational capabilities, not documents. Annex IV readiness is a Phase 1-through-3 discipline; launch (Phase 5) is when the documentation is finalised and the declaration of conformity (§7) is signed, not when the documentation is created.

**Asserting Article 6(3) carve-out to avoid Annex IV obligations without counsel sign-off.** The cost of producing Annex IV documentation defensively is much lower than the cost of a regulator-finding non-conformity after market placement. When in doubt, document. The Article 6(3) carve-out is the most litigation-likely boundary in the entire Act; do not bet a product launch on an in-house interpretive call.

**Missing the serious-incident reporting path (§9 + Article 73).** Product orgs without prior sectoral incident-reporting experience routinely under-design §9. The Article 73 timeline (15 days standard; 2 days for widespread serious incidents) does not allow for "draft a playbook reactively after the first incident." The playbook must be operational before market placement.

**Conflating GPAI documentation (Annex XI) with high-risk system documentation (Annex IV).** GPAI obligations under Articles 53 + 55 use a different taxonomy. A system that is both a GPAI model AND deployed in a high-risk context attaches BOTH documentation regimes; one does not substitute for the other.

---

## 9. V2V Cross-References

**PRIMARY upstream authority**:
- **Q2-1.A `ai-act-readiness.md`** — high-risk classification (Article 6 + Annex III), GPAI obligations (Articles 53 + 55), effective-date staging through **2028-08-02** (post-Digital-Omnibus disaggregation: GPAI enforcement 2026-08-02 unchanged; stand-alone high-risk Annex III moved to 2027-12-02; Annex I product-embedded moved to 2028-08-02 — all provisional), Article 9 risk management system, conformity assessment routes. M42 sequencing: this pack's Pass 2 substantive review is gated on Q2-1.A Pass 2 GO to eliminate statutory-citation drift.

**Sibling Q2-3 packs**:
- **`agent-identity.md` (Q2-3.1)** — Annex IV §3 (monitoring, functioning, control) consumes agent-identity audit trail per the lifecycle controls in that pack; high-risk agent systems must produce identity-bound audit per Article 11.
- **`mcp-governance.md` (Q2-3.2)** — Annex IV §3 (monitoring, audit-trail) and §4 (risk management system) requirements consume MCP-server registry records, approval-workflow evidence, and audit-trail completeness from that pack for high-risk systems consuming MCP integrations.
- **`csa-ai-controls-matrix.md` (Q2-3.3)** — Control taxonomy that feeds Annex IV §3 (monitoring) and §4 (risk management system) evidence. AICM is the control vocabulary; Annex IV is the evidentiary structure regulators consume.
- **`ai-bom.md` (Q2-3.5)** — **Upstream evidence pack**. AI BOM feeds Annex IV §1 (general description, versions, dependencies), §2 (training data provenance, datasheets, design specifications), and §3 (monitoring, functioning, control) directly per AI BOM §3.1.

**Sibling Q2-5 packs**:
- **`mcp-architecture.md` (Q2-5.1)** — When high-risk systems use MCP transport, Annex IV §1 (architecture) and §2 (design specifications) documentation cites that pack's transport variant, capability negotiation, and server architecture decisions.
- **`agentic-security.md` (Q2-5.3)** — Article 15 (robustness, accuracy, cybersecurity) obligations for high-risk systems consume that pack's MITRE ATLAS + OWASP LLM Top 10 + CSA Agentic Trust Framework threat-model coverage; Annex IV §3 documentation cites the security controls in place.

**Existing context**:
- `compliance-frameworks.md` — control-to-obligation matrix (§3 of that pack), where AI control IDs trace to AI Act Article evidence requirements.
- `privacy-frameworks.md` — GDPR Article 35 DPIA + AI Act Article 27 FRIA overlap, relevant to §3 (foreseeable unintended outcomes for specific persons or groups).
- `data-governance.md` — Annex IV §2 dataset documentation discipline at the data-governance-policy layer.

**Sidecar**: ``compliance-frameworks.md`` — AI Office Annex IV template publication status, CEN-CENELEC harmonised standards stack status, Member State transposition status, high-risk / Annex IV enforcement landing tracker (now **2027-12-02** for Annex III per the Digital Omnibus — moved from 2026-08-02; provisional, pending Official Journal publication) plus the separate **2026-08-02 GPAI** enforcement tracker.

---

## 11. 2026-06 Delta Update — Digital Omnibus (as of 2026-06-06)

> **Status: provisional agreement, NOT yet formally adopted.** The change below reflects the EU AI Act "Digital Omnibus" amendment (part of "Omnibus VII"), on which the Council, Parliament, and Commission reached **provisional political agreement on 2026-05-07**. Formal adoption and Official Journal publication are expected "in the coming weeks" ahead of 2026-08-02. Until OJ publication, treat the high-risk / Annex IV date below as **agreed but not yet settled law** and verify against the Official Journal before relying on it. If formal adoption changes details, this section requires a future update.

This section is referenced throughout the pack as **§11** (the in-line date corrections in §2, §6, §7, and §9 point here for the full rationale and sources).

### Why this matters for Annex IV specifically

Annex IV technical-documentation obligations are tied to **Article 11**, which is a **stand-alone high-risk system obligation** (Articles 8-15). The Digital Omnibus moved the stand-alone high-risk (Annex III) landing **from 2026-08-02 to 2027-12-02** — a 16-month deferral. Therefore **the operative Annex IV anchor moved with it: from 2026-08-02 to 2027-12-02** (Annex III systems), and **2028-08-02** for Annex I product-embedded high-risk systems (moved from 2027-08-02). This pack's old "Aug 2, 2026" anchor is now stale for Annex IV purposes and has been corrected in-place in §2, §6, §7, and §9.

### What changed (Annex-IV-relevant subset)

| Obligation | Old anchor | New anchor | Status |
|---|---|---|---|
| **Stand-alone high-risk (Annex III) obligations — incl. Article 11 + Annex IV** | 2026-08-02 | **2027-12-02** (16-month deferral) | Provisional |
| **Annex I product-embedded high-risk obligations (incl. their Annex IV docs)** | 2027-08-02 | **2028-08-02** | Provisional |
| **GPAI obligations (Articles 51-56)** — *Annex IV does NOT govern these* | enforcement 2026-08-02 | **UNCHANGED** — still 2026-08-02 enforcement | In force (obligations); enforcement unchanged |

### The load-bearing nuance (do not collapse)

- **Annex IV = high-risk = 2027-12-02 (Annex III) / 2028-08-02 (Annex I), MOVED.** Wherever this pack tied Annex IV / Article 11 / high-risk obligations to Aug-2-2026, that is now stale and has been corrected.
- **GPAI = 2026-08-02 enforcement, UNCHANGED — but Annex IV does NOT cover GPAI.** GPAI model documentation uses Annex XI (Articles 53 + 55), a different taxonomy (see §1 "What this pack does NOT cover" and the anti-pattern in §8). So the unchanged GPAI date is not an Annex IV anchor; do not import it as one.

### Two new prohibitions + watermarking grace period (context only — not Annex IV obligations)

The Digital Omnibus also adds two new Article-5-family prohibitions (non-consensual intimate imagery generation; CSAM generation) effective **2026-12-02**, and extends the **Article 50 watermarking grace period to 2026-12-02** for systems placed on the market before 2026-08-02. These are NOT Annex IV technical-documentation obligations; they are noted here for completeness and tracked in the primary pack (`ai-act-readiness.md` §15). For prohibited-practice and transparency-marking assessment, route to `ai-act-readiness.md`.

### Sources

- EU Commission Digital Omnibus AI Regulation proposal — https://digital-strategy.ec.europa.eu/en/library/digital-omnibus-ai-regulation-proposal
- Gibson Dunn, "EU AI Act Omnibus Agreement: Postponed High-Risk Deadlines and Other Key Changes" — https://www.gibsondunn.com/eu-ai-act-omnibus-agreement-postponed-high-risk-deadlines-and-other-key-changes/
- Covington Global Policy Watch, "EU AI Act Update: Timeline Relief, Targeted Simplification, and New Prohibitions" — https://www.globalpolicywatch.com/2026/05/eu-ai-act-update-timeline-relief-targeted-simplification-and-new-prohibitions/
- White & Case, "EU Agrees Digital Omnibus Deal to Simplify AI Rules" — https://www.whitecase.com/insight-alert/eu-agrees-digital-omnibus-deal-simplify-ai-rules

### Reviewer flag (sensitive-skill scaffolding)

Because this is a **provisional agreement**, any downstream skill output that states an Annex IV / high-risk effective date MUST carry the caveat "agreed but not yet formally published (Digital Omnibus, provisional agreement 2026-05-07)" and defer to licensed EU counsel + the Official Journal for the settled date. This is reflected in the `## Cannot Assess Without` enumeration (§7).

---

## 10. Operating Principle

> "Annex IV is not 9 documents to write at launch. It is 9 disciplines to practice from inception. The skill produces drafting and triage scaffolding for human compliance, conformity, and counsel review — never the review itself."
