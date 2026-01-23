---
globs:
  - "**/*"
---

# Skill Awareness

Master catalog of all skills available in the V2V Product Org Plugin. All agents have access to all skills and should use them based on their R&R and the task at hand.

## Skill Categories

### Context Layer Skills (7)
| Skill | Purpose |
|-------|---------|
| `/context-save` | Save decision, bet, or learning to context registry |
| `/context-recall` | Query past decisions, bets, and learnings by topic |
| `/portfolio-status` | View current state of all active strategic bets |
| `/relevant-learnings` | Find past learnings applicable to current work |
| `/handoff` | Capture context for agent-to-agent delegation |
| `/feedback-capture` | Capture and analyze product feedback |
| `/feedback-recall` | Query past feedback by topic, source, or theme |

### Principle Validator Skills (5)
| Skill | Principle | Purpose |
|-------|-----------|---------|
| `/ownership-map` | #1 End-to-End | Map accountability across V2V phases |
| `/customer-value-trace` | #3 Customer Obsession | Validate work traces to customer value |
| `/collaboration-check` | #6 Collaborative Excellence | Validate RACI and stakeholder consultation |
| `/scale-check` | #8 Scalable Systems | Assess scalability at 2x, 10x, 100x |
| `/phase-check` | V2V Flow | Assess which phase an initiative is in |

### Decision Skills (5)
| Skill | Purpose |
|-------|---------|
| `/decision-record` | Create a structured decision record |
| `/decision-charter` | Create Decision Interface Charter for recurring decisions |
| `/escalation-rule` | Define escalation rules for a decision area |
| `/decision-quality-audit` | Audit recent decisions for quality |
| `/portfolio-tradeoff` | Structure portfolio-level tradeoff decision |

### Strategy Skills (5)
| Skill | Purpose |
|-------|---------|
| `/strategic-intent` | Document strategic intent and direction |
| `/strategic-bet` | Formulate strategic bet with explicit assumptions |
| `/commitment-check` | Validate commitment readiness before point of no return |
| `/vision-statement` | Draft a product vision statement |
| `/strategy-communication` | Create strategy communication package |

### Market & Competitive Skills (5)
| Skill | Purpose |
|-------|---------|
| `/market-analysis` | Create comprehensive market analysis |
| `/market-segment` | Define a market segment |
| `/competitive-landscape` | Create comprehensive competitive analysis report |
| `/competitive-analysis` | Structure a focused competitive analysis |
| `/positioning-statement` | Create a positioning statement |

### Business & Pricing Skills (4)
| Skill | Purpose |
|-------|---------|
| `/business-case` | Create comprehensive business case |
| `/business-plan` | Create complete business plan |
| `/pricing-strategy` | Create complete pricing strategy document |
| `/pricing-model` | Design a pricing model |

### Roadmap Skills (3)
| Skill | Purpose |
|-------|---------|
| `/product-roadmap` | Create complete product roadmap document |
| `/roadmap-theme` | Define a roadmap theme with initiatives |
| `/roadmap-item` | Define a specific roadmap item |

### GTM & Launch Skills (4)
| Skill | Purpose |
|-------|---------|
| `/gtm-strategy` | Create comprehensive go-to-market strategy |
| `/gtm-brief` | Create a go-to-market brief |
| `/launch-plan` | Create complete product launch plan |
| `/launch-readiness` | Launch readiness decision checklist |

### Requirements Skills (4)
| Skill | Purpose |
|-------|---------|
| `/prd` | Create complete Product Requirements Document |
| `/prd-outline` | Create a PRD outline |
| `/feature-spec` | Create a feature specification |
| `/user-story` | Write a user story with acceptance criteria |

### Operational Skills (6)
| Skill | Purpose |
|-------|---------|
| `/campaign-brief` | Create marketing campaign brief |
| `/sales-enablement` | Create sales enablement package |
| `/stakeholder-brief` | Create stakeholder communication brief |
| `/onboarding-playbook` | Create customer onboarding playbook |
| `/value-realization-report` | Create value realization report |
| `/customer-health-scorecard` | Create customer health scorecard |

### Learning & Review Skills (3)
| Skill | Purpose |
|-------|---------|
| `/outcome-review` | Structure an outcome review for learning |
| `/retrospective` | Conduct structured retrospective |
| `/qbr-deck` | Create Quarterly Business Review presentation |

### Assessment Skills (2)
| Skill | Purpose |
|-------|---------|
| `/maturity-check` | Assess organizational maturity for a dimension |
| `/pm-level-check` | Assess PM competency level |

### Utility Skills (2)
| Skill | Purpose |
|-------|---------|
| `/setup` | Initialize the Product Org plugin |
| `/present` | Convert a deliverable document to HTML presentation |

---

## Document Intelligence

Most document-generating skills support three modes: **Create**, **Update**, and **Find**.

### How It Works

Skills automatically detect which mode to use:
- **CREATE**: Default when just providing a topic (e.g., `/prd authentication`)
- **UPDATE**: When using "update", "revise", providing a path, or referencing "the [doc type]"
- **FIND**: When using "find", "search", or "list"

### Skills with Document Intelligence (43)

All skills that produce documents support Create/Update/Find:
- Decision skills: decision-record, decision-charter, escalation-rule, decision-quality-audit, portfolio-tradeoff
- Strategy skills: strategic-intent, strategic-bet, commitment-check, vision-statement, strategy-communication
- Market skills: market-analysis, market-segment, competitive-landscape, competitive-analysis, positioning-statement
- Business skills: business-case, business-plan, pricing-strategy, pricing-model
- Roadmap skills: product-roadmap, roadmap-theme, roadmap-item
- GTM skills: gtm-strategy, gtm-brief, launch-plan, launch-readiness
- Requirements skills: prd, prd-outline, feature-spec, user-story
- Operational skills: campaign-brief, sales-enablement, stakeholder-brief, onboarding-playbook, value-realization-report, customer-health-scorecard
- Learning skills: outcome-review, retrospective, qbr-deck
- Validator skills: ownership-map, customer-value-trace, collaboration-check, scale-check

### Skills WITHOUT Document Intelligence (13)

These are context/retrieval skills that operate differently:
- Context layer: context-save, context-recall, portfolio-status, relevant-learnings, handoff, feedback-capture, feedback-recall
- Assessment: maturity-check, pm-level-check
- Utility: setup, present
- Validator: phase-check

---

## Skills by V2V Phase

### Phase 1: Strategic Foundation
`/strategic-intent`, `/market-analysis`, `/competitive-landscape`, `/competitive-analysis`, `/vision-statement`, `/market-segment`

### Phase 2: Strategic Decisions
`/business-case`, `/business-plan`, `/pricing-strategy`, `/pricing-model`, `/positioning-statement`, `/decision-record`, `/strategic-bet`, `/decision-charter`, `/escalation-rule`

### Phase 3: Strategic Commitments
`/product-roadmap`, `/roadmap-theme`, `/roadmap-item`, `/gtm-strategy`, `/gtm-brief`, `/launch-plan`, `/strategy-communication`, `/commitment-check`, `/prd`, `/prd-outline`, `/feature-spec`, `/user-story`

### Phase 4: Coordinated Execution
`/campaign-brief`, `/sales-enablement`, `/launch-readiness`, `/stakeholder-brief`

### Phase 5: Business & Customer Outcomes
`/onboarding-playbook`, `/value-realization-report`, `/customer-health-scorecard`

### Phase 6: Learning & Adaptation
`/outcome-review`, `/retrospective`, `/decision-quality-audit`, `/relevant-learnings`, `/context-save`, `/feedback-capture`

### Cross-Phase
`/context-recall`, `/feedback-recall`, `/portfolio-status`, `/portfolio-tradeoff`, `/handoff`, `/setup`, `/present`, `/qbr-deck`, `/maturity-check`, `/pm-level-check`, `/phase-check`, `/ownership-map`, `/customer-value-trace`, `/collaboration-check`, `/scale-check`

---

## Skill Selection Guidelines

### By Task Type

**Strategic planning**: `/strategic-intent`, `/strategic-bet`, `/vision-statement`
**Market understanding**: `/market-analysis`, `/competitive-landscape`, `/market-segment`
**Commercial decisions**: `/business-case`, `/pricing-strategy`, `/decision-record`
**Execution planning**: `/product-roadmap`, `/gtm-strategy`, `/launch-plan`
**Requirements**: `/prd`, `/feature-spec`, `/user-story`
**Go-to-market**: `/campaign-brief`, `/sales-enablement`, `/launch-readiness`
**Customer success**: `/onboarding-playbook`, `/value-realization-report`
**Learning**: `/outcome-review`, `/retrospective`, `/decision-quality-audit`

### By Validation Need

**Before decisions**: `/context-recall`, `/feedback-recall`, `/customer-value-trace`
**Before commitments**: `/commitment-check`, `/ownership-map`, `/phase-check`
**After outcomes**: `/outcome-review`, `/scale-check`, `/context-save`

---

## Skill Count Summary

| Category | Count |
|----------|-------|
| Context Layer | 7 |
| Principle Validators | 5 |
| Decisions | 5 |
| Strategy | 5 |
| Market & Competitive | 5 |
| Business & Pricing | 4 |
| Roadmap | 3 |
| GTM & Launch | 4 |
| Requirements | 4 |
| Operational | 6 |
| Learning & Review | 3 |
| Assessment | 2 |
| Utility | 2 |
| **TOTAL** | **55** |

---

## V2V Operating Principle

> "Every skill exists for a reason. Choose the right skill for the task, not the task for the skill you know."
