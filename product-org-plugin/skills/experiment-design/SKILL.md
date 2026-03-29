---
name: experiment-design
description: |
  Design a lean experiment to validate a specific assumption or hypothesis. Includes discovery maturity scoring.
  Activate when: "experiment", "test hypothesis", "validate assumption", "lean experiment", "experiment design", "discovery maturity", "A/B test design", "hypothesis testing"
  Do NOT activate for: A/B test implementation (/ab-test-setup), assumption mapping (/assumption-map), pre-mortem (/pre-mortem)
argument-hint: [hypothesis or assumption to test] or [update path/to/experiment.md]
user-invocable: true
metadata:
  author: Product Org OS
  version: 1.1.0
  category: discovery
compatibility: Requires Product Org OS v3+ context layer and rules
---

<!-- Source: Experiment Design — consolidated from Alberto Savoia "The Right It" (2019, HarperOne) pretotyping methodology, Lean Experiment Canvas, and Strategyzer's Test Card + Learning Card (Alex Osterwalder). -->

# /experiment-design

Design a lean experiment to validate a specific assumption or hypothesis. Includes discovery maturity scoring.

## Document Intelligence

This skill supports three modes: **Create**, **Update**, and **Find**.

### Mode Detection

| Signal | Mode | Confidence |
|--------|------|------------|
| "update", "revise", "modify" in input | UPDATE | 100% |
| File path provided (`@path/to/experiment.md`) | UPDATE | 100% |
| "create", "new", "design experiment" in input | CREATE | 100% |
| "find", "search", "list experiments" | FIND | 100% |
| "the experiment", "our hypothesis" | UPDATE | 85% |
| Just hypothesis or assumption text | CREATE | 60% |

**Threshold**: ≥85% auto-proceed | 70-84% state assumption | <70% ask user

### Mode Behaviors

**CREATE**: Generate complete new experiment design using template below.

**UPDATE**:
1. Read existing experiment doc (search if path not provided)
2. Preserve unchanged sections exactly
3. Update only sections mentioned by user (e.g., results, guard rails, success criteria)
4. Show diff summary: "Updated: [sections]. Unchanged: [sections]."
5. Update `last_modified` metadata

**FIND**:
1. Search paths below for experiment designs
2. Present results: title, path, date, hypothesis summary
3. Ask: "Update one of these, or create new?"

### Search Locations

- `experiment/`
- `experiments/`
- `discovery/`
- `product/experiments/`
- `product/discovery/`

---

## When to Use

- After `/assumption-map` identifies Critical Risk or Validate First assumptions
- Before committing significant resources to an initiative
- When stakeholders disagree and data could resolve it
- During Phase 1-2 to de-risk strategic bets

## Vision to Value Phase

**Phase 1-2: Strategic Foundation / Decisions**

## Gotchas

- Hypothesis must be falsifiable — 'users will like this' is not testable, 'signup rate will increase by 10%' is
- Sample size must be estimated before running — experiments without power analysis are coin flips
- Success criteria must be defined before the experiment, not after seeing results

## Workflow

### Step 1: Define the Hypothesis

Structure as a testable statement:

```
We believe [target users] will [expected behavior]
because [rationale].
We will know this is true when [measurable outcome]
within [timeframe].
```

### Step 2: Choose Experiment Type

| Type | Speed | Fidelity | Best For |
|------|-------|----------|----------|
| **Fake Door** | Days | Low | Demand validation ("would they click?") |
| **Concierge** | Days-Weeks | Medium | Process validation ("does the workflow work?") |
| **Wizard of Oz** | Weeks | Medium-High | Experience validation ("do they value it?") |
| **Smoke Test** | Days | Low | Market validation ("is there interest?") |
| **A/B Test** | Weeks | High | Optimization ("which approach wins?") |
| **Prototype Test** | Days-Weeks | Medium | Usability validation ("can they use it?") |
| **Survey/Interview** | Days | Low | Problem validation ("is this a real pain?") |
| **Data Analysis** | Hours-Days | Varies | Pattern validation ("does the data support this?") |

**Selection criteria**:
- How much confidence do you need? (Low -> survey, High -> A/B test)
- How much time do you have? (Hours -> data analysis, Weeks -> prototype)
- What are you testing? (Demand -> fake door, Usability -> prototype)

### Step 3: Design the Experiment

Define these elements:

| Element | Description |
|---------|-------------|
| **Hypothesis** | The testable statement from Step 1 |
| **Experiment type** | Selected from Step 2 |
| **Target audience** | Who participates? How many? |
| **Setup** | What needs to be built/configured? |
| **Duration** | How long will it run? |
| **Success metric** | Primary metric that determines pass/fail |
| **Threshold** | Specific number that means "validated" |
| **Fail criteria** | What result means "invalidated"? |
| **Data collection** | How will you capture results? |

### Step 4: Define Guard Rails

- **Minimum sample size**: How many data points needed for confidence?
- **Maximum investment**: Cap the time/money spent before stopping
- **Kill criteria**: What would cause you to stop early?
- **Bias checks**: How will you avoid confirmation bias?

### Step 5: Plan the Analysis

Before running, decide:
- What statistical method (if applicable)?
- Who reviews the results?
- What happens if results are inconclusive?
- What's the next step for each outcome (validated, invalidated, inconclusive)?

### Step 6: Assess Discovery Maturity

<!-- Source: Discovery Maturity Scoring — inspired by tomaszstaniak/pm-ai-skills discovery rubric. Adapted with 0-10 scale and level-up recommendations for Product Org OS. -->

Score the team's discovery practice maturity on a 0-10 rubric. This is not about the experiment itself but about the organization's overall discovery capability.

| Score | Level | Description |
|-------|-------|-------------|
| 0-1 | **No Discovery** | No experiments run. Ship and hope. |
| 2-3 | **Ad Hoc** | Occasional user conversations. No structured experiments. Decisions based on opinions. |
| 4-5 | **Emerging** | Some experiments run but inconsistently. Hypotheses sometimes documented. Results not always acted on. |
| 6-7 | **Structured** | Regular experiment cadence. Hypotheses well-formed. Success criteria defined upfront. Results feed decisions. |
| 8-9 | **Systematic** | Experiment backlog maintained. Discovery and delivery balanced. Assumption maps drive experiment priorities. Team reflexively tests before building. |
| 10 | **Continuous** | Discovery is culture, not process. Every decision has an evidence base. Experiments run at multiple fidelity levels simultaneously. Organization-wide learning loops. |

#### Assessment Questions

For each level, ask these diagnostic questions to determine the team's current score:

**No Discovery (0-1)**:
- Are any experiments being run at all?
- Is "let's just build it" the default response to uncertainty?

**Ad Hoc (2-3)**:
- Do experiments happen, but only when someone champions them?
- Are results shared informally (if at all)?
- Do user conversations happen but without a structured approach?

**Emerging (4-5)**:
- Are hypotheses written down before experiments start?
- Is there a mix of experiment types (not just surveys)?
- Are results sometimes ignored when they contradict the plan?

**Structured (6-7)**:
- Are success/fail criteria defined before experiments run?
- Do experiment results actually change roadmap decisions?
- Is there a regular cadence (e.g., weekly experiment reviews)?

**Systematic (8-9)**:
- Is there a prioritized backlog of assumptions to test?
- Does the team balance discovery and delivery capacity?
- Do `/assumption-map` outputs directly drive experiment priorities?

**Continuous (10)**:
- Does the organization run experiments at multiple fidelity levels simultaneously?
- Is evidence cited in every major product decision?
- Do teams across the organization share and build on each other's learnings?

#### Level-Up Recommendations

| Current Level | Recommendation to Level Up |
|---------------|---------------------------|
| **No Discovery (0-1)** | Start with one experiment per quarter. Use `/experiment-design` to structure it. Pick the riskiest assumption from your next initiative. |
| **Ad Hoc (2-3)** | Introduce `/assumption-map` to identify what to test. Document hypotheses before running experiments. Share results in a visible channel. |
| **Emerging (4-5)** | Define success criteria upfront for every experiment. Create a rule: no feature ships without at least one validated assumption. Review experiment results in sprint retros. |
| **Structured (6-7)** | Maintain an experiment backlog alongside the product backlog. Allocate a fixed percentage of capacity to discovery. Use `/context-save` to build organizational memory from results. |
| **Systematic (8-9)** | Run experiments at multiple fidelity levels (survey + prototype + A/B simultaneously). Build cross-team learning loops. Make discovery metrics part of team health dashboards. |
| **Continuous (10)** | Mentor other teams. Publish internal case studies. Contribute to industry knowledge. You are the benchmark. |

Include the discovery maturity score in the experiment design output (see Output Format below).

---

## Output Format

```markdown
# Experiment Design: [Name]

**Hypothesis**: We believe [users] will [behavior] because [rationale].
**Date**: [YYYY-MM-DD]
**Owner**: [Who runs this experiment]
**Related**: [A-N from assumption map, SB-YYYY-NNN, etc.]
**Discovery Maturity**: [Score]/10 — [Level Name]

## Design

| Element | Value |
|---------|-------|
| Type | [Experiment type] |
| Target | [Audience description] |
| Sample size | [N participants/data points] |
| Duration | [Timeframe] |
| Setup effort | [What needs building] |

## Success Criteria

| Metric | Threshold (Pass) | Fail | Inconclusive |
|--------|------------------|------|--------------|
| [Primary] | >= [X]% | < [Y]% | [Y-X]% range |
| [Secondary] | [criteria] | [criteria] | [range] |

## Guard Rails

- Max investment: [time/money cap]
- Kill criteria: [early stop conditions]
- Bias mitigation: [how you'll stay objective]

## Analysis Plan

- Method: [How results will be analyzed]
- Reviewer: [Who reviews besides the owner]
- Next steps per outcome:
  - Validated -> [action]
  - Invalidated -> [action]
  - Inconclusive -> [action]

## Results (fill after experiment)

- **Outcome**: [Validated / Invalidated / Inconclusive]
- **Key data**: [Summary of findings]
- **Decision**: [What we're doing based on results]
- **Learnings**: [What we learned beyond the hypothesis]
```

## Integration

- Feeds from `/assumption-map` (validates critical assumptions)
- Results feed into `/context-save` (organizational learning)
- Links to `/strategic-bet` (de-risks bets)
- Links to `/outcome-review` (post-experiment analysis)

## Based On

- Alberto Savoia's "The Right It" pretotyping methodology
- Lean Experiment Canvas
- Strategyzer's Test Card + Learning Card
