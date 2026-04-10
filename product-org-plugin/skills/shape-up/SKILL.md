---
name: shape-up
description: "Apply Basecamp's Shape Up methodology — fixed time, variable scope product development with pitches, bets, and 6-week cycles. Activate when: \"shape up\", \"pitch\", \"bet table\", \"6-week cycle\", \"hill chart\", \"appetite\", \"fixed time variable scope\", \"cool down period\", \"circuit breaker\" Do NOT activate for: prioritization (/prioritize-features), roadmap planning (/product-roadmap), sprint planning (use Scrum), strategic bets (/strategic-bet)"
argument-hint: "[feature or initiative] or [update path/to/shape-up.md]"
user-invocable: true
metadata:
  author: Product Org OS
  version: 1.0.0
  category: product-management
compatibility: Requires Product Org OS v3+ context layer and rules
---

## Document Intelligence

This skill supports three modes: **Create**, **Update**, and **Find**.

### Mode Detection

| Signal | Mode | Confidence |
|--------|------|------------|
| "update", "revise", "refresh" in input | UPDATE | 100% |
| File path provided (`@path/to/shape-up.md`) | UPDATE | 100% |
| "create", "new", "shape", "pitch" in input | CREATE | 100% |
| "find", "search", "list pitches" | FIND | 100% |
| "the pitch for [feature]", "our bet table" | UPDATE | 85% |
| Just a feature or initiative name | CREATE | 60% |

**Threshold**: >=85% auto-proceed | 70-84% state assumption | <70% ask user

### Mode Behaviors

**CREATE**: Shape the initiative into a pitch with appetite, solution sketch, rabbit holes, and no-go's. Produce bet table entry and hill chart scope breakdown.

**UPDATE**:
1. Read existing pitch or cycle document (search if path not provided)
2. Preserve appetite and core problem statement
3. Update solution sketch, hill chart positions, or scope assignments
4. Show diff summary: "Updated: [sections]. Appetite unchanged at [X weeks]."

**FIND**:
1. Search paths below for Shape Up documents
2. Present results: initiative name, appetite, cycle, path
3. Ask: "Update one of these, or create new?"

### Search Locations

- `product/`
- `planning/`
- `cycles/`
- `pitches/`

---

## Gotchas

- Appetite is NOT an estimate — it is a **budget**. Do not ask "how long will this take?" Ask "how much time is this worth?"
- Shaping happens BEFORE the cycle begins, by senior people. It is not sprint planning done by the delivery team
- Hill charts track scopes, not tasks. Each scope is a meaningful slice of the project that one person can complete
- Circuit breakers are non-negotiable — if work is not done when the cycle ends, it does NOT automatically continue. It must be re-pitched

## Vision to Value Phase

**Phase 3: Strategic Commitments** - Shape Up converts strategic decisions into executable commitments via pitches and bets, with fixed time budgets and clear scope boundaries.

**Prerequisites**: Phase 1-2 complete (strategic intent defined, business case validated, problem understood)
**Outputs used by**: Phase 4 (coordinated execution within cycles), Phase 5 (outcome tracking per cycle), `/commitment-check` (verifying commitment boundaries)

## Methodology

<!-- Source: "Shape Up: Stop Running in Circles and Ship Work that Matters" — Ryan Singer, Basecamp (2019). Free at basecamp.com/shapeup. Shape Up is Basecamp's product development methodology that replaces Scrum sprints with 6-week cycles, emphasizes shaping work before building, and uses appetite (fixed time, variable scope) instead of estimation (variable time, fixed scope). -->

<!-- Source: Hill Charts — Basecamp internal tool concept documented in Shape Up. Hills represent the two phases of every scope: the uphill phase (figuring things out, uncertainty, unknown unknowns) and the downhill phase (execution, known work, implementation). Dots on the hill chart represent scopes, not tasks. A scope stuck on the uphill side is a risk signal. -->

<!-- Source: Inspired by wdavidturner/product-skills shape-up skill structure. Adapted and expanded with full pitch template, hill chart tracking, and bet table protocol. -->

### Shaping vs. Building

| Aspect | Shaping (Before Cycle) | Building (During Cycle) |
|--------|----------------------|----------------------|
| **Who** | Senior product people, designers | Delivery team (1-3 people) |
| **When** | Before the cycle starts | During the 6-week cycle |
| **Fidelity** | Fat marker sketches, not wireframes | Full implementation |
| **Scope** | Defined boundaries, not task lists | Team decides HOW within boundaries |
| **Output** | Pitch document | Shipped software |

### Appetite Setting

Appetite is the **time budget** you are willing to spend. It constrains scope — not the other way around.

| Batch Size | Duration | Team | Use When |
|-----------|----------|------|----------|
| **Small Batch** | 1-2 weeks | 1-2 people | Well-understood problems, minor improvements |
| **Big Batch** | 6 weeks | 2-3 people | Significant features, new capabilities |

**Key principle**: If the solution cannot fit the appetite, **narrow the scope** — do not extend the time.

### The Pitch Format

A pitch is the shaped proposal that goes to the bet table. It must contain:

| Section | Purpose | Anti-Pattern |
|---------|---------|-------------|
| **Problem** | What customer problem are we solving? Raw idea + specific use case | Vague "it would be nice if" |
| **Appetite** | How much time is this worth? Small batch or big batch | Estimate disguised as appetite |
| **Solution** | Fat marker sketch — enough to show the approach, rough enough to leave room | Wireframes, pixel-perfect mockups |
| **Rabbit Holes** | Known complexities and how to avoid them | Ignoring edge cases |
| **No-Go's** | What is explicitly OUT of scope | Unbounded scope |

### The Bet Table

Leadership reviews pitches and decides what to bet on for the next cycle. Not all pitches get picked. Unpicked pitches are not automatically carried over — they must be re-pitched (they may no longer be relevant).

| Decision | Meaning |
|----------|---------|
| **Bet** | Commit to this pitch for the next cycle |
| **Pass** | Not now — may be re-pitched later |
| **Kill** | This idea is not worth pursuing |

### Hill Chart Tracking

The hill chart has two sides:

```
         /\
   Uphill/  \Downhill
  (figuring  (execution,
   it out)    making it happen)
```

- **Uphill**: Uncertainty, unknowns, exploration, problem-solving
- **Downhill**: Execution, known work, implementation, integration
- Each **scope** (not task) gets a dot on the hill
- Scopes stuck on the uphill side for too long = **risk signal**

### Circuit Breaker

If work is not finished when the 6-week cycle ends:

1. The work **stops**. No extensions by default
2. The team presents what they learned
3. If the work is still valuable, it must be **re-pitched** at the next bet table
4. This prevents runaway projects and forces honest appetite-setting

### Cool Down (2 weeks)

Between every 6-week cycle, a 2-week cool-down period:

- Fix bugs discovered during the cycle
- Explore new ideas and prototypes
- Address tech debt
- No shaped work, no scheduled projects
- Teams have autonomy over cool-down activities

## Output Structure

```markdown
# Shape Up Pitch: [Initiative Name]

**Date**: [YYYY-MM-DD]
**Shaped by**: [Who shaped this pitch]
**Appetite**: [Small Batch: X weeks / Big Batch: 6 weeks]
**Status**: [Draft / Ready for Bet Table / Bet / Building / Shipped]

---

## Problem

### Raw Idea
[The original idea or request that sparked this pitch]

### Specific Use Case
[A concrete scenario showing the customer pain]

### Why Now
[What makes this worth considering for the next cycle]

---

## Appetite

**Batch size**: [Small Batch (1-2 weeks) / Big Batch (6 weeks)]
**Team size**: [X people]
**Time budget**: [X weeks]

**Appetite rationale**: [Why this amount of time is appropriate — what makes it worth X weeks but not more]

---

## Solution

### Approach (Fat Marker Sketch)
[High-level solution approach — enough detail to show the shape, rough enough to leave room for the builders]

### Key Elements
| Element | Description | Why It Matters |
|---------|-------------|---------------|
| [Element 1] | [What it is] | [Why it solves the problem] |
| [Element 2] | [What it is] | [Why it solves the problem] |
| [Element 3] | [What it is] | [Why it solves the problem] |

---

## Rabbit Holes

| Risk | Mitigation | Decision |
|------|-----------|----------|
| [Complexity 1] | [How to avoid] | [Simplify / Cut / Timebox] |
| [Complexity 2] | [How to avoid] | [Simplify / Cut / Timebox] |
| [Complexity 3] | [How to avoid] | [Simplify / Cut / Timebox] |

---

## No-Go's

Explicitly **out of scope** for this pitch:

- [Thing we are NOT doing 1] — [Why]
- [Thing we are NOT doing 2] — [Why]
- [Thing we are NOT doing 3] — [Why]

---

## Scopes & Hill Chart

| Scope | Description | Hill Position | Owner |
|-------|-------------|---------------|-------|
| [Scope 1] | [What this slice covers] | [Uphill / Over the hill / Downhill / Done] | [TBD] |
| [Scope 2] | [What this slice covers] | [Uphill / Over the hill / Downhill / Done] | [TBD] |
| [Scope 3] | [What this slice covers] | [Uphill / Over the hill / Downhill / Done] | [TBD] |

**Hill chart last updated**: [YYYY-MM-DD]

---

## Bet Table Entry

| Field | Value |
|-------|-------|
| Pitch | [Initiative Name] |
| Appetite | [X weeks] |
| Cycle | [Cycle number or date range] |
| Decision | [Bet / Pass / Kill] |
| Decided by | [Who] |
| Decision date | [YYYY-MM-DD] |
| Rationale | [Why this was bet on / passed / killed] |

---

## Cycle Schedule

| Phase | Dates | Duration |
|-------|-------|----------|
| **Shaping** | [Start - End] | [Variable] |
| **Bet Table** | [Date] | 1 day |
| **Cycle** | [Start - End] | 6 weeks |
| **Cool Down** | [Start - End] | 2 weeks |

---

## Assumptions to Validate

| # | Assumption | Validation Method | Impact if Wrong |
|---|-----------|------------------|-----------------|
| 1 | [Assumption] | [Method] | High/Med/Low |
| 2 | [Assumption] | [Method] | High/Med/Low |

## Next Steps

- [ ] Review pitch at bet table
- [ ] Assign team if bet is placed
- [ ] Break into scopes during cycle kickoff
- [ ] Track hill chart weekly during cycle
- [ ] Run `/commitment-check` to verify boundaries
```

## Instructions

1. Start by understanding the problem — what customer pain are we solving?
2. Set the appetite FIRST — ask "how much time is this worth?" not "how long will it take?"
3. Shape the solution at fat-marker fidelity — no wireframes, no task lists
4. Identify rabbit holes and explicitly decide how to handle each one
5. Define no-go's — what is OUT of scope is as important as what is in
6. Break the shaped work into scopes (meaningful slices, not tasks)
7. Position each scope on the hill chart
8. Produce a bet table entry with clear decision recommendation
9. Save output as markdown file
10. Offer `/commitment-check` to verify commitment boundaries are clear

## Integration

- Links to `/commitment-check` (verify commitment boundaries before betting)
- Links to `/product-roadmap` (cycle planning feeds roadmap)
- Links to `/prd` (pitches may reference or feed into PRDs)
- Links to `/feature-spec` (scopes may become feature specs during building)
- Links to `/retrospective` (cycle outcomes feed learning)
- Links to `/context-save` (save bet decisions and cycle outcomes)
