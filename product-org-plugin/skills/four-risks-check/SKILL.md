---
name: four-risks-check
description: 'Assess a feature or initiative against Marty Cagan''s Four Big Risks (Value, Usability, Feasibility, Business Viability) to determine readiness for commitment. Activate when: "four risks",
  "risk check", "value risk", "usability risk", "feasibility risk", "viability risk", "should we build", "Cagan", "discovery risks", "VUFE check", "product risk assessment" Do NOT activate for: assumption
  mapping (/assumption-map), experiment design (/experiment-design), enterprise risk management (@risk-manager)'
argument-hint: '[feature or initiative name] or [update path/to/risk-check.md]'
user-invocable: true
metadata:
  author: Product Org OS
  version: 1.0.0
  category: product-management
  skill_type: task-capability
  owner: vp-product
  primary_consumers:
  - vp-product
  - pm
  - general-counsel
  - chief-architect
  - security-architect
  - risk-manager
  secondary_consumers:
  - cpo
  - pm-dir
  - bizdev
  - contracts-counsel
  - ai-architect
  - ma-analyst
  - corporate-venture
  - ml-engineer
  - cfo
---
## Document Intelligence

This skill supports three modes: **Create**, **Update**, and **Find**.

### Mode Detection

| Signal | Mode | Confidence |
|--------|------|------------|
| "update", "revise", "re-assess" in input | UPDATE | 100% |
| File path provided (`@path/to/risk-check.md`) | UPDATE | 100% |
| "create", "new", "check risks for" in input | CREATE | 100% |
| "find", "search", "list risk checks" | FIND | 100% |
| "the risk check", "our risk assessment" | UPDATE | 85% |
| Just a feature/initiative name | CREATE | 60% |

**Threshold**: >=85% auto-proceed | 70-84% state assumption | <70% ask user

### Mode Behaviors

**CREATE**: Assess the feature/initiative against all four risk dimensions. Produce risk matrix with validation recommendations.

**UPDATE**:
1. Read existing risk check (search if path not provided)
2. Preserve unchanged assessments
3. Update specific risk dimensions based on new evidence
4. Show diff summary: "Updated: [risks]. Unchanged: [risks]. Overall verdict changed: [yes/no]."

**FIND**:
1. Search paths below for risk check documents
2. Present results: title, feature, verdict, path
3. Ask: "Update one of these, or create new?"

### Search Locations

- `product/`
- `discovery/`
- `risks/`
- `planning/`

---
## Gotchas

- Value risk, usability risk, feasibility risk, and viability risk must each be assessed independently
- Don't conflate technical feasibility with business viability — both must pass separately



## Vision to Value Phase

**Phase 2: Strategic Decisions** - The Four Risks Check validates whether an initiative is ready for resource commitment, acting as a quality gate before Phase 3.

**Prerequisites**: Phase 1 complete (strategic foundation, initial discovery)
**Outputs used by**: `/commitment-check` (Phase 3), `/decision-record`, `/prd`

## Methodology

<!-- Source: Four Big Risks — Marty Cagan, Silicon Valley Product Group (SVPG). From "Inspired: How to Create Tech Products Customers Love" (2nd edition, 2017, Wiley) and "Empowered: Ordinary People, Extraordinary Products" (2020, Wiley). Core thesis: the purpose of product discovery is to address four critical risks BEFORE committing to delivery. Teams that skip discovery and go straight to delivery are essentially gambling with the company's resources. The four risks are: Value (will customers buy/use it?), Usability (can users figure it out?), Feasibility (can we build it with the time, skills, and technology available?), and Business Viability (does it work for our business — legal, financial, sales, marketing, support?). -->

<!-- Source: VUFE Pattern — phuryn/pm-skills. Mnemonic ordering: Value, Usability, Feasibility, Ethics/Viability. The categorization pattern for grouping assumptions by risk type, complementing Cagan's framework with structured assumption categorization. -->

<!-- Source: Discovery techniques mapping — Teresa Torres, "Continuous Discovery Habits" (2021, Product Talk). Torres maps specific discovery techniques to each risk type, emphasizing that different risks require different validation approaches. Opportunity Solution Trees help connect customer opportunities to solutions while surfacing risks across all four dimensions. -->

### The Four Risks

| Risk | Core Question | What Failure Looks Like |
|------|--------------|------------------------|
| **Value Risk** | Will customers buy it or choose to use it? | Product launches but nobody adopts. Low conversion, high churn, feature unused. |
| **Usability Risk** | Can users figure out how to use it? | Users try but fail. High support tickets, low task completion, user frustration. |
| **Feasibility Risk** | Can we build it with the time, skills, and technology available? | Delivery takes 3x longer than expected, quality is poor, technical debt accumulates. |
| **Business Viability Risk** | Does it work for our business? | Product succeeds with users but undermines the business (legal issues, cannibalization, unsustainable economics, misaligned sales motion). |

### Risk Assessment Framework

For each risk, assess three dimensions:

| Dimension | Description | Scale |
|-----------|-------------|-------|
| **Risk Level** | How likely is this risk to materialize? | High / Medium / Low |
| **Evidence Quality** | How strong is the evidence for our assessment? | Strong (data) / Moderate (proxies) / Weak (assumptions) |
| **Validation Status** | Have we tested this risk? | Validated / Partially Validated / Unvalidated |

### Validation Techniques by Risk Type

| Risk | Recommended Validation Techniques |
|------|----------------------------------|
| **Value Risk** | Customer interviews, demand tests, fake door tests, concierge MVP, landing page tests, wizard of Oz prototypes, customer letters of intent |
| **Usability Risk** | Prototype usability testing, user testing sessions, task completion analysis, first-click testing, 5-second tests, card sorting |
| **Feasibility Risk** | Technical spike, architecture review, proof of concept, vendor evaluation, performance benchmarks, security review |
| **Business Viability Risk** | Stakeholder review (legal, finance, sales, compliance), unit economics modeling, channel conflict analysis, support capacity assessment |

### Risk Level Determination

| Level | Criteria |
|-------|---------|
| **High** | No evidence to support our assumption, significant unknowns, high stakes if wrong |
| **Medium** | Some indirect evidence, moderate unknowns, manageable consequences if wrong |
| **Low** | Strong direct evidence, few unknowns, limited downside if wrong |

### Overall Verdict

| Verdict | Criteria | Action |
|---------|---------|--------|
| **GO** | All risks Low or Medium with strong evidence | Proceed to commitment (Phase 3) |
| **GO WITH CONDITIONS** | 1-2 risks Medium with moderate evidence | Proceed but monitor; define risk mitigation plan |
| **NEEDS DISCOVERY** | Any risk High OR multiple risks Medium with weak evidence | Return to discovery; run specific validation before committing |
| **NO-GO** | Multiple risks High, fundamental issues identified | Do not proceed; pivot or kill |

## Output Structure

```markdown
# Four Risks Check: [Feature/Initiative Name]

**Date**: [YYYY-MM-DD]
**Owner**: [Who owns this assessment]
**Product**: [Product name]
**Phase**: [Current Vision to Value phase]

## Initiative Summary

**What**: [Brief description of the feature/initiative]
**Who**: [Target user/customer]
**Why**: [Problem being solved or opportunity being captured]
**How big**: [Scope — small feature / major feature / new product]

## Risk Assessment Matrix

| Risk | Level | Evidence Quality | Validation Status | Key Concern |
|------|-------|-----------------|-------------------|-------------|
| **Value** | [High/Med/Low] | [Strong/Moderate/Weak] | [Validated/Partial/Unvalidated] | [One-line concern] |
| **Usability** | [High/Med/Low] | [Strong/Moderate/Weak] | [Validated/Partial/Unvalidated] | [One-line concern] |
| **Feasibility** | [High/Med/Low] | [Strong/Moderate/Weak] | [Validated/Partial/Unvalidated] | [One-line concern] |
| **Viability** | [High/Med/Low] | [Strong/Moderate/Weak] | [Validated/Partial/Unvalidated] | [One-line concern] |

## Detailed Assessment

### Value Risk
**Question**: Will customers buy it or choose to use it?

**Current evidence**:
- [Evidence point 1]
- [Evidence point 2]

**Gaps**:
- [What we don't know]

**Assessment**: [Narrative assessment]
**Risk level**: [High/Medium/Low]

### Usability Risk
**Question**: Can users figure out how to use it?

**Current evidence**:
- [Evidence point 1]
- [Evidence point 2]

**Gaps**:
- [What we don't know]

**Assessment**: [Narrative assessment]
**Risk level**: [High/Medium/Low]

### Feasibility Risk
**Question**: Can we build it with the time, skills, and technology available?

**Current evidence**:
- [Evidence point 1]
- [Evidence point 2]

**Gaps**:
- [What we don't know]

**Assessment**: [Narrative assessment]
**Risk level**: [High/Medium/Low]

### Business Viability Risk
**Question**: Does it work for our business?

**Stakeholders consulted**: [Legal, Finance, Sales, etc. — or "None yet"]

**Current evidence**:
- [Evidence point 1]
- [Evidence point 2]

**Gaps**:
- [What we don't know]

**Assessment**: [Narrative assessment]
**Risk level**: [High/Medium/Low]

## Overall Verdict

**Verdict**: [GO / GO WITH CONDITIONS / NEEDS DISCOVERY / NO-GO]

**Rationale**: [Why this verdict]

## Validation Plan (for Medium/High risks)

| Risk | Validation Technique | Success Criteria | Timeline | Owner |
|------|---------------------|-----------------|----------|-------|
| [Risk] | [Technique] | [What would de-risk this] | [When] | [Who] |

## Conditions for Proceeding (if GO WITH CONDITIONS)

- [ ] [Condition 1]
- [ ] [Condition 2]

## Assumptions Log

| # | Assumption | Risk Type | Impact if Wrong | Confidence |
|---|-----------|-----------|-----------------|------------|
| 1 | [Assumption] | [V/U/F/B] | [High/Med/Low] | [High/Med/Low] |

## Next Steps

- [ ] Run validation for [highest risk] via `/experiment-design`
- [ ] If GO: proceed to `/commitment-check` and `/prd`
- [ ] If NEEDS DISCOVERY: schedule discovery sprint for [risk area]
- [ ] Save decision via `/decision-record`
```

## Instructions

1. Ask for the feature/initiative description if not provided
2. Assess each risk dimension independently; do not let one risk color the others
3. Be honest about evidence quality; "we think customers want this" with no interviews = Weak evidence, not Moderate
4. For feasibility, note that you cannot estimate implementation effort; recommend consulting engineering for technical assessment
5. For business viability, prompt consideration of: legal/compliance, finance/unit economics, sales channel fit, support implications, brand impact
6. The verdict must follow the criteria table; do not give GO when any risk is High
7. Always produce a validation plan for Medium and High risks
8. Save output as markdown file
9. Offer `/experiment-design` for validation or `/commitment-check` when verdict is GO

## Integration

- Links to `/assumption-map` (deeper assumption analysis across all risk types)
- Links to `/experiment-design` (design validation experiments for High/Medium risks)
- Links to `/commitment-check` (proceed to commitment when risks are addressed)
- Links to `/decision-record` (document the go/no-go decision)
- Links to `/prd` (write requirements once risks are de-risked)
- Links to `/context-recall` (check if similar risks were encountered before)
- Links to `/feedback-recall` (incorporate customer feedback into Value Risk assessment)
