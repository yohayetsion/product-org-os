---
name: tour
description: Interactive walkthrough of Product Org OS - gateways, agents, skills, and context layer
argument-hint: (no arguments needed)
model: haiku
tools:
  - Read
  - Glob
---

# Product Org OS Tour

Interactive 5-step walkthrough that teaches the system's architecture through hands-on exploration with demo data.

## V2V Phase

**Cross-phase** - Onboarding and education skill.

## When to Use

- First-time users exploring capabilities
- Returning users wanting a refresher
- Demonstrating the system to colleagues
- After running `/reset-demo` to explore restored content

## Prerequisites

- Context layer should exist (`context/` folder)
- Demo data recommended (run `/reset-demo` if cleared)

## Process

### 1. Check Prerequisites

Verify context layer exists:
- If `context/` folder missing: Suggest running `/setup` first
- If `context/demo/` empty: Note that demo data is missing, suggest `/reset-demo`
- Otherwise: Proceed with tour

### 2. Welcome

```markdown
## 🎓 Product Org OS Tour

Welcome! This 5-step walkthrough teaches the system's architecture:

**Gateway → Agent → Skill → Document → Utility**

Each step introduces a concept. You'll try a command and see the result before continuing.

---

Let's start with **Step 1: Gateways**...
```

### 3. Step 1: Gateways (Entry Points)

```markdown
## 🚪 Step 1: Gateways (Entry Points)

Product Org OS has two main entry points that route requests to the right experts:

| Gateway | What It Does |
|---------|--------------|
| `@product` | Routes to relevant owners, coordinates execution |
| `@plt` (Product Leadership Team) | Gets multi-perspective input on decisions |

**Try this with the demo data:**
```
@plt Based on our enterprise strategy and customer feedback,
should we prioritize the dashboard redesign or API improvements?
```

This will spawn multiple agents who weigh in with their perspectives.
```

*Wait for user to run the command, then continue to Step 2...*

---

### 4. Step 2: Individual Agents

```markdown
## 👤 Step 2: Individual Agents (Expert Perspectives)

Beyond gateways, you can invoke specific agents directly for their expertise:

| Agent | Focus |
|-------|-------|
| `@pm` | Requirements, delivery, user stories |
| `@vp-product` | Strategy, portfolio, pricing |
| `@pmm` | Positioning, GTM, competitive |

**Try this:**
```
@pm Review the dashboard PRD and identify any gaps in the requirements.
```

The PM agent will analyze the demo PRD and give their perspective.
```

*Wait for user to run the command, then continue to Step 3...*

---

### 5. Step 3: Skills (Deliverable Creation)

```markdown
## 🛠️ Step 3: Skills (Deliverable Creation)

Skills create production-ready deliverables following proven frameworks:

| Skill | Creates |
|-------|---------|
| `/prd` | Product Requirements Document |
| `/decision-record` | Structured decision with rationale |
| `/strategic-bet` | Bet with explicit assumptions |
| `/launch-plan` | Complete launch playbook |

**Try this:**
```
/decision-record Should we add webhook support to the API?
```

This creates a structured decision record you can fill in.
```

*Wait for user to run the command, then continue to Step 4...*

---

### 6. Step 4: Document Updates

```markdown
## 📝 Step 4: Document Updates (Agent + Existing Doc)

Agents can work with existing documents in your codebase—not just create new ones.

**Try this:**
```
@pm Update the dashboard PRD to add acceptance criteria for the filtering feature.
```

The PM will read the existing PRD and add to it.
```

*Wait for user to run the command, then continue to Step 5...*

---

### 7. Step 5: Utility Skills (Context Layer)

```markdown
## 🔧 Step 5: Utility Skills (Context Layer)

The context layer stores decisions, feedback, and learnings—organizational memory:

| Skill | Purpose |
|-------|---------|
| `/context-recall [topic]` | Find related decisions/context |
| `/feedback-recall [topic]` | Query customer feedback |
| `/portfolio-status` | View active strategic bets |
| `/clear-demo` | Remove demo data for production |

**Try this:**
```
/context-recall pricing
```

This shows how past decisions on pricing are retrieved.
```

*Wait for user to run the command, then show completion...*

---

### 8. Completion

```markdown
## 🎉 Tour Complete!

You've seen the core patterns:

✓ **Gateways** for multi-perspective input (`@product`, `@plt`)
✓ **Agents** for expert perspectives (`@pm`, `@vp-product`)
✓ **Skills** for deliverable creation (`/prd`, `/decision-record`)
✓ **Document updates** with agents
✓ **Context layer** for organizational memory

---

### What's Next?

| Goal | Command |
|------|---------|
| Start using skills on YOUR product | `/prd [topic]` |
| Keep demo as reference | Demo content coexists with your work |
| Go production-ready | `/clear-demo` removes sample data |
| Run tour again | `/tour` |

**Quick reference:** See `reference/v2v-skill-map.md`
```

## Instructions

1. Check prerequisites (context layer, demo data)
2. Present each step one at a time
3. Wait for user to try the command before proceeding
4. Provide brief context on what they'll see
5. End with completion summary and next steps

## Notes

- Tour can be run multiple times
- Works best with demo data present
- Each step builds on previous concepts
- Users can exit anytime and resume later
