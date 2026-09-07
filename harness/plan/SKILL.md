---
name: plan
description: 'Plan a non-trivial piece of work before executing it, the ProductBeacon operator way — a plan MD, the right existing agents, phased with verification, the spawn protocol + telemetry; every material decision noted but NOT self-decided, settled with the owner in a Q&A session, recorded in a DR, folded back into the plan, and only then audited. Activate when: "plan this", "write a plan first", "/plan", or before executing any multi-step work. Can also be referenced as the planning step inside a larger prompt. Do NOT activate for: trivial one-step tasks, or recalling an existing plan.'
argument-hint: '[what to plan]'
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
    - name: Draft the plan
      description: Draft or update the plan MD, and write every material fork into the Open Decisions register WITHOUT deciding it. An empty register is a correct outcome.
    - name: Owner Q&A
      description: Settle the register with the owner in one consolidated batched round. Record verdicts and the owner own wording; record supersessions rather than overwriting them.
    - name: Record the decisions
      description: Capture the rulings as drafted decision records, with a separate record for any ruling that supersedes or contradicts a standing one. Nothing survives only in chat.
    - name: Update the plan
      description: Fold each ruling and its consequences into the phases, steps and agent instructions. Any still-open entry becomes a named blocker on the phases that depend on it.
    - name: Pre-execution review
      description: Run the audit skill in plan mode on the UPDATED plan. The agents who would do the work return per-step confidence and the mitigations that raise it.
    - name: Execute
      description: Execute only after the review, phase by phase, updating the plan MD after every phase and having the executing agents verify the deliverables.
---

Plan a non-trivial piece of work **before any step executes** — written intent first, so you steer cheaply on paper instead of expensively mid-execution. This skill is the operator's planning discipline as a single, repeatable move.

It works two ways: as a standalone command (`/plan <what to plan>`) and as a **composable step referenced inside a larger prompt** ("…use `/plan` to plan this first, then …"). When referenced inline, apply this discipline to the work at hand without assuming you own the whole conversation.

## The order of operations (NON-NEGOTIABLE)

```
1. DRAFT the plan MD          — and note every major decision WITHOUT making it
2. Q&A SESSION with the owner — get the answers and clarifications
3. RECORD the answers in a DR — including any that supersede a standing record
4. UPDATE the plan MD         — fold the rulings in, with their consequences
5. AUDIT the updated plan     — /audit Mode B pre-execution review
6. EXECUTE
```

**If the register is empty** — the plan has genuinely no material forks — **Steps 2–4 do not fire.** Say so in the plan ("Open Decisions: none — no material forks") and go to Step 5. An empty register is a correct outcome, not a failure to look.

## The prompt this skill runs (verbatim — do not paraphrase or invent new logic)

This is the operator's actual planning prompt. The skill's job is to **apply this exact discipline**, not to substitute generic planning advice:

```
Plan accordingly. If a plan's MD file already exists, update it.
If none exists, create one for this plan.

- Make sure you have backups if needed.
- Use the relevant agents from the ProductBeacon agent teams to
  execute, don't invent/create new agents, and make sure the plan
  calls for the entire context, details and instructions to be
  given to them per execution.
- Phase the plan as needed. Make sure to update the plan's MD after
  every phase. Make sure the executing agents are used to verify the
  deliverables after every phase, as well as at the end of the
  process.
- Use the spawning protocol that makes sure each agent reads its
  full definition as well as the relevant skills / knowledge packs
  they will need when performing their tasks. Make sure agent
  telemetry is created per the instructions.

Also, should we do it in this context window? If not, build me the
prompt and instructions to the next context window + reference the
plan's MD of course. Open it in my notepad.
```

## What that means in practice

1. **Plan MD, always.** If a plan MD for this work exists, **update it**; otherwise **create one**. The plan is the artifact — goal, steps, files touched, what each step produces, and the risks. Never plan only in chat.
2. **Backups first** where a step could overwrite or lose work.
3. **Use the existing ProductBeacon agent teams — never invent agents.** The plan must hand each agent the *entire* context, details, and instructions it needs per execution (don't assume the agent shares this conversation's memory).
4. **Phase it.** Break the work into phases; **update the plan MD after every phase**; the **executing agents verify the deliverables after each phase and at the end** (see `/audit` for the post-execution result audit).
5. **Spawn protocol + telemetry.** Each agent reads its full definition plus the skills / knowledge packs its tasks need (per `rules/agent-spawn-protocol.md`); agent telemetry is created per the instructions.
6. **Right context window.** Decide whether to execute in this context window. If not, produce the hand-off prompt + instructions for the next window, referencing the plan MD.

---

## Rule 2 — One Plan; Escape the Loop

- Keep one controlling plan.
- Keep logs, scans, hashes, screenshots, and receipts as evidence.
- Add an annex only for a separate executor or machine that needs it.
- If new controls create the next blockers, return to the settled outcome and collapse those controls.
- No third review of the same structure without an owner exception.

**Use the escape immediately.** The repeat limit is a backstop, not a reason to wait.

## Rule 3 — Route the Next Phase

| Next phase | Guidance |
|---|---|
| Bounded and reversible | Lean plan; verify the result |
| One irreversible boundary | Do reversible work; stop at the owner gate |
| Several irreversible steps or conflicting authority | Full plan and independent review |

- The planner declares the route in one sentence.
- No separate agent approves it.
- Result audit catches misrouting and reclassifies the next phase.

**Limitation:** routing reduces ambiguity; it is not self-enforcing.

---

## Step 1b — The Open Decisions register (write it while you draft; do NOT decide)

While drafting the plan, every time you reach a fork where more than one answer is defensible, **stop and write the question down instead of picking**. The plan MD carries a section (the heading is a literal anchor `/audit` matches on — do not decorate it):

```markdown
## Open Decisions

| # | Question | My proposal (NOT a decision) | Why it matters / what it forecloses | Status |
|---|----------|------------------------------|-------------------------------------|--------|
| 1 | …        | …                            | …                                   | ⬜ OPEN |
```

### What belongs in the register (the test)

Register it when **any** of these is true:

| Trigger | Example |
|---|---|
| **Scope** — what ships now vs. defers | "Does the ledger ship in this phase, or defer?" |
| **More than one defensible mechanism**, and the choice is visible to the user or buyer | "Policies org-wide, or scoped by department?" |
| **It trades against a standing affirmed record** (a DR, a rule, a prior ruling) | "This would make the model subject-aware at a band the DR calls subject-absent." |
| **Hard or expensive to reverse** once built | "Which existing cases carry the policy-set severity" — moves pinned invariants |
| **You'd otherwise pick a silent default the owner can't see** | persistence, ordering, naming, what a surface does when a dependency is unavailable |
| **It costs a guarantee** the owner previously bought | "This gives up count-immobility; what's the consideration?" |

### What does NOT belong (decide these yourself)

Routine judgment calls with a conventional answer, file paths and naming inside existing conventions, which installed agent fits a phase, anything already settled in a standing record. **Registering everything is the same failure as registering nothing** — it hands the owner your job. If the register is long, you are probably not filtering; re-read the test.

### How to write each entry

- **State the question plainly** — plain language first, no unexplained acronyms. The owner should be able to answer without reading the build.
- **Never leave the proposal cell blank** — silence is not neutrality. A recommendation the owner can reject beats a blank.
- **Flag tensions with standing records by ID.** If the proposal contradicts an affirmed DR or rule, say so in the entry, quote the conflicting line, and do not resolve it yourself.
- **Never mark anything decided that the owner has not answered.** No pre-filled ✅.

---

## Step 2 — The Q&A session (MANDATORY gate — the plan does not advance without it)

Take the register to the owner and settle it **in conversation**, before the audit and before a single step executes.

### How to run it

- **One consolidated round, batched.** Present the whole register at once — not one question per turn. Drip-feeding approvals is its own failure mode.
- Use **`AskUserQuestion`** for entries that are genuinely a choice among options (batch up to 4 per call, options carrying the consequence in the description) — **or the inline numbered register wherever that tool is not available in the harness.** Use the **inline numbered register** for open-ended entries, and for any round with more than a handful of questions. Mixing both in one round is fine.
- **A second round only if an answer changes what the later questions are.** Two rounds is normal; a fourth means the register was badly built.
- **Capture clarifications, not just verdicts.** The owner's framing sentence ("very simple to demo") is often more load-bearing than the yes/no, and becomes a constraint the plan quotes verbatim.
- **Push back once where you see a real tension**, then accept the ruling. If the owner's answer conflicts with an affirmed record, show them the conflicting line and let them rule; their ruling governs. Do not re-litigate after they've ruled.
- **Ask, don't assume, on anything you registered.** If the owner skips an entry, it stays ⬜ OPEN and the plan says so — an unanswered decision is never quietly resolved by the plan's default.

### Recording the answers in the register

Update each row in place: **✅ APPROVED** / **✅ AMENDED** / **❌ DECLINED** / **↩️ YOURS** (the owner says this should not have been registered) / **⬜ OPEN**, with the owner's own words where they gave any.

If the owner says an entry was not worth asking, record it **↩️ YOURS**. Those rows are the measurement of whether the filter is too loose — **do not omit them to look disciplined.**

⛔ **Record supersessions, never overwrite them.** When the owner amends an earlier answer, keep the original answer, the tension that was flagged, and the ruling that replaced it — all three. A fresh context window that sees only the final answer re-discovers the tension and re-opens the question.

⛔ **Write down the consequences that must not be "fixed" later by someone who wasn't in the room.** A deliberate inconsistency reads as a bug to the next reader. Say why it is deliberate, in the plan.

---

## Step 3 — Record the answers in a Decision Record

Run `/decision-record` on the session's rulings, per `.claude/rules/dr-affirmation-presentation.md`.

- **One DR** when the answers form a single coherent design ruling.
- **A separate DR** for any ruling that **supersedes, scopes, or contradicts a standing record** — those need their own `Supersedes` field and their own affirmation, and burying them inside a combined DR is how a supersession goes missing.
- **Every answer lands somewhere durable**: either in a DR, or in the plan's Open Decisions register that the DR references. Nothing survives only in chat.

Mechanics:

- Allocate the next free DR id with the workspace's id allocator; collision-check the id **before and after** the write; register the record in the decisions index.
- **Follow `dr-affirmation-presentation.md`** — it is the format authority for how a DR is written and surfaced for affirmation. Do not restate its rules here; read it.
- Dispatch Mode is typically **`mode-1-with-embedded-mode-2-summary`**: the owner authored the substance in the Q&A; you drafted the record.
- The DR is **drafted** here. It closes only when the owner affirms it — never auto-close.
- The plan MD links the DR by ID; the DR links back to the plan MD.

---

## Step 4 — Update the plan

Fold the rulings into the plan itself — not as an appendix the reader has to reconcile, but into the phases, the steps, and the agent instructions. Restate each ruling's **consequence** where the work touches it. Anything ⬜ OPEN is carried at the top of the plan as an explicit blocker. **An ⬜ OPEN entry blocks execution of every phase whose work depends on it — name those phases in the blocker line.** Phases that do not depend on it may proceed.

## Step 5 — Pre-execution review (run only on the UPDATED plan)

**Invoke `/audit` Mode B on the updated plan.** It runs the pre-execution review (the verbatim A2 prompt lives there, once), and it re-checks the Open Decisions register from the other side. ⛔ **Do not inline your own version of this review** — `/audit` Mode B additionally requires a reviewer who did **not** author the plan on high-stakes or substantially-rewritten plans, plus a roster-and-already-shipped reality check. An inline substitute silently drops both, and the non-author requirement is the FB-2026-039 property this whole gate exists to protect.

What comes back:

- The agents who will do the work return a **confidence level per step** and **pre-execution mitigations** that raise it.
- **Low confidence is not a blocker — it is where the mitigation goes.** Low-confidence steps get scoped down, human-checked, or given an explicit mitigation written into the plan, not discovered at runtime.
- **Surface the confidence levels and mitigations to the owner** — don't just fold them into the plan silently.
- Only after this review does execution begin.

---

## Spawn discipline (non-negotiable)

Every agent this skill uses MUST be spawned through the **full** spawn protocol (`.claude/rules/agent-spawn-protocol.md`): the mandatory identity / prompt-injection template, **Phase 1 self-orientation** (the agent reads its own `SKILL.md` + its preload knowledge packs before acting), and the **Spawn Audit Block + telemetry**. No shortcuts, and no bare/generic `general-purpose` subagents that skip the protocol.

Use **only agents installed in this deployment's roster** (the ProductBeacon agent teams). **Never invent or create new agents**, and never call an agent that isn't installed here. If no installed agent fits the work, say so and ask — do not improvise one. The plan must name the specific installed agents per phase and hand each the entire context it needs.

**Agents surface decisions; they do not settle them.** A planning agent that hits a fork adds it to the Open Decisions register and keeps going. Only the owner closes a register entry.

## Output

1. A plan MD at the appropriate path (created or updated), phased, carrying the **Open Decisions register** with every entry resolved (or explicitly still open), the rulings folded into the phases, and per-step confidence + mitigations recorded from the review.
2. **If the register had entries**: one or more **drafted DRs** capturing the Q&A rulings, registered in the decisions index, awaiting owner affirmation. An empty register owes no DR — inventing one is the DR spam this skill exists to avoid.
3. If executing in a fresh context window, the hand-off prompt referencing the plan MD **and the DR IDs**.

## Guardrails

- **Fidelity, not reinvention.** Apply the verbatim discipline above. Do not swap in a generic planning template or add logic the prompt doesn't call for.
- **Never execute a phase that depends on an open decision.** The register's open rows are execution blockers, not annotations. Phase-scoped, not whole-plan — unrelated phases proceed.
- **Don't decide what you registered.** Once a question is in the register, answering it yourself defeats the gate — even if the answer seems obvious by the time you get there.
- **Don't register what you should decide.** Routine judgment calls are yours; the register is for material forks.
- **No invented agents.** Use the existing ProductBeacon agent teams only.
- **No fabricated estimates.** Don't invent effort/timeline/cost numbers (`rules/no-estimates.md`); the plan names steps, owners, deliverables, and risks — engineering/owners estimate.
- **Composable.** Works standalone or as a referenced step in a larger prompt; when inline, plan the work at hand and continue the surrounding flow.

## Relationship to adjacent skills

| Skill | Difference |
|-------|------------|
| `/audit` | Audits the **result** after the plan runs (Mode A), or the **updated** plan before it runs (Mode B). `/plan` owns the front end, the Q&A gate, and the pre-execution review. **The audit runs after the Q&A, never before.** |
| `/decision-record` | The format authority for Step 3. `/plan` decides *that* a DR is written and *what* goes in it; `/decision-record` writes it. |
| `/context-harvest` | Runs at the **end** of the loop to record the work into memory. |
| `writing-plans` (superpowers) | Generic implementation-plan authoring. `/plan` is the ProductBeacon-opinionated discipline (agent teams, spawn protocol, telemetry, phase-verify cadence, owner Q&A gate) — wraps the same idea, does not replace it. |
