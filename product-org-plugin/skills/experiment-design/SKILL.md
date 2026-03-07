# /experiment-design

Design a lean experiment to validate a specific assumption or hypothesis.

## When to Use

- After `/assumption-map` identifies Critical Risk or Validate First assumptions
- Before committing significant resources to an initiative
- When stakeholders disagree and data could resolve it
- During Phase 1-2 to de-risk strategic bets

## V2V Phase

**Phase 1-2: Strategic Foundation / Decisions**

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

## Output Format

```markdown
# Experiment Design: [Name]

**Hypothesis**: We believe [users] will [behavior] because [rationale].
**Date**: [YYYY-MM-DD]
**Owner**: [Who runs this experiment]
**Related**: [A-N from assumption map, SB-YYYY-NNN, etc.]

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
