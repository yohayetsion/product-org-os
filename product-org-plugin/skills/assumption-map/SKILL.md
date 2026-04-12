---
name: assumption-map
description: "/assumption-map"
user-invocable: true
metadata:
  skill_type: task-capability
  author: Product Org OS
---

# /assumption-map

Map and prioritize assumptions underlying a product decision, strategy, or bet.

## When to Use

- Before committing resources to a new initiative (Phase 2-3 transition)
- When a strategic bet has implicit assumptions that need surfacing
- After `/strategic-bet` to make assumptions explicit and testable
- During Phase 1 discovery to challenge founding hypotheses

## Vision to Value Phase

**Phase 1: Strategic Foundation** (also used at Phase 2-3 boundary)

## Gotchas

- Assumptions must be falsifiable — 'the market will grow' is too vague, 'TAM will exceed $1B by 2027 (source: X)' is testable
- High-risk assumptions (high impact, low certainty) must have validation plans

## Workflow

### Step 1: Identify the Decision/Bet

What decision, strategy, or bet are we mapping assumptions for?

### Step 2: Surface All Assumptions

Extract assumptions across these categories:

| Category | Question |
|----------|----------|
| **Customer** | Who is the target? Do they have this problem? Will they pay? |
| **Problem** | Is this a real problem? How painful is it? How do they solve it today? |
| **Solution** | Will our approach work? Can we build it? Will users adopt it? |
| **Market** | Is the market big enough? Is timing right? Can we reach them? |
| **Business** | Can we make money? Is the unit economics viable? Can we scale? |
| **Competitive** | Can we differentiate? Will competitors respond? Is the moat real? |

### Step 3: Score Each Assumption

For each assumption, assess:

| Dimension | Scale | Meaning |
|-----------|-------|---------|
| **Impact if wrong** | High / Medium / Low | How much damage if this assumption is false? |
| **Confidence level** | High / Medium / Low | How confident are we this is true? |
| **Evidence quality** | Strong / Weak / None | What evidence supports this? |

### Step 4: Prioritize (The Assumption Map)

Plot assumptions on a 2x2 matrix:

```
                    HIGH IMPACT IF WRONG
                    |
    VALIDATE FIRST  |  CRITICAL RISK
    (test quickly)  |  (must validate before committing)
                    |
   -----------------+------------------
                    |
    MONITOR         |  DOCUMENT
    (check later)   |  (acknowledge, move on)
                    |
                    LOW IMPACT IF WRONG

    HIGH CONFIDENCE -------- LOW CONFIDENCE
```

**Priority order**:
1. **Critical Risk** (low confidence + high impact) - Validate BEFORE committing
2. **Validate First** (high confidence + high impact) - Quick tests to confirm
3. **Monitor** (high confidence + low impact) - Track for changes
4. **Document** (low confidence + low impact) - Note and move on

### Step 5: Design Validation Plan

For each Critical Risk and Validate First assumption:
- **Test method**: How will you validate? (interview, prototype, data analysis, experiment)
- **Success criteria**: What result would confirm/deny this assumption?
- **Timeline**: When will you know? (days, weeks, months)
- **Owner**: Who is responsible for validating?

## Output Format

```markdown
# Assumption Map: [Decision/Bet Name]

**Decision**: [What we're deciding]
**Date**: [YYYY-MM-DD]
**Owner**: [Who owns this map]

## Assumptions Inventory

| # | Category | Assumption | Impact | Confidence | Evidence | Priority |
|---|----------|-----------|--------|------------|----------|----------|
| A-1 | Customer | [statement] | High | Low | None | Critical Risk |
| A-2 | Solution | [statement] | High | Medium | Weak | Validate First |
| ... | ... | ... | ... | ... | ... | ... |

## Priority Matrix

### Critical Risk (Validate Before Committing)
- **A-1**: [assumption] - Test: [method] by [date]

### Validate First (Quick Tests)
- **A-2**: [assumption] - Test: [method] by [date]

### Monitor
- [assumptions to track]

### Document (Acknowledged)
- [low-priority assumptions]

## Validation Plan

| # | Test Method | Success Criteria | Timeline | Owner |
|---|------------|-----------------|----------|-------|
| A-1 | [method] | [criteria] | [date] | [person] |
```

## Integration

- Links to `/strategic-bet` (assumptions feed into bet documentation)
- Links to `/context-save` (save validated/invalidated assumptions)
- Links to `/experiment-design` (design experiments for critical assumptions)
- Assumptions register: `context/assumptions/registry.md`

## Based On

- Itamar Gilad's Assumption Mapping framework
- Alberto Savoia's pretotyping methodology
- Lean Startup validation principles
