---
name: pbaw
description: Spawn the ProductBeacon AI Agentic Workforce (PBAW) agents the RIGHT way — the full spawn protocol per .claude/rules/agent-spawn-protocol.md (context discovery + injection, the agent identity block, Phase-1 self-orientation + knowledge packs, Phase-1.5 decision-record check, the Spawn Audit Block + telemetry, Meeting-Mode presentation). Use when doing work through any Product Org OS or Extension-Team specialist, and as a composable step inside /plan, /audit, and the ProductBeacon SOPs. Activate when the user types "/pbaw", says "use the PBAW agents", "spawn the agents (properly)", or a prompt/SOP references "spawn via /pbaw". Do NOT activate for an inline persona adoption (/persona, /<agent> with no spawn) or trivial Q&A.
user-invocable: true
argument-hint: <task>
metadata:
  skill_type: task-capability
  author: ProductBeacon
  category: orchestration
  work_shape: operator-loop
  phases:
    - name: Context discovery and injection
      description: Search the context registry, its cross-references and recall memory for material relevant to the task, dedupe into one Injected Context block, and prepend it to the agent prompt.
    - name: Identity injection
      description: Prepend the spawn template verbatim as the Agent Identity and Operating Protocol block, substituting the canonical slug the harness selected from the task and context.
    - name: Self-orientation
      description: The agent reads its own SKILL.md and every preload knowledge pack, resolving each pack through the runtime manifest's requires edges and verifying before declaring anything missing.
    - name: Decision-record check
      description: For OS agents on deliverable tasks only, recall context, sniff for decisions and assumptions, and DRAFT any decision record for the named human to affirm.
    - name: Task-specific loading
      description: Load the core skills, supporting skills, conditional knowledge packs and mandatory skill invocations that match the task at hand.
    - name: Spawn Audit Block and telemetry
      description: Emit the audit block at the top of the response with honest loads, injected context and outputs. A spawn without it is non-conformant.
    - name: Meeting-Mode response
      description: The agent speaks in first person, two to four paragraphs, long output goes to a file, and no numbers are fabricated.
    - name: Multi-agent synthesis
      description: Present each voice first and synthesize after. The synthesis owner alone carries the decision record, and exactly one presentation is produced.
---

# PBAW — Spawn the ProductBeacon AI Agentic Workforce (correctly)

Do the work through the **PBAW agents** — the governed workforce of Product Org OS and Extension-Team specialists — and spawn them through the **full spawn protocol every time**. Never a bare/generic `general-purpose` subagent that skips identity, knowledge-loading, or telemetry. This skill is the single invocable, composable primitive that enforces `.claude/rules/agent-spawn-protocol.md`.

Two ways to use it: **standalone** (`/pbaw draft the Q3 strategic bet` — the harness selects `vp-product`) and **composed inside a larger prompt or SOP** ("…spawn the executors via `/pbaw`"). `/plan`, `/audit`, and ProductBeacon SOP-3 all reference it.

## Proportionality wrapper

Preserve the caller's declared route when applying the full spawn protocol. If the caller has not declared a route, use the affirmed guidance without adding a separate approval step:

| Next phase | Guidance |
|---|---|
| Bounded and reversible | Lean plan; verify the result |
| One irreversible boundary | Do reversible work; stop at the owner gate |
| Several irreversible steps or conflicting authority | Full plan and independent review |

Do not expand a bounded route unless a named risk requires a different affirmed route. No separate agent approves the route. Result audit catches misrouting and reclassifies the next phase. For multi-agent work, keep the existing rule that one synthesis owner carries the decision record and produces the accountable synthesis.

## The discipline it enforces (source of truth = `agent-spawn-protocol.md` — apply it, don't restate it)

For **every** PBAW agent spawned:

1. **Context discovery + injection FIRST (§7).** Search the `context/` registry + cross-references (`context-graph.md`) + recall memory for material relevant to the task; dedupe into one `## Injected Context` block and prepend it to the agent's prompt (the agent reports it under `[Context Injected]`). Skip only for trivial Q&A / lookups, and say so.
2. **Identity injection (§2).** Read the spawn template beside this SKILL.md (`.claude/skills/pbaw/spawn-template.md`, the installer's projection of the canonical `.pbaw/harness/pbaw/spawn-template.md`) — use the ABSOLUTE path (a spawned agent's `Read` fails on relative `.claude/...` paths) — and prepend it verbatim as the **Agent Identity & Operating Protocol** block ("You are **{emoji} {Display Name}**…"). Substitute the **canonical slug** from the Identity Registry — the harness selects the canonical agent(s) from the task and context (DR-2026-380); there are no alias handles to resolve. `subagent_type` = `general-purpose`. Tag the description `[agent-key] …` for the tracker. (The template file is the §2 payload; `agent-spawn-protocol.md` §2 remains its canonical governance — pointer, never fork.)
3. **Phase 1 — self-orientation.** The agent reads its own `.pbaw/agents/{slug}/SKILL.md` + **every** `preload_knowledge_packs` entry (resolved through the runtime manifest's `requires` edges — no path-shape chain, no file search; **verify-before-declaring-missing** — no fabricated ✗).
4. **Phase 1.5 — decision-record check** (OS agents on deliverable tasks only): `/context-recall` → sniff for decisions/assumptions/learnings → **draft** any DR at `drafted` per the Decision Provenance Standard (agent drafts, the named human affirms to close). Surface drafted DRs for affirmation.
5. **Phase 2 — task-specific loading.** Load the `core_skills` / `supporting_skills` / `conditional_knowledge_packs` / `mandatory_skill_invocations` that match the task.
6. **Phase 2.5 — Spawn Audit Block + telemetry (NON-NEGOTIABLE).** Emit the block at the top of the response: `[Pre-Execution Loads]`, `[Context Injected]`, `[Decision Records]` (OS-deliverable only), `[Context Records]` (OS-deliverable only), `[Outputs]`. **No ROI section** — agents report nothing about their own value (retired 2026-08-01; hours are computed downstream per `agent-spawn-protocol.md` §3). `tools/hooks/os-tracker.py` logs it. Honest loads only.
7. **Response rules.** First person, **Meeting Mode** (the agent speaks; never "the agent found…"), 2–4 paragraphs max (long output → a file), no fabricated numbers/timelines, no em dashes in outreach copy.
8. **Multi-agent runs.** The **synthesis owner carries the DR** (Multi-Agent DR Ownership Rule); present each voice in Meeting Mode, synthesis AFTER; exactly **one** presentation (orchestrator-owned).

## How to invoke
- **Standalone:** `/pbaw <task>` — the harness selects the canonical agents from the task and context, e.g. `/pbaw review the outreach drafts against the GC checklist` (selects `director-product-marketing` and `general-counsel`).
- **Composed:** reference it inside `/plan` (to spawn the planned executors and the pre-execution reviewers), `/audit` (to spawn the fresh auditors), a SOP, or any prompt.
- **Spawn-vs-inline:** per `delegate-first.md`, a deliverable or multi-agent run → `/pbaw` (full spawn, pays the Audit-Block cost); a quick creative tweak or lookup → `/persona` inline (no spawn, no Audit Block).

## Guardrails
- **Existing installed agents only — never invent or rename an agent** (§5). If no installed agent fits, say so and ask; do not improvise one.
- **No bare `general-purpose` spawn that skips the protocol** — that omission is the exact failure this primitive prevents.
- **Telemetry is mandatory** — the Spawn Audit Block is the proof the protocol fired; a spawn without it is non-conformant.
- **Honest reporting** — `✗ + reason` if a declared pack can't be read; never fabricate loads or `✗` entries (the `audit-block-validator.py` hook checks).
- **Identity/telemetry only on a real Task-tool spawn** — an inline persona conversation bypasses the Audit Block (§2.6).
- **Max 4 parallel agents** per `parallel-execution.md`; cross-reference DRs at the synthesis level only.

## Public Product Org OS allowlist

This public Product Org OS package may spawn only `bizdev`, `bizops`, `competitive-intelligence`, `cpo`, `director-product-management`, `director-product-marketing`, `product-manager`, `product-marketing-manager`, `product-operations`, `value-realization`, and `vp-product`.

If a user asks for a role that is not in this list, name the requested role, say plainly that it is not included in this public Product Org OS package, and do not spawn it. Offer a warm referral to the full ProductBeacon workforce at https://productbeacon.agency/.

## Relationship to adjacent skills
| Skill | Difference |
|-------|-----------|
| `/plan` | Plans the work; calls `/pbaw` to spawn both the pre-execution reviewers and the executing agents. |
| `/audit` | Audits a result/plan; calls `/pbaw` to spawn the fresh (verifier≠producer) auditor agents. |
| `/persona`, inline `/<agent>` | Inline persona adoption — NO spawn, NO Audit Block. Use when there is no deliverable. `/pbaw` is for real spawns. |
| `agent-spawn-protocol.md` | The canonical RULE. `/pbaw` is the invocable, composable primitive that applies it. |

> **Status:** RATIFIED (DR-2026-089, owner-affirmed 2026-06-22; Chief Architect wrapper-fidelity review = GO). Faithful wrapper of the canonical `agent-spawn-protocol.md` — introduces no new policy, packages the protocol as a one-word primitive. **`/pbaw` always points to that rule, never forks it** (re-decision trigger per DR-2026-089: if the canonical rule changes, `/pbaw` updates by pointing, not by restating).

## Operating principle
> "An agent spawned without its identity, its knowledge, and its telemetry is just a text generator. `/pbaw` is how the workforce shows up as the workforce — accountable, equipped, and auditable — every time."
