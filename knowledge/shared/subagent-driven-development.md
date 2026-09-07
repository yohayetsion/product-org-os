---
pack: subagent-driven-development
consumers:
- tech-lead
- backend-dev
- frontend-dev
- devops
---
# Sub-agent Driven Development (V2V Knowledge Pack)

**Adapted from**:
  - obra/superpowers methodology (github.com/obra/superpowers, public OSS pattern, 226k (as of 2026-06-12) stars 2026)
  - Claude Code dynamic workflows (Anthropic, research preview 2026-05-28, Opus 4.8; code.claude.com/docs/en/workflows) — supersedes the earlier Agent Teams / Swarm Mode framing (Opus 4.6, Feb 2026), which is now partially stale
  - 2026 sub-agent dev landscape (Cursor, Aider, Cline, GitHub Copilot Workspace, Devin)
**Source licence**: per-source-terms (obra/superpowers MIT; Anthropic publicly-documented patterns; other vendors per their public docs)
**V2V refinements**:
- Translated obra/superpowers from a personal workflow to product-organization adoption guidance — the WHY of each discipline, not the literal checklist
- Held the boundary between sub-agent driven *development* (writes code) and agent-driven *product-org work* (this V2V repo's pattern) — they're related but different programming models
- Added 2026 landscape comparison (Cursor, Aider, Claude Code, Cline, Devin, Copilot Workspace) at the practice level, not the marketing level
- Anti-patterns specific to product orgs: engineering-as-prompt-engineering, abandoned-handoff, "agent did it" attribution risk, framework-mandated-TDD skipping, over-orchestration
- V2V Phase mapping (Intent → Learning) for where sub-agent dev fits cleanly vs forces
- **2026-06 delta**: added Claude Code dynamic workflows (2026-05-28, Opus 4.8) as a distinct, newer orchestration pattern superseding the Swarm-Mode framing, plus the Opus 4.8 self-written-code-flaw currency note

---

## What Sub-agent Driven Development Is

Sub-agent driven development is a programming model where a human engineer orchestrates one or more LLM sub-agents that write code, edit files, run tests, and review work — and the engineer's primary leverage shifts from typing to deciding. The engineer still owns intent, architecture, code review, and merge; the sub-agent absorbs the keystroke layer and a growing slice of the routine-decision layer.

The 2026 inflection point is that agent orchestration crossed from research demo to de facto practice. Tools that existed as proofs of concept in 2024-2025 (Devin, early Aider, GitHub Copilot Workspace previews) are now in daily use alongside Claude Code, Cursor agent mode, and Cline. The obra/superpowers methodology (226k (as of 2026-06-12) GitHub stars by Q2 2026) became the most-cited opinionated workflow on top of Claude Code, and its disciplines — `/skills` + `/commands` separation, mandatory TDD, two-stage review, conversational planning — are showing up as the default playbook across teams.

This is distinct from agent-driven *product-org work* (the pattern this V2V repo embodies, where agents represent organizational roles producing strategy, GTM, and decision artifacts). Sub-agent driven dev writes shipping code; product-org agents write decisions and artifacts. The underlying orchestration mechanics are similar; the failure modes, governance, and accountability shape are different.

## The 2026 Landscape

| Tool | Position | Notable patterns |
|---|---|---|
| Claude Code + obra/superpowers | Workflow-defined, opinionated | `/skills` + `/commands`, TDD-mandatory, two-stage review, conversational planning |
| Cursor Agent | IDE-native, low-orchestration | Composer mode, multi-file edits, lighter test discipline, fast inner loop |
| Aider | CLI-native, conversation-driven | Git-aware, repo-map context, minimalist, pair-programming feel |
| Cline | VSCode extension, low-friction | Plan/act split, tool-use focus, transparent action log |
| Devin | Autonomous, long-running | Async agent, planner+executor split, browser + shell, asynchronous PRs |
| GitHub Copilot Workspace | GitHub-native | Issue → spec → plan → PR pipeline, GitHub identity + repo permissions baked in |
| Claude Code dynamic workflows | Script-orchestrated, context-isolated | Claude writes a JS orchestration script that fans work across subagents (max 16 concurrent, 1,000 total/execution); the script holds the loop/branches, only the final answer returns to the calling context. Research preview 2026-05-28, Opus 4.8, requires Claude Code v2.1.154+. Supersedes the earlier Swarm-Mode framing. See the 2026-06 Delta Update. |

The category splits along two axes: how much orchestration the tool imposes (Claude Code high, Cursor low), and how synchronous the loop is (Cursor/Aider/Cline tight; Devin/Copilot Workspace async). No single tool dominates; teams mix them, often using Cursor for tight-loop edits and Claude Code for opinionated workflows that need TDD discipline.

## The obra/superpowers Pattern (most adopted in 2026)

**`/skills` and `/commands` discipline.** Skills are reusable, named capabilities (a how-to). Commands are workflows that compose skills (a what-to-do). The separation matters because it makes the agent's behavior auditable: when something goes wrong, you debug the skill or the command, not "the agent." Skills travel between projects; commands are project-specific. This is the same architectural intuition that makes V2V's own SKILL.md layer work.

**Mandatory TDD.** Write the test first; let the agent implement against it. The framework's claim is not that TDD is morally better — it's that tests are the only scaffolding a sub-agent can verify itself against without human round-trip. Without tests, "done" is whatever the agent says is done. With tests, "done" is green CI. The discipline survives sub-agent driven dev because the failure mode without it (agent-confident-but-wrong code) is the dominant cost in 2026.

**Two-stage code review.** The sub-agent reviews its own output first against a checklist (style, test coverage, edge cases, the original spec). The human reviews second, focusing on architectural fit, security implications, and whether the change actually solves the original problem. The first stage isn't theater — it catches roughly the same class of issues a junior engineer's self-review catches, which lets human review time go to higher-leverage questions.

**Conversational planning.** Plan-mode before act-mode. For non-trivial work, the agent produces a written plan, the human approves or revises, and only then does code change. The plan becomes the spec the agent verifies against. Skipping plan-mode for "small" changes is the most common discipline failure in 2026 teams adopting this pattern; the cost of a wrong-direction implementation almost always exceeds the cost of a five-minute plan.

## V2V Phase Mapping

| V2V Phase | Sub-agent dev application |
|---|---|
| Intent | Not a fit — intent setting is a human-judgment activity; sub-agents executing here produce plausible-but-misaligned scope |
| Decisions | Bounded fit — sub-agent OK for research and option-comparison drafts; the decision itself stays human |
| Commitments | Strong fit — spec authoring, PRD scaffolding, acceptance-criteria drafting all benefit from sub-agent first draft + human refinement |
| Execution | Native habitat — code writing, test authoring, refactor work, migration scripting. Where the 10x leverage shows up |
| Outcomes | Strong fit — telemetry instrumentation, dashboard scaffolding, retro analysis from logs |
| Learning | Mixed — pattern extraction OK; the *judgment* about which patterns matter stays human-curated |

The phases that feel forced are Intent and Learning's judgment layer. The phases that fit cleanly are Commitments, Execution, and Outcomes. Decisions is the interesting middle: sub-agents are excellent at the research and option-laying-out work, but a sub-agent making the call risks accountability washing (Anti-Patterns, below).

## Adoption Guidance for Product Orgs

Adoption decisions differ at three scales.

**Individual engineer.** The bar is low: pick one tool, internalize plan-mode and TDD discipline, accept that the first month will feel slower because of the new workflow. After ~6 weeks the leverage compounds — the engineer is shipping more, with better tests, with cleaner commit history. Friction stays high on legacy codebases where the agent's context window can't hold the relevant slice.

**Team.** Two new decisions appear. First, tool standardization: a team where half uses Cursor and half uses Claude Code has different code-review cultures, different test discipline, different commit shapes. Pick one default; allow exceptions with documented reasons. Second, review-load redistribution: sub-agent driven dev produces more PRs per engineer; review capacity becomes the constraint. Either invest in review tooling or accept that throughput is review-bound, not authoring-bound.

**Org-wide.** Three additional decisions. First, identity and access — sub-agents acting on behalf of engineers need scoped credentials (production-prod separation, secret rotation, audit logs that survive the sub-agent's session). Second, accountability — who owns code the sub-agent wrote when it breaks production? The answer is always "the human who merged it," but that has to be policy, not assumption. Third, training — the gap between engineers who internalize plan-mode + TDD and those who treat the agent as autocomplete becomes the dominant performance variance within ~3 quarters; structured training closes the gap faster than informal osmosis.

## Anti-Patterns / Common Failures

- **Engineering-as-prompt-engineering.** Engineer's fundamentals atrophy because they no longer hand-write the routine code. Six months in, the engineer can't debug what the agent produced because they don't fluently read the patterns the agent emits. Fix: keep doing routine code work by hand periodically; treat agent output as code you would have written, not code you delegated away.
- **Abandoned-handoff.** Sub-agent produces output (a PR, a draft, a refactor proposal); no human picks it up and owns it. The artifact rots in a branch. Fix: every sub-agent output has a named human owner before the agent is allowed to produce the next one; queue depth is bounded.
- **"Agent did it" attribution risk.** When a sub-agent-authored change ships a bug or a security issue, accountability washing is the natural temptation. "The agent wrote it" is not a defense; the human who reviewed and merged owns the outcome. Fix: codify in team norms that sub-agent authorship is invisible to accountability — the merging human owns it the same way they own their own keystrokes.
- **TDD-skipping despite framework mandate.** Team adopts obra/superpowers, declares TDD mandatory, then quietly skips it for "small" changes. Six weeks later, the small changes are 60% of the codebase and have no tests. Fix: enforce in CI (no green without tests touching the changed lines), not in culture alone.
- **Over-orchestration.** Team spawns three sub-agents in parallel for a task one engineer could have done in 20 minutes. Coordination overhead exceeds the work value; reconciliation of conflicting agent outputs takes longer than serial execution would have. Fix: parallelize only when sub-tasks are genuinely independent and the work value exceeds 1-2 engineer-hours per stream.
- **Sub-agent-as-decision-maker.** Sub-agent produces a recommendation; team treats the recommendation as the decision. The human decision step gets compressed to "yes, sounds right." Fix: require an explicit human-rationale paragraph for any decision a sub-agent recommended — surfaces whether the human actually evaluated or rubber-stamped.

## 2026-06 Delta Update (as of 2026-06-06)

**Claude Code "dynamic workflows" (2026-05-28, Opus 4.8) — a distinct, newer orchestration pattern.** This supersedes the earlier "Claude Code Agent Teams / Swarm Mode (Opus 4.6)" framing referenced in older versions of this pack. Swarm Mode is now partially stale; dynamic workflows are the current mechanism.

- **Shipped as a research preview 2026-05-28** alongside **Opus 4.8**; requires **Claude Code v2.1.154+**.
- **Mechanism**: Claude writes a **JavaScript orchestration script** that fans work across subagents. Concurrency limits are **max 16 concurrent subagents** and **1,000 total subagents per execution**.
- **The architecturally novel property — context isolation via the script.** The orchestration **script** (not the model's context window) holds the loop, the branches, and the intermediate results. Only the **final answer** returns to the calling context. This is the key difference from prior fan-out patterns where every subagent result flowed back through (and bloated) the caller's context. Moving the control flow into a script lets the orchestration scale to thousands of subagents without the calling context paying the token tax for intermediate state.
- **Proof point**: Jarred Sumner ported Bun from Zig to Rust — ~750k LOC, 99.8% test pass rate, in ~11 days — using this pattern.
- **Currency note on the underlying model**: Opus 4.8 (2026-05-28) reports being **~4× less likely than Opus 4.7 to let flaws in its own self-written code pass**. This is a model-quality improvement, not a structural change to the methodology, but it raises the floor on the "agent-confident-but-wrong code" failure mode that the mandatory-TDD discipline (above) exists to catch.

**How this fits the existing pack.** Dynamic workflows are an orchestration *mechanism* for the same programming model this pack describes — the human still owns intent, architecture, review, and merge. The context-isolation property strengthens the case against the over-orchestration anti-pattern's coordination tax (the script absorbs reconciliation that previously bloated the caller's context), but it does NOT remove the anti-pattern: spawning 16 subagents for a 20-minute task is still over-orchestration. The accountability shape is unchanged — the human who merges owns the output regardless of how many subagents a script fanned across.

**Sources:**
- Claude Code dynamic workflows docs: https://code.claude.com/docs/en/workflows
- Anthropic announcement: https://claude.com/blog/introducing-dynamic-workflows-in-claude-code
- InfoQ coverage: https://www.infoq.com/news/2026/06/dynamic-workflows-claude-code/
- Claude Opus 4.8: https://www.anthropic.com/news/claude-opus-4-8

## 2026-06-12 Delta Update (currency only)

- **obra/superpowers figures refreshed**: **226k GitHub stars** and **v5.1.0 (released 2026-05-04)**, MIT, multi-host (Claude Code, Cursor, Copilot CLI, Gemini CLI, OpenCode) — verified by direct fetch of https://github.com/obra/superpowers on 2026-06-12. The "226k (as of 2026-06-12) stars" figure elsewhere in this pack is the older 2026-Q1 number. Added to the Anthropic skills marketplace 2026-01-15 *(single-source)*.
- **New companion pack**: spec-driven development, context engineering (host instruction files), worktree/conductor parallel-lane mechanics, and the compound loop now live in companion engineering-practice guidance (created 2026-06-12). This pack keeps its boundary: programming model, tool landscape, anti-patterns.

## V2V Cross-References

**Sibling Q2-5 packs**:
- **`mcp-architecture.md` (Q2-5.1)** — the protocol sub-agents use to reach tools and data; sub-agent dev sits on MCP as its plumbing layer. Tool-integration architecture for sub-agent dev consumes that pack's transport variants, three primitives, and client architecture patterns.
- **`a2a-architecture.md` (Q2-5.2)** — when sub-agents delegate to other sub-agents, A2A is the wire; pair-read for multi-agent execution patterns. Star/mesh/hybrid topology choices apply when sub-agent driven dev scales beyond a single executor.
- **`agentic-security.md` (Q2-5.3)** — security threat model for sub-agent dev: credential scope on production-vs-prod separation, prompt injection at the code-authoring layer (an adversary-controlled README or comment can re-direct an agent's coding intent), supply-chain risk in agent-installed dependencies, secret rotation across sub-agent sessions.

**Sibling Q2-3 packs**:
- **`agent-identity.md` (Q2-3.1)** — identity layer that makes sub-agent action auditable. Org-wide adoption decisions in this pack (identity & access section) consume that pack's Identity Registry-vs-system-identity distinction; sub-agent-authored code that takes autonomous action (deploys, merges, calls APIs) needs the agent-identity binding established at that pack's lifecycle layer.
- **`mcp-governance.md` (Q2-3.2)** — governance pattern applies to sub-agent tool use, not just MCP integrations generally. Registry, approval workflow, and audit-trail standards extend to the tools sub-agents invoke during code authoring.
- **`csa-ai-controls-matrix.md` (Q2-3.3)** — when sub-agent driven dev is the development methodology for AI systems in scope for AICM, domain 1 (Model Lifecycle Management), domain 5 (Change Management), and domain 9 (Identity & Access Management) operationalize on the sub-agent dev workflow.

**Existing packs**:
- team-level operating principles — team-level adoption decisions live there once an org commits.
- `code-review.md` — code-review discipline that the two-stage review pattern (sub-agent self-review then human review) extends.
- TDD discipline — TDD discipline that the obra/superpowers methodology mandates; sub-agent dev's TDD mandate sits on top of that pack's TDD patterns.
- `api-design.md` — when sub-agent-authored code exposes APIs, API-design discipline applies regardless of authorship.

**Sensitive-skill applicability**: Not sensitive per `sensitive-skill-guardrails.md` §2 (methodology guidance, no legal/HR/compliance output). Skills built on top of sub-agent driven dev that automate consequential actions (auto-merge, auto-deploy) inherit sensitive-skill scaffolding independently.

## Sensitive-skill applicability

**Not sensitive.** This is a technical-reference pack — methodology guidance for an engineering practice. Skills built on top of sub-agent driven dev (e.g., a delegated code-review skill that auto-merges) may be sensitive depending on what they automate, and those skills inherit `sensitive-skill-guardrails.md` scaffolding independently. The methodology layer itself does not require Findings / Reviewer Checklist / Cannot Assess Without structure.

## Operating Principle

> *Sub-agent driven development amplifies engineer judgment — it doesn't replace it. The 10x leverage shows up when the human knows WHY each task is being delegated; it disappears when the prompt is the only spec.*
