---
name: wardley-map
description: 'Create a Wardley Map to visualize value chains and component evolution for strategic decision-making. Activate when: "wardley map", "value chain map", "component evolution", "strategic landscape", "wardley", "evolution stages", "map the landscape" Do NOT activate for: competitive landscape (/competitive-landscape), market analysis (/market-analysis), business model (/business-model-canvas)'
argument-hint: '[user need or business domain] or [update path/to/wardley-map.md]'
user-invocable: true
metadata:
  author: Product Org OS
  category: strategy
  skill_type: task-capability
  owner: chief-architect
  primary_consumers:
  - chief-architect
  secondary_consumers:
  - cpo
  - vp-product
  - ci
  - head-corpdev
  - corporate-venture
  - ceo
---

# Wardley Map — Decision Evidence

**Sources consulted**: Simon Wardley originated Wardley Mapping.
**Source licence**: Simon Wardley's published work is available under CC BY-SA 4.0.
**Our determination**: `describes-public-method` — this skill is original Vision to Value prose describing and applying a public method. It does not reproduce Wardley text, diagrams, tables, or the source's chapter organization.
**V2V refinements**: organizes mapping as a decision-evidence workflow that connects a user need, dependency observations, movement signals, options, and a traceable decision.

## Choose the operating mode

Use **Create** when the user supplies a need, domain, or decision but no existing map. Use **Update** when a path or an existing map is supplied. Use **Find** when the user asks to locate prior maps.

For Update, preserve the existing anchor and dependency logic unless new evidence invalidates them. Report what moved, what evidence changed, and which decision consequence follows. For Find, search `strategy/`, `product/`, `planning/`, `analysis/`, and `competitive/`, then return paths and map dates before asking whether to update or create.

## Confirm the decision boundary

Before mapping, write the decision as a question with a named decision owner. A map without a live decision becomes an attractive inventory.

Capture:

- the user or stakeholder whose need anchors the map;
- the outcome they are trying to achieve;
- the decision that the map must inform;
- the boundary of the system being mapped;
- the evidence date and any material unknowns.

If the request is a market comparison rather than a dependency-and-evolution question, use `/competitive-landscape`. If it is an industry-structure question, use `/market-analysis` or `/porter-five-forces`.

## Build an evidence chain from the need

Start at the visible need and work downward by asking, “What must be true or available for this to work?” Repeat until the chain reaches enabling infrastructure.

For every component, record:

1. **Dependency** — what directly depends on it.
2. **User visibility** — how close it is to the anchor need.
3. **Current evidence** — an observation, source, or owner statement supporting its placement.
4. **Consequence of failure** — what decision or outcome breaks if it is missing.

Do not add components merely because they exist in the organization. Include only components that participate in the selected need.

## Place components using observable evolution signals

A Wardley Map uses two dimensions:

- vertical position shows proximity to the user need, from visible value near the top to less-visible enabling components below;
- horizontal position shows how the component is supplied and understood, from novel and uncertain on the left to standardized and interchangeable on the right.

Use the conventional evolution labels because they are the public method's vocabulary:

- **Genesis** — the capability is emerging, poorly understood, and lacks dependable market alternatives.
- **Custom-built** — the need is understood enough to build repeatedly, but solutions remain bespoke.
- **Product or rental** — repeatable offerings and recognizable vendors exist, with meaningful differentiation between them.
- **Commodity or utility** — supply is standardized, widely available, and selected mainly for fitness, reliability, and cost.

Treat a position as an evidence-backed hypothesis, not a score. If evidence conflicts, show a range or mark the placement uncertain. Never force precision to make the map look complete.

## Read the tensions that affect the decision

Inspect the completed chain for tensions that change what the organization should do:

- bespoke work sitting on top of a mature market alternative;
- a differentiating capability constrained by a commodity dependency;
- a component moving toward standard supply while the organization still treats it as unique;
- inertia created by contracts, skills, incentives, legacy architecture, or identity;
- a bottleneck whose failure propagates upward to the user need;
- an immature dependency carrying more operational certainty than the evidence supports;
- two components coupled together even though their rates of change differ.

State each tension as an observation plus decision consequence. Do not turn patterns into universal rules.

## Convert the map into options

For every material tension, produce at least two credible options. Typical option types include build, buy, rent, partner, standardize, isolate, experiment, migrate, or stop.

For each option record:

- the dependency or tension it addresses;
- evidence supporting it;
- what must be true for it to work;
- the principal downside or exposure;
- the earliest reversible test;
- the decision owner.

Recommend an option only when the evidence supports the link from map observation to action. If the map cannot distinguish the options, name the missing evidence instead of manufacturing certainty.

## Output contract

Create or update a Markdown document using this V2V structure:

```markdown
# Decision Map: [domain]

**Decision owner**: [name/role]
**Evidence date**: [date]
**Status**: Draft | Active | Superseded

## Decision to inform

[One decision question]

## Anchor need and boundary

- User/stakeholder: [who]
- Need/outcome: [what]
- In scope: [boundary]
- Out of scope: [boundary]

## Dependency evidence

| Component | Depends on | User proximity | Evolution hypothesis | Evidence | Confidence note |
|---|---|---|---|---|---|
| [component] | [component/need] | [high/medium/low] | [stage or range] | [source/observation] | [why uncertain] |

## Map view

[Mermaid, map notation, or a clearly labelled text representation. Every component must match the dependency table.]

## Movement and constraints

| Component | Observed direction | Constraint or inertia | Decision consequence |
|---|---|---|---|
| [component] | [stable/moving/uncertain] | [evidence] | [so what] |

## Options

| Option | Map evidence | Assumptions | Principal downside | Reversible test | Owner |
|---|---|---|---|---|---|
| [option] | [observation] | [assumption] | [risk] | [test] | [role] |

## Recommendation

[Recommended choice, evidence chain, and why the alternatives are weaker]

## Open evidence gaps

- [Unknown that could change the decision]

## Decision trace

- Strategic bet or decision record: [path/TBD]
- Review trigger: [observable event]
```

## Quality checks

Before returning the map, confirm:

- the anchor is a real user need, not an internal department goal;
- every component connects to that need through an explicit dependency;
- evolution placements cite observations rather than intuition alone;
- movement is distinguished from current position;
- inertia is stated as evidence, not as a label for resistance;
- recommendations trace back to mapped observations;
- important unknowns remain visible;
- the output contains a decision owner and a review trigger.

## Vision to Value integration

Use the map as an input to Phase 1 strategic intent and Phase 2 strategic decisions. Route a selected high-stakes option to `/strategic-bet` and record a committed choice with `/decision-record`. Use `/assumption-map` when multiple unknowns could reverse the recommendation, and `/build-buy-partner` when the central question is sourcing.

The map informs a decision; it does not replace the decision record, evidence review, or accountable owner.
