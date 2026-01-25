# ROI Display (MANDATORY)

This rule governs how time-savings are displayed after skill and agent completions.

---

## The Principle

Every skill and agent invocation saves time compared to manual equivalent work. Making this visible helps users understand the leverage they're getting from the Product Org OS.

---

## Display Requirements

### After EVERY Skill Completion

Display the ROI block at the end of the skill output:

```markdown
---
⏱️ **Time saved**: ~[X] minutes
📊 Manual equivalent: [brief description]
📈 This session: ~[Y] hours saved ([N] interactions)
---
```

### After EVERY Agent Completion

Same format, adjusted for agent context:

```markdown
---
⏱️ **Time saved**: ~[X] minutes
📊 Task: [what the agent did]
📈 This session: ~[Y] hours saved ([N] interactions)
---
```

---

## Calculation Method

### Step 1: Identify Base Time
Look up the skill/agent in `reference/roi-baselines.md`

### Step 2: Assess Complexity
Determine complexity factor based on:
- **Simple (0.5×)**: Short prompt, single topic, straightforward request
- **Standard (1.0×)**: Typical request, moderate detail
- **Complex (1.5×)**: Multiple topics, significant context, stakeholder considerations
- **Enterprise (2.0×)**: Strategic, cross-functional, multi-phase

### Step 3: Calculate
```
Estimated Savings = Base Time × Complexity Factor
```

### Step 4: Update Session Total
Add to running session total for cumulative display.

---

## Examples

### Simple User Story
```markdown
---
⏱️ **Time saved**: ~10 minutes
📊 Manual equivalent: Writing story + acceptance criteria
📈 This session: ~0.5 hours saved (3 interactions)
---
```

### Complex PRD
```markdown
---
⏱️ **Time saved**: ~360 minutes (6 hours)
📊 Manual equivalent: Requirements research + documentation + stakeholder alignment
📈 This session: ~8.5 hours saved (12 interactions)
---
```

### PLT Meeting Session
```markdown
---
⏱️ **Time saved**: ~600 minutes (10 hours)
📊 Task: Cross-functional portfolio tradeoff with 5 perspectives synthesized
📈 This session: ~14 hours saved (8 interactions)
---
```

---

## Quiet Mode

Users can request minimal display by including "quiet" or "minimal" in their prompt:

**Quiet format** (single line):
```markdown
⏱️ ~120 min saved | Session: ~4.5 hrs
```

---

## Session Tracking

### What Gets Tracked
- Each skill invocation (skill name, complexity, time saved)
- Each agent invocation (agent name, task type, time saved)
- Session start time
- Cumulative totals

### Where It's Stored
Session data logged to `context/roi/session-log.md` (ephemeral, per-session)

### Format
```markdown
## Session: [Date] [Time]

| Time | Type | Name | Complexity | Minutes Saved |
|------|------|------|------------|---------------|
| 09:15 | skill | /prd | complex | 360 |
| 09:32 | agent | @pm | standard | 90 |
| 10:05 | skill | /user-story | simple | 10 |

**Session Total**: 460 minutes (~7.7 hours)
```

---

## Monthly Aggregation

At session end, update `context/roi/history/[YYYY-MM].md` with:
- Date
- Session duration
- Total minutes saved
- Top skills used
- Skill count

This enables `/roi-report` to show 30/90 day summaries.

---

## Enforcement

### MUST Display
- After completing any `/skill` invocation
- After completing any `@agent` task
- After `@plt` or `@product` gateway completions

### MAY Skip
- Context retrieval skills (`/context-recall`, `/feedback-recall`, `/relevant-learnings`)
- Pure assessment skills with no deliverable (`/phase-check`)
- When user explicitly requests no ROI display

### NEVER Display
- During streaming/progress output
- For failed/cancelled operations
- For system operations (setup, indexing)

---

## Accuracy Notes

1. **Conservative estimates**: Better to underestimate than overclaim
2. **Complexity is approximate**: Use judgment, not precise rules
3. **Value varies**: Experienced users may be faster at manual equivalents
4. **Focus on trend**: Individual estimates matter less than cumulative pattern

---

## V2V Operating Principle

> "What gets measured gets managed. Tracking time savings makes the value of AI-assisted product work visible and improvable."
