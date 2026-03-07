# /compound

Extract and save learnings from completed tasks to build compound organizational intelligence.

## When to Use

- After completing a significant task or deliverable
- After a project milestone or sprint
- When something went wrong (or unexpectedly right)
- Periodically as a reflection habit (weekly/monthly)

## V2V Phase

**Phase 6: Learning & Adaptation** (but usable after any phase)

## Workflow

### Step 1: Extract

Reflect on the completed work:

| Question | Purpose |
|----------|---------|
| What was the task? | Clear scope |
| What was the outcome? | Actual result |
| What worked well? | Repeat these |
| What didn't work? | Avoid these |
| What surprised us? | New insights |
| What took longer than expected? | Estimation calibration |

### Step 2: Root Cause

For things that didn't work or surprised:
- **Why** did this happen? (5 Whys if needed)
- Was it a **process** issue, **knowledge** gap, **tool** problem, or **assumption** error?
- Was it preventable with information we had at the time?

### Step 3: Generalize

Turn specific observations into reusable principles:

| Specific | Generalized Learning |
|----------|---------------------|
| "The API changed and broke our integration" | "External API dependencies need health monitoring" |
| "The customer interview revealed a need we hadn't considered" | "Always include open-ended questions in discovery interviews" |
| "Estimating this feature took 3x longer than planned" | "Features touching 3+ system boundaries need 2x estimation buffer" |

### Step 4: Save

Save each learning to `context/learnings/` using `/context-save`:

```markdown
# L-NNN: [Learning Title]

**Date**: [YYYY-MM-DD]
**Source**: [Task/project that generated this]
**Category**: [Process | Technical | Customer | Market | Team | Tool]
**Confidence**: [High | Medium | Low] (proven once vs multiple times)

## Learning
[1-2 sentence generalized principle]

## Evidence
[What specifically happened that taught us this]

## Application
[When should someone recall this learning]

## Related
[Links to decisions, bets, or other learnings]
```

### Step 5: Index

Update the learnings index so future `/context-recall` and `/relevant-learnings` can find them:
- Add to `context/learnings/index.md`
- Update topic tags in `context/index.json`
- Cross-reference to related decisions/bets if applicable

## Triggers

### Manual (user-initiated)
- "Let's do a compound learning extraction"
- "What did we learn from [project]?"
- After `/retrospective` or `/outcome-review`

### Suggested (agent-initiated)
After completing significant work, agents should offer:
> "Want me to extract learnings from this work? (`/compound`)"

### Periodic
- End of week: Quick scan of the week's work
- End of project phase: Deeper extraction
- After failures or surprises: Immediate extraction

## Output Format

```markdown
# Compound Learning: [Context/Project]

**Date**: [YYYY-MM-DD]
**Scope**: [What work this covers]

## Learnings Extracted

### L-NNN: [Title]
**Category**: [category]
**Learning**: [principle]
**Evidence**: [what happened]
**Application**: [when to recall]

### L-NNN+1: [Title]
...

## Updated Indexes
- Added [N] learnings to `context/learnings/index.md`
- Cross-referenced to: [list of related IDs]

## Prevention Measures
- [Concrete changes to prevent recurring issues]
- [Process adjustments recommended]
```

## Integration

- Feeds from: `/retrospective`, `/outcome-review`, `/decision-quality-audit`
- Outputs to: `context/learnings/`, `context/index.json`
- Retrieved by: `/context-recall`, `/relevant-learnings`
- Cross-references: decisions, bets, assumptions

## Based On

- Compound learning principle: each learning makes the next task better
- Double-loop learning (Argyris): not just fixing errors but questioning the reasoning
- Blameless post-mortems (SRE culture)
