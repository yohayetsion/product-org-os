---
name: opportunity-tree
description: /opportunity-tree
user-invocable: true
metadata:
  skill_type: task-capability
  author: Product Org OS
  owner: pm
  primary_consumers:
  - pm
  secondary_consumers:
  - bizdev
  - user-researcher
  - growth-marketer
---
# /opportunity-tree

Build an Opportunity Solution Tree to map the path from desired outcome to testable solutions.

## When to Use

- At the start of discovery (Phase 1) to structure exploration
- When you have a desired outcome but many possible approaches
- To align a team on what opportunities to pursue
- Before jumping to solutions, to ensure you're solving the right problems

## Vision to Value Phase

**Phase 1: Strategic Foundation**

## Workflow

### Step 1: Define the Desired Outcome

A clear, measurable business or product outcome:

```
Outcome: [Specific measurable result]
Metric: [How we measure it]
Current: [Where we are today]
Target: [Where we want to be]
Timeframe: [By when]
```

Good outcomes are specific and measurable, not vague aspirations.

### Step 2: Discover Opportunities

Opportunities are unmet needs, pain points, or desires expressed by customers. They come from:

| Source | Method |
|--------|--------|
| Customer interviews | "What's hardest about...?" |
| Support tickets | Recurring themes |
| Usage data | Drop-off points, underused features |
| Feedback | `/feedback-recall` for existing signals |
| Competitive gaps | What competitors solve that we don't |
| Market research | Emerging needs, shifting expectations |

**Rules for good opportunities**:
- Stated from the customer's perspective
- Not solutions disguised as problems
- Specific enough to act on
- Supported by evidence (not assumed)

### Step 3: Structure the Tree

```
DESIRED OUTCOME
|
+-- Opportunity 1 (customer need/pain)
|   +-- Solution A
|   |   +-- Experiment 1
|   |   +-- Experiment 2
|   +-- Solution B
|       +-- Experiment 3
|
+-- Opportunity 2 (customer need/pain)
|   +-- Solution C
|   |   +-- Experiment 4
|   +-- Solution D
|       +-- Experiment 5
|
+-- Opportunity 3 (customer need/pain)
    +-- Solution E
        +-- Experiment 6
```

**At each level**:
- **Outcome -> Opportunities**: What customer needs, if addressed, would drive this outcome?
- **Opportunities -> Solutions**: What are multiple ways we could address this need?
- **Solutions -> Experiments**: How could we test if this solution works?

### Step 4: Assess and Prioritize Opportunities

For each opportunity:

| Dimension | Question |
|-----------|----------|
| **Opportunity size** | How many customers have this need? |
| **Market factors** | Is this need growing? Any urgency? |
| **Company factors** | Are we positioned to address this? Do we have capabilities? |
| **Customer factors** | How painful is this? How important to them? |

Select 1-3 opportunities to pursue (not all of them).

### Step 5: Generate Multiple Solutions

For each selected opportunity, brainstorm 3+ solutions:
- At least one simple/cheap solution
- At least one ambitious solution
- Consider solutions from adjacent industries

**Anti-pattern**: Jumping to the first solution. Force breadth before depth.

### Step 6: Design Experiments

For the most promising solutions, design small experiments (link to `/experiment-design`).

## Output Format

```markdown
# Opportunity Solution Tree: [Outcome Name]

**Desired Outcome**: [Measurable outcome]
**Metric**: [Measurement] | **Current**: [X] | **Target**: [Y] | **By**: [Date]
**Owner**: [Name]
**Date**: [YYYY-MM-DD]

## Tree

### Outcome: [Statement]

#### Opportunity 1: [Customer need]
**Evidence**: [Source and strength]
**Size**: [Large/Medium/Small]
**Priority**: [Selected / Deferred / Rejected]

- **Solution 1a**: [Description]
  - Experiment: [Quick test]
- **Solution 1b**: [Description]
  - Experiment: [Quick test]

#### Opportunity 2: [Customer need]
**Evidence**: [Source and strength]
**Size**: [Large/Medium/Small]
**Priority**: [Selected / Deferred / Rejected]

- **Solution 2a**: [Description]
  - Experiment: [Quick test]

## Selected Path

**Pursuing**: Opportunity [N] via Solution [Na]
**First experiment**: [Description]
**Decision date**: [When we'll evaluate results]

## Deferred Opportunities

| Opportunity | Reason Deferred | Revisit Trigger |
|-------------|----------------|-----------------|
| [Name] | [Why not now] | [What would change this] |
```

## Integration

- Feeds from customer research, `/feedback-recall`, `/market-analysis`
- Outputs feed into `/assumption-map` (assumptions behind selected path)
- Solutions feed into `/experiment-design` (validation)
- Selected path feeds into `/prd` or `/strategic-bet`

## Based On

- Teresa Torres' "Continuous Discovery Habits" (Opportunity Solution Tree)
- Marty Cagan's discovery principles
- Dual-track agile (discovery + delivery)
