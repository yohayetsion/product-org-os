---
name: theory-of-constraints
description: 'Apply Goldratt''s Theory of Constraints (TOC) to identify and eliminate the system''s bottleneck using the 5 Focusing Steps. Activate when: "theory of constraints", "TOC", "bottleneck analysis",
  "constraint", "Goldratt", "five focusing steps", "throughput", "drum buffer rope", "system constraint" Do NOT activate for: general process optimization, product operations (/prodops agent), lean methodology,
  six sigma'
argument-hint: '[system, process, or workflow to analyze] or [update path/to/toc-analysis.md]'
user-invocable: true
metadata:
  author: Product Org OS
  version: 1.0.0
  category: operations
  skill_type: task-capability
  owner: coo
  primary_consumers:
  - prodops
  - coo
  - operations-dir
  - process-engineer
  secondary_consumers:
  - program-manager
---
## Document Intelligence

This skill supports three modes: **Create**, **Update**, and **Find**.

### Mode Detection

| Signal | Mode | Confidence |
|--------|------|------------|
| "update", "revise", "reassess" in input | UPDATE | 100% |
| File path provided (`@path/to/toc-analysis.md`) | UPDATE | 100% |
| "create", "new", "find the bottleneck" in input | CREATE | 100% |
| "find", "search", "list TOC" | FIND | 100% |
| "the constraint", "our bottleneck" | UPDATE | 85% |
| Just a process or system name | CREATE | 60% |

**Threshold**: >=85% auto-proceed | 70-84% state assumption | <70% ask user

### Mode Behaviors

**CREATE**: Walk through all 5 Focusing Steps for the identified system, produce a complete constraint analysis with throughput accounting and action plan.

**UPDATE**:
1. Read existing TOC analysis (search if path not provided)
2. Check if constraint has moved (Step 5: Repeat)
3. Update exploitation/subordination/elevation strategies
4. Show diff summary: "Constraint status: [same/moved]. Updated: [sections]. New constraint: [if moved]."

**FIND**:
1. Search paths below for TOC analysis documents
2. Present results: system, constraint identified, date, path
3. Ask: "Update one of these, or create new?"

### Search Locations

- `operations/`
- `process/`
- `product/`
- `analysis/`

---
## Gotchas

- There is only ONE constraint at a time — if you identify multiple, you haven't found the real one yet. The constraint is whatever limits the system's throughput the most RIGHT NOW.
- Exploit BEFORE Elevate — most organizations jump to buying more capacity (Step 4) before maximizing what they already have (Step 2). Exploitation is cheaper and faster.
- Subordination is the hardest step — it means deliberately sub-optimizing non-constraint resources, which feels wrong to managers who want everything running at 100%.
- After elevating the constraint, it WILL move — always plan for Step 5. The new constraint is often in a completely unexpected place.

## Vision to Value Phase

**Phase 4: Coordinated Execution** - TOC is most valuable during execution to identify and remove delivery bottlenecks. Also applicable in Phase 3 (process design) when designing workflows to prevent constraints.

**Prerequisites**: A defined system or process with measurable throughput, visibility into where work queues or stalls
**Outputs used by**: `/product-roadmap` (constraint-aware planning), `/launch-readiness` (constraint removal before launch), `/retrospective` (learning from constraint resolution), `/scale-check` (system scaling decisions)

## Methodology

<!-- Source: Theory of Constraints — Eliyahu M. Goldratt, "The Goal: A Process of Ongoing Improvement" (1984, North River Press). Goldratt was an Israeli physicist who applied physical science thinking to business management. "The Goal" is written as a novel (Socratic method) and has sold over 6 million copies. -->

<!-- Source: Five Focusing Steps and Throughput Accounting — Goldratt, "The Theory of Constraints" (1990, North River Press) and subsequent works including "It's Not Luck" (1994) and "Critical Chain" (1997, applying TOC to project management). -->

<!-- Source: Drum-Buffer-Rope — Goldratt's production scheduling methodology from "The Goal". Applied to software development by David J. Anderson and others in the Kanban/Lean community. -->

### The 5 Focusing Steps

The core of TOC is relentlessly simple: find the bottleneck, fix it, repeat.

#### Step 1: IDENTIFY the Constraint
Find the single resource, process, policy, or capability that limits the system's throughput:
- Where does work pile up? Where are the queues longest?
- Which resource is always at 100% utilization while others wait?
- What do people most frequently complain about waiting for?
- Types of constraints: physical (capacity), policy (rules/approvals), market (demand), material (inputs), knowledge (expertise)

#### Step 2: EXPLOIT the Constraint
Maximize the output of the bottleneck with CURRENT resources — no new investment:
- Eliminate waste at the constraint (no idle time, no rework)
- Ensure the constraint only works on highest-value items
- Remove any non-essential tasks from the constraint
- Buffer the constraint's input so it never starves
- Quality-check BEFORE the constraint (don't waste constraint capacity on defective inputs)

#### Step 3: SUBORDINATE Everything Else
Align all non-constraint processes to serve the constraint:
- Non-constraints should produce at the constraint's pace, NOT at their maximum capacity
- Excess capacity at non-constraints is EXPECTED and GOOD (this is counter-intuitive)
- Do NOT optimize non-constraints independently — local optimization hurts global throughput
- Policies, metrics, and incentives must align with the constraint's needs

#### Step 4: ELEVATE the Constraint
If exploitation and subordination are insufficient, invest to increase the constraint's capacity:
- Add resources, hire, buy equipment, outsource
- Redesign the process to bypass the constraint
- Automate the constraint's work
- This costs money — which is why Steps 2-3 come first

#### Step 5: REPEAT (Prevent Inertia)
Once the constraint is broken, it moves. Go back to Step 1:
- The new constraint is often somewhere unexpected
- WARNING: Do not let inertia become the new constraint — the policies and processes built around the OLD constraint must be updated
- Goldratt's warning: "Do not allow inertia to cause a system's constraint"

### Throughput Accounting

TOC replaces traditional cost accounting with three measures:
- **Throughput (T)**: Rate at which the system generates money (revenue minus truly variable costs)
- **Investment (I)**: Money tied up in the system (inventory, equipment, buildings)
- **Operating Expense (OE)**: Money spent to turn I into T (salaries, rent, utilities)
- **Goal**: Maximize T while minimizing I and OE
- **Decision rule**: Any change that increases T, decreases I, or decreases OE without negatively impacting the others is beneficial

### Drum-Buffer-Rope (DBR)

A scheduling methodology derived from TOC:
- **Drum**: The constraint sets the pace for the entire system (the "drumbeat")
- **Buffer**: A time buffer placed BEFORE the constraint to protect it from upstream variation
- **Rope**: A signal from the constraint back to the start of the process, limiting the release of new work (WIP limiting)

In product development: the Drum is typically the constraint team/process, the Buffer is a prioritized backlog sized to protect the constraint, and the Rope is the intake process that limits how much new work enters the system.

### Evaporating Cloud (Conflict Resolution)

When requirements appear to conflict: (1) Define the shared objective, (2) Identify the two conflicting requirements, (3) Surface underlying ASSUMPTIONS behind each, (4) Challenge assumptions — at least one is flawed, and breaking it resolves the conflict.

### Product Development Constraints (Common)

| Common Constraint | Symptoms | Typical Exploitation |
|------------------|----------|---------------------|
| Design capacity | Long design queues, engineering idle | Prioritize ruthlessly, design systems, self-service templates |
| QA throughput | Release backlog, testing bottleneck | Shift-left testing, automation, quality gate before constraint |
| Decision-making speed | Approval queues, stakeholder delays | Pre-approve categories, decision frameworks, delegation |
| Specialized expertise | Single expert bottleneck, knowledge silos | Document expertise, pair programming, cross-train |

## Output Structure

```markdown
# Theory of Constraints Analysis: [System / Process / Workflow]

**Date**: [YYYY-MM-DD]
**Owner**: [Who owns this analysis]
**System Boundary**: [What is included in this system]
**Throughput Metric**: [What does "throughput" mean for this system?]
**Context**: [Why this analysis is needed now]

## System Overview

[Brief description of the system, its purpose, and its current performance]

### System Flow

[Describe or diagram the flow of work through the system — identify each stage/resource]

| Stage | Resource/Team | Capacity | Utilization | Queue Size |
|-------|--------------|----------|-------------|------------|
| [Stage 1] | [Resource] | [Units/time] | [%] | [Items waiting] |
| [Stage 2] | [Resource] | [Units/time] | [%] | [Items waiting] |
| [Stage 3] | [Resource] | [Units/time] | [%] | [Items waiting] |
| [Stage 4] | [Resource] | [Units/time] | [%] | [Items waiting] |
| [Stage 5] | [Resource] | [Units/time] | [%] | [Items waiting] |

## Step 1: IDENTIFY the Constraint

**The constraint is**: [Specific resource, process, policy, or capability]

**Evidence**:
- [Evidence 1: queue data, utilization, wait times]
- [Evidence 2: what people complain about waiting for]
- [Evidence 3: where work piles up]

**Constraint type**: Physical / Policy / Market / Material / Knowledge

**Why this is THE constraint (not just A bottleneck)**:
[Explain why this specific element limits the ENTIRE system's throughput more than any other]

## Step 2: EXPLOIT the Constraint

*Maximize output with current resources — zero new investment.*

| # | Exploitation Action | Expected Impact | Effort |
|---|-------------------|----------------|--------|
| 1 | [Action] | [Impact on throughput] | Low/Med/High |
| 2 | [Action] | [Impact on throughput] | Low/Med/High |
| 3 | [Action] | [Impact on throughput] | Low/Med/High |
| 4 | [Action] | [Impact on throughput] | Low/Med/High |

**Current waste at constraint**: [What non-value-adding work does the constraint currently do?]
**Quality gate before constraint**: [How do we prevent defective inputs from wasting constraint capacity?]

## Step 3: SUBORDINATE Everything Else

*Align non-constraints to serve the constraint's needs.*

| Non-Constraint | Current Behavior | Required Change | Impact on Local Metrics |
|---------------|-----------------|-----------------|------------------------|
| [Stage/Resource] | [What it does now] | [What it should do] | [Expected metric change] |
| [Stage/Resource] | [What it does now] | [What it should do] | [Expected metric change] |
| [Stage/Resource] | [What it does now] | [What it should do] | [Expected metric change] |

**Policies to change**: [Existing policies that optimize non-constraints at the expense of the constraint]
**Metrics to realign**: [Local metrics that incentivize the wrong behavior]
**Expected resistance**: [Who will resist subordination and why?]

## Step 4: ELEVATE the Constraint

*If Steps 2-3 are insufficient, invest to increase capacity.*

| # | Elevation Option | Cost | Throughput Gain | ROI |
|---|-----------------|------|-----------------|-----|
| 1 | [Option] | [TBD] | [Expected gain] | [TBD] |
| 2 | [Option] | [TBD] | [Expected gain] | [TBD] |
| 3 | [Option] | [TBD] | [Expected gain] | [TBD] |

**Recommendation**: [Which elevation option, if any, and why Steps 2-3 are not sufficient]

## Step 5: REPEAT — Where Will the Constraint Move?

**Predicted new constraint**: [Where will the bottleneck shift after current constraint is resolved?]
**Evidence for prediction**: [Why do you expect it to move there?]
**Inertia risk**: [What policies/processes built around the current constraint might become the new constraint?]

## Throughput Accounting

| Measure | Current | After Exploit (Step 2) | After Elevate (Step 4) |
|---------|---------|----------------------|----------------------|
| Throughput (T) | [Current rate] | [Expected] | [Expected] |
| Investment (I) | [Current] | [Same] | [New investment] |
| Operating Expense (OE) | [Current] | [Same] | [New expense] |

## Drum-Buffer-Rope

**Drum**: [Constraint] at [rate] | **Buffer**: [Amount] before constraint | **Rope**: [Intake mechanism] limits WIP to [number]

## Assumptions

| # | Assumption | Step | Confidence | If Wrong |
|---|-----------|------|------------|----------|
| 1 | [Assumption] | 1/2/3/4/5 | High/Med/Low | [Impact] |
| 2 | [Assumption] | 1/2/3/4/5 | High/Med/Low | [Impact] |

## Next Steps

- [ ] Implement exploitation actions (Step 2) immediately
- [ ] Communicate subordination changes to affected teams (Step 3)
- [ ] Monitor throughput metric and schedule re-identification in [timeframe]
- [ ] Use `/retrospective` to evaluate impact after one cycle
```

## Instructions

1. Clarify the system boundary and throughput metric with the user
2. **Check prior context**: Run `/context-recall [topic]` to find related process analyses or bottleneck discussions
3. Map the system flow — identify every stage and resource
4. Use data to identify the constraint: queue sizes, utilization rates, wait times. Do NOT guess — ask for data.
5. Work through Steps 2-3 THOROUGHLY before considering Step 4. Most teams jump straight to "hire more people" — challenge this.
6. In Step 3, explicitly identify who will resist subordination and why (local metrics, status, habit)
7. In Step 5, always predict where the constraint will move — a TOC analysis without Step 5 is incomplete
8. Save output as markdown file
9. Offer to track throughput improvements via `/outcome-review` or feed into `/product-roadmap` for constraint-aware planning

## Integration

- Links to `/product-roadmap` (constraint-aware capacity planning)
- Links to `/launch-readiness` (identify and resolve constraints before launch)
- Links to `/scale-check` (evaluate system scalability through constraint lens)
- Links to `/retrospective` (evaluate constraint resolution effectiveness)
- Links to `/outcome-review` (track throughput improvements over time)
- Links to `/collaboration-check` (subordination requires cross-team alignment)
- Links to `/context-save` (persist constraint analysis for future reference and re-identification)
