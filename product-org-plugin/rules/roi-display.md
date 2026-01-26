# ROI Display (MANDATORY)

This rule governs how time-savings are displayed after skill and agent completions.

---

## The Principle

Every skill and agent invocation saves time compared to **manual product management work**. Making this visible helps users understand the leverage they're getting from the Product Org OS.

**CRITICAL**: The Product Org OS helps with PRODUCT WORK - strategy, decisions, requirements, GTM, analysis, documentation, etc. ROI comparisons should ALWAYS reference the manual PM/product equivalent, NEVER software development or coding effort.

---

## Display Requirements

### Compact Single-Line Format (DEFAULT)

Display ROI on a single line after skill or agent completion:

```markdown
⏱️ ~[X] min saved (vs. [brief manual equivalent])
```

**Examples (Product Work):**
- `⏱️ ~4 hrs saved (vs. manual PRD writing + stakeholder reviews)`
- `⏱️ ~2 hrs saved (vs. conducting competitive analysis manually)`
- `⏱️ ~90 min saved (vs. documenting decision + aligning stakeholders)`
- `⏱️ ~45 min saved (vs. gathering context from past decisions)`

**NEVER frame as:**
- "vs. coding this feature" (wrong - we don't code)
- "vs. implementing manually" (wrong - we don't implement)
- "vs. building this" (wrong - we don't build software)

### When to Show
- After agent spawning (Task tool) produces planning, insights, or deliverables
- After skill execution that creates or updates documents
- After PLT or gateway sessions that produce recommendations

### When NOT to Show
- Simple lookups or context retrieval (`/context-recall`, `/feedback-recall`)
- Failed operations
- System operations (setup, indexing)
- Pure read operations with no synthesis

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

## Examples (Always Reference Product Work)

### Simple User Story
```markdown
⏱️ ~20 min saved (vs. writing story + acceptance criteria manually)
```

### Complex PRD
```markdown
⏱️ ~6 hrs saved (vs. gathering requirements + stakeholder interviews + documentation)
```

### PLT Meeting Session
```markdown
⏱️ ~10 hrs saved (vs. scheduling + running cross-functional alignment meeting)
```

### Agent Spawning (PM Review)
```markdown
⏱️ ~90 min saved (vs. manual competitive research + synthesis)
```

### Decision Record
```markdown
⏱️ ~60 min saved (vs. documenting decision + gathering stakeholder input)
```

### Context Retrieval
```markdown
⏱️ ~30 min saved (vs. searching through past decisions manually)
```

---

## Session Totals (Optional)

For longer sessions, you may optionally add session totals after the standard line:

```markdown
⏱️ ~90 min saved (vs. market research + analysis)
📈 Session total: ~4.5 hrs saved
```

Only add session totals when:
- Session has 5+ skill/agent interactions
- User has requested session tracking
- Using `/roi-report` skill

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
