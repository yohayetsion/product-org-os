---
name: business-case
description: 'Create comprehensive business case with ROI analysis and investment justification. Activate when: "build a business case", "justify this investment", "ROI analysis", investment justification,
  cost-benefit Do NOT activate for: full business plan with operations (/business-plan), pricing decisions (/pricing-strategy), strategic bet formulation (/strategic-bet)'
argument-hint: '[initiative or investment name] or [update path/to/business-case.md]'
user-invocable: true
metadata:
  author: Product Org OS
  version: 3.0.0
  category: business-planning
  skill_type: task-capability
  owner: bizops
  primary_consumers:
  - bizops
  - cfo
  - finance-dir
  - fpa-analyst
  secondary_consumers:
  - ceo
  - revenue-analyst
  - financial-controller
  - treasury-analyst
  - tax-planning
  - investor-relations
  - compensation-analyst
---
## Document Intelligence

This skill supports three modes: **Create**, **Update**, and **Find**.

### Mode Detection

| Signal | Mode | Confidence |
|--------|------|------------|
| "update", "revise", "modify" in input | UPDATE | 100% |
| File path provided (`@path/to/business-case.md`) | UPDATE | 100% |
| "create", "new", "draft" in input | CREATE | 100% |
| "find", "search", "list business cases" | FIND | 100% |
| "the business case", "our business case" | UPDATE | 85% |
| Just initiative/investment name | CREATE | 60% |

**Threshold**: ≥85% auto-proceed | 70-84% state assumption | <70% ask user

### Mode Behaviors

**CREATE**: Generate complete new business case using template below.

**UPDATE**:
1. Read existing business case (search if path not provided)
2. Preserve unchanged sections exactly
3. Update specific sections (financials, risks, assumptions)
4. Show diff summary: "Updated: [sections]. Unchanged: [sections]."
5. Note: Financial projections may need recalculation

**FIND**:
1. Search paths below for business cases
2. Present results: title, initiative, status, path
3. Ask: "Update one of these, or create new?"

### Search Locations for Business Cases

- `business/`
- `strategy/`
- `proposals/`
- `cases/`

---
## Gotchas

- Never fabricate financial projections (revenue, costs, ROI) — provide frameworks with [TBD] inputs
- Sensitivity analysis must test key assumptions — a business case with only one scenario is fiction
- Opportunity cost must be stated — what are we NOT investing in if we do this?
- The business case MUST commit to a specific Continuation Threshold for the next major capital gate. A business case without a named threshold is incomplete — it means the organization is committing to an investment with no defined affirmative test for whether the thesis still holds at the next gate firing. The downstream `/continuation-threshold` skill cannot evaluate what the business case did not declare.



Create a **comprehensive Business Case** for the specified initiative or investment.

## Vision to Value Phase

**Phase 2: Strategic Decisions** - Business cases are the commercial filter that determines whether to proceed.

**Prerequisites**: Phase 1 complete (strategic foundation, market analysis)
**Outputs used by**: Phase 3 (roadmap, GTM commitment), Decision records

## Output Structure

Generate a complete business case with the following sections:

### 1. Executive Summary
- One paragraph recommendation
- Investment ask
- Expected return
- Timeline to value
- Key risks

### 2. Problem/Opportunity Statement
- Current state
- Problem being solved OR opportunity being captured
- Cost of inaction
- Why now?

### 3. Proposed Solution
- Solution description
- Key capabilities
- Differentiators
- Build vs buy analysis (if applicable)

### 4. Market Analysis
- Market size (TAM, SAM, SOM)
- Market trends
- Customer segments
- Growth projections

### 5. Competitive Landscape
- Key competitors
- Competitive positioning
- Differentiation strategy
- Competitive risks

### 6. Financial Projections

#### Revenue Model
| Year | Revenue | Growth Rate |
|------|---------|-------------|
| Year 1 | $X | - |
| Year 2 | $X | X% |
| Year 3 | $X | X% |

#### Cost Structure
| Category | Year 1 | Year 2 | Year 3 |
|----------|--------|--------|--------|
| Development | $X | $X | $X |
| Operations | $X | $X | $X |
| Marketing | $X | $X | $X |
| **Total** | $X | $X | $X |

#### ROI Analysis
- Investment required: $X
- Payback period: X months
- NPV: $X
- IRR: X%

### 7. Investment Requirements
- Capital expenditure
- Operating expenditure
- Resource requirements (headcount)
- Technology requirements
- Timeline of investment

### 8. Risk Analysis
| Risk | Probability | Impact | Mitigation | Residual Risk |
|------|-------------|--------|------------|---------------|
| [Risk] | High/Med/Low | High/Med/Low | [Plan] | High/Med/Low |

### 9. Implementation Timeline
| Phase | Duration | Key Deliverables | Investment |
|-------|----------|------------------|------------|
| Phase 1 | X months | [Deliverables] | $X |
| Phase 2 | X months | [Deliverables] | $X |

### 10. Success Criteria
| Metric | Target | Timeframe | Measurement Method |
|--------|--------|-----------|-------------------|
| [Metric] | [Target] | [When] | [How measured] |

### 11. Assumptions
- Key assumptions underlying the analysis
- Sensitivity of results to assumption changes

### 11.5. Continuation Threshold

The Continuation Threshold is the specific, signal-driven affirmative gate this business case commits to clear at the next major capital checkpoint. It is the inverse of an invalidation criterion: invalidation says "stop if this fires"; the Continuation Threshold says "continue only if this holds." The threshold is DEFINED here in the business case and EVALUATED downstream by `/continuation-threshold` when the gate fires.

A business case without a Continuation Threshold is incomplete — it means the organization is committing capital with no declared affirmative test for whether the thesis still holds at the next gate.

| Field | Definition |
|-------|------------|
| `next_gate_firing` | The specific checkpoint at which this threshold will be evaluated (e.g., "Q4 portfolio review", "Series-stage funding decision", "Phase 2 to Phase 3 commit") |
| `threshold_criteria` | The named, signal-driven criteria the bet must clear at the gate. Each criterion specifies a metric or evidence requirement and the level it must reach. |
| `re_decision_triggers_minimum` | The minimum number of the bet's named re-decision triggers that must remain in "not yet fired" state for the threshold to be eligible to pass. If fewer than this minimum remain unfired, the threshold is NOT met regardless of headline criteria. |
| `default_action_if_not_met` | Always: **reopen and route to portfolio review**. Silent continuation under the original commitment is a process failure. |

Example:

> **Continuation Threshold for next gate (Q4 portfolio review)**:
> - At least N early-customer wins from the target segment by gate firing date
> - Conversion-rate signal at or above [target] across the validation cohort
> - At least [M] of the bet's [N total] named re-decision triggers remain in "not yet fired" state
>
> If any criterion is not met, the business case reopens for portfolio review.

### 12. Recommendation
- Clear recommendation (proceed / don't proceed / conditional)
- Conditions or prerequisites
- Next steps if approved

### 13. Conformance Signals

Two signals on this business case that downstream skills consume:

| Signal | Definition | Computed at |
|--------|------------|-------------|
| `continuation_threshold_declared` | TRUE if §11.5 is populated with `next_gate_firing`, `threshold_criteria`, and `re_decision_triggers_minimum`; FALSE otherwise. A FALSE value means the business case is incomplete and cannot be consumed by `/continuation-threshold` at the next gate. | Authoring time |
| `re_decision_triggers_minimum_met` | TRUE if the bet's named re-decision triggers (declared in the bound `/strategic-bet` record) currently have at least `re_decision_triggers_minimum` of them in "not yet fired" state; FALSE if too many have fired. | Audit time (each gate firing) |

The `re_decision_triggers_minimum_met` signal is computed dynamically each time the business case is read for a gate decision — it is not a static field. The `/continuation-threshold` skill consumes this signal directly when producing its pass / fail / reopen verdict; if the signal is FALSE, the threshold cannot be met regardless of how the headline criteria look.

This signal mirrors the level-1 conformance signal of the same name in the V5.2 Decision Standard (Section 6) — the business case is the primary artifact in which the signal becomes computable for a strategic bet.

## Integration with /continuation-threshold

This skill is the upstream artifact that **defines** the Continuation Threshold. The downstream `/continuation-threshold` skill **evaluates** whether the threshold is met at a specific gate firing. The split is deliberate:

- `/business-case` declares the test once, at commitment time, when the organization is most clear-eyed about what would justify continuing.
- `/continuation-threshold` runs the test repeatedly, at each gate firing, against the current evidence base.

The two skills are paired: a Continuation Threshold evaluation cannot be produced without a business case that declared one, and a business case without a declared threshold cannot have a structured continue / fail / reopen verdict at the gate.

A `/phase-check` decision that consumes a Phase 2 → Phase 3 advance hard-gates on a `pass` verdict from `/continuation-threshold`, which in turn consumes the threshold definition from this business case. The chain is: `/business-case` (declares threshold) → `/continuation-threshold` (evaluates at gate, returns pass / fail / reopen) → `/phase-check` (authorizes phase advance only on pass).

## Instructions

1. Ask clarifying questions about scope and assumptions
2. Reference any market or financial documents provided via @file syntax
3. Be explicit about assumptions
4. Include sensitivity analysis for key variables
5. Populate §11.5 Continuation Threshold with named criteria, the minimum number of re-decision triggers required in "not yet fired" state, and the next gate firing window — without these the business case is incomplete and cannot be consumed by `/continuation-threshold` at the next gate
6. Save as markdown file
7. Offer to create presentation version using /present
