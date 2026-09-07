# RFP Templates Knowledge Pack

**Version**: 1.0
**Type**: knowledge-pack
**Primary Users**: `procurement-specialist`, `program-manager`, `project-manager`
---
<!-- Attribution:
  Frameworks and patterns in this knowledge pack were informed by:
  - run-llama/auto_rfp (github.com/run-llama/auto_rfp) — LLM-powered RFP automation patterns
  - SalesforceLabs — enterprise procurement and RFP response frameworks
  Adapted and expanded for Product Org OS agents.
-->

## RFP Process Framework

The full procurement lifecycle runs 6 phases. Each phase has mandatory inputs and outputs before proceeding.

| Phase | Name | Key Activities | Output |
|-------|------|---------------|--------|
| **1** | Need Identification | Stakeholder interviews, requirements gathering, budget approval | Approved business case, budget envelope |
| **2** | Requirements Development | Functional/technical/commercial requirements, evaluation criteria | Requirements document, weighting matrix |
| **3** | RFP Creation | Draft RFP document, legal review, approval | Final RFP document ready for distribution |
| **4** | Distribution & Response | Vendor list, Q&A period, proposal receipt | Submitted proposals |
| **5** | Evaluation | Scoring, demonstrations, due diligence | Evaluation scorecard, shortlist |
| **6** | Selection & Award | Final negotiations, contract execution, transition planning | Signed contract, implementation kickoff |

**Minimum timelines by procurement size**:

| Contract Value | Minimum RFP Window | Evaluation Period |
|---------------|-------------------|------------------|
| Under $100K | 2 weeks | 1 week |
| $100K - $500K | 3-4 weeks | 2 weeks |
| $500K - $2M | 4-6 weeks | 3-4 weeks |
| Over $2M | 6-8 weeks | 4-6 weeks |

---

## RFQ vs. RFP vs. RFI Decision Matrix

Use the right instrument for the right stage:

| Instrument | Full Name | When to Use | Output |
|-----------|-----------|-------------|--------|
| **RFI** | Request for Information | Early market research; don't know what solutions exist; no budget commitment | Vendor landscape, preliminary specs |
| **RFQ** | Request for Quotation | Requirements are clear and fixed; selecting on price; commodity procurement | Price quotes, delivery terms |
| **RFP** | Request for Proposal | Requirements defined but solution approach is open; value beyond price matters | Full proposals including approach, team, price |
| **RFT** | Request for Tender | Highly specified requirements; formal/government procurement; price-driven | Tender submissions against fixed spec |

**Decision rule**:
- Do you know exactly what you want AND is price the primary differentiator? → RFQ
- Do you need vendors to propose HOW to solve your problem? → RFP
- Are you gathering market intelligence before committing to procurement? → RFI
- Is this a government or highly regulated formal procurement? → RFT

---

## RFP Document Structure Template

### Cover Page / Executive Summary

```
[ORGANIZATION NAME]
Request for Proposal

Project Title: [Name of Initiative]
RFP Reference Number: [Internal tracking number]
Issue Date: [Date]
Proposal Due Date: [Date and time, including timezone]
Point of Contact: [Name, title, email]
Questions Deadline: [Date — typically 1-2 weeks before due date]
```

### Section 1: Company Overview

```markdown
## 1. About [Organization Name]

### 1.1 Organization Background
[2-3 paragraphs describing the organization: industry, size, mission, and why this procurement is strategic]

### 1.2 Current State
[Brief description of existing solution/process being replaced or augmented]

### 1.3 Strategic Context
[Why this initiative matters now — business driver, regulatory requirement, growth initiative]
```

### Section 2: Scope of Work / Requirements

```markdown
## 2. Scope of Work

### 2.1 Project Objectives
Primary objectives this solution must achieve:
1. [Objective 1 — measurable outcome]
2. [Objective 2 — measurable outcome]
3. [Objective 3 — measurable outcome]

### 2.2 Functional Requirements

| ID | Requirement | Priority | Acceptance Criteria |
|----|-------------|----------|---------------------|
| FR-01 | [Requirement description] | Must Have | [How we'll verify] |
| FR-02 | [Requirement description] | Should Have | [How we'll verify] |
| FR-03 | [Requirement description] | Nice to Have | [How we'll verify] |

Priority definitions:
- Must Have (M): Non-negotiable; disqualifier if not met
- Should Have (S): Strong preference; significant scoring weight
- Nice to Have (N): Differentiator; limited scoring weight

### 2.3 Technical Requirements

| ID | Requirement | Priority | Notes |
|----|-------------|----------|-------|
| TR-01 | [Integration requirement] | M/S/N | [API, format, protocol] |
| TR-02 | [Security requirement] | M/S/N | [Standard or certification] |
| TR-03 | [Performance requirement] | M/S/N | [SLA, response time, uptime] |
| TR-04 | [Scalability requirement] | M/S/N | [Volume, growth projections] |

### 2.4 Commercial Requirements
- Contract term: [Preferred initial term + renewal options]
- Budget range: [Optional — consider disclosing to attract relevant responses]
- Payment terms: [Net-30, milestone-based, subscription]
- Geographic scope: [Countries, regions]
- Minimum SLA requirements: [Uptime, response time, support tiers]

### 2.5 Out of Scope
[Explicitly list what is NOT included in this procurement to avoid scope creep in proposals]
```

### Section 3: Evaluation Criteria and Weighting

```markdown
## 3. Evaluation Criteria

Proposals will be evaluated on the following criteria:

| Category | Weight | Subcriteria |
|----------|--------|-------------|
| Technical Solution | [X%] | Functional fit, technical architecture, innovation |
| Vendor Qualifications | [X%] | Experience, references, financial stability, team |
| Implementation Approach | [X%] | Methodology, timeline, risk management, change mgmt |
| Pricing / Commercial | [X%] | Total cost of ownership, pricing model, contract terms |
| Support & Service | [X%] | SLA, support model, ongoing partnership |
| **TOTAL** | **100%** | |

Scoring scale: 1-5 per criterion (1=Does not meet, 3=Meets, 5=Exceeds)
Final score = weighted average across all criteria
```

### Section 4: Timeline and Milestones

```markdown
## 4. Procurement Timeline

| Milestone | Date |
|-----------|------|
| RFP Issued | [Date] |
| Questions Submission Deadline | [Date] |
| Q&A Responses Published | [Date] |
| Proposals Due | [Date, Time, Timezone] |
| Proposal Evaluation Complete | [Date] |
| Vendor Shortlist Announced | [Date] |
| Vendor Demonstrations / Presentations | [Date range] |
| Final Selection | [Date] |
| Contract Execution Target | [Date] |
| Project Kickoff | [Date] |

[Organization] reserves the right to modify this timeline. Vendors will be notified of any changes.
```

### Section 5: Submission Requirements

```markdown
## 5. Submission Instructions

### 5.1 Format
- Submit proposals in PDF format (preferred) or Word
- Maximum page limit: [X pages] (excluding appendices and pricing)
- Font: minimum 11pt, 1-inch margins

### 5.2 Required Sections
All proposals must include:
- [ ] Executive Summary (max 2 pages)
- [ ] Understanding of Requirements / Solution Description
- [ ] Proposed Approach and Methodology
- [ ] Implementation Timeline
- [ ] Team Qualifications and Key Personnel
- [ ] Client References (minimum 3, similar in scope)
- [ ] Pricing Proposal (separate sealed document or clearly labeled section)
- [ ] Standard Terms and Conditions / Exceptions to Our Terms

### 5.3 Submission Method
Submit to: [email or procurement portal URL]
Subject line: [RFP Reference Number] — [Vendor Name]
Submission deadline: [Date] [Time] [Timezone]
Late submissions: [Will / Will not] be accepted

### 5.4 Questions
Submit questions to: [email]
Deadline for questions: [Date]
All Q&A will be distributed to all vendors anonymously
```

### Section 6: Terms and Conditions

```markdown
## 6. Terms and Conditions

### 6.1 RFP General Terms
- This RFP does not constitute a commitment to award a contract
- [Organization] reserves the right to cancel this RFP at any time
- [Organization] reserves the right to accept or reject any proposal in whole or in part
- Costs incurred in responding to this RFP are the vendor's sole responsibility
- All proposals become property of [Organization]

### 6.2 Confidentiality
[Organization] will treat proposals as confidential to the extent permitted by applicable law.

### 6.3 Conflict of Interest
Vendors must disclose any potential conflicts of interest.

### 6.4 Anti-Collusion
By submitting, vendor certifies the proposal was prepared independently without collusion.

### 6.5 Governing Law
This RFP and any resulting contract shall be governed by the laws of [State/Country].
```

---

## Evaluation Criteria Framework

### Weighted Scoring Methodology

**Setup**:
1. Define categories and assign percentage weights (must total 100%)
2. Define subcriteria within each category (weighted within the category)
3. Use consistent numeric scale (recommend 1-5)
4. Have multiple evaluators score independently before discussing

**Scoring Scale Definition** (use consistently across all evaluators):

| Score | Definition |
|-------|-----------|
| **5 — Exceptional** | Exceeds requirements significantly; offers capabilities beyond what was asked |
| **4 — Strong** | Fully meets requirements with notable strengths in this area |
| **3 — Adequate** | Meets baseline requirements; no significant gaps or differentiators |
| **2 — Partial** | Partially meets requirements; gaps identified that require mitigation |
| **1 — Inadequate** | Does not meet requirements; disqualifying gap |

**Calculation**:
```
Category Score = Average of subcriteria scores (within category)
Weighted Score = Category Score × Category Weight
Final Score = Sum of all Weighted Scores
```

### Technical Evaluation Template

| Criterion | Weight | Vendor A | Vendor B | Vendor C |
|-----------|--------|----------|----------|----------|
| Functional requirements coverage (Must Haves) | 30% | /5 | /5 | /5 |
| Functional requirements coverage (Should Haves) | 15% | /5 | /5 | /5 |
| Technical architecture and integration | 20% | /5 | /5 | /5 |
| Security and compliance | 20% | /5 | /5 | /5 |
| Performance and scalability | 15% | /5 | /5 | /5 |
| **Technical Score** | **100%** | | | |

### Commercial Evaluation Template

| Criterion | Weight | Vendor A | Vendor B | Vendor C |
|-----------|--------|----------|----------|----------|
| Total cost of ownership (3-year) | 40% | /5 | /5 | /5 |
| Pricing model fit (predictability, transparency) | 20% | /5 | /5 | /5 |
| Contract terms alignment | 20% | /5 | /5 | /5 |
| Payment terms | 10% | /5 | /5 | /5 |
| Value-added inclusions | 10% | /5 | /5 | /5 |
| **Commercial Score** | **100%** | | | |

**Total Cost of Ownership (3-Year) Formula**:
```
TCO = Initial License/Setup Fees
    + Annual License/Subscription (Year 1 + Year 2 + Year 3)
    + Implementation Services
    + Training
    + Ongoing Support/Maintenance
    + Estimated Internal Resource Cost
    + Estimated Integration Development
    - Expected Productivity/Cost Savings
```

### Risk Assessment Template

| Risk Category | Vendor A | Vendor B | Vendor C | Notes |
|--------------|----------|----------|----------|-------|
| Financial stability (D&B, revenue, funding) | H/M/L | H/M/L | H/M/L | |
| Reference quality (similar size/scope) | H/M/L | H/M/L | H/M/L | |
| Implementation track record | H/M/L | H/M/L | H/M/L | |
| Key person dependency | H/M/L | H/M/L | H/M/L | |
| Technology lock-in / switching cost | H/M/L | H/M/L | H/M/L | |
| Data portability and exit provisions | H/M/L | H/M/L | H/M/L | |
| Contract terms exceptions | H/M/L | H/M/L | H/M/L | |

Risk Rating: H = High concern (mitigate or reject), M = Medium (acceptable with controls), L = Low

---

## Vendor Evaluation Scorecard

```
VENDOR EVALUATION SCORECARD
RFP: [Project Name / Reference]
Vendor: ___________________________
Evaluator: _________________________
Date: ______________________________

SECTION 1: TECHNICAL SOLUTION (Weight: ___%)
  1.1 Functional fit — Must Have requirements      [ ] 1 [ ] 2 [ ] 3 [ ] 4 [ ] 5
  1.2 Functional fit — Should Have requirements    [ ] 1 [ ] 2 [ ] 3 [ ] 4 [ ] 5
  1.3 Technical architecture                       [ ] 1 [ ] 2 [ ] 3 [ ] 4 [ ] 5
  1.4 Integration approach                         [ ] 1 [ ] 2 [ ] 3 [ ] 4 [ ] 5
  1.5 Security and compliance posture              [ ] 1 [ ] 2 [ ] 3 [ ] 4 [ ] 5
  Notes: _______________________________________________

SECTION 2: VENDOR QUALIFICATIONS (Weight: ___%)
  2.1 Relevant experience (similar scope/industry) [ ] 1 [ ] 2 [ ] 3 [ ] 4 [ ] 5
  2.2 Reference quality                            [ ] 1 [ ] 2 [ ] 3 [ ] 4 [ ] 5
  2.3 Financial stability                          [ ] 1 [ ] 2 [ ] 3 [ ] 4 [ ] 5
  2.4 Proposed team qualifications                 [ ] 1 [ ] 2 [ ] 3 [ ] 4 [ ] 5
  Notes: _______________________________________________

SECTION 3: IMPLEMENTATION APPROACH (Weight: ___%)
  3.1 Methodology and project approach             [ ] 1 [ ] 2 [ ] 3 [ ] 4 [ ] 5
  3.2 Timeline realism                             [ ] 1 [ ] 2 [ ] 3 [ ] 4 [ ] 5
  3.3 Risk management plan                         [ ] 1 [ ] 2 [ ] 3 [ ] 4 [ ] 5
  3.4 Change management approach                   [ ] 1 [ ] 2 [ ] 3 [ ] 4 [ ] 5
  Notes: _______________________________________________

SECTION 4: COMMERCIAL (Weight: ___%)
  4.1 Total cost of ownership (3-year)             [ ] 1 [ ] 2 [ ] 3 [ ] 4 [ ] 5
  4.2 Pricing model transparency and fit           [ ] 1 [ ] 2 [ ] 3 [ ] 4 [ ] 5
  4.3 Contract terms alignment                     [ ] 1 [ ] 2 [ ] 3 [ ] 4 [ ] 5
  Notes: _______________________________________________

SECTION 5: SUPPORT & ONGOING PARTNERSHIP (Weight: ___%)
  5.1 Support model and SLA commitments            [ ] 1 [ ] 2 [ ] 3 [ ] 4 [ ] 5
  5.2 Product roadmap alignment                    [ ] 1 [ ] 2 [ ] 3 [ ] 4 [ ] 5
  5.3 Customer success / partnership approach      [ ] 1 [ ] 2 [ ] 3 [ ] 4 [ ] 5
  Notes: _______________________________________________

RECOMMENDATION: [ ] Select [ ] Shortlist [ ] Reject
Rationale: _______________________________________________
```

---

## Proposal Response Best Practices

For vendors responding to RFPs (also useful for procurement teams evaluating proposal quality):

### High-Scoring Proposal Structure

| Element | What Evaluators Look For |
|---------|--------------------------|
| **Executive Summary** | Demonstrates understanding of the problem, not a capabilities brochure |
| **Solution Description** | Specific to the requirements — not copy-paste from generic deck |
| **Differentiators** | Clear "why us" vs. stated alternatives, not marketing fluff |
| **Implementation Plan** | Realistic timeline with milestones, named resources, risk items |
| **References** | Similar scope, size, and industry — offered proactively with contact details |
| **Pricing** | Clear TCO, no hidden fees, flexible packaging explained |
| **Exceptions to Terms** | Clearly marked, with rationale and proposed alternatives |

### Proposal Red Flags (Evaluator Warning Signs)

| Red Flag | Likely Cause | Impact |
|----------|-------------|--------|
| Generic proposal (no specific reference to RFP requirements) | Not read the RFP carefully | Deduct points; consider disqualification |
| Pricing significantly below market | Scope misunderstanding or low-ball to win | Risk of cost overruns post-award |
| No client references similar to your size/industry | Limited relevant experience | Elevated implementation risk |
| Key personnel named but not committed | Bait-and-switch risk | Require contractual key-person commitments |
| Vague implementation timeline | Poor planning maturity | Add time buffer; scrutinize PM methodology |
| Extensive exceptions to contract terms | High negotiation friction ahead | Assess legal feasibility before shortlisting |
| Missing required sections | Poor attention to detail or resource-constrained | Disqualify if sections are mandatory |

---

## RFP Automation Patterns

### AI-Powered RFP Response Generation

Modern RFP automation uses a Retrieve-Augment-Generate (RAG) pipeline to accelerate proposal responses:

```
Architecture:
  1. Knowledge Base
     - Company capabilities, case studies, certifications
     - Past RFP responses (approved, redacted)
     - Standard terms and conditions
     - Technical documentation

  2. Ingestion Pipeline
     - Parse incoming RFP (PDF/Word) → extract questions
     - Classify questions by type (technical, commercial, company background)
     - Map to knowledge base sections

  3. Retrieval
     - Semantic search across knowledge base
     - Retrieve top-K relevant passages per question
     - Apply recency and quality weighting

  4. Generation
     - LLM generates draft response grounded in retrieved content
     - Human review and customization layer
     - Compliance check against RFP requirements

  5. Assembly
     - Populate proposal template with generated responses
     - Flag sections requiring human input (pricing, key commitments)
     - Produce draft for review
```

**Quality gates for AI-generated RFP content**:
- [ ] All "Must Have" requirements explicitly addressed
- [ ] No hallucinated capabilities (responses tied to real source documents)
- [ ] Pricing reviewed and approved by finance
- [ ] Legal review of any contractual commitments in prose
- [ ] Named personnel have confirmed availability

### AI-Powered RFP Evaluation (Issuer Side)

```
Use case: Scoring 10+ proposals across 50+ criteria
Pipeline:
  1. Ingest proposals (PDF → text extraction)
  2. For each criterion:
     - Retrieve relevant section from proposal
     - Score 1-5 with rationale
     - Flag for human review if confidence < threshold
  3. Aggregate scores per vendor
  4. Surface scoring discrepancies across evaluators
  5. Generate comparison summary for evaluation committee
```

---

## Common RFP Pitfalls

| Pitfall | Problem | Prevention |
|---------|---------|-----------|
| **Requirements are vague** | Vendors interpret differently; apples-to-oranges comparison | Invest in requirements discovery before drafting RFP |
| **Too short a response window** | Limits quality vendor participation; favors incumbents | Allow minimum 3 weeks for complex procurements |
| **No evaluation criteria disclosed** | Vendors can't optimize proposals; reduces competition | Publish categories and weights in RFP |
| **Questions answered privately** | Unequal information; fairness and legal risk | All Q&A published to all vendors anonymously |
| **Incumbent vendor writes the spec** | RFP written to fit one vendor; competition theater | Firewall incumbent from requirements development |
| **Evaluation team not aligned** | Conflicting scores with no rubric | Pre-calibrate on scoring scale before evaluation begins |
| **Price-only decision** | Lowest TCO not always lowest price | Weight total cost of ownership, not just initial price |
| **No reference checks** | Proposal promises not validated | Require 3 references; call them all |
| **No transition/exit requirements** | Locked into vendor; migration costs unknown | Include data portability and exit provisions in RFP |
| **Legal review too late** | Contract terms surprises after selection | Legal reviews RFP before issue; flags standard terms |

---

## Vendor Due Diligence Checklist

Before awarding contract, complete the following due diligence:

### Financial Stability
- [ ] Review most recent audited financials (or equivalent for private companies)
- [ ] Check D&B or equivalent credit rating
- [ ] Assess funding stability (runway for startups)
- [ ] Verify insurance certificates (general liability, E&O, cyber)

### Legal and Compliance
- [ ] Verify business entity in good standing
- [ ] Check for material litigation (PACER search for US companies)
- [ ] Confirm no debarment (government procurement)
- [ ] Review data processing agreement / DPA for personal data handling
- [ ] Confirm security certifications (SOC 2, ISO 27001, etc.)

### Operational Readiness
- [ ] Conduct reference checks (minimum 3 similar-scope clients)
- [ ] Verify key personnel named in proposal are committed to this contract
- [ ] Confirm implementation methodology and PM assigned
- [ ] Review subcontractor usage and their qualifications

### Contract Review
- [ ] Confirm all required terms and conditions are addressed
- [ ] Verify SLA commitments are contractually binding
- [ ] Confirm IP ownership provisions align with requirements
- [ ] Review exit provisions and data return/deletion terms

---

## Contract Transition Planning

After award, plan the transition carefully:

```
TRANSITION PLANNING CHECKLIST

Pre-Contract Execution
  [ ] Finalize and execute contract (target: within 2 weeks of selection decision)
  [ ] Confirm implementation team from vendor (named resources, not roles)
  [ ] Confirm internal project sponsor and project manager
  [ ] Notify unsuccessful vendors promptly with brief rationale

Kickoff Preparation (Week 1-2 post-signature)
  [ ] Schedule project kickoff meeting
  [ ] Share internal system documentation / data specs with vendor
  [ ] Complete security access provisioning process
  [ ] Align on communication cadence (weekly status, steering committee)

Incumbent Transition (if replacing existing vendor)
  [ ] Notify incumbent of contract expiration date
  [ ] Request data export in agreed format
  [ ] Negotiate parallel run period if needed
  [ ] Confirm exit provisions are honored (data deletion timeline, etc.)
  [ ] Document lessons learned from incumbent relationship for future RFP

Go-Live Gate Criteria
  [ ] All Must Have functional requirements tested and accepted
  [ ] User acceptance testing (UAT) completed and signed off
  [ ] Training completed for all affected users
  [ ] Support escalation path confirmed
  [ ] Rollback plan documented
```
