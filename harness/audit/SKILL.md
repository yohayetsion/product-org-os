---
name: audit
description: 'Audit work the rigorous, non-rubber-stamp way — mode-aware: it first detects whether the context calls for a RESULT audit (work that has already run) or a PLAN audit (a plan / updated plan, before it runs), then runs the right method. RESULT mode: 3 checks (executed-correctly / aligned / no-bugs) verified by opening and running things, by the right panel of agents — sized to the dimensions of the work (one auditor per angle, in parallel), different from the originals where a fresh angle helps, at least one that did not do the work — ending in GO / NO-GO. PLAN mode: the same pre-execution review /plan uses — the agents who would do the work give per-step confidence + pre-execution mitigations, ending in PROCEED / REWORK-PLAN; it refuses to review a plan whose Open Decisions register still has unanswered entries, sending it back to the /plan owner Q&A first. Activate when: "audit the result", "audit this", "audit the plan", "audit the updated plan", "/audit", before sign-off OR before executing a (revised) plan. Can also be referenced as a composable step inside a larger prompt. Do NOT activate for: generic code review (/code-review).'
argument-hint: '[what to audit]'
user-invocable: true
metadata:
  author: ProductBeacon AI Workforce
  category: workflow
  skill_type: task-capability
  owner: product-operations
  primary_consumers:
    - product-operations
  secondary_consumers:
    - director-product-management
    - vp-product
  sensitive: false
  work_shape: operator-loop
  phases:
    - name: Detect the mode
      description: Read the target and decide whether this is a RESULT audit (Mode A, the work has run) or a PLAN audit (Mode B, before it runs). Ask one question only if genuinely ambiguous.
    - name: Mode A — size the auditor panel
      description: Bring one auditor per dimension that matters, in parallel. At least one must be a fresh agent that did not do the work; that is the floor, not the target.
    - name: Mode A — run the three checks
      description: Against the plan MD, check executed-correctly, aligned, and no-bugs. Verify by opening files, running checks and looking at the live result; never assume.
    - name: Mode A — report and verdict
      description: Report findings by severity (blocker, important, minor), fix what is safe and re-verify, flag what you cannot, and end on a clear GO or NO-GO.
    - name: Mode B — Open Decisions gate
      description: Read the plan register BEFORE spawning anyone. Any unanswered entry returns REWORK-PLAN back to the plan owner Q&A. Do not answer the open entries yourself.
    - name: Mode B — confidence and mitigations
      description: The agents who would execute the plan return per-step confidence plus the pre-execution mitigations that raise it. Low confidence is where the mitigation goes, not a blocker.
    - name: Mode B — reality check and verdict
      description: Check the plan against reality (named agents exist, phases verifiable, no contradiction with shipped work), write confidence and mitigations back into the plan MD, and end on PROCEED or REWORK-PLAN.
---

Audit work the rigorous way, before you sign off or before you commit to executing. The skill is **mode-aware**: a plan that hasn't run yet and a plan that *has* run need different scrutiny, and this skill detects which the context calls for and runs the matching method — never a generic review.

It works two ways: standalone (`/audit <what to audit>`) and as a **composable step referenced inside a larger prompt** ("…then `/audit` the result", or "…`/audit` the updated plan before we run it"). When referenced inline, audit the work at hand and continue the surrounding flow.

## Rule 1 — Findings, Not Votes

A binding blocker exists only when one of the following evidence conditions is met. Stop only the affected phase when evidence shows:

1. an unresolved owner or authority decision;
2. an unsafe, infeasible, or untestable phase; or
3. an irreversible step without an enforceable acceptance check or owner gate.

Everything else is a mitigation, including low confidence, buildable scripts, logging, and wording improvements.

**Mixed reviews:** test findings against this rule. Preserve dissent. Do not let one label become an automatic veto.

## Step 0 — Detect the mode (do this first, every time)

Decide whether you are auditing a **result** or a **plan**, because the method differs:

| Signal | Mode |
|--------|------|
| The work/phases have **executed**; deliverables exist; the user says "the plan has run", "audit the result", "before I sign off", or it's the post-execution step of a loop | **Mode A — Result audit** |
| The target is a **plan / updated plan that has NOT run** (status DRAFT/for-review, phases unstarted, or a plan revised mid-stream that needs re-review); the user says "audit the plan", "audit the updated plan", "review this before we execute" | **Mode B — Plan audit** |

Read the plan MD (or the artifact) to check its actual state — do not assume. If a plan's phases are partly executed and partly not, audit the executed part in Mode A and the remaining/updated part in Mode B, and say so. **If genuinely ambiguous, ask one question:** "Is this a result audit (it's run) or a plan audit (before it runs)?" Both modes share the spawn discipline and the no-rubber-stamp / fresh-perspective principle below; only the checks and the verdict differ.

---

## Mode A — Result audit (work that has already run)

### The prompt this mode runs (verbatim — do not paraphrase or invent new logic)

This is the operator's actual post-execution audit prompt. The skill's job is to **run this exact audit**, not to substitute a generic review:

```
The plan has run. Audit the result before I sign off. Use the
agents, and include at least one fresh agent that did not do the
work, so this is an audit, not a rubber stamp.

Check three things against the plan's MD:
1. Executed correctly - every phase and deliverable the plan
   called for actually exists and does what it was meant to.
   Call out anything skipped, stubbed, or quietly dropped.
2. Aligned - the deliverables are consistent with each other and
   with the plan. No contradictions, stale references, or claims
   that disagree across files.
3. No bugs - nothing broken: dead links, errors, anything that
   doesn't render or run.

Verify, don't assume - open the files, run the checks, look at
the live result. Report findings by severity (blocker /
important / minor), say what's wrong and where, fix what's safe
and re-verify, flag what you can't. End with a clear GO / NO-GO
and what's still open. Be honest - I'd rather hear what isn't
done than get a clean bill that isn't true.
```

## What that means in practice

1. **Right-size the auditor panel — independence is the floor, coverage is the goal.** Bring the *number and mix* of agents the work actually needs: ideally one auditor per dimension that matters (correctness, security, legal/compliance, financial, build-integrity, cross-file consistency, live-surface behavior, …), run in parallel. **At least one must be a fresh agent that did not do the work** — that is the no-rubber-stamp *floor, not the target*. Prefer agents *different from* the original executors wherever a new angle sharpens the audit (a security reviewer on a security pack, a counsel on a legal doc). A multi-dimension deliverable warrants several auditors looking from different angles; a narrow one needs fewer. Don't collapse to a single auditor when the work spans domains, and never let an agent audit only its own work. (High-stakes → the adversarial-review posture: fresh context, no prior-turn rationale, `rules/delegation-protocol.md` Pattern 5; respect the parallel cap in `rules/parallel-execution.md`.)
2. **Three checks against the plan MD:**
   - **Executed correctly** — every phase and deliverable exists and does what it was meant to; call out anything skipped, stubbed, or quietly dropped.
   - **Aligned** — deliverables are consistent with each other and the plan; no contradictions, stale references, or claims that disagree across files.
   - **No bugs** — nothing broken: dead links, errors, anything that doesn't render or run.
3. **Verify, don't assume** — open the files, run the checks, look at the live result. A claim of "done" is not evidence of done.
4. **Report by severity under Rule 1** — use **Blocker** only for one of its three evidenced conditions. Everything else remains **Important** or **Minor** with a mitigation; severity labels do not vote.
5. **Fix what's safe and re-verify; flag what you can't.**
6. **End on GO / NO-GO** and what's still open. Be honest — an explicit "here's what isn't done" beats a clean bill that isn't true.

---

## Mode B — Plan audit (a plan or updated plan, before it runs)

When the target hasn't executed, "verify it ran correctly" is the wrong question — there is nothing to open and run yet. The right scrutiny is the **same pre-execution review `/plan` folds in**: the agents who would do the work review the plan and return confidence + mitigations, so you steer on paper before spending execution. This mode lets `/audit` run that review **standalone** — most useful when a plan was **updated** after its original review (revised scope, new phase, post-incident change) and needs re-review without re-running all of `/plan`.

### ⛔ Gate before you review — the plan's decisions must be settled first

**Read the plan's `## Open Decisions` register before spawning a single reviewer.**

- **A declared register with any `⬜ OPEN` row → stop and return `REWORK-PLAN`**, naming the unanswered entries and pointing back to `/plan` Step 2 (the owner Q&A session). Do not review, do not spawn the panel, **do not answer the open entries yourself.**
- **No register at all → review it, and state the limitation.** Put this on the verdict verbatim: *"No Open Decisions register present; this review does not attest that the plan's design questions were settled with the owner."* ⛔ **Do not bounce a plan for lacking a register** — that would make you apply `/plan`'s filter test blind to someone else's plan, which is a false-positive engine, and it would bounce every legacy, hand-written, or pre-v1.2.0 plan on arrival.
- **Exception — a plan that declares itself `/plan`-authored and has no register is a defect** → `REWORK-PLAN`. There the register's absence is evidence, not an unknown.

**Why this is a hard stop and not a caveat**: reviewing a plan whose design questions are open audits *the planner's guesses*, and returns confidence in them. The reviewers then bless a shape the owner never chose, and the resulting confidence figure is worse than none — it launders an unmade decision into an approved one. The whole point of `/plan`'s Q&A gate is that the audit sees the plan the owner actually chose.

Two things this gate is **not**:
- **Not a demand that every risk be resolved.** Open *risks* are exactly what Mode B exists to price. Open **decisions** are what it cannot price.
- **Not applicable to a plan the owner has explicitly told you to review as-is.** If they say "review it with question 3 still open," honor that — **but only where you can quote the instruction.** The verdict records the owner's words verbatim and names which register entries the override covers. **No quote, no override.** Record that the review is conditional on those entries, and which findings would move if they land the other way.

### The prompt this mode runs (verbatim — the `/plan` pre-execution review)

```
Once there's a detailed plan, have the planned agents deeply
review it before executing, and provide their confidence level
and any pre-execution mitigations that can raise confidence.
```

### What that means in practice

1. **Spawn the agents who would actually execute the plan** (the ones the plan names per phase), plus — for a high-stakes or substantially-rewritten plan — at least one agent who did **not** author the plan, for a fresh-perspective read (the same no-rubber-stamp principle as Mode A; `rules/delegation-protocol.md` Pattern 5).
2. **Each returns a per-step / per-phase confidence level** and the **pre-execution mitigations** that would raise it.
3. **Low confidence is not a blocker — it is where the mitigation goes.** Low-confidence steps get scoped down, sequenced behind a checkpoint, human-gated, or given an explicit written mitigation folded into the plan — not discovered at runtime.
4. **Check the plan against reality** the same way Mode A checks deliverables: do the named agents exist in the roster? Are phases verifiable? Does the updated plan still align with what already shipped (no contradiction with executed phases)? Surface anything missing, hand-wavy, or stale.
5. **Write the confidence + mitigations back into the plan MD** (don't leave them in chat) and end on a verdict: **PROCEED** (optionally PROCEED-WITH-MITIGATIONS, listing them) or **REWORK-PLAN** only where Rule 1 evidences a binding blocker, naming the affected phase and the condition to close.

## Spawn discipline (non-negotiable)

Every agent this skill uses — including the fresh auditor — MUST be spawned through the **full** spawn protocol (`.claude/rules/agent-spawn-protocol.md`): the mandatory identity / prompt-injection template, **Phase 1 self-orientation** (the agent reads its own `SKILL.md` + its preload knowledge packs before acting), and the **Spawn Audit Block + telemetry**. No shortcuts, and no bare/generic `general-purpose` subagents that skip the protocol.

Use **only agents installed in this deployment's roster** (the ProductBeacon agent teams). **Never invent or create new agents**, and never call an agent that isn't installed here. The fresh auditor must be an installed agent that did not do the work — not an improvised one. If no suitable installed agent is available, say so and ask.

## Output

State which mode you ran, then:
- **Mode A (result):** a findings list grouped by severity (blocker / important / minor) — what's wrong and where, what was fixed and re-verified, what's still open — ending in a clear **GO / NO-GO**.
- **Mode B (plan):** per-step/phase **confidence + pre-execution mitigations** written back into the plan MD, ending in **PROCEED** (or PROCEED-WITH-MITIGATIONS, listing them) / **REWORK-PLAN** (with the gaps to close first).

## Guardrails

- **Detect the mode first (Step 0).** Don't run a result audit on a plan that hasn't executed (there's nothing to open and run), and don't run a plan review on already-shipped work (too late for mitigations — it needs the result audit). When genuinely ambiguous, ask the one-line mode question.
- **Mode B: never review an undecided plan.** `⬜ OPEN` entries in the plan's Open Decisions register → `REWORK-PLAN` before the panel is spawned, back to `/plan` Step 2. Confidence in a guess is worse than no confidence figure. The one exception is an explicit owner instruction to review as-is, which the verdict must record as a conditional.
- **Fidelity, not reinvention.** Run the verbatim prompt for the detected mode — the Mode A post-execution audit or the Mode B `/plan` pre-execution review. Do not substitute a generic review.
- **No rubber stamp; size the panel to the work.** Bring as many auditors as the dimensions need (one per angle, in parallel), not a token single reviewer — at least one must be a fresh agent that did not do the work (Mode A) / did not author the plan (Mode B), and prefer non-original agents for the angles where independence matters most. Never let an agent bless only its own work.
- **Verify against reality, don't assume.** Mode A findings come from actually opening/running things; Mode B confidence comes from the executing agents reading the real plan + roster, not from re-reading chat.
- **Honest verdict.** Never issue a clean bill (GO or PROCEED) to please; surface what isn't done / what lowers confidence.
- **Composable.** Works standalone or as a referenced step in a larger prompt.

## Relationship to adjacent skills

| Skill | Difference |
|-------|------------|
| `/plan` | Owns plan **creation**, the **owner Q&A gate** (Step 2) that settles the plan's Open Decisions, and its first pre-execution review. `/audit` **Mode B** runs that *same* review method standalone on a plan/updated plan (e.g., a plan revised mid-stream that needs re-review without re-running all of `/plan`) — **and enforces the Q&A gate from the other side**, refusing to review while decisions are open; `/audit` **Mode A** runs the **result** audit after execution. Same review discipline, reachable from the audit verb. |
| `/context-harvest` | Runs after a clean result audit (Mode A GO) to record the work into memory. |
| `/code-review` | A narrower code-focused tool. `/audit` is the operator's whole-deliverable audit (result or plan) ending on GO/NO-GO or PROCEED/REWORK. |
