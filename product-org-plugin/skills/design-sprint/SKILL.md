---
name: design-sprint
description: "Plan and facilitate a Google Ventures-style 5-day Design Sprint to answer critical business questions through design, prototyping, and customer testing. Activate when: \"design sprint\", \"GV sprint\", \"5-day sprint\", \"sprint week\", \"Google Ventures sprint\", \"rapid prototyping sprint\", \"Jake Knapp\", \"sprint plan\", \"design sprint planning\" Do NOT activate for: Scrum sprint planning, agile sprint (/pmtk-scrum-backlog), brainstorming (/brainstorming), experiment design (/experiment-design)"
argument-hint: "[challenge or problem to sprint on] or [update path/to/design-sprint.md]"
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
| "update", "revise", "adjust sprint" in input | UPDATE | 100% |
| File path provided (`@path/to/design-sprint.md`) | UPDATE | 100% |
| "create", "new", "plan sprint", "run sprint" in input | CREATE | 100% |
| "find", "search", "list sprints" | FIND | 100% |
| "the sprint", "our design sprint" | UPDATE | 85% |
| Just a problem statement | CREATE | 60% |

**Threshold**: >=85% auto-proceed | 70-84% state assumption | <70% ask user

### Mode Behaviors

**CREATE**: Define the sprint challenge, identify the team, plan the 5-day schedule, design the prototype strategy, and prepare the customer test plan.

**UPDATE**:
1. Read existing sprint plan (search if path not provided)
2. Preserve completed days and decisions
3. Update remaining days, adjust based on findings
4. Show diff summary: "Updated: [sections]. Completed: [days]. Remaining: [days]."

**FIND**:
1. Search paths below for design sprint documents
2. Present results: challenge, date, status, path
3. Ask: "Update one of these, or create new?"

### Search Locations

- `product/`
- `design/`
- `sprints/`
- `planning/`

---
## Gotchas

- A Design Sprint is NOT a Scrum sprint -- it is a 5-day structured process for answering one critical question, not a development iteration
- The Decider must be available all 5 days -- without clear decision authority, Day 3 stalls and the sprint fails
- Customer interviews on Day 5 must be scheduled BEFORE the sprint starts -- recruiting takes time and cannot be a last-minute scramble
- The prototype must be a realistic facade, not a working product -- spending Day 4 building real code defeats the purpose

## Vision to Value Phase

**Phase 3: Strategic Commitments** - Design Sprints convert strategic decisions into testable prototypes before committing full development resources. They sit at the boundary between decision and commitment, de-risking before the point of no return.

**Prerequisites**: Phase 2 complete (strategic direction decided, specific challenge identified), target customer access secured for Day 5
**Outputs used by**: `/prd` (validated concepts become requirements), `/feature-spec` (prototype insights inform specifications), `/commitment-check` (sprint results inform go/no-go)

## Methodology

<!-- Source: Design Sprint -- Jake Knapp, John Zeratsky, and Braden Kowitz, "Sprint: How to Solve Big Problems and Test New Ideas in Just Five Days" (2016, Simon & Schuster). Developed at Google Ventures (GV). Knapp developed the process while at Google. -->

<!-- Source: Design Sprint 2.0 -- AJ&Smart adaptation that compresses the sprint into 4 days (merging Day 1-2 into one day). -->

<!-- Source: Inspired by wdavidturner/product-skills design-sprint skill. Adapted with full day-by-day protocol, remote adaptations, and integration with V2V methodology. -->

### When to Use a Design Sprint

| Good Fit | Poor Fit |
|----------|----------|
| High-stakes decision with significant uncertainty | Problem is well-understood with clear solution |
| Cross-functional alignment needed | Single-discipline task (just engineering, just design) |
| Customer validation would de-risk investment | Already committed -- no room to change direction |
| Team is stuck or going in circles | Incremental improvement on existing feature |
| New market, new product, or major pivot | Routine bug fix or optimization |

### Sprint Team

| Role | Count | Responsibility |
|------|-------|---------------|
| **Facilitator** | 1 | Runs the process, manages time, keeps team on track |
| **Decider** | 1 | Makes final calls (usually CEO, VP, or product lead) |
| **Team members** | 4-5 | Cross-functional: PM, designer, engineer, domain expert, customer-facing role |
| **Max total** | 7 | More than 7 people slows everything down |

### Prerequisites Checklist

- [ ] Clear challenge statement defined
- [ ] Decider identified and committed for all 5 days
- [ ] Sprint team assembled (5-7 people, cross-functional)
- [ ] Room booked for full week (whiteboards, sticky notes, markers)
- [ ] 5 customer interviews scheduled for Friday (Day 5)
- [ ] No phones/laptops policy communicated (except for reference)
- [ ] Expert interviews scheduled for Monday afternoon (2-3 experts)

### Day 1: Map (Monday)

**Goal**: Create a shared understanding of the problem and pick a target for the sprint.

| Time | Activity | Output |
|------|----------|--------|
| 10:00-10:30 | **Set the long-term goal** -- Where do we want to be in 6 months/1 year/2 years? | Long-term goal statement |
| 10:30-11:00 | **List sprint questions** -- What questions must we answer? What could cause failure? | Sprint question list |
| 11:00-12:00 | **Make a map** -- Draw the customer journey from discovery to key goal (simplified) | Journey map on whiteboard |
| 13:00-14:30 | **Ask the Experts** -- Interview 2-3 domain experts (15-30 min each). Team takes HMW notes. | "How Might We" sticky notes |
| 14:30-15:00 | **Organize HMW notes** -- Affinity cluster and dot vote | Prioritized HMW themes |
| 15:00-15:30 | **Pick a target** -- Decider chooses which customer and which moment on the map to focus the sprint on | Sprint target (circled on map) |

**Key artifacts**: Long-term goal, sprint questions, customer map, HMW clusters, target

### Day 2: Sketch (Tuesday)

**Goal**: Generate a range of solution ideas, culminating in detailed individual solution sketches.

| Time | Activity | Output |
|------|----------|--------|
| 10:00-11:00 | **Lightning Demos** -- Each team member presents inspiring solutions from other products (3 min each) | Inspiration board |
| 11:00-11:30 | **Divide or Swarm** -- If the target is large, assign parts to individuals | Assignment map |
| 11:30-12:00 | **Step 1: Notes** -- Individual review of all info gathered; jot key ideas | Personal notes |
| 13:00-13:20 | **Step 2: Ideas** -- Rough solution ideas, one per sticky note | Idea collection |
| 13:20-13:40 | **Step 3: Crazy 8s** -- Fold paper into 8 panels, sketch 8 variations in 8 minutes | 8 rapid sketches per person |
| 14:00-16:00 | **Step 4: Solution Sketch** -- Each person creates a detailed 3-panel storyboard of their best solution | Solution sketches (anonymous) |

**Critical rule**: Solution sketches are anonymous. No names on sketches. Ideas stand on their own merit.

### Day 3: Decide (Wednesday)

**Goal**: Choose the best solution(s) and create a storyboard for prototyping.

| Time | Activity | Output |
|------|----------|--------|
| 10:00-10:30 | **Art Museum** -- Post all solution sketches on the wall; silent review | Sketches displayed |
| 10:30-11:00 | **Heat Map** -- Everyone places dot stickers on interesting parts of sketches | Heat map of popular ideas |
| 11:00-11:45 | **Speed Critique** -- 3 min per sketch: narrator describes, team discusses, creator reveals | Critique notes per sketch |
| 11:45-12:00 | **Straw Poll** -- Each person votes for one sketch | Vote tally |
| 12:00-12:15 | **Supervote** -- Decider gets 3 special votes; Decider's choice wins | Winning solution(s) |
| 13:00-14:00 | **Rumble or All-in-One** -- If conflicting winners, decide: test both (Rumble) or merge (All-in-One) | Decision on approach |
| 14:00-16:00 | **Storyboard** -- Draw a step-by-step storyboard (10-15 frames) of the prototype experience | Prototype storyboard |

**Decider authority**: The Decider's supervote is final. This is not a democracy -- it is a benevolent dictatorship for speed.

### Day 4: Prototype (Thursday)

**Goal**: Build a realistic facade that customers can interact with on Day 5.

**The Goldilocks Quality Principle**: The prototype must be just enough to feel real -- not too polished (wastes time), not too rough (customers can't react naturally).

| Role | Responsibility |
|------|---------------|
| **Makers** (2) | Build the prototype screens/pages |
| **Stitcher** (1) | Connect screens into a realistic flow |
| **Writer** (1) | Write all copy (realistic, not lorem ipsum) |
| **Asset Collector** (1) | Find images, icons, example data |
| **Interviewer** (1) | Prepare Day 5 interview script and practice |

**Prototype tools**: Figma, Keynote/PowerPoint, HTML/CSS, paper (for physical products). Whatever is fastest.

**End-of-day test**: One team member who was NOT a maker does a dry run through the prototype. Fix anything confusing.

### Day 5: Test (Friday)

**Goal**: Put the prototype in front of 5 real customers and identify patterns.

| Time | Activity | Notes |
|------|----------|-------|
| 9:00-9:30 | Setup | Interviewer + prototype in one room; team watching live stream in another |
| 9:30-10:30 | **Interview 1** | Team takes notes on sticky notes (green = positive, red = negative, yellow = neutral) |
| 10:30-11:30 | **Interview 2** | Same process |
| 11:30-12:30 | **Interview 3** | Pattern recognition usually starts here |
| 13:30-14:30 | **Interview 4** | Confirms or challenges emerging patterns |
| 14:30-15:30 | **Interview 5** | Final data point |
| 15:30-16:30 | **Pattern identification** | Team reviews all notes; look for patterns across 5 interviews |

**Why 5 interviews**: Jakob Nielsen's research shows 5 users uncover ~85% of usability problems. Beyond 5, diminishing returns.

**Interview script structure**:
1. Warm-up (5 min) -- Background, context, rapport
2. Context questions (5 min) -- Current behavior related to the problem
3. Prototype introduction (2 min) -- "This is an early concept. There are no wrong answers."
4. Task walkthrough (30 min) -- Observe; ask "What are you thinking?" not "Do you like it?"
5. Debrief (5 min) -- Overall reaction, willingness to use/pay

### Sprint Outcomes

| Pattern | Meaning | Next Step |
|---------|---------|-----------|
| 5/5 positive | Strong signal -- concept validated | Move to `/prd` and build |
| 3-4/5 positive | Promising with refinements needed | Iterate on weak points, consider another sprint |
| 2/5 positive | Mixed signal -- concept needs rethinking | Analyze what worked; pivot the approach |
| 0-1/5 positive | Concept invalidated | Valuable learning -- you saved months of wrong-direction building |

**All outcomes are good outcomes.** A failed sprint that prevents 6 months of wrong development is a massive success.

### Remote Sprint Adaptations

<!-- Source: Design Sprint 2.0 -- AJ&Smart adaptation that compresses the sprint into 4 days (merging Day 1-2 into one day). -->

| In-Person Element | Remote Equivalent |
|-------------------|-------------------|
| Whiteboard + sticky notes | Miro, FigJam, or MURAL |
| Dot voting on wall | Digital voting in collaboration tool |
| Physical prototype | Figma/InVision prototype |
| Live-stream interview | Zoom with screen share; team in separate call |
| Room for the week | Recurring video call with camera-on policy |

**Remote-specific rules**:
- Camera on at all times (engagement drops without visual accountability)
- Shorter sessions: split days into 2-hour blocks with breaks
- Async sketching: share sketches in a shared folder before Day 3
- Facilitator must actively manage energy and participation

## Output Structure

```markdown
# Design Sprint Plan: [Challenge Name]

**Date**: [YYYY-MM-DD]
**Owner**: [Sprint Facilitator]
**Decider**: [Name and Role]
**Sprint Dates**: [Monday date] - [Friday date]
**Format**: [In-person / Remote / Hybrid]

## The Challenge

**Long-term goal**: [Where do we want to be?]
**Sprint question**: [The critical question this sprint will answer]
**Target customer**: [Who are we testing with?]
**Target moment**: [Which part of the journey are we focusing on?]

## Sprint Team

| Role | Name | Function | Availability |
|------|------|----------|-------------|
| Facilitator | [Name] | [Role] | All 5 days |
| Decider | [Name] | [Role] | All 5 days |
| Member | [Name] | [Role] | All 5 days |
| Member | [Name] | [Role] | All 5 days |
| Member | [Name] | [Role] | All 5 days |

## Prerequisites Checklist

- [ ] Challenge statement reviewed by Decider
- [ ] Sprint team confirmed (max 7)
- [ ] Room/space booked for full week
- [ ] Expert interviews scheduled for Day 1 (names: [])
- [ ] 5 customer interviews scheduled for Day 5 (recruitment via: [])
- [ ] Supplies ready (whiteboards, sticky notes, markers, dot stickers, timer)
- [ ] Prototype tools selected: []
- [ ] No-devices policy communicated

## Day-by-Day Schedule

### Day 1: Map (Monday)
[Detailed schedule with times, activities, and expected outputs]

### Day 2: Sketch (Tuesday)
[Detailed schedule]

### Day 3: Decide (Wednesday)
[Detailed schedule]

### Day 4: Prototype (Thursday)
[Role assignments and prototype plan]

### Day 5: Test (Friday)
[Interview schedule with participant IDs and observation plan]

## Interview Script Outline

1. **Warm-up** (5 min): [Key background questions]
2. **Context** (5 min): [Current behavior questions]
3. **Prototype tasks** (30 min): [Specific tasks to observe]
4. **Debrief** (5 min): [Closing questions]

## Success Criteria

| Signal | Meaning | Action |
|--------|---------|--------|
| [What we'd see if concept is validated] | Go | [Next step] |
| [What we'd see if partially validated] | Iterate | [Next step] |
| [What we'd see if invalidated] | Pivot | [Next step] |

## Sprint Results (Complete After Day 5)

### Patterns Observed

| Pattern | Positive/Negative/Neutral | Frequency (out of 5) | Impact |
|---------|--------------------------|----------------------|--------|
| [Pattern] | [+/-/~] | [N/5] | [High/Med/Low] |

### Key Learnings
1. [Learning]
2. [Learning]
3. [Learning]

### Decision
[Go / Iterate / Pivot] -- [Rationale]

### Next Steps
- [ ] [Action item with owner and deadline]
- [ ] [Action item with owner and deadline]
```

## Instructions

1. Start by understanding the challenge: What critical question needs answering? What is the risk of building without testing?
2. Help the user define the long-term goal and sprint question -- these anchor the entire week
3. Identify the Decider early -- if no one can commit to the role, flag this as a blocker
4. Stress the Day 5 interview scheduling prerequisite -- this is the most common sprint-killer
5. For remote sprints, recommend the Design Sprint 2.0 compressed format and appropriate digital tools
6. The prototype strategy should match the challenge: digital product = Figma; physical product = paper/foam; service = role-play scenario
7. Do not fabricate interview results or predict outcomes -- the entire point is learning what you do not know
8. Save output as markdown file
9. After the sprint, offer `/prd` to convert validated concepts into requirements or `/assumption-map` to track remaining uncertainties

## Integration

- Links to `/prd` (validated sprint concepts become product requirements)
- Links to `/feature-spec` (prototype insights inform detailed specifications)
- Links to `/commitment-check` (sprint results inform go/no-go on resource commitment)
- Links to `/experiment-design` (sprint learnings may require follow-up experiments)
- Links to `/assumption-map` (track which assumptions were validated/invalidated by the sprint)
- Links to `/user-story` (customer interview insights feed user story creation)
- Links to `/context-save` (save sprint results as organizational learning)
- Links to `/retrospective` (post-sprint retrospective on the process itself)

## Vision to Value Operating Principle

> "A Design Sprint compresses months of debate into one week of focused action. The goal is not a perfect prototype -- it is a fast, cheap answer to a critical question before you commit resources you cannot get back."
