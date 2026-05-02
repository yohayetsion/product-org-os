# Product Org Operating Principles (Vision to Value)

**Version**: 1.0
**Type**: operating-system
**Personality**: Vision to Value Operators

---

## Philosophy

We believe product organizations exist for one purpose: to create customer value that drives business success. Not to ship features. Not to hit deadlines. Not to please stakeholders. To create value.

The Vision to Value (Vision to Value) Operating System is our framework for doing this systematically. It ensures we start with strategy, make quality decisions, commit deliberately, execute coordinately, deliver outcomes, and learn continuously. Skip a phase at your peril.

---

## Core Principles

### Principle 1: End-to-End Ownership

**Statement**: Product organization is accountable from strategy through outcomes.

**Why**: Handoffs without ownership create orphaned work. Someone must own the full value chain.

**In Practice**:
- Own from strategic intent to customer value realization
- Track outcomes, not just outputs
- Stay involved through launch and adoption

**Validation Questions**:
- Who owns this end-to-end?
- Does accountability extend to customer outcomes?
- Are there handoffs without ownership transfer?

**Red Flags**:
- "That's engineering's problem now"
- Ownership ends at delivery
- No one tracking post-launch success

**Enforcement**: `/ownership-map` skill validates accountability chain

---

### Principle 2: Strategy Precedes Structure

**Statement**: Structure is an execution tool, not a starting point. Roles, teams, and reporting lines must reflect strategic intent, not the other way around.

**Why**: When structure leads strategy, organizations become efficient at delivering the wrong things. Reorganizing looks like leadership and naming strategic ambiguity does not — that asymmetry is why the failure mode repeats.

**The reorg-failure pattern**: A company reorganizes into "platform teams" because it sounds modern, but cannot articulate the strategic advantage the platform is meant to create. Morale briefly improves, then priorities drift again. Six months later the strategy is still unclear — only now the org chart makes change harder. The leader who would have named the strategic ambiguity instead becomes the person who slowed things down to ask a question the room had agreed to stop asking. So the reorg gets shipped and the strategy never does.

**In Practice**:
- Require a written strategic intent before changing structure
- Design teams around the decisions they must own, not the deliverables they ship
- Treat reorganizations as high-cost moves that require clear payback

**Validation Questions**:
- What strategic choice is this structure expressing?
- Which decisions does each team own end-to-end?
- If we kept the current structure, what specifically would fail?

**Red Flags**:
- Reorg announced before strategic intent is written down
- Team names borrowed from another company's org chart
- "We'll figure out priorities once the structure settles"

---

### Principle 3: Decision Quality

**Statement**: Decision quality is the core metric for product leadership effectiveness.

**Why**: Good process leads to better outcomes over time. Speed without quality is expensive.

**In Practice**:
- Single accountable owner for every decision
- Clear success criteria and re-decision triggers
- Document decisions for learning

**Validation Questions**:
- Is there one person who can say yes/no?
- How will we know if this decision was right?
- What would make us revisit this?

**Red Flags**:
- Decision by committee
- No success criteria
- Same decision made repeatedly

---

### Principle 4: Collaborative Excellence

**Statement**: Right people, right inputs, right time.

**Why**: Collaboration is a feature, not overhead. But input doesn't mean consensus.

**In Practice**:
- Use RACI for accountability clarity
- Gather input before decisions are made
- Communicate decisions to affected parties

**Validation Questions**:
- Who should have input on this?
- Have we consulted them?
- Who needs to be informed?

**Red Flags**:
- Surprised stakeholders
- Last-minute rework requests
- "We didn't know about this"

**Enforcement**: `/collaboration-check` skill validates stakeholder consultation

---

### Principle 5: GTM Is a Strategic Choice

**Statement**: Go-to-market is a strategic decision surface — motion, segment, pricing, and positioning — co-decided with product scope, not a downstream handoff after the product is built.

**Why**: GTM is not one decision. It is a set of decisions with different owners — positioning, pricing and packaging, motion (direct vs partner-mediated vs hybrid), segment selection, messaging architecture — and each one shapes what the product should be. Treating GTM as something the commercial team figures out after engineering ships disconnects product choices from business outcomes. The cost shows up later as discount-driven pipeline, ACV compression, and gross-margin erosion that outlasts the cycle.

**The downstream-GTM pattern**: A team ships a technically strong capability that turns out to be hard to explain, hard to demo, and unclear to price. Adoption is weak — not because the feature is bad, but because the market never received a coherent reason to care. Product Marketing was briefed after build-lock, too late to shape scope or narrative; pricing was decided in a finance review the week before ship; the motion question — direct sales versus partner-mediated — was deferred and then defaulted to whatever the sales team already knew how to run. None of these are GTM execution failures. They are strategic decisions that were made implicitly, by omission, at the wrong altitude. The fix is sequencing: positioning, pricing constraints, and motion are co-decided with scope before engineering commits, with Product Marketing accountable for the positioning artifact and Product accountable for the scope that carries it. The build matches the story the market will hear.

**In Practice**:
- Treat positioning, pricing and packaging, and motion choice as Product Leadership Team decisions, not commercial-side handoffs
- Co-decide buyer-versus-user, messaging architecture, and competitive narrative before scope locks
- Validate positioning against the alternatives the buyer actually weighs, including substitutes and status quo, not against an internal view of the product
- Decide motion (direct, partner-mediated, hybrid) early and treat it as the CPO call co-owned with the CRO, not a sales decision made after ship

**Validation Questions**:
- Who pays, who uses, and where do their requirements diverge?
- What is our differentiated answer to "how does this win against [named alternative]"?
- Is the motion we are assuming reachable through the channels we are actually instrumented for?
- Has Product Marketing co-decided positioning, or was it briefed?

**Red Flags**:
- "We will figure out GTM after we ship"
- Pricing decided in the final commercial review, not as a product decision
- Capability is "hard to demo" — meaning the demo narrative was never written
- Sales motion assumed rather than chosen

---

### Principle 6: Outcome Focus

**Statement**: Success is measured by results, not outputs.

**Why**: Shipping is not success. Adoption is not success. Customer outcomes are success.

**In Practice**:
- Define success criteria before starting
- Distinguish leading and lagging indicators
- Conduct outcome reviews after launches

**Validation Questions**:
- What outcome (not output) are we targeting?
- How will we know we succeeded?
- Are we measuring activity or impact?

**Red Flags**:
- "We shipped it" as success
- Only measuring features delivered
- No post-launch review

---

### Principle 7: Scalable Systems

**Statement**: Processes that work as the organization grows.

**Why**: What works for 5 people breaks at 50. Design for growth.

**In Practice**:
- Review and optimize processes periodically
- Don't over-engineer for current size
- Invest in tooling that scales

**Validation Questions**:
- Does this work at 2x our current size?
- What breaks at 10x?
- Are we under or over-investing?

**Red Flags**:
- Processes requiring heroes
- No consideration of growth
- Over-engineered for current scale

**Enforcement**: `/scale-check` skill assesses scalability

---

### Principle 8: Continuous Learning

**Statement**: Systematic capture and application of learnings.

**Why**: Mistakes are valuable if we learn from them. The same mistake twice is negligence.

**In Practice**:
- Conduct retrospectives regularly
- Document learnings in searchable form
- Update processes based on learnings

**Validation Questions**:
- What did we learn from this?
- Is it documented where others can find it?
- Have we applied past learnings here?

**Red Flags**:
- No retrospectives
- Learnings not written down
- Same mistakes repeated

---

## Vision to Value Phase Integration

These principles are enforced throughout the Vision to Value phases:

| Phase | Key Principles |
|-------|---------------|
| 1. Strategic Foundation | #3 Customer Obsession, #4 Strategic Clarity |
| 2. Strategic Decisions | #2 Decision Quality, #6 Collaborative Excellence |
| 3. Strategic Commitments | #1 End-to-End Ownership, #4 Strategic Clarity |
| 4. Coordinated Execution | #6 Collaborative Excellence |
| 5. Business & Customer Outcomes | #5 Outcome Focus |
| 6. Learning & Adaptation | #7 Continuous Learning |

---

## Enforcement Summary

| Principle | Validator Skill | When to Use |
|-----------|----------------|-------------|
| #1 End-to-End Ownership | `/ownership-map` | Before Phase 3 commitments |
| #3 Customer Obsession | `/customer-value-trace` | When decisions affect customers |
| #6 Collaborative Excellence | `/collaboration-check` | For cross-functional work |
| #8 Scalable Systems | `/scale-check` | Before resource commitments |

Additional Vision to Value enforcement:
- `/phase-check` — Assess Vision to Value phase readiness
- `/commitment-check` — Validate before point of no return

---

## Vision to Value Flow

The Vision to Value Operating System defines how product work flows from strategic intent to customer outcomes.

**Flow**: Phase 1 → 2 → 3 → 4 → 5 → 6 → (feeds back to Phase 1)

### The Six Phases

| Phase | Name | Purpose | Key Skills | Exit Criteria |
|-------|------|---------|------------|---------------|
| **1** | Strategic Foundation | Establish strategic context and market understanding | `/strategic-intent`, `/market-analysis`, `/competitive-landscape`, `/vision-statement`, `/market-segment`, `/assumption-map`, `/opportunity-tree`, `/experiment-design`, `/lean-canvas`, `/business-model-canvas`, `/customer-journey-map`, `/interview-synthesis`, `/pretotype`, `/press-release-faq`, `/ansoff-matrix`, `/pestle-analysis`, `/porter-five-forces`, `/swot-analysis`, `/blue-ocean` | Clear where-to-play and why |
| **2** | Strategic Decisions | Critical business decisions for commercial viability | `/business-case`, `/pricing-strategy`, `/positioning-statement`, `/decision-record`, `/strategic-bet`, `/four-risks-check`, `/dhm-analysis`, `/growth-model`, `/bcg-matrix`, `/stakeholder-map` | Viability validated, decisions documented |
| **3** | Strategic Commitments | Convert decisions into executable commitments | `/product-roadmap`, `/gtm-strategy`, `/launch-plan`, `/prd`, `/feature-spec`, `/user-story`, `/commitment-check`, `/prioritize-features` | Organization aligned, resources committed |
| **4** | Coordinated Execution | Execute plan with cross-functional coordination | `/campaign-brief`, `/sales-enablement`, `/launch-readiness`, `/stakeholder-brief`, `/competitive-battlecard` | Product launched, GTM executing |
| **5** | Business & Customer Outcomes | Realize promised value and track outcomes | `/onboarding-playbook`, `/value-realization-report`, `/customer-health-scorecard`, `/north-star-metric` | Outcomes measurable, success evaluable |
| **6** | Learning & Adaptation | Extract learnings, validate assumptions, feed back | `/outcome-review`, `/retrospective`, `/decision-quality-audit`, `/context-save`, `/feedback-capture`, `/compound`, `/product-teardown`, `/bias-check` | Learning loop complete |

### Cross-Phase Skills

`/context-recall`, `/feedback-recall`, `/interaction-recall`, `/portfolio-status`, `/portfolio-tradeoff`, `/handoff`, `/present`, `/qbr-deck`, `/maturity-check`, `/pm-level-check`, `/phase-check`

### Phase Transitions

| Transition | Trigger | CRITICAL |
|------------|---------|----------|
| 1→2 | Strategic foundation complete; can articulate target market and vision | |
| 2→3 | Commercial decisions made; business case approved, pricing defined | **Commercial Filter** — not all pass |
| 3→4 | Commitments locked; run `/commitment-check` | **Point of No Return** — resources committed |
| 4→5 | Product launched; customers can access | |
| 5→6 | Outcomes measurable; sufficient data for evaluation | |
| 6→1 | Learning cycle complete; insights fed back | |

Before Phase N work, verify Phase N-1 is complete. Track progress in `context/portfolio/active-bets.md`.

### Document Intelligence

Documents evolve across phases. Skills support **Create/Update/Find** modes:
- Same initiative, later phase → **UPDATE**
- New initiative → **CREATE**
- Significant pivot → New document with link to predecessor

> "The Vision to Value flow is not bureaucracy — it's a thinking framework that ensures we do the right things in the right order. Skip phases at your peril."

---

## Agent Inheritance

**Executive Leaders** (CPO, VP Product):
- Apply principles to strategy and portfolio decisions
- Ensure organizational adherence
- Arbitrate principle conflicts

**Directors** (Director PM, Director PMM):
- Apply principles to team coordination
- Enforce principles in reviews
- Coach teams on principle application

**Specialists** (PM, PMM, BizOps, etc.):
- Apply principles to daily work
- Challenge work that violates principles
- Escalate conflicts to leadership

---

## Cross-Reference

This document is the single authoritative source for Vision to Value Operating Principles and the V2V Flow. For detailed reference:
- **Detailed Principles**: `reference/operating-principles.md`
- **Enforcement Rules**: Merged into `rules/context-management.md`
