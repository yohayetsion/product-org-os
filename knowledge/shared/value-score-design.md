---
pack: value-score-design
consumers:
- csm
- cs-ops
- value-realization
- cs-dir
- vp-product
- bizops
- product-manager
- privacy-counsel
---
# Value Score Design (V2V Knowledge Pack)


**Version**: 1.0
**Type**: knowledge-pack (sensitive-adjacent)
**Primary Users**: `csm`, `cs-ops`, `cs-dir`
**Secondary Users**: `value-realization` (Pattern-1 consultant per M35), `bizops`, `product-operations`, `director-product-marketing`
**Status**: Q2-4.1 authored 2026-05-18 (V2V Q2 2026 refresh, Wave 1 of Q2-4)
**Joint Authors**: 🌟 CSM + 📊 CS Ops (Pattern-1 consultation: 💰 Value Realization)
**Token Budget Variance Rationale**: Pack exceeds the 2000-token soft cap per D14 cases (a) joint-authoring (two-author technical content with explicit ownership demarcation) AND (c) regulatory-scaffolding (sensitive-adjacent: full §3 scaffolding stack required — disclaimer block, Jurisdiction Assumed, Findings with severity, Reviewer Checklist, Cannot Assess Without — for Title VII disparate-impact and GDPR Article 22 coverage on customer-scoring features). Pack is preload-target for Wave 2 cross-references (`ai-agent-supervisor.md` sibling, `customer-success-methodology.md` refresh, Q2-2 pricing/metrics packs); concentrating the design pattern + scaffolding in a single load-bearing reference is preferable to fragmenting it across multiple consumers.

---

**Adapted from**:
  - TSIA Value Score framework — publicly documented in TSIA member research and TSIA conference presentations through 2026. The Value Score construct is TSIA's named successor framing to the legacy Health Score; the framework is referenced (not reproduced) per TSIA membership terms.
  - Gainsight (CS platform) — publicly documented Value Score and Customer 360 patterns through Pulse 2026 sessions and the Gainsight Knowledge Base; "Atlas AI-Native Services" managed-services business announced 2026-05-27 (globenewswire.com/news-release/2026/05/27/3302230), tying accountability to GRR/NRR via AI "renewal pods" + human Renewal Agent Managers.
  - Pendo (product analytics + in-product engagement) — publicly documented value-realization analytics patterns through 2026.
  - Staircase AI — acquired by Gainsight 2024; MCP (Model Context Protocol) support announced April 2026, enabling Value Score signals to flow into agentic CS tooling.
  - Journeyz — publicly documented customer-journey instrumentation patterns through 2026.
  - Kyndryl + AWS — publicly documented enterprise customer-value-realization frameworks through 2026 partner content.
  - GDPR Article 22 (Regulation (EU) 2016/679) — automated individual decision-making, including profiling.
  - Title VII of the Civil Rights Act of 1964 (42 U.S.C. § 2000e et seq.) — disparate-impact analysis under Griggs v. Duke Power Co., 401 U.S. 424 (1971), as applied to algorithmic scoring per EEOC guidance "The Americans with Disabilities Act and the Use of Software, Algorithms, and Artificial Intelligence to Assess Job Applicants and Employees" (2022) and analogous EEOC analyses for race/sex/national-origin disparate impact in AI-assisted decisions.

**Source licence**:
  - TSIA / Gainsight / Pendo / Staircase AI / Journeyz / Kyndryl / AWS — per-source commercial terms; cited by name and concept reference only. No proprietary content reproduced.
  - GDPR + Title VII — public statute, no license restriction on reference or summary.

**V2V refinements**:
  - Translated the TSIA Value Score construct into a product-organization CS-Ops design pattern with explicit operational ownership (`csm` customer-facing; `cs-ops` instrumentation) and audit cadence.
  - Cross-referenced the per-seat-pricing structural failure thesis to Q2-2 packs (`pricing-frameworks.md` and `metrics-frameworks.md`, both TBC after Wave 2 stitching per M40).
  - Added sensitive-adjacent scaffolding per `sensitive-skill-guardrails.md` §3: protected-class disparate-impact risk on scoring features that correlate with protected classes (industry, geography, language, company size as proxies); GDPR Article 22 coverage when scoring drives consequential decisions on EU data subjects.
  - Integrated with V2V Phase 5 (Outcomes) Decision Interface as the pre-authored content target for the Customer-Outcome Decision Interface Charter when V5.2 alignment resumes (per D10).
  - ROI framing as "drafting and triage" per `roi-display.md` Prohibited Phrasings enumeration.
  - **2026-06 delta**: added the emerging "CS-as-outcome-service" commercial model (Gainsight Atlas AI-Native Services, 2026-05-27) as a real-world answer to the §6.x Success Paradox — a vendor moving from software to outcome-priced managed service tied to retention metrics.

---

> ⚠️ **Not legal/HR/privacy advice.** This output is a drafting and triage aid produced by a V2V knowledge pack, not counsel. No attorney-client relationship is created by its production or use. Customer-scoring models that use features correlated with protected classes (race, sex, national origin, disability, age, religion) carry disparate-impact exposure under Title VII (when scoring informs employment-adjacent decisions on customer-side individuals) and GDPR Article 22 exposure (when scoring drives consequential automated decisions on EU data subjects). Decisions to deploy a customer Value Score model MUST be reviewed by licensed counsel + qualified privacy/HR specialists in the operative jurisdiction before production use.
>
> **Jurisdiction Assumed:** U.S. federal (Title VII disparate-impact analysis when Value Score informs retention/expansion outcomes that affect employment-adjacent decisions, e.g., customer-side individual access, license assignment, or workforce-affecting renewals) + EU (GDPR Article 22 automated individual decision-making coverage when Value Score drives consequential decisions on EU data subjects). Other jurisdictions (UK DPA 2018, California CCPA, state-level AI-in-decisions statutes including Colorado SB 24-205 effective 2027, Texas TRAIGA, NYC LL144 by analogy, Illinois HB 3773) require independent counsel review. Cross-border data transfer obligations apply if scoring data crosses jurisdictions.

---

## 1. Why Value Score, Not Health Score

The 2026 inflection that forced this pack: **Health Score asks "is this customer healthy?" Value Score asks "is this customer GETTING VALUE?"** The distinction is load-bearing because per-seat SaaS pricing is structurally failing.

The mechanism is straightforward and increasingly hard to ignore. AI agents are cutting customer-side headcount across knowledge-work functions — support, ops, finance, marketing. The customer's seat count goes down. A traditional Health Score reads that signal as churn risk: utilization decay, fewer logins, fewer DAU. But the customer is **still extracting value** — often more value than before, because the AI-augmented workflow produces more output per remaining seat. Health Score flags the account red. CSM scrambles. Customer is confused: they're getting more done than ever. The metric is lying about what's happening.

Value Score reverses the question. Instead of "are usage signals trending down?" it asks "are outcome signals trending up?" Outcomes are workflow completions, jobs-to-be-done satisfied, business KPIs moved. A customer with 30 seats extracting 2x the workflow throughput of an equivalent 50-seat customer is, by Value Score, healthier — even though by seat count and by login volume they look weaker. The metric tracks what the customer pays for, not what the vendor sold them.

This is not a rebrand. It's a re-instrumentation. The inputs change, the weights change, the operational use changes, and the governance changes. Pack §3 walks through each. Pack §6 documents the anti-patterns we are most likely to fall into.

**Why this matters for V2V Phase 5 (Outcomes)**: when V5.2 alignment resumes, the Customer-Outcome Decision Interface Charter (per D10) needs a metric that survives the per-seat collapse. Value Score is that metric. This pack is the pre-authored content target.

## 2. Sensitive-Adjacent Applicability

Value Score design is sensitive-adjacent (not core-sensitive like HR-AI), but the disparate-impact and automated-decision-making risk surface is real enough to require structural scaffolding per `sensitive-skill-guardrails.md` §3.

**The disparate-impact pathway**: customer Value Score features that look operationally neutral can be protected-class proxies. Common examples:

| Feature | Why it's a potential proxy |
|---|---|
| Industry vertical | Industry correlates with workforce demographics; certain verticals carry strong race/sex/national-origin skews |
| Company size (employee count) | Correlates with industry; correlates with founder demographics in earlier-stage segments |
| Geography (country, region, state) | Direct correlation with national origin; state-level correlations with race and ethnicity |
| Language (primary working language of customer) | Direct national-origin proxy |
| Founder/leadership demographic signals | Direct protected-class signal if explicitly captured |
| Tech-stack proxies (e.g., legacy stack vs. modern) | Correlates with company age, which correlates with industry, which correlates with workforce demographics |

If Value Score drives consequential decisions — renewal probability, expansion eligibility, support-tier assignment, executive escalation routing, customer-side individual access decisions — the disparate-impact analysis attaches. The mere fact that the scored entity is a "customer" not an "employee" does not eliminate the exposure when downstream decisions affect employment-adjacent outcomes on customer-side individuals (e.g., who at the customer gets access to a feature that confers career-relevant skill development).

**The GDPR Article 22 pathway**: when Value Score is used to make automated decisions that produce legal or similarly significant effects on EU data subjects, Article 22 applies. The data subject has the right to (i) not be subject to a solely automated decision, (ii) human intervention, (iii) express their view, and (iv) contest the decision. A Value Score that auto-triggers a non-renewal recommendation or auto-blocks a feature for an EU-based individual is squarely within Article 22's scope unless one of the narrow exceptions applies (necessary for contract performance, authorized by Union/Member State law with safeguards, or based on explicit consent).

**The customer-trust pathway** (not statutory but structurally important): customers acting on AI-driven scoring of THEIR business carry their own transparency obligations. A B2B customer using your platform may need to disclose to their employees, contractors, or end-customers that vendor-side AI scoring is influencing decisions affecting them. Value Score transparency policy is therefore not just a vendor governance question; it's a contractual and reputational question.

## 3. The Value Score Design Stack

The stack runs top-to-bottom: inputs → outputs → composition → operational use → audit. Each layer has explicit ownership.

### 3.1 Value Inputs — What customers DO  [Owner: 📊 CS Ops]

The instrumentation layer. CS Ops owns this because it requires platform-analytics and product-analytics integration that customer-facing CSMs neither can nor should maintain.

**Workflow completions** are the foundational input. A workflow is a customer-defined unit of work the platform enables. Examples: a campaign sent, an invoice processed, a candidate screened, a ticket resolved, a deal closed. Workflow completions are counted with a time window (typically 30 days rolling), normalized by customer tier or segment, and trended quarter-over-quarter. A flat or rising workflow count under a falling seat count is the signal Value Score is designed to surface.

**Outcome milestones** are customer-attested or platform-verified achievements tied to the customer's success plan. The first complete onboarding milestone. The first integration deployed. The first cross-functional team trained. Hitting target performance on a customer-defined KPI. These are sparse, high-signal events; they do not occur weekly.

**Expansion events** include addition of a new product line, a new department's adoption, a new use case launched on existing seats. Expansion events are independent of net-new seat purchase; a customer extracting more value per seat without buying more seats is a positive Value Score signal that traditional revenue-expansion metrics miss.

**Renewal signals** are the highest-confidence value signal but also the latest. By the time a renewal commits, the value question has been answered. Renewal signals are still input to Value Score because they are the gold-label data the model is ultimately validated against.

### 3.2 Value Outputs — Customer-attested signals  [Owner: 🌟 CSM]

The customer-voice layer. CSMs own this because the signals require customer dialogue, not platform telemetry.

**NPS retirement** is the deliberate choice. NPS measures sentiment toward the brand, not value extracted. It survives in vendor reporting because it's simple and benchmarkable, but it predicts almost nothing about Value Score. We retire it from Value Score composition (it can survive as a separate marketing metric).

**CSAT-by-job-to-be-done** replaces blanket CSAT. The customer answers "how satisfied are you with how the platform helps you do [specific JTBD]?" rather than "how satisfied are you with [platform]?". The JTBD-bound CSAT correlates substantially better with workflow completion trends than blanket CSAT does.

**Explicit value verbatim** is direct customer language captured in EBR/QBR notes about value experienced: "we replaced two contract reviewers with this," "our close cycle dropped from 9 days to 4," "we onboard customers 60% faster." Verbatim signals are coded against the customer's stated success plan goals and counted as one outcome milestone hit per coherent verbatim. The verbatim itself is preserved for downstream use (case studies, expansion conversations, renewal narratives).

### 3.3 Score Composition  [Owner: 📊 CS Ops + 🌟 CSM]

Weighted composite, tier-segmented, time-windowed. Composition is owned jointly: CS Ops calculates and maintains; CSM validates that the composition reflects what they observe in the field.

**Weighting** is segment-specific. An enterprise customer's Value Score weights expansion events and outcome milestones heavily; a mid-market customer's Value Score weights workflow completion velocity more heavily; an SMB customer's Value Score weights renewal-signal proxies (login frequency at the user level, not the seat level) more heavily because the higher-signal inputs are operationally too rare to instrument well at SMB price points.

**Tier segmentation** prevents the cross-segment averaging that destroys signal in single-population Health Scores. An enterprise red is operationally very different from an SMB red.

**Time-windowed** means the score is calculated on a rolling window (30, 60, 90 days) and trended, not pointed-in-time. Velocity of change matters more than absolute level for triggering operational action. A customer at 70 trending up is a different conversation from a customer at 70 trending down.

**Forbidden inputs** at composition time: any explicit protected-class feature, any feature whose disparate-impact analysis has not been run (see §3.5), and any feature for which subgroup-disaggregated evaluation is not feasible.

### 3.4 Operational Use  [Owner: 🌟 CSM + 🌟 CS Director]

What the score triggers. Misuse here is the most common failure mode.

**Who acts on the score**: the assigned CSM acts on individual account scores; the CS Director acts on portfolio-level score distributions; the renewal lead consumes scores at T-90 days as input (not decision) to renewal planning; the executive sponsor consumes top-of-funnel red-trend reports.

**Frequency**: CSMs review their book's scores weekly. CS Director reviews portfolio distributions monthly. Renewal teams pull scores at T-90 and T-30. EBRs reference Value Score with full transparency to the customer; QBRs internalize them.

**Threshold-driven actions** are the operational levers. Crossing from yellow to red triggers an internal account review, not an automatic action. Crossing from green to yellow triggers a CSM check-in. Crossing into champion-tier triggers expansion qualification and case-study qualification, with a customer-side opt-in for both. **No threshold should auto-trigger a consequential decision (non-renewal, license suspension, support tier downgrade, individual feature block) without human review.** This is the GDPR Article 22 line — and as a matter of customer-trust practice, it's also the right line outside EU jurisdiction.

### 3.5 Audit + Governance  [Owner: 📊 CS Ops + 💰 Value Realization (consultant)]

The control layer. The protected-class disparate-impact analysis lives here.

**Pre-deployment audit**: BEFORE the Value Score model deploys, run subgroup-disaggregated evaluation. For each feature in the composition, evaluate score distribution across protected-class proxies (industry, geography, language, company size). If a feature produces materially different score distributions across proxy groups for similarly-situated customers, the feature requires either (a) removal, (b) reweighting, or (c) documented business-necessity justification with counsel review. The "four-fifths rule" (EEOC, 29 CFR §1607.4(D)) gives a starting threshold for "materially different" but is not the only test; consult §5 Cannot Assess Without.

**Ongoing audit**: the same subgroup-disaggregated evaluation runs quarterly on production scores. Drift detection is required because input data shifts, customer-base composition shifts, and feature meaning shifts.

**Ownership of retraining**: CS Ops owns the model; `value-realization` is the Pattern-1 consultant on whether the metric construct still reflects V2V Phase 5 outcomes intent. Retraining cadence is at least quarterly; ad-hoc retraining is triggered by drift detection or by material change in customer segment composition.

**Customer transparency policy**: customers are informed (in onboarding, in EBR, and in contract terms) that a Value Score is calculated, what the broad input categories are (workflow completions, outcome milestones, customer-attested signals), and that consequential decisions are human-reviewed not algorithm-triggered. The right-to-explanation does not require revealing the exact weights; it does require revealing the existence and scope of the scoring.

## 4. Cross-References to Per-Seat Structural Failure (Load-Bearing)

This section will mature once Q2-2 packs land. For Wave 1 standalone authoring per M40, the placeholder is explicit.

The per-seat-pricing structural failure thesis (currently distributed across Q2-2 Wave-2-target packs `pricing-frameworks.md` §[2026 per-seat structural failure] and `metrics-frameworks.md` §9, both TBC) is the macro context for Value Score. The short version:

Per-seat pricing made sense when seats were a reasonable proxy for value extracted. A larger team using software extracted more value than a smaller team. AI agents broke that proxy: a smaller AI-augmented team extracts more value than a larger non-augmented team. Vendors who continue measuring success in seats are systematically misreading their healthiest customers as their weakest customers, and vice versa.

Value Score is the metric that survives the per-seat collapse. It measures what the customer extracts (workflows completed, outcomes hit, value realized), not what they consume (seats, logins, sessions). The implication for pricing: vendors will need to shift toward value-aligned pricing (usage, outcomes, hybrid) to keep pricing signal aligned with value signal. That is the Q2-2 pricing-frameworks pack's territory, not this pack's. But the metric has to land first; pricing follows the metric.

**Concrete example (illustrative)**: Customer A has 50 seats, Customer B has 30 seats. Customer B completes 2x the workflows of Customer A on the same product, hits more outcome milestones in EBRs, and has higher JTBD-bound CSAT. Customer A's Health Score (seat utilization, logins per week, DAU) is healthier than Customer B's. Customer B's Value Score is meaningfully higher than Customer A's. When renewal comes, Customer A is more likely to question value (low extraction per seat); Customer B is more likely to expand (high extraction per seat). Health Score told the wrong story; Value Score tells the right one.

## 2026-06 Delta Update (as of 2026-06-06)

### CS-as-outcome-service: Gainsight Atlas AI-Native Services (2026-05-27)

The §4 per-seat structural failure thesis (per-seat pricing fails as AI cuts customer-side headcount) implies a Success Paradox: the metric that survives the collapse (Value Score) is not the metric the vendor is paid against (seats). On 2026-05-27 Gainsight announced a real-world answer — **Atlas AI-Native Services (AINS)**, a managed-services business where Gainsight owns the renewal **outcome** end-to-end, with accountability tied directly to **GRR/NRR** rather than to seat consumption or software usage. It is the first canonical CS-platform vendor moving from selling software to selling the retention outcome itself.

**Operating model** (as announced):
- **"Renewal pods"** of AI agents paired with human **Renewal Agent Managers** who handle escalations and edge cases — the human-on-the-loop supervisor pattern (see `ai-agent-supervisor.md`) applied to the renewal motion rather than the support motion.
- Agents run personalized outreach, follow-ups, and contract execution across the **long-tail customer base** (the segment where per-CSM economics never worked under headcount-priced CS).
- Accountability is **outcome-priced**: Gainsight is measured on the GRR/NRR it produces, not on seats deployed or activity volume.

**Why this matters for Value Score**: AINS is the commercial-model corollary to the metric this pack defines. Value Score answers "is the customer getting value?" at the metric layer; AINS answers "who is accountable for the value outcome, and how are they paid?" at the commercial layer. When a vendor's revenue is tied to GRR/NRR, the Value Score (what the customer extracts) and the vendor's incentive (the retention outcome) finally point the same direction — closing the per-seat misalignment §4 describes. For V2V-scale orgs, AINS is also the "Managed" tier of the build-vs-buy-vs-managed sourcing model in the `ai-agent-supervisor.md` 2026-06 delta: outsourcing the renewal outcome to a vendor whose Renewal Agent Managers govern the agent fleet, while the internal org governs the contract and the outcome SLA.

**The governance carry-over (load-bearing)**: an outcome-priced managed service does not eliminate the disparate-impact and Article 22 exposure this pack scaffolds — it relocates it. If the vendor's renewal pods score the long-tail customer base to prioritize outreach and contract-execution effort, that scoring is a Value-Score-class model with the same §2 protected-class-proxy and §3.5 audit obligations, now run by a third party. The §7 Reviewer Checklist and §8 Cannot Assess Without items apply to the vendor's model under data-processing and sub-processing terms (see §8 bullet on customer contract permissions). Outsourcing the model does not outsource the accountability.

**Cross-reference**: the reciprocal is `ai-agent-supervisor.md` 2026-06 delta (Gainsight Agentic Stack, 2026-05-28) — the build-vs-buy-vs-managed three-tier sourcing model, of which AINS is the "Managed" tier.

## 5. V2V Phase 5 (Outcomes) Integration

Value Score outputs feed the V2V Phase 5 Outcomes Decision Interface. When V5.2 alignment resumes (per D10), this pack is the pre-authored content target for the Customer-Outcome Decision Interface Charter.

**Cadence**: quarterly review. The Customer-Outcome Decision Interface convenes the `cs-dir` (action protocol owner), `value-realization` (metric construct integrity owner, Pattern-1 consultant on this pack), `vp-product` (Phase 5 escalation), and `bizops` (financial linkage). Value Score portfolio distributions and trend data are the primary inputs.

**Decision rights**:
- `value-realization` owns whether the Value Score metric still measures the right thing (construct validity)
- `cs-dir` owns the action protocol — what operational moves the score triggers
- `vp-product` owns the strategic question of whether Value Score patterns indicate a Phase 5 outcome miss that escalates to Phase 1 (strategic intent re-examination) or Phase 2 (commitment re-examination)
- `bizops` owns the financial linkage — does Value Score correlate with NRR, GRR, expansion ARR

**Escape hatch**: if a quarterly review surfaces that Value Score is failing as a construct (e.g., it's tracking sentiment not value, or it's been gamed, or its protected-class audit fails), the Decision Interface has authority to pause use and trigger retraining. This is a structural protection against the Value-Score-becomes-Health-Score-in-disguise failure mode.

## 6. Findings

### Finding 1
**What**: Customer Value Score features that are operationally neutral on their face can be protected-class proxies. Common proxies include industry vertical, company size, geography, primary working language, and tech-stack signals (see §2 table).
**Why it matters**: When Value Score drives consequential decisions (renewal, expansion eligibility, support tier, individual feature access), disparate-impact exposure attaches under Title VII (employment-adjacent customer-side outcomes), GDPR Article 22 (EU data subjects), and analogous state-level statutes. Subgroup-disaggregated evaluation BEFORE deployment is required; post-hoc evaluation when a complaint arrives is too late.
**Severity**: P0
**Suggested next step**: Before any production Value Score deployment, run subgroup-disaggregated evaluation per §3.5; document the evaluation; counsel-review the documentation. Any feature failing the evaluation requires removal, reweighting, or documented business-necessity justification with counsel sign-off.

### Finding 2
**What**: Threshold-driven Value Score actions that auto-trigger consequential decisions (non-renewal, license suspension, support downgrade, individual feature block) without human review create GDPR Article 22 exposure on EU data subjects and customer-trust exposure across all jurisdictions.
**Why it matters**: Article 22 grants the EU data subject the right not to be subject to a solely automated decision producing legal or similarly significant effects. Auto-trigger architectures violate this right unless a narrow exception applies. Even outside EU jurisdiction, customers acting on AI-driven scoring of their business may have downstream transparency obligations to their own employees or end-customers.
**Severity**: P0
**Suggested next step**: Architect threshold crossings as triggers for human-reviewed action, not as autonomous action triggers. Document the human-review step in the score's operational protocol. Privacy counsel review on the Article 22 exception analysis if any auto-trigger is contemplated.

### Finding 3
**What**: The most common Value Score failure mode is rebranding Health Score as Value Score without changing inputs, composition, operational use, or audit. The label changes; the metric stays the same. Customers see through this fast; CSMs lose trust in the construct; the model becomes operationally useless.
**Why it matters**: Beyond the credibility cost, a rebrand-without-substance preserves all the failures the per-seat collapse exposed. Health-Score-as-Value-Score continues misreading AI-augmented customers as at-risk, continues missing extraction-rich expansion opportunities, and continues providing false confidence in the metric construct. The protected-class audit obligations attach to the metric whether or not it's been rebranded, but a rebranded metric is more likely to skip the audit because it was assumed to inherit the audit status of the prior Health Score.
**Severity**: P1
**Suggested next step**: When transitioning from Health Score to Value Score, validate that at least three of the five layers (inputs, outputs, composition, operational use, audit) have materially changed. If the answer is fewer than three, the transition is a rebrand, not a re-instrumentation; either complete the re-instrumentation or do not relabel.

## 7. Reviewer Checklist
- [ ] Jurisdiction confirmed (US Title VII analysis if scoring informs employment-adjacent decisions on customer-side individuals; EU GDPR Article 22 analysis if EU data subjects are scored; UK DPA 2018, California CCPA, state-level analogs as applicable)
- [ ] Subgroup-disaggregated evaluation completed BEFORE production deployment, documented, and counsel-reviewed
- [ ] Protected-class-correlated features identified per §2 table; each evaluated and either removed, reweighted, or business-necessity-justified with counsel sign-off
- [ ] Threshold-driven actions architected as human-review triggers, not autonomous triggers; GDPR Article 22 exception analysis on any contemplated auto-trigger
- [ ] Model retraining cadence and ownership defined; quarterly minimum; drift detection in place
- [ ] Customer transparency policy in place (onboarding notice, EBR/QBR disclosure, contract terms covering scoping of the scoring, right-to-explanation scope)
- [ ] V2V Phase 5 Decision Interface escape hatch confirmed (quarterly review can pause use if construct fails)
- [ ] Counsel engaged on Cannot Assess Without items
- [ ] `value-realization` Pattern-1 consultation completed on construct-validity question

## 8. Cannot Assess Without Licensed Counsel
- Title VII disparate-impact analysis on protected-class-correlated scoring features (when Value Score informs retention/expansion or feature-access decisions that affect employment-adjacent outcomes for customer-side individuals)
- GDPR Article 22 automated decision-making coverage and the Article 22(2) exception analysis (when scoring drives consequential decisions on EU data subjects)
- UK Data Protection Act 2018 Section 14 + ICO guidance on automated decision-making and profiling
- California CCPA + CPRA automated decision-making rule-making (rule-making in progress at CPPA as of 2026; subject to updates)
- Colorado SB 24-205 (Consumer Protections for Artificial Intelligence, effective 2027-01-01 per S.B. 26-189 postponement) coverage of "consequential decisions" by AI systems acting on consumers
- Texas TRAIGA (in force 2026-01-01) coverage of consumer-facing AI decisions
- NYC LL144 (AEDT) by analogy if Value Score outputs influence customer-side individual employment outcomes
- Sector-specific regimes: HIPAA when Value Score touches PHI (e.g., healthcare-vertical customers); GLBA when Value Score touches financial customer data; FERPA when Value Score touches education-sector individual data
- Customer contract permissions on automated scoring of customer data (data processing agreements, sub-processing obligations, audit rights)
- Cross-border data transfer obligations (SCCs, adequacy decisions, transfer impact assessments) when Value Score data crosses jurisdictions
- The four-fifths rule (29 CFR §1607.4(D)) as a starting threshold but not the exclusive test for "materially different" subgroup outcomes; counsel review on the appropriate disparate-impact threshold for the specific context

## 9. Anti-Patterns / Common Failures

**Health Score rebranded as Value Score without changed inputs**:. The most common failure. Validation test: at least three of the five layers (inputs, outputs, composition, operational use, audit) must have materially changed.

**Value Score deployed without subgroup-disaggregated evaluation**:. The protected-class audit is non-negotiable before production; running it post-hoc when a complaint surfaces is too late and undermines defense.

**Protected-class-correlated features included without disparate-impact review**: see §2 table. "We didn't intend it as a proxy" is not a defense under disparate-impact theory; intent is irrelevant, outcome is what matters.

**Threshold-driven actions taken without customer transparency**: even outside Article 22 jurisdiction, customers acting on the score may have downstream transparency obligations. Surprise actions create both regulatory exposure and operational trust costs.

**Value Score conflated with renewal-probability score**: these are different questions, different models, different governance. Renewal probability asks "will they renew?" — a vendor-facing question. Value Score asks "are they getting value?" — a customer-facing question. Conflating them lets the vendor-facing question's incentives bleed into the customer-facing metric; the result is a Value Score that optimizes for renewal probability and stops measuring value extraction.

**Value Score gamed by CSMs**: where CSMs are compensated on portfolio Value Score, the incentive to game inputs is real. CS Ops audit needs to include CSM-driven input integrity checks (no manual overrides without documented rationale; outlier verbatim coding review; suspicious-pattern detection on outcome-milestone declarations).

**Value Score used as the sole renewal input**:. Even when human-reviewed, a Value Score-only renewal decision creates concentration risk on the metric. Renewal decisions should incorporate Value Score, financial signals (NRR/GRR, expansion ARR), strategic signals (logo importance, reference value), and customer-relationship signals (sponsor changes, M&A events).

**Skipping the quarterly construct-validity review** (V2V Phase 5 escape hatch, §5): once the metric is operational, the temptation is to leave it running. Construct validity decays as customer-base composition shifts and as AI-augmented workflow patterns evolve. Quarterly review is the structural protection.

## 10. V2V Cross-References

**Sibling Q2-4 packs**:
- **`ai-agent-supervisor.md` (Q2-4.2)** — **load-bearing reciprocal**: AI support fleet supervisor consumes Value Score signals as input to escalation routing per §"Cross-References to Q2-4.1 Value Score" in that pack. High-Value-Score customer reopens are P0 supervisor events; banded Resolution Durability requires Value Score as the band axis.
- **`customer-success-methodology.md` (Q2-4.3 refresh)** — the Health→Value Score transition is the load-bearing methodology update; this pack is the design reference cited inline in that pack's §"Customer Health Scoring Framework" transition note.

**Sibling Q2-6 packs**:
- **`retention-marketing.md` (Q2-6.2)** — Value Score is the metric that distinguishes value-retention from seat-retention in retention marketing's 2026 reframe; the per-seat structural failure pattern in that pack consumes the metric defined here.

**Sibling Q2-3 packs (sensitive-skill scaffolding lineage)**:
- **`eu-ai-act-annex-iv.md` (Q2-3.4)** — if Value Score drives consequential decisions on EU data subjects, the deployment is high-risk under Article 6 + Annex III; Annex IV §3 + §4 documentation cites the Value Score governance and audit cadence per §3.5 of this pack.
- **`csa-ai-controls-matrix.md` (Q2-3.3)** — AICM domain 12 (AI Privacy) + domain 13 (AI Risk Management) + domain 18 (AI Transparency) controls operationalize on Value Score deployment.
- **`ai-bom.md` (Q2-3.5)** — Value Score is itself an AI system with training data, features, and outputs; AI BOM disclosure applies when Value Score is deployed (model lineage in §2.1, feature engineering in §2.7, ongoing audit in §2.8).

**Sibling Q2-5 packs**:
- **`agentic-security.md` (Q2-5.3)** — Title VII disparate-impact analysis on protected-class-correlated features cross-references that pack's `## Cannot Assess Without` item on FCRA/Title VII for any agent system output that qualifies as employment-decision-adjacent.

**Q2-2 macro context** (per references in §4 of this pack):
- `pricing-frameworks.md` §[2026 per-seat structural failure] — the macro pricing context that motivates Value Score.
- `metrics-frameworks.md` §9 (Value-not-headcount framing) + §6 (KORE Score) — the broader metric-system context.

**Existing packs**:
- `customer-success-methodology.md` — current Health Score framework, pre-refresh (transitional context).
- `saas-metrics.md` — NRR/GRR/CAC/LTV linkage that Value Score informs.
- `privacy-frameworks.md` — GDPR Article 22 substantive coverage.
- `employment-law.md` — Title VII disparate-impact substantive law.
- `ai-act-readiness.md` — EU AI Act high-risk analysis for AI-driven decisions on individuals.
- `hr-ai-governance.md` — FCRA structural treatment per `sensitive-skill-guardrails.md` §1.4 / §3.5.1 (relevant when Value Score informs employment-adjacent decisions on customer-side individuals).

**Rule files**:
- `sensitive-skill-guardrails.md` §3 — scaffolding pattern this pack follows.
- `roi-display.md` Sensitive Skill ROI Framing — "drafting and triage" framing only.

## Operating Principle

> *Value Score is the metric that survives the per-seat collapse — but only if it's designed for what the customer extracts, not for what they pay. Drafting and triage scaffold; counsel reviews; human acts.*
