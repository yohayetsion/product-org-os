# Contract Templates Knowledge Pack

> Informational reference for drafting and triage, not legal advice. No attorney-client relationship is created by its use. Engage licensed counsel before relying on any clause, template, or position herein.

**Version**: 1.0
**Type**: knowledge-pack
**Primary Users**: @contracts-counsel, @general-counsel, @legal-dir

---
<!-- Attribution:
  Frameworks and patterns in this knowledge pack were informed by:
  - open-agreements/open-agreements (github.com/open-agreements/open-agreements) — open-source contract templates
  - oneNDA (github.com/oneNDA/oneNDA) — standardized NDA framework
  Adapted and expanded for Product Org OS agents.
-->

## Contract Structure Fundamentals

Every well-drafted contract follows a consistent structural hierarchy. Understanding this framework ensures completeness and enforceability.

### Standard Contract Anatomy

| Section | Purpose | Key Considerations |
|---------|---------|-------------------|
| **Cover / Title** | Identifies the agreement type and parties | Include full legal entity names, jurisdiction of incorporation |
| **Recitals (Whereas)** | Establish context and intent | Not legally binding but guide interpretation; keep factual and concise |
| **Definitions** | Define capitalized terms used throughout | Define every material term; avoid circular definitions; alphabetize |
| **Operative Clauses** | Core rights, obligations, and restrictions | Organize logically: grant, obligations, restrictions, remedies |
| **Representations & Warranties** | Factual assertions by each party | Distinguish between reps (current facts) and warranties (ongoing promises) |
| **Covenants** | Ongoing obligations during the term | Affirmative (shall do) vs. negative (shall not do) |
| **Conditions Precedent** | Requirements before obligations activate | Closing conditions, regulatory approvals, third-party consents |
| **Indemnification** | Risk allocation for third-party claims | Scope, procedure, caps, baskets, survival period |
| **Limitation of Liability** | Caps on direct exposure between parties | Cap amount, carve-outs, exclusion of consequential damages |
| **Termination** | How the agreement ends | For cause, for convenience, automatic expiration, wind-down |
| **General Provisions (Boilerplate)** | Standard legal mechanics | Notices, assignment, entire agreement, severability, waiver |
| **Schedules / Exhibits** | Supplementary details | SOWs, pricing, SLAs, data processing terms; incorporated by reference |
| **Signature Block** | Execution by authorized signatories | Ensure signatory has authority; include title and date |

### Recitals Best Practices

- Use "WHEREAS" clauses to establish: (1) who the parties are, (2) what each party does, (3) why they are entering the agreement
- Recitals should never contain operative language (obligations, rights, or restrictions)
- End with a transitional clause: "NOW, THEREFORE, in consideration of the mutual covenants herein, the parties agree as follows:"
- Keep to 3-5 clauses; excessive recitals signal overengineering

### Definitions Section Rules

- Every capitalized term used more than once should be defined
- Definitions must be self-contained (no forward references to undefined terms)
- Cross-reference definitions from schedules/exhibits into the main body
- Avoid "including but not limited to" in definitions -- it creates ambiguity
- Common defined terms: Agreement, Confidential Information, Effective Date, Intellectual Property, Services, Term

### Operative Clause Drafting

| Obligation Type | Language | Example |
|----------------|----------|---------|
| Mandatory | "shall" / "must" | "Provider shall deliver the Services..." |
| Prohibitive | "shall not" / "must not" | "Recipient shall not disclose..." |
| Permissive | "may" | "Either party may terminate..." |
| Conditional | "if...then" / "provided that" | "If Customer exceeds the usage cap, Provider may..." |
| Discretionary | "in its sole discretion" | "Provider may, in its sole discretion, approve..." |

Avoid: "will" (ambiguous -- future tense or obligation?), "should" (precatory, not binding), "best efforts" without objective standards.

---

## Common Contract Types and Templates

### 1. SaaS / Software License Agreement

**Purpose**: Governs access to cloud-hosted software on a subscription basis.

**Template Structure**:

| Section | Key Clauses | Notes |
|---------|-------------|-------|
| 1. Definitions | Software, Documentation, Users, Customer Data, SLA | Define "Authorized Users" precisely (named vs. concurrent) |
| 2. License Grant | Scope, restrictions, usage limits | Non-exclusive, non-transferable, limited to internal business use |
| 3. Service Levels | Uptime commitment, measurement, credits | Target 99.9%+; define "Downtime" excluding maintenance windows |
| 4. Customer Data | Ownership, processing, security, portability | Customer owns all data; provider processes as instructed |
| 5. Data Processing | DPA reference/attachment, sub-processors | GDPR Article 28 compliance; list sub-processors |
| 6. Security | Standards, certifications, breach notification | SOC 2 Type II, encryption at rest/in transit, 72-hour breach notice |
| 7. Fees & Payment | Pricing, billing cycle, payment terms, taxes | Net 30; auto-renewal pricing caps; late payment interest |
| 8. Term & Renewal | Initial term, renewal mechanism, price escalation | Auto-renewal with 60-90 day opt-out; cap annual increases |
| 9. IP Ownership | Platform IP, customer content, feedback | Provider owns platform; customer owns content; feedback license |
| 10. Warranties | Performance, compliance, non-infringement | Warrant conformance to documentation and specs |
| 11. Limitation of Liability | Cap, carve-outs, consequential damages | Cap at 12 months' fees; carve out IP infringement and data breach |
| 12. Indemnification | IP infringement, data breach, third-party claims | Mutual indemnification for respective obligations |
| 13. Termination | For cause, for convenience, data return | 30-day cure period; 90-day data export window post-termination |
| 14. Confidentiality | Scope, exceptions, duration | Survive 3-5 years post-termination |
| 15. General | Governing law, dispute resolution, assignment | Arbitration preferred for cross-border; anti-assignment without consent |

**SLA Framework**:

| Metric | Standard | Premium | Enterprise |
|--------|----------|---------|------------|
| Uptime | 99.5% | 99.9% | 99.99% |
| Planned Maintenance | 8 hrs/month | 4 hrs/month | 2 hrs/month (off-peak) |
| Response Time (P1) | 4 hours | 1 hour | 15 minutes |
| Resolution Time (P1) | 24 hours | 8 hours | 4 hours |
| Service Credit (per 0.1% below SLA) | 5% monthly fee | 5% monthly fee | 10% monthly fee |
| Max Service Credit | 15% | 25% | 30% |

### 2. Master Service Agreement (MSA) + Statement of Work (SOW)

**Purpose**: Umbrella agreement governing an ongoing service relationship, with individual SOWs for specific engagements.

**MSA Template Structure**:

| Section | Content |
|---------|---------|
| 1. Definitions | Services, Deliverables, Work Product, SOW, Change Order |
| 2. Services | Provider performs services per SOW terms |
| 3. SOW Mechanics | How SOWs are created, modified, and terminated |
| 4. Fees & Payment | Payment terms, invoicing, expenses, taxes |
| 5. Change Orders | Process for scope changes (written approval required) |
| 6. IP Ownership | Work-for-hire vs. licensed; pre-existing IP |
| 7. Confidentiality | Mutual NDA terms |
| 8. Warranties | Professional standards, compliance, non-infringement |
| 9. Indemnification | IP infringement, negligence, third-party claims |
| 10. Limitation of Liability | Per-SOW cap or aggregate cap |
| 11. Term & Termination | MSA term, SOW termination, survival |
| 12. Insurance | Required coverage types and minimums |
| 13. General | Governing law, dispute resolution, assignment, notices |

**SOW Template Structure**:

| Section | Content |
|---------|---------|
| 1. Background | Context and objectives |
| 2. Scope of Services | Detailed description of work |
| 3. Deliverables | Specific outputs with acceptance criteria |
| 4. Timeline & Milestones | Dates, phases, dependencies |
| 5. Fees & Payment Schedule | Fixed/T&M, milestone payments, rate card |
| 6. Assumptions & Dependencies | What each party provides |
| 7. Acceptance | Testing period, acceptance criteria, rejection process |
| 8. Resources | Named personnel, substitution rules |
| 9. Change Order Process | Reference to MSA change order procedure |

**MSA-SOW Hierarchy Rule**: Where MSA and SOW conflict, the SOW prevails for that engagement unless the MSA explicitly states otherwise. State this in the MSA.

### 3. Non-Disclosure Agreement (NDA)

**Purpose**: Protect confidential information shared between parties.

**Mutual NDA Template** (preferred for business discussions):

| Clause | Standard Position |
|--------|------------------|
| Parties | Both parties as "Disclosing Party" and "Receiving Party" |
| Confidential Information | All information disclosed in connection with the Purpose, marked or reasonably understood as confidential |
| Exclusions | (1) Public knowledge, (2) independently developed, (3) received from third party, (4) already known, (5) compelled by law |
| Obligations | Reasonable care (at least same as own), need-to-know basis, no reverse engineering |
| Purpose | Specific business purpose (evaluating potential transaction/partnership) |
| Term | 2-3 years for commercial; 5 years for technical/trade secrets |
| Return/Destruction | Within 30 days of request or expiration; certification of destruction |
| Residuals | Receiving party may use general knowledge retained in unaided memory (optional, often negotiated) |
| No Obligation | NDA does not obligate either party to proceed with any transaction |
| Remedies | Injunctive relief acknowledged; monetary damages preserved |

**One-Way NDA** (use when only one party discloses):

- Same structure but fixed roles: "Disclosing Party" = company, "Receiving Party" = counterparty
- Typically used for: employee onboarding, vendor evaluation, investor presentations
- Tighter obligations on the receiving party; no reciprocal protections needed

**NDA Red Flags**:

| Red Flag | Risk | Counter-Position |
|----------|------|-----------------|
| Overly broad definition of "Confidential Information" | Everything becomes confidential | Require marking or written designation |
| No exclusions | Cannot use publicly available information | Insist on standard five exclusions |
| Perpetual term | Indefinite obligation | Cap at 3-5 years (longer for trade secrets) |
| Non-compete disguised as NDA | Restricts future business activities | Remove any non-compete or non-solicitation language |
| No residuals clause | Cannot use general learning | Include standard residuals clause |
| Mandatory arbitration in foreign jurisdiction | Expensive dispute resolution | Negotiate local jurisdiction or mediation first |

### 4. Employment Agreement

**Purpose**: Establish the terms of an employment relationship.

**Template Structure**:

| Section | Key Terms |
|---------|-----------|
| 1. Position & Duties | Title, reporting line, location, full-time/part-time |
| 2. Compensation | Base salary, bonus structure, equity, benefits |
| 3. Term | At-will vs. fixed term; probationary period |
| 4. IP Assignment | All work product created in scope of employment assigned to company |
| 5. Confidentiality | Obligation to protect company confidential information |
| 6. Non-Compete | Duration (6-24 months), geographic scope, activity scope |
| 7. Non-Solicitation | Restrictions on soliciting employees and customers |
| 8. Termination | Voluntary, involuntary, for cause definitions |
| 9. Severance | Conditions, amount, release requirement |
| 10. Garden Leave | Paid notice period with no active duties (alternative to non-compete) |
| 11. Clawback | Conditions under which bonuses/equity must be returned |
| 12. Governing Law | Employment law jurisdiction |

**IP Assignment Clause Elements**:

- Scope: All inventions, works, and discoveries made during employment relating to company business
- Prior inventions: Schedule of excluded pre-existing IP
- Moral rights: Waiver where permitted by law
- Cooperation: Obligation to execute assignment documents
- Survival: IP assignment survives termination

**Non-Compete Enforceability Factors**:

| Factor | More Enforceable | Less Enforceable |
|--------|-----------------|------------------|
| Duration | 6-12 months | 24+ months |
| Geography | Specific markets/regions | Worldwide |
| Scope | Narrow activity restriction | Broad industry ban |
| Consideration | Adequate compensation/severance | Employment alone (varies by jurisdiction) |
| Seniority | C-level/executives | Junior employees |

### 5. Independent Contractor Agreement

**Purpose**: Engage an individual or entity for services without creating an employment relationship.

**Template Structure**:

| Section | Key Terms |
|---------|-----------|
| 1. Services | Detailed scope referencing SOW or exhibit |
| 2. Relationship | Independent contractor, not employee; no benefits |
| 3. Fees & Payment | Rate, invoicing, payment terms, expenses |
| 4. Term & Termination | Project duration, termination notice (typically 30 days) |
| 5. IP Ownership | Work-for-hire assignment with backup assignment clause |
| 6. Confidentiality | Protection of company information |
| 7. Non-Solicitation | Restrictions on soliciting company employees |
| 8. Insurance | Contractor carries own liability/professional insurance |
| 9. Indemnification | Contractor indemnifies for negligence, tax obligations |
| 10. Representations | Authority, no conflicts, compliance with laws |
| 11. Taxes | Contractor responsible for own taxes; 1099/equivalent |

**Misclassification Risk Factors** (worker vs. contractor):

| Factor | Contractor | Employee |
|--------|-----------|----------|
| Control over how work is done | Contractor decides | Company directs |
| Tools and equipment | Contractor provides | Company provides |
| Financial risk | Bears profit/loss | Fixed salary |
| Exclusivity | Multiple clients | Typically exclusive |
| Integration | Project-based | Core to business |
| Benefits | None from company | Health, pension, leave |

### 6. Reseller / Channel Partner Agreement

**Purpose**: Authorize a partner to resell products or services.

**Template Structure**:

| Section | Key Terms |
|---------|-----------|
| 1. Appointment | Non-exclusive (default) or exclusive; territory; product scope |
| 2. Reseller Obligations | Minimum commitments, marketing efforts, training, support tier |
| 3. Pricing & Discounts | Wholesale pricing, discount tiers, MAP (minimum advertised price) |
| 4. Orders & Fulfillment | Ordering process, fulfillment responsibility, returns |
| 5. Payment | Payment terms, commission structure, reconciliation |
| 6. IP License | Limited trademark license for marketing; brand guidelines |
| 7. Customer Ownership | Who owns the customer relationship and data |
| 8. Support Responsibilities | Tier 1 (reseller) vs. Tier 2+ (vendor) |
| 9. Exclusivity & Non-Compete | Territory exclusivity, competing products |
| 10. Term & Termination | Annual term, renewal, minimum performance thresholds |
| 11. Post-Termination | Customer transition, inventory return, commission tail |
| 12. Reporting | Sales reports, pipeline visibility, forecasting |

### 7. Data Processing Agreement (DPA) -- GDPR-Compliant

**Purpose**: Govern the processing of personal data by a processor on behalf of a controller, as required by GDPR Article 28.

**Mandatory Provisions (GDPR Article 28(3))**:

| Provision | Requirement |
|-----------|-------------|
| Subject matter & duration | What data, why, how long |
| Nature & purpose of processing | Operations performed (storage, analysis, transfer) |
| Types of personal data | Categories (names, emails, financial, health) |
| Categories of data subjects | Whose data (employees, customers, prospects) |
| Controller obligations & rights | Instructions, audit rights, data subject requests |
| Processor obligations | Process only on instructions, confidentiality, security, sub-processors, assistance, deletion/return, audit support |

**DPA Template Structure**:

| Section | Content |
|---------|---------|
| 1. Definitions | Personal Data, Processing, Controller, Processor, Sub-processor, Data Subject |
| 2. Scope | Data types, processing activities, duration |
| 3. Processor Obligations | Process only on documented instructions; confidentiality |
| 4. Security Measures | Technical and organizational measures (TOMs); encryption, access controls |
| 5. Sub-processors | Prior written consent; sub-processor list; flow-down obligations |
| 6. Data Subject Rights | Assistance with access, rectification, erasure, portability requests |
| 7. Data Breach | Notification within 72 hours; cooperation with investigation |
| 8. Cross-Border Transfers | SCCs, adequacy decisions, binding corporate rules |
| 9. Data Protection Impact Assessment | Cooperation on DPIAs |
| 10. Audit Rights | Controller right to audit (or accept SOC 2/ISO 27001 reports) |
| 11. Term & Data Return | Deletion or return of data upon termination |
| Annex A | Description of processing activities |
| Annex B | Technical and organizational security measures |
| Annex C | List of approved sub-processors |

### 8. Terms of Service (ToS) / Terms of Use

**Purpose**: Unilateral terms governing use of a product or service, typically for self-service/PLG models.

**Template Structure**:

| Section | Content |
|---------|---------|
| 1. Acceptance | Click-wrap, browse-wrap, or sign-in-wrap mechanism |
| 2. Account Registration | Eligibility, accuracy of information, account security |
| 3. License Grant | Limited, non-exclusive, non-transferable right to use |
| 4. Acceptable Use | Prohibited conduct, content restrictions |
| 5. User Content | License granted to provider, responsibility for content |
| 6. Intellectual Property | Provider IP ownership, trademark guidelines |
| 7. Fees & Payment | Pricing, billing, refunds, free tier limitations |
| 8. Privacy | Reference to Privacy Policy |
| 9. Disclaimers | "AS IS" / "AS AVAILABLE"; no warranty of fitness |
| 10. Limitation of Liability | Cap on damages; exclusion of consequential damages |
| 11. Indemnification | User indemnifies provider for misuse |
| 12. Termination | Provider right to terminate/suspend; user right to cancel |
| 13. Modifications | Right to update terms; notification mechanism |
| 14. Governing Law | Jurisdiction, arbitration clause, class action waiver |
| 15. Miscellaneous | Severability, entire agreement, contact information |

### 9. Privacy Policy Framework

**Purpose**: Disclose data collection, use, sharing, and individual rights.

**Required Sections (GDPR + CCPA/CPRA)**:

| Section | Content | Regulatory Basis |
|---------|---------|-----------------|
| Data Controller Identity | Company name, address, DPO contact | GDPR Art. 13 |
| Data Collected | Categories: provided, automatic, third-party | GDPR Art. 13, CCPA 1798.100 |
| Purposes of Processing | Legitimate interest, consent, contractual necessity | GDPR Art. 6 |
| Legal Basis | Lawful basis for each processing activity | GDPR Art. 6 |
| Data Sharing | Categories of recipients, purpose | GDPR Art. 13, CCPA 1798.110 |
| International Transfers | Transfer mechanisms (SCCs, adequacy) | GDPR Art. 46 |
| Retention Periods | How long each category is retained | GDPR Art. 13 |
| Individual Rights | Access, rectification, erasure, portability, objection | GDPR Art. 15-21, CCPA 1798.105-125 |
| Cookies & Tracking | Cookie types, opt-out mechanisms | ePrivacy Directive |
| Children's Data | Age verification, parental consent (if applicable) | COPPA, GDPR Art. 8 |
| Security Measures | General description of safeguards | GDPR Art. 32 |
| Policy Updates | How changes are communicated | Best practice |
| Contact Information | How to exercise rights, lodge complaints | GDPR Art. 13 |

### 10. Vendor / Supplier Agreement

**Purpose**: Govern the purchase of goods or services from a vendor.

**Template Structure**:

| Section | Key Terms |
|---------|-----------|
| 1. Scope | Products/services, specifications, quantities |
| 2. Pricing & Payment | Unit pricing, volume discounts, payment terms (Net 30-60) |
| 3. Delivery | Delivery terms (Incoterms for goods), timelines, acceptance |
| 4. Quality Standards | Specifications, testing, rejection rights |
| 5. Warranties | Product/service warranty, fitness for purpose |
| 6. IP | Ownership of any custom deliverables, license to use |
| 7. Confidentiality | Mutual protection of business information |
| 8. Compliance | Anti-bribery, sanctions, labor standards, environmental |
| 9. Insurance | Minimum coverage requirements |
| 10. Indemnification | Product liability, IP infringement, negligence |
| 11. Limitation of Liability | Proportional cap; carve-outs for willful misconduct |
| 12. Termination | For cause, for convenience, supply disruption |
| 13. Business Continuity | Disaster recovery, alternate supply, escrow |
| 14. Audit Rights | Right to audit compliance with terms |

---

## Key Negotiation Clauses and Fallback Positions

### Limitation of Liability

| Position | Standard | Fallback | Walk-Away |
|----------|----------|----------|-----------|
| **Cap Amount** | 12 months' fees paid/payable | 24 months' fees | Uncapped liability |
| **Carve-Outs from Cap** | IP infringement, confidentiality breach, data breach | Add gross negligence, willful misconduct | No carve-outs at all |
| **Consequential Damages** | Mutually excluded | Excluded except for carve-out items | Included without limitation |
| **Super Cap** | 2-3x fees for carve-out items | 5x fees | No super cap (carve-outs = uncapped) |

**Drafting Notes**:
- Always define what constitutes "direct" vs. "indirect/consequential" damages
- Lost profits classification varies by jurisdiction -- address explicitly
- Insurance-backed risks (data breach, IP infringement) can support higher caps
- Cap should be proportional to deal value and risk profile

### Indemnification

| Element | Standard Position | Fallback |
|---------|------------------|----------|
| **Scope** | Mutual: each party indemnifies for own breach, negligence, IP infringement | Asymmetric: vendor indemnifies for IP, breach; customer indemnifies for misuse |
| **Procedure** | Prompt notice, sole control of defense, cooperation | Shared control with consent on settlement |
| **Cap** | Subject to overall liability cap | Carve out from cap (with separate super cap) |
| **IP Indemnification** | Vendor defends, indemnifies, and holds harmless | Add obligation to modify, replace, or refund |
| **Survival** | 12-24 months post-termination | Tied to statute of limitations |

**Indemnification Procedure Checklist**:
1. Prompt written notice of claim (not a condition, but obligation)
2. Indemnifying party assumes sole control of defense
3. Indemnified party cooperates and provides reasonable assistance
4. No settlement without written consent of indemnified party
5. Indemnified party may participate with own counsel at own expense

### Termination

| Type | Standard Terms |
|------|---------------|
| **For Cause** | Material breach + 30-day cure period; insolvency events; regulatory prohibition |
| **For Convenience** | 90-day written notice (vendor); 30-day written notice (customer) |
| **Automatic Expiration** | End of initial or renewal term |
| **Wind-Down** | 30-90 day transition period; data export; service continuity during transition |
| **Effect of Termination** | Accrued obligations survive; licenses terminate; data returned/destroyed |
| **Survival** | Confidentiality, indemnification, limitation of liability, governing law |

**Termination Fallback Positions**:

| Issue | Our Position | Fallback |
|-------|-------------|----------|
| Cure period too short | 30 days | 15 days for payment; 30 days for other breaches |
| No convenience termination | Include for both parties | Include for customer only with longer notice |
| No transition assistance | Include mandatory transition | Paid transition services at standard rates |
| Immediate termination rights | Only for insolvency, criminal conduct | Add repeated material breach (3+ in 12 months) |

### IP Ownership and Licensing

| Scenario | Ownership Position | License Position |
|----------|-------------------|-----------------|
| **Custom Development (MSA/SOW)** | Customer owns all deliverables | Provider retains license to pre-existing IP and tools |
| **SaaS Platform** | Provider owns platform IP | Customer receives limited use license |
| **Customer Data** | Customer owns all customer data | Provider has limited processing license |
| **Feedback/Suggestions** | Provider owns improvements | Royalty-free, perpetual license from customer |
| **Joint Development** | Avoid if possible; define ownership per deliverable | Cross-license with field-of-use restrictions |

### Warranty and Disclaimer

| Warranty Type | Standard Language |
|---------------|------------------|
| **Performance** | Services will conform to documentation/specifications |
| **Professional Standards** | Services performed in a professional and workmanlike manner |
| **Compliance** | Provider complies with applicable laws |
| **Non-Infringement** | Services will not infringe third-party IP rights |
| **Authority** | Each party has authority to enter into the agreement |
| **Disclaimer** | EXCEPT AS EXPRESSLY SET FORTH HEREIN, ALL OTHER WARRANTIES ARE DISCLAIMED, INCLUDING IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE |

### Force Majeure

**Standard Covered Events**: Natural disasters, war, terrorism, government action, pandemic, embargo, labor disputes, utility failures, cyberattacks (increasingly included).

**Key Provisions**:

| Element | Standard Position |
|---------|------------------|
| Obligation | Affected party must use reasonable efforts to mitigate |
| Notice | Prompt written notice with expected duration |
| Performance | Suspended (not excused) for duration of event |
| Payment | Payment obligations typically not excused |
| Extended Duration | If event persists beyond 90-180 days, either party may terminate |
| Termination Right | No liability for termination due to extended force majeure |

### Governing Law and Dispute Resolution

| Mechanism | When to Use | Pros | Cons |
|-----------|-------------|------|------|
| **Litigation** | Domestic disputes, need for precedent, injunctive relief | Court enforcement, appeals, discovery | Slow, expensive, public |
| **Arbitration** | Cross-border, confidentiality needed, technical disputes | Faster, private, expert arbitrators | Limited appeal, still expensive |
| **Mediation** | Commercial disputes, preserve relationship | Cheap, fast, collaborative | Non-binding |
| **Tiered** | Complex relationships | Escalation path; mediation first | Adds time |

**Standard Clause**: Mediation first (30 days), then binding arbitration under [rules] in [seat]. Each party bears own costs; arbitrator allocates fees.

---

## Contract Review Checklist

### Red Flags (Stop and Escalate)

| Red Flag | Why It Matters |
|----------|---------------|
| Uncapped liability | Existential financial risk |
| Unlimited indemnification | Open-ended exposure |
| Unilateral amendment rights | Counterparty can change terms without consent |
| Automatic renewal with no opt-out notice | Locked into unfavorable terms |
| Broad IP assignment (beyond deliverables) | Loss of background IP |
| Non-compete disguised as exclusivity | Restricts future business |
| "Best efforts" obligations without parameters | Undefined standard of performance |
| No data return/deletion on termination | Data hostage risk |
| Foreign governing law with mandatory arbitration | Expensive, unfamiliar forum |
| Perpetual license surviving termination | Cannot stop counterparty's use |
| Most Favored Nation (MFN) clause | Constrains future pricing/terms |
| Change of control termination right (one-sided) | Disrupts M&A transactions |

### Must-Haves (Ensure Present)

| Clause | Minimum Standard |
|--------|-----------------|
| Limitation of liability | Capped at 12-24 months' fees |
| Mutual confidentiality | Standard 5 exclusions, 3-5 year term |
| Termination for cause | Material breach with cure period |
| IP ownership clarity | Unambiguous ownership of work product and data |
| Data protection | DPA if personal data involved |
| Governing law | Favorable or neutral jurisdiction |
| Assignment | Consent required (except to affiliates/successors) |
| Notices | Written, to specified addresses, effective on receipt |
| Entire agreement | Supersedes prior agreements on same subject |
| Severability | Invalid provisions severed; remainder enforceable |
| Insurance | Adequate coverage for the risk profile |
| Representations | Authority, no conflicts, compliance with laws |

### Commercial Review Points

| Area | What to Verify |
|------|---------------|
| Pricing | Matches commercial proposal; escalation caps |
| Payment terms | Align with cash flow (Net 30 minimum) |
| Auto-renewal | Opt-out window is reasonable (60-90 days) |
| Volume commitments | Minimums are achievable; consequence of shortfall |
| Benchmarking | Right to benchmark pricing against market |
| Audit | Access to verify compliance with terms |

---

## Contract Lifecycle Management

### Phase 1: Drafting

| Step | Owner | Output |
|------|-------|--------|
| Business requirements intake | Business owner + Legal | Requirements brief |
| Template selection | Contracts Counsel | Appropriate template identified |
| First draft | Contracts Counsel | Draft agreement from template |
| Internal review | Business owner | Confirmed commercial terms |
| Compliance check | Privacy/Compliance (if applicable) | Regulatory sign-off |

### Phase 2: Review (Inbound Contracts)

| Step | Action |
|------|--------|
| Risk triage | Classify: Low (<$[TBD]k/year), Medium, High (>$[TBD]k/year or strategic) |
| Red flag scan | Check against Red Flags checklist above |
| Clause-by-clause review | Analyze each material provision against standard positions |
| Deviation analysis | Compare against template/playbook; flag non-standard terms |
| Risk summary | Document risk items with severity and recommendation |

### Phase 3: Negotiation

| Step | Action |
|------|--------|
| Position paper | Document preferred position, fallback, and walk-away for each issue |
| Redline preparation | Tracked changes with explanatory comments |
| Negotiation rounds | Prioritize: resolve critical issues first; trade less important ones |
| Escalation | Issues exceeding authority escalated to General Counsel |
| Final review | Confirm all negotiated changes are accurately reflected |

### Phase 4: Execution

| Step | Action |
|------|--------|
| Signatory verification | Confirm authority of all signatories |
| Version control | Final, clean version with all changes accepted |
| Execution | Wet ink, DocuSign, or counterpart signatures |
| Distribution | Fully executed copy to both parties |
| Filing | Centralized contract repository with metadata |

### Phase 5: Management & Renewal

| Activity | Frequency |
|----------|-----------|
| Key date tracking | Ongoing (renewal, termination, milestones) |
| Compliance monitoring | Per obligation schedule |
| Amendment management | As needed; formal change orders only |
| Renewal assessment | 90 days before expiration |
| Performance review | Annually for strategic contracts |
| Audit exercise | Per audit rights schedule |

---

## Playbook Approach

### Standard Positions by Contract Type

| Contract Type | Review Tier | Target Cycle Time | Escalation Threshold |
|---------------|------------|-------------------|---------------------|
| NDA (mutual, standard) | Low | 1-2 days | Non-standard exclusivity or non-compete terms |
| NDA (one-way or custom) | Medium | 3-5 days | Perpetual term, no residuals, IP-adjacent restrictions |
| SaaS Agreement (<$[TBD]k/yr) | Low | 3-5 days | Uncapped liability, broad IP assignment |
| SaaS Agreement (>$[TBD]k/yr) | High | 10-15 days | Any deviation from standard positions |
| MSA + SOW | High | 10-15 days | IP ownership disputes, uncapped liability |
| Employment Agreement | Medium | 5-7 days | Non-compete scope, equity terms |
| Contractor Agreement | Low-Medium | 3-5 days | IP assignment gaps, misclassification risk |
| Reseller Agreement | Medium | 5-10 days | Exclusivity, minimum commitments, customer ownership |
| DPA | Medium | 5-7 days | Non-GDPR-compliant processing terms |
| Vendor Agreement (>$[TBD]k/yr) | High | 10-15 days | Lock-in, data hostage, uncapped liability |

### Escalation Matrix

| Issue Severity | Action | Escalate To |
|---------------|--------|-------------|
| Standard deviation | Negotiate within playbook | None (Contracts Counsel authority) |
| Non-standard risk | Flag and recommend | General Counsel |
| Strategic/high-value exception | Briefing with recommendation | General Counsel + business sponsor |
| Walk-away threshold reached | Full risk assessment | General Counsel + C-level sponsor |

### Precedent Tracking

When a negotiation results in a non-standard position, record:
- Contract ID and counterparty
- Clause modified and final position
- Business rationale for the deviation
- Whether this should become a new standard or remains an exception

---

## Common Pitfalls in SaaS Contracts

| Pitfall | Description | Prevention |
|---------|-------------|------------|
| **Subscription lock-in** | Long initial terms with no termination for convenience | Negotiate annual terms with 30-day convenience termination |
| **Price escalation** | Uncapped renewal pricing increases | Cap annual increases (3-5% or CPI) |
| **Data hostage** | No data portability or export on termination | Require data export in standard format within 90 days |
| **Feature degradation** | Provider can remove features during term | Warrant material functionality throughout term |
| **Sub-processor sprawl** | Unlimited right to engage sub-processors | Require prior notice and objection right |
| **Unilateral SLA changes** | Provider can modify SLAs without consent | Lock SLA terms for the contract period |
| **Broad audit waivers** | Accepting SOC 2 in lieu of any audit rights | Accept SOC 2 as baseline but preserve audit right for cause |
| **Ambiguous "unlimited" plans** | Fair use policies that limit "unlimited" use | Define specific usage thresholds and consequences |
| **Auto-renewal traps** | Short opt-out windows (30 days) on annual contracts | Require 90-day notice; calendar the date |
| **Survival overreach** | Too many clauses surviving termination indefinitely | Limit survival to confidentiality, indemnification, liability, IP |
| **Benchmark restrictions** | Prohibition on publishing performance benchmarks | Remove or narrow to non-public disclosure only |
| **Assignment blocking** | Cannot assign to affiliates or in M&A | Permit assignment to affiliates and in change of control |

---

## Quick Reference: Clause Library

### Essential Boilerplate Clauses

| Clause | Purpose | Standard Language Guidance |
|--------|---------|--------------------------|
| **Entire Agreement** | Prevents reliance on prior discussions | "This Agreement constitutes the entire agreement and supersedes all prior agreements, written or oral" |
| **Severability** | Preserves agreement if a clause is invalid | "If any provision is held invalid, the remainder shall continue in full force and effect" |
| **Waiver** | Prevents failure to enforce from becoming a permanent waiver | "No waiver shall be effective unless in writing; no waiver constitutes a continuing waiver" |
| **Assignment** | Controls transferability | "Neither party may assign without prior written consent, except to an affiliate or successor" |
| **Notices** | Establishes valid communication channels | "All notices shall be in writing and deemed given when delivered by [methods] to [addresses]" |
| **Counterparts** | Allows signing in separate copies | "This Agreement may be executed in counterparts, each of which shall be deemed an original" |
| **Amendment** | Requires written agreement to modify | "No amendment shall be effective unless in writing and signed by both parties" |
| **Relationship** | Clarifies no partnership/agency created | "Nothing in this Agreement creates a partnership, joint venture, or agency relationship" |
| **Third-Party Beneficiaries** | Prevents outsiders from enforcing terms | "This Agreement does not confer any rights on any third party" |
| **Headings** | Prevents headings from affecting interpretation | "Section headings are for convenience only and shall not affect interpretation" |

---

> "A well-drafted contract is not a legal document -- it is an operating manual for a business relationship. The best contracts anticipate problems before they arise and provide clear resolution paths when they do."
