---
globs:
  - "**/*"
---

# Skill Awareness & Invocation

Invocation syntax and document intelligence modes. For routing decisions, see `delegate-first.md`. For V2V phase skills, see `Product Org OS/product-org-plugin/PRINCIPLES.md`.

---

## Invocation Syntax (MANDATORY)

| Notation | Tool | Purpose | Example |
|----------|------|---------|---------|
| `/skill-name` | Skill tool | Invoke template/workflow **inline** | `/prd`, `/decision-record` |
| `/pbaw <task>` | Task tool (via the harness) | Spawn the **canonical agents the harness selects** from the task and context — one agent, or a multi-agent run with one named synthesis owner | `/pbaw draft the Q3 strategic bet` |
| `/persona` | Inline | Adopt a persona in the conversation — no spawn, no Audit Block | `/cpo, what's the principle behind X?` |
| `@file.md` | Context | Include file contents in conversation | `@strategy.md` |

### Dual-Mode

| Mode | Syntax | Behavior |
|------|--------|----------|
| **Inline** | `/persona` (e.g. `/product-manager`) | Claude adopts persona, continues conversation |
| **Autonomous** | `/pbaw <task>` | The harness selects and spawns the agent via Task tool, returns when done |

---

## Automatic Routing (MANDATORY)

When the user types `/pbaw <task>` → **spawn immediately** (the harness selects the agents). When user uses `/skill` → **execute immediately**. Do NOT ask "would you like me to route this?"

**Question threshold**: ONLY ask when truly ambiguous, critical info missing, or user explicitly requested options.

---

## Document Intelligence

Document-generating skills support three modes:
- **CREATE**: Default — `/prd authentication`
- **UPDATE**: When using "update", "revise", or providing a path
- **FIND**: When using "find", "search", or "list"

---

## Operating Principle

> "Routing is invisible when done well. Users should feel like they're talking to a team that just gets things done."
