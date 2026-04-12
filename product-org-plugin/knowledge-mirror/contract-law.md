# Contract Patterns Knowledge Pack

**Version**: 1.0
**Type**: knowledge-pack
**Primary Users**: @contracts-counsel, @general-counsel, @legal-dir

---

## CUAD Contract Analysis Categories

The Contract Understanding Atticus Dataset (CUAD) defines 41 key clause categories for contract review. Agents should check for these when reviewing agreements.

### High-Risk Categories (Always Review)

| # | Category | What to Check | Risk if Missed |
|---|----------|---------------|----------------|
| 1 | **Competitive Restriction** | Non-compete scope, duration, geography | Over-broad restrictions limit business |
| 2 | **Exclusivity** | Exclusive rights granted, scope, territory | May block other partnerships |
| 3 | **Non-Compete** | Post-termination competition restrictions | Limits future business options |
| 4 | **Non-Solicitation** | Employee/customer solicitation restrictions | Restricts hiring and sales |
| 5 | **Termination for Convenience** | Who can terminate, notice period, consequences | Sudden loss of critical vendor/partner |
| 6 | **Unlimited/All You Can Eat License** | Unlimited usage rights without caps | Uncontrolled exposure |
| 7 | **Uncapped Liability** | No liability cap or unlimited liability | Existential financial risk |
| 8 | **IP Ownership Assignment** | Who owns created IP, work product | Loss of critical IP |
| 9 | **Most Favored Nation (MFN)** | Price/terms matching obligations | Constrains future pricing flexibility |
| 10 | **Change of Control** | Rights upon acquisition/merger | May trigger unwanted obligations |

### Standard Categories (Review for Material Contracts)

| # | Category | What to Check |
|---|----------|---------------|
| 11 | Anti-Assignment | Whether contract is assignable |
| 12 | Audit Rights | Right to audit counterparty's compliance |
| 13 | Cap on Liability | Maximum liability amounts |
| 14 | Covenant Not to Sue | Restrictions on litigation |
| 15 | Effective Date | When obligations begin |
| 16 | Expiration Date | When the agreement ends |
| 17 | Governing Law | Which jurisdiction's law applies |
| 18 | Indemnification | Who indemnifies whom for what |
| 19 | Insurance | Required insurance coverage |
| 20 | IP License Grant | Scope of IP licenses granted |

### Operational Categories (Review for Completeness)

| # | Category | What to Check |
|---|----------|---------------|
| 21 | Joint IP Ownership | Shared IP rights and obligations |
| 22 | Liquidated Damages | Pre-agreed damage amounts |
| 23 | Minimum Commitment | Volume or revenue minimums |
| 24 | Notice Period | Required advance notice for actions |
| 25 | Post-Termination Services | Obligations after contract ends |
| 26 | Price Restrictions | Price increase caps, adjustment mechanisms |
| 27 | Renewal Terms | Auto-renewal, renewal conditions |
| 28 | Revenue/Profit Sharing | Revenue share percentages, calculation methods |
| 29 | Right of First Refusal (ROFR) | Pre-emptive rights on opportunities |
| 30 | Warranties | Representations and warranty scope |

### Data & Compliance Categories

| # | Category | What to Check |
|---|----------|---------------|
| 31 | Confidentiality | Scope of confidential information, exceptions |
| 32 | Data Protection | Data handling, processing, security requirements |
| 33 | Force Majeure | Excused performance events |
| 34 | Right to Access/Use Data | Data access, portability, deletion rights |
| 35 | SLA/Service Level | Performance guarantees, remedies for breach |

---

## SaaS Agreement Frameworks

### Standard SaaS Agreement Structure

| Section | Key Terms | Negotiation Priority |
|---------|-----------|---------------------|
| **Subscription** | Term, seats/units, pricing, payment terms | High |
| **Service Levels** | Uptime SLA (99.9%+), credits, measurement | High |
| **Data** | Ownership, processing, security, portability, deletion | Critical |
| **IP** | Customer content ownership, platform IP, feedback | High |
| **Liability** | Cap (typically 12 months fees), exclusions, indemnification | Critical |
| **Termination** | For cause, for convenience, data return period | High |
| **Security** | SOC2, encryption, incident notification, audit rights | High |
| **Compliance** | GDPR, CCPA, industry-specific (HIPAA, PCI) | Varies |

### SaaS Pricing Models — Legal Implications

| Model | Legal Considerations |
|-------|---------------------|
| **Per-seat** | Define "seat" precisely; active vs provisioned; fair use policies |
| **Usage-based** | Measurement methodology, dispute resolution for counts, overage rates |
| **Flat-rate** | Fair use limits, throttling rights, what constitutes abuse |
| **Tiered** | Feature gating clarity, tier migration terms, downgrade restrictions |
| **Freemium** | Terms of service for free tier, data handling on conversion, upgrade terms |

### Data Processing Addendum (DPA) Essentials

| Clause | Purpose | Standard Position |
|--------|---------|-------------------|
| Processing scope | Define what data is processed and why | Limited to service delivery |
| Sub-processors | Who else processes the data | List maintained, notification of changes |
| Data location | Where data is stored/processed | Customer-selected region or disclosed |
| Security measures | Technical and organizational measures | SOC2 Type II minimum |
| Breach notification | Timeline for notifying of incidents | 72 hours (GDPR standard) |
| Data deletion | What happens post-termination | Delete within 30-90 days, certification |
| Audit rights | Customer's right to verify compliance | Annual SOC2 report + questionnaire |

---

## Negotiation Frameworks

### BATNA-Based Negotiation

| Step | Action | Example |
|------|--------|---------|
| 1 | Identify your BATNA | Alternative vendors, build-in-house option |
| 2 | Estimate their BATNA | Other customers, market position |
| 3 | Define your reservation price | Walk-away terms |
| 4 | Identify the ZOPA | Zone of Possible Agreement |
| 5 | Prepare value-creating trades | Terms you value differently than counterparty |

### Contract Negotiation Playbook Structure

```
Playbook for: [Agreement Type]

Tier 1 (Must Have — Walk Away If Not Met):
- [Term]: [Our position] | [Walk-away threshold]

Tier 2 (Important — Push Hard):
- [Term]: [Preferred position] | [Acceptable fallback]

Tier 3 (Nice to Have — Trade If Needed):
- [Term]: [Preferred] | [Concession value]

Pre-Approved Concessions:
- [What we can give up without escalation]

Escalation Triggers:
- [What requires GC or business approval]
```

### Common Negotiation Trade-Offs

| We Want | They Want | Possible Trade |
|---------|-----------|----------------|
| Lower liability cap | Higher cap | Carve-outs for specific risks instead of blanket cap |
| Shorter auto-renewal | Longer commitment | Multi-year discount for shorter notice period |
| Broader termination rights | Longer lock-in | Early termination fee instead of lock-in |
| Better SLA | Less exposure on SLA credits | Tiered credits instead of termination right |
| Data portability | Stickiness | Clear export format but reasonable timeline |

---

## Contract Template Library (Recommended)

### Template Coverage Targets

| Template | Priority | Use Frequency |
|----------|----------|---------------|
| **Mutual NDA** | Must Have | Weekly |
| **SaaS Subscription Agreement** | Must Have | Monthly |
| **Master Service Agreement (MSA)** | Must Have | Monthly |
| **Statement of Work (SOW)** | Must Have | Weekly |
| **Consulting Agreement** | Must Have | Monthly |
| **Contractor Agreement** | Must Have | Monthly |
| **Employment Offer Letter** | Must Have | As needed |
| **Data Processing Agreement (DPA)** | Must Have | Monthly |
| **Vendor Terms** | Should Have | Quarterly |
| **Partner/Reseller Agreement** | Should Have | Quarterly |
| **EULA / Terms of Service** | Should Have | Annually |
| **Privacy Policy** | Should Have | Annually |

### Template Quality Standards

| Standard | Requirement |
|----------|------------|
| Plain language | Non-lawyers can understand key obligations |
| Defined terms | All capitalized terms have definitions |
| Consistent formatting | Numbered sections, cross-references work |
| Negotiation guidance | Embedded comments noting flex points |
| Last reviewed | Updated within last 12 months |
| Jurisdiction appropriate | Matches primary operating jurisdictions |
| Version controlled | Change log maintained |

---

## Contract Risk Scoring

### Risk Assessment Matrix

| Factor | Low (1) | Medium (2) | High (3) | Critical (4) |
|--------|---------|-----------|----------|---------------|
| **Contract Value** | <$10K | $10K-$100K | $100K-$1M | >$1M |
| **Term Length** | Month-to-month | 1 year | 2-3 years | 5+ years |
| **Data Sensitivity** | No personal data | Limited PII | Sensitive PII | Regulated data |
| **IP Risk** | No IP exchange | Standard license | Custom development | IP assignment |
| **Exclusivity** | None | Limited scope | Broad scope | Full exclusivity |
| **Liability** | Capped, standard | Capped, elevated | High cap | Uncapped |

**Scoring**: Sum factors. Total 6-10 = Standard review. 11-16 = Enhanced review. 17-24 = GC review required.

### Review SLA by Risk Score

| Risk Score | Review Turnaround | Reviewer |
|------------|-------------------|----------|
| 6-10 (Low) | 2 business days | Any counsel |
| 11-16 (Medium) | 3-5 business days | Senior counsel |
| 17-20 (High) | 5-7 business days | GC review |
| 21-24 (Critical) | Full negotiation cycle | GC + business sponsor |

---

## Common Contract Pitfalls

| Pitfall | Why It Happens | Prevention |
|---------|---------------|------------|
| **Auto-renewal trap** | 90-day notice buried in terms | Calendar all renewal/notice dates |
| **Scope creep** | Vague SOW language | Define deliverables with acceptance criteria |
| **Indemnity asymmetry** | Only one party indemnifies | Mutual indemnification as default |
| **Data lock-in** | No portability clause | Always include data export rights |
| **Assignment block** | Anti-assignment prevents M&A | Carve out change of control |
| **Survival overreach** | Too many clauses survive termination | Limit survival to confidentiality, IP, indemnity |
| **Ambiguous definitions** | Terms used but not defined | Define all capitalized terms in Section 1 |

---

*Last Updated: 2026-02-14*
*References: CUAD (Hendrycks et al., 2021), IACCM Most Negotiated Terms, SaaS industry standards*
*Disclaimer: This is informational guidance, not legal advice. Consult qualified legal counsel for binding decisions.*


## Common Pitfalls

- Contract templates are starting points, not final documents — always flag for legal review
- Limitation of liability clauses vary by jurisdiction — don't assume universal enforceability
- Indemnification scope should be conservative — broader is riskier for the indemnifying party
- Always check for change-of-control clauses in vendor agreements
