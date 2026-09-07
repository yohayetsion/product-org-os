# Product Org Operating Principles (Vision to Value)

**Version**: 1.0
**Type**: operating-system
**Personality**: Vision to Value Operators

---

## Philosophy

We believe product organizations exist for one purpose: to create customer value that drives business success. Not to ship features. Not to hit deadlines. Not to please stakeholders. To create value.

The Vision to Value (Vision to Value) Operating System is our framework for doing this systematically. It ensures we start with strategy, make quality decisions, commit deliberately, execute coordinately, deliver outcomes, and learn continuously. Skip a phase at your peril.

**Primary audience**: Product Org leadership (CPO → VP Product → PLT → product professionals). These are the operators of the system — the ones who make decisions, run the Charters, and ship the outcomes.

**Secondary audience**: C-suite peers (CEO, CFO, CMO, CIO, General Counsel, CHRO) as context readers. They read the OS to understand how the product organization decides and operates, not to operate it themselves. The system is designed to make product-org behavior legible to executive peers without requiring them to adopt the operating model.

---

## The v5 Posture: Decision System, Human-Held, Bridged by the Standard

This section is the strategic posture of the Vision to Value Operating System. It sits upstream of the Core Principles: the principles describe operating discipline; the posture describes the strategic choices the OS makes about *how* a product organization should be structured. It is grounded in the book and the Decision Provenance Standard — *the book is the architecture, the Standard is the bridge, the Product Org OS is the reference implementation.* Cross-reference the V2V book for full treatment.

### Decision system

This book treats product leadership as a **decision system** — not a collection of best practices, and not a methodology. Vision becomes value through a repeatable decision system, not through isolated execution. The product organization is, at its core, that decision system; shipped output and delivery are downstream consequences of well-run decisions. This reframes what a product org optimizes for: decision quality, decision provenance, and the systematic capture of decisions so that future decisions inherit context. Skills like `/decision-record`, `/decision-charter`, `/strategic-bet`, and the entire Phase 2 (Strategic Decisions) stack are the surface area of this posture. The Decision Interface Charter is the single artifact at the center of that blueprint — the **decision instrument**, not the bridge.

### Human-held custodianship

Custodianship of the company-wide decision system stays **human-held**. The Standard makes a Product Organization's decisions affirmable, auditable, and resumable, regardless of whether a human or a model produced the underlying analysis. That is what keeps custodianship human-held as AI participation deepens. **None of it works without a human in the seat.** The product leader is the custodian of how decisions get made across the company; the Standard's Layer 4 attestation schema is the mechanism by which human review at the Reviewer Checklist gate becomes machine-readable, so the gate stays human (a licensed counsel, a CPO sign-off, an HR reviewer) while the chain of provenance is preserved. `sensitive-skill-guardrails.md` operationalizes this seam.

### Standard-as-bridge

The open Decision Provenance Standard is **the bridge** between two things: the Product Organization's human custodianship of the company-wide decision system, and the AI tooling that increasingly participates in it. The bridge mechanism is the Standard's affirmable, auditable, and resumable **records** — not decisions handed downstream to other functions, and not the Decision Interface Charter (which is the decision instrument, not the bridge). **The book is the architecture. The Standard is the bridge. The Product Org OS is the reference implementation.**

> Read-or-run is not a strategic posture. It is a property of the Standard's reporter: the human-read gate corresponds to the Standard's human-attestation layers (Layer 2/3/4), and machine-run checks correspond to Layer 1 plus conformance signals.

---

## Core Principles

### Principle 1: End-to-End Ownership Is Non-Negotiable

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

### Principle 2: Product Leadership Is About Decision Quality

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

### Principle 3: Strategy Precedes Structure

**Statement**: Strategy comes first; structure, teams, and process follow from it — never the reverse.

**Why**: Organizing the org chart before the strategy locks in the wrong shape. Structure should be the consequence of where you've chosen to play and how you've chosen to win, and every choice should still trace to customer value rather than internal convenience.

**In Practice**:
- Settle the strategy (where-to-play, how-to-win) before designing teams or process
- Start every document with the customer problem the strategy serves
- Let structure follow the strategy; revisit structure when the strategy changes

**Validation Questions**:
- Is the strategy clear enough to derive structure from it?
- What customer problem does this strategy solve?
- Are we shaping teams to the strategy, or bending the strategy to existing teams?

**Red Flags**:
- Org chart decided before the strategy
- Internal convenience driving the structure
- Strategy reverse-engineered to fit the team you already have

**Enforcement**: `/customer-value-trace` skill validates customer connection

---

### Principle 4: Go-to-market Is a Strategic Choice, Not a Handoff

**Statement**: Go-to-market is part of the product strategy, owned by product leadership — not a downstream handoff to another function.

**Why**: When GTM is treated as a handoff, the product organization abdicates a strategic choice. How a product reaches its market shapes what the product should be; the two decisions are inseparable, so the product org owns both.

**In Practice**:
- Treat GTM motion (PLG / SLG / channel) as a strategic decision, made with explicit assumptions
- Make the GTM choice alongside the product choice, not after it
- Frame the cross-functional handoff as a Decision Interface Charter, not an ad-hoc toss-over-the-wall

**Validation Questions**:
- Is the GTM motion a deliberate choice or a default?
- What are we assuming about how this product reaches its market?
- Who owns the GTM decision — product leadership, or is it being handed off?

**Red Flags**:
- GTM treated as someone else's problem after the product is built
- No explicit GTM motion decision
- Product and GTM strategy decided in isolation from each other

---

### Principle 5: Organizations Learn Through Outcomes

**Statement**: Success is measured by results, not outputs — and outcomes are how the organization learns.

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

### Principle 6: Alignment Beats Consensus

**Statement**: Right people, right inputs, right time — align on the decision without requiring everyone to agree.

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

### Principle 7: Execution Is a Leadership Discipline

**Statement**: Execution is a leadership discipline, not a delegated afterthought. Product leadership owns getting decisions all the way to delivered value.

**Why**: Decisions that don't get executed are not decisions, they're opinions. Leaders who treat execution as someone else's job lose the thread between strategy and outcome. Execution is where strategy is tested, so it stays a leadership responsibility — including the discipline of learning from how it went.

**In Practice**:
- Stay accountable through delivery, not just through the decision
- Run retrospectives and outcome reviews; document learnings in searchable form
- Close the loop: feed what execution taught you back into the next decision

**Validation Questions**:
- Did this decision actually reach delivered value, or stall after the call was made?
- What did execution teach us, and is it documented where others can find it?
- Are we treating execution as a leadership discipline or handing it off?

**Red Flags**:
- Decisions made but never driven to delivery
- Execution treated as below leadership's pay grade
- No retrospectives; learnings not written down; same mistakes repeated

---

### Principle 8: Scale Changes the Nature of the Work

**Statement**: Scale doesn't just add more work — it changes the kind of work. Processes must evolve as the organization grows.

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

## Vision to Value Phase Integration

These principles are enforced throughout the Vision to Value phases:

| Phase | Key Principles |
|-------|---------------|
| 1. Strategic Foundation | #3 Strategy Precedes Structure |
| 2. Strategic Decisions | #2 Product Leadership Is About Decision Quality, #6 Alignment Beats Consensus |
| 3. Strategic Commitments | #1 End-to-End Ownership Is Non-Negotiable, #4 Go-to-market Is a Strategic Choice |
| 4. Coordinated Execution | #6 Alignment Beats Consensus, #7 Execution Is a Leadership Discipline |
| 5. Business & Customer Outcomes | #5 Organizations Learn Through Outcomes |
| 6. Learning & Adaptation | #5 Organizations Learn Through Outcomes, #7 Execution Is a Leadership Discipline |

---

## Enforcement Summary

| Principle | Validator Skill | When to Use |
|-----------|----------------|-------------|
| #1 End-to-End Ownership Is Non-Negotiable | `/ownership-map` | Before Phase 3 commitments |
| #3 Strategy Precedes Structure | `/customer-value-trace` | When decisions affect customers |
| #6 Alignment Beats Consensus | `/collaboration-check` | For cross-functional work |
| #8 Scale Changes the Nature of the Work | `/scale-check` | Before resource commitments |

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
- **Detailed Principles**: this single authoritative source
- **Enforcement Rules**: Merged into `rules/context-management.md`
