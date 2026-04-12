---
name: ooda-loop
description: 'Apply Boyd''s OODA Loop (Observe-Orient-Decide-Act) for rapid decision-making cycles and competitive tempo analysis. Activate when: "OODA", "OODA loop", "observe orient decide act", "Boyd",
  "decision cycle", "rapid decision", "competitive tempo", "decision speed" Do NOT activate for: decision records (/decision-record), DACI (/daci), pre-mortem (/pre-mortem)'
argument-hint: '[situation or decision context] or [update path/to/ooda-loop.md]'
user-invocable: true
metadata:
  author: Product Org OS
  version: 1.0.0
  category: decision-making
  skill_type: task-capability
  secondary_consumers:
  - cpo
  - vp-product
  - chief-architect
  - ceo
  - growth-marketer
---
## Document Intelligence

This skill supports three modes: **Create**, **Update**, and **Find**.

### Mode Detection

| Signal | Mode | Confidence |
|--------|------|------------|
| "update", "revise", "iterate" in input | UPDATE | 100% |
| File path provided (`@path/to/ooda-loop.md`) | UPDATE | 100% |
| "create", "new", "run OODA" in input | CREATE | 100% |
| "find", "search", "list OODA" | FIND | 100% |
| "the OODA", "our decision cycle" | UPDATE | 85% |
| Just a situation or decision topic | CREATE | 60% |

**Threshold**: >=85% auto-proceed | 70-84% state assumption | <70% ask user

### Mode Behaviors

**CREATE**: Walk through all four OODA phases for the given situation, produce a complete cycle document with orientation analysis and action plan.

**UPDATE**:
1. Read existing OODA analysis (search if path not provided)
2. Preserve prior observations and orientations that remain valid
3. Add new observations, reorient based on new information, update decisions/actions
4. Show diff summary: "New observations: [items]. Reoriented: [sections]. Actions updated: [items]."

**FIND**:
1. Search paths below for OODA analysis documents
2. Present results: situation, date, cycle number, path
3. Ask: "Update one of these, or create new?"

### Search Locations

- `decisions/`
- `strategy/`
- `product/`
- `analysis/`

---
## Gotchas

- Orientation is the MOST IMPORTANT step — don't rush through it. This is where biases, mental models, and cultural assumptions shape interpretation. Challenge them explicitly.
- OODA is a LOOP, not a linear checklist — the output of Act feeds back into Observe. Always define the feedback mechanism.
- Don't confuse speed with haste — Boyd's insight is about cycle speed relative to competitors, not about skipping analysis.
- Implicit guidance (experienced practitioners skipping Decide/Act) only applies when orientation is deeply internalized — document when this is appropriate vs. when explicit steps are needed.

## Vision to Value Phase

**Cross-Phase (Rapid Decision Cycle)** - OODA applies throughout the Vision to Value flow. It is most valuable during Phase 1 (rapid environmental scanning), Phase 4 (execution tempo), and Phase 6 (learning feedback loops).

**Prerequisites**: A situation requiring a decision, competitive context, or environmental uncertainty
**Outputs used by**: `/decision-record` (formalize the Decide step), `/strategic-bet` (high-stakes OODA outputs), `/experiment-design` (Act step as experiment), `/retrospective` (learning from completed cycles)

## Methodology

<!-- Source: OODA Loop — Colonel John Boyd, USAF (1976, "Destruction and Creation" + subsequent briefings). Boyd never published a formal paper; his ideas were disseminated through briefings like "Patterns of Conflict" (1986) and "The Strategic Game of ? and ?" (1987). -->

<!-- Source: joelparkerhenderson/ooda-loop — comprehensive OODA Loop reference with examples and applications to business strategy. -->

<!-- Source: "Boyd: The Fighter Pilot Who Changed the Art of War" — Robert Coram (2002, Little Brown). The definitive Boyd biography explaining the development and application of OODA. -->

### The OODA Loop

The OODA Loop is a decision-making framework developed by military strategist Colonel John Boyd. The core principle: **whoever cycles through OODA fastest gains the initiative and wins.** In product strategy, this means faster market sensing, faster interpretation, faster decisions, and faster execution than competitors.

#### 1. Observe (Environmental Scanning)
Gather raw information from the environment:
- Market signals, customer behavior changes, competitive moves
- Internal metrics, usage data, support tickets, churn signals
- Technology shifts, regulatory changes, ecosystem developments
- Team sentiment, organizational friction, process bottlenecks

#### 2. Orient (The Critical Step)
Analyze and synthesize observations into a mental model. **This is where competitive advantage lives.** Orientation is shaped by:
- **Cultural traditions**: Industry norms, company culture, "how we've always done it"
- **Previous experience**: Pattern recognition from past cycles, institutional memory
- **New information**: Fresh data that challenges existing mental models
- **Analysis & synthesis**: Breaking apart observations and recombining them into new understanding
- **Genetic heritage**: Core identity, mission, values that filter interpretation

Boyd's key insight: **orientation shapes observation** (you see what your mental model allows) AND **orientation shapes action** (you act based on how you interpret, not on raw data). Challenging orientation biases is the highest-leverage activity.

#### 3. Decide (Select Course of Action)
Based on the oriented mental model, select a course of action:
- Hypothesis: "If we do X, we expect Y because of Z"
- Alternatives considered (minimum 2)
- Reversibility assessment: one-way door vs. two-way door
- Speed vs. accuracy tradeoff: when is "good enough" better than "perfect"?

#### 4. Act (Execute and Feed Back)
Execute the decision and establish the feedback loop:
- Ship the change, launch the experiment, make the move
- Define what to observe in the next cycle (close the loop)
- Set the tempo: how fast should the next cycle begin?
- Communicate the action to the team (shared orientation)

#### Implicit Guidance and Control
Experienced practitioners develop such strong orientation that they can flow directly from Orient to Act, bypassing explicit Decide. This is analogous to expert intuition — but it requires:
- Deep domain expertise
- Many completed OODA cycles building pattern recognition
- High-trust environment where rapid action is supported

#### Tempo and Competitive Advantage
Operating INSIDE the competitor's OODA loop means:
- You observe and act before they can orient to your last move
- They are perpetually reacting to a reality you've already moved past
- Their orientation becomes increasingly disconnected from the actual environment

#### Anti-Patterns
- **Analysis paralysis**: Stuck in Orient, never reaching Decide
- **Fire-ready-aim**: Acting without observing (skipping O-O)
- **Confirmation bias in Orient**: Only seeing data that confirms existing mental model
- **Single-loop**: Running OODA once as a linear process instead of a continuous cycle
- **Individual OODA without shared orientation**: Team members cycling at different speeds with different mental models

## Output Structure

```markdown
# OODA Loop Analysis: [Situation / Decision Context]

**Date**: [YYYY-MM-DD]
**Owner**: [Who owns this decision cycle]
**Cycle**: [#1, #2, etc. — increment for recurring analysis]
**Tempo Target**: [How fast should this cycle complete?]
**Context**: [Why this OODA cycle is needed now]

## Observe: Environmental Scan

### External Signals

| # | Observation | Source | Freshness | Reliability |
|---|-------------|--------|-----------|-------------|
| OB1 | [Signal] | [Source] | [When observed] | High/Med/Low |
| OB2 | [Signal] | [Source] | [When observed] | High/Med/Low |
| OB3 | [Signal] | [Source] | [When observed] | High/Med/Low |
| OB4 | [Signal] | [Source] | [When observed] | High/Med/Low |
| OB5 | [Signal] | [Source] | [When observed] | High/Med/Low |

### Internal Signals

| # | Observation | Source | Freshness | Reliability |
|---|-------------|--------|-----------|-------------|
| OB6 | [Signal] | [Source] | [When observed] | High/Med/Low |
| OB7 | [Signal] | [Source] | [When observed] | High/Med/Low |
| OB8 | [Signal] | [Source] | [When observed] | High/Med/Low |

### Blind Spots
[What are we NOT seeing? What data sources are we missing?]

## Orient: Mental Model Formation

### Current Mental Model
[How do we currently interpret the situation? What is our working hypothesis about what's happening?]

### Orientation Filters (Boyd's Factors)

| Filter | How It Shapes Our View | Challenge |
|--------|----------------------|-----------|
| Cultural traditions | [Industry/company norms influencing interpretation] | [How might this be wrong?] |
| Previous experience | [Past patterns we're matching to] | [Is this situation actually different?] |
| New information | [Data that challenges our existing model] | [Are we weighting this appropriately?] |
| Analysis & synthesis | [How we're combining signals] | [What alternative synthesis exists?] |

### Reoriented Mental Model
[After challenging filters: what is our UPDATED interpretation of the situation?]

### Key Insight
[The single most important realization from orientation — what changed in our understanding?]

## Decide: Course of Action

### Options Considered

| Option | Hypothesis | Reversibility | Speed | Expected Outcome |
|--------|-----------|---------------|-------|-----------------|
| A: [Action] | If we [X], then [Y] because [Z] | One-way / Two-way | [Time] | [Expected result] |
| B: [Action] | If we [X], then [Y] because [Z] | One-way / Two-way | [Time] | [Expected result] |
| C: [Action] | If we [X], then [Y] because [Z] | One-way / Two-way | [Time] | [Expected result] |

### Selected Action
**Option [X]**: [Name]

**Rationale**: [Why this option, given our orientation]
**Speed vs. Accuracy**: [Are we optimizing for tempo or precision in this cycle?]

## Act: Execution Plan

### Immediate Actions

| # | Action | Owner | By When | Done? |
|---|--------|-------|---------|-------|
| 1 | [Action] | [Who] | [When] | [ ] |
| 2 | [Action] | [Who] | [When] | [ ] |
| 3 | [Action] | [Who] | [When] | [ ] |

### Feedback Loop (Close the Cycle)

**What to observe next**: [Specific signals to watch for after acting]
**Next cycle trigger**: [When/what triggers the next OODA iteration]
**Tempo**: [Target time for next complete cycle]
**Shared orientation**: [How will the team be aligned on the updated mental model?]

## Competitive Tempo Assessment

**Our cycle speed**: [Estimated time for this OODA cycle]
**Competitor cycle speed**: [Estimated — are we inside or outside their loop?]
**Tempo advantage**: [Are we gaining or losing initiative?]

## Assumptions

| # | Assumption | Phase | Confidence | If Wrong |
|---|-----------|-------|------------|----------|
| 1 | [Assumption] | O/O/D/A | High/Med/Low | [Impact] |
| 2 | [Assumption] | O/O/D/A | High/Med/Low | [Impact] |

## Next Steps

- [ ] Execute Act items and begin observing results
- [ ] Schedule next OODA cycle based on tempo target
- [ ] Formalize decision via `/decision-record` if high-stakes
- [ ] Feed learnings into `/retrospective` after cycle completes
```

## Instructions

1. Clarify the situation or decision context with the user
2. **Check prior context**: Run `/context-recall [topic]` to find related past decisions or cycles
3. Walk through each OODA phase sequentially — spend the most time on Orient
4. In Orient, explicitly challenge each of Boyd's orientation filters (cultural traditions, experience, new information, analysis/synthesis)
5. Require at least 2 options in the Decide phase — if only one option exists, the decision is already made
6. Define the feedback loop in Act — an OODA cycle without a feedback mechanism is not a loop
7. Assess competitive tempo: are we cycling faster or slower than the competition?
8. Save output as markdown file
9. Offer to formalize high-stakes decisions via `/decision-record` or frame strategic bets via `/strategic-bet`

## Integration

- Links to `/decision-record` (formalize the Decide step for high-stakes choices)
- Links to `/strategic-bet` (frame Act as a strategic bet when stakes are high)
- Links to `/experiment-design` (structure the Act phase as a formal experiment)
- Links to `/retrospective` (evaluate completed OODA cycles for learning)
- Links to `/competitive-landscape` (inform Observe phase with competitive data)
- Links to `/assumption-map` (track assumptions across OODA phases)
- Links to `/context-save` (persist cycle for future reference and cross-cycle learning)
