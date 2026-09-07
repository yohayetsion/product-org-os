---
globs:
  - "**/*"
---

# Parallel Agent Execution

Enables parallel spawning of agents for efficient cross-functional work.

## When to Parallelize

**DO parallelize when:**
- Gathering inputs from multiple functions
- Analyses don't depend on each other's output
- Time-sensitive decisions need fast input collection

**DON'T parallelize when:**
- Outputs are dependencies
- Coordination is required
- Sequence matters (Vision to Value phase order)

## Common Parallel Patterns

| Use Case | Agents | Synthesizer | Approx. Tier-1 cost (v2 strict mode) |
|----------|--------|-------------|-------|
| Portfolio Review | `bizops`, `competitive-intelligence`, `value-realization`, `product-operations` | `cpo` or `vp-product` (portfolio roster, `agent-spawn-protocol.md` §6) | ~80-100k |
| Launch Decision | `product-manager`, `product-marketing-manager`, `product-operations` | `director-product-management` | ~50-70k |
| Strategic Planning | `competitive-intelligence`, `bizops`, `value-realization` | `vp-product` | ~50-70k |
| GTM Preparation | `product-marketing-manager`, `bizdev`, `sales-enablement` (skill) | `director-product-marketing` | ~50-70k |
| Customer Review | `value-realization`, `user-researcher`, `product-manager` | `vp-product` | ~50-70k |
| Brand Launch (Marketing) | `director-product-marketing`, `marketing-dir`, `pr-comms-specialist`, `growth-marketer` | `cmo` | ~80-100k |

**Cost note (v2 spawn protocol, 2026-05-27)**: With `lightweight_spawn` removed, every agent in a parallel pattern pays full Tier-1. The synthesizer ALSO pays full Tier-1 for its synthesis spawn. Plan parallel patterns with this token budget in mind. For low-stakes coordination across multiple specialists, consider sequential `/persona` invocations (no Audit Block, no spawn cost) instead.

**Synthesis owner carries DRs** in multi-agent runs (per `agent-spawn-protocol.md` Multi-Agent DR Ownership Rule). Sub-agents do NOT each emit a `[Decision Records]` section. Sub-agents MAY surface candidate DRs verbally in their individual responses for the synthesizer to commit.

## Delegation-Enhanced Parallel Patterns

Combine parallel execution with delegation patterns for complex cross-functional work:

| Use Case | Pattern | Agents | Example |
|----------|---------|--------|---------|
| PRD with specialist sections | Delegation | `product-manager` owns, delegates to `competitive-intelligence`, `user-researcher` | PM delegates competitive + research sections |
| Pre-commitment validation | Review | `director-product-management`, `vp-product` review in parallel | Both review the roadmap simultaneously |
| GTM motion decision | Debate | `bizops` vs `director-product-marketing` | Structured debate on PLG vs SLG |
| Launch readiness | Consultation | `product-operations` consults `product-manager`, `product-marketing-manager`, `tech-lead` | Quick status check from all functions |

When combining patterns, the delegating/reviewing agent is responsible for synthesis and presenting the unified result.

## How to Invoke

Use multiple Task tool calls in a single message:

```
Spawning parallel agents:
[Task: bizops - Financial analysis for Q2]
[Task: competitive-intelligence - Competitive update for Q2]
[Task: value-realization - Customer outcomes for Q2]
```

Each agent receives the same context and works independently.

## Presentation

**See `agent-spawn-protocol.md` Section 10 for presentation requirements.**

Key points:
- Show each agent's response with attribution
- Agents speak in first person
- Synthesis comes AFTER individual voices

## Guardrails

- **Max parallel agents**: 4
- **Context sharing**: All receive `/handoff`, `/portfolio-status`, `/context-recall` context, plus the `## Injected Context` block from the orchestrator's §7 Context Discovery (`agent-spawn-protocol.md`), which each parallel agent reports in its `[Context Injected]` Audit Block section
- **Conflict resolution**: Document disagreements, identify root cause, escalate if needed

## Vision to Value Operating Principle

> "Parallel execution is about comprehensive input, not speed. Speed is a side effect of good design."
