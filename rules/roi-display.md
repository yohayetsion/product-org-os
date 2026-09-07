# ROI Display (computed hours-only model — 2026-08-01)

**Agents report nothing about their own value.** The per-spawn `[Post-Execution ROI]` Audit Block section is retired (see `agent-spawn-protocol.md` §2.5 and §3, incl. the migration note for legacy blocks). ROI is now a **pipeline computation and a display concern**, never an agent emission. This rule defines the computed model and its display surfaces; the sensitive-framing control at the bottom is retained unchanged and binds every display surface.

---

## The Computed Model

- **The number is computed, not self-reported.** Hours come from the **owner-affirmed activity table** (`../tools/hooks/baselines.json` → `agents` rows, one affirmed `baseMinutes` time basis per agent seat), resolved per **canonical agent slug** (the frozen alias map's merges; identity for unmapped slugs) by the telemetry pipeline. The published hours come from the maintained table, not from anything agents wrote.
- **No fallback exists.** The table's `_default` row is refused by the resolution chain. A spawn whose canonical slug has no affirmed table row is **counted, not priced**: present in the data with its spawn count, contributing zero hours, shown as "no time basis yet" — never `0 hrs` styled as a measurement, never an estimate.
- **Hours only.** There is **no dollar value figure, no rate table, and no $/hr anywhere in the value chain**. (A separately-labeled *measured compute cost* may arrive later as its own input — an expense, never a value figure, and never a ratio against hours.)
- **Coverage is stated** wherever hours are shown: priced spawns / total receipts, with tool_use_id-level provenance in the dashboard data.
- Always reference product / knowledge work, never coding/development.

## Display Surfaces

| Surface | Generator | What it shows |
|---------|-----------|---------------|
| Operator dashboard | the private operator dashboard pipeline | Computed hours (man-day scaling), coverage, per-agent hours + spawns, counted-not-priced rows visible |
| Weekly email digest | the private operator email-digest pipeline | Trailing-window computed hours, coverage, top contributors by hours |

No per-spawn ROI section, no inline metrics in agent responses, no synthesizer aggregate footer. Agents and gateways simply do the work; the pipeline prices it.

## Record Keeping

The receipts store (`context/roi/audit-receipts.jsonl`, appended by `telemetry-extract.py`) is the record the pipeline prices. Legacy `context/roi/session-log.md` entries and legacy blocks carrying `[Post-Execution ROI]` are history — tolerated-but-ignored per the migration note in `agent-spawn-protocol.md` §3.

---

> **Scope (2026-08-01):** the framing control below is retained verbatim and governs the dashboard, the weekly email digest, and any user-facing surface that displays computed hours for sensitive-domain seats — the retirement of per-spawn ROI reporting changes nothing about it.

## Sensitive Skill ROI Framing (MANDATORY)

Legal, HR, compliance, privacy, and other sensitive skills (per `.claude/rules/sensitive-skill-guardrails.md`) MUST frame ROI as **"time saved on drafting and triage,"** never as anything that implies the skill substitutes for, accelerates, or replaces expert review. The reason is liability framing: describing the skill as saving review time implies it replaces counsel, which is the precise claim we cannot defensibly make — the whole point of the two-pass publication gate (`sensitive-skill-guardrails.md` Section 4) is that a licensed human reviews every sensitive output before action. "Drafting and triage" accurately captures what the skill actually does: produces a structured first pass that a human expert then reviews, validates, and owns.

### Prohibited Phrasings (Non-Exhaustive Enumeration)

The following phrasings — and any semantic equivalent — are PROHIBITED in ROI framing for sensitive skills, in agent responses, in marketing/positioning copy, and in any user-facing surface:

- "time saved on legal review" / "time saved on HR review" / "time saved on compliance review" / "time saved on privacy review"
- "faster legal review" / "faster HR review" / "faster compliance review" / "review acceleration" / "review velocity"
- "saves attorney time" / "saves counsel time" / "reduces attorney hours" / "cuts legal-team workload"
- "legal department efficiency" / "legal team productivity gains" / "HR department efficiency"
- "faster than counsel" / "faster than your attorney" / "faster than human review"
- "[X] hours of legal review saved" / "[X] hours of HR review saved" / "[X] hours of compliance review saved"
- "review at scale" / "scale your legal review" / "review more contracts in less time"
- "AI-accelerated review" / "AI-augmented review" (where the implication is that the AI is doing review work)

The pattern to avoid: anything that implies the deliverable is "review" rather than "drafting and triage scaffold for human review."

### Acceptable Phrasings

The following phrasings ARE acceptable and accurately describe what sensitive skills do:

- "~[X] hrs saved on drafting and triage" / "drafting and triage at scale"
- "first-pass scaffold produced in [time]" / "structured first-pass input for review"
- "structured input prepared for [reviewer role] review" — note: this frames the skill output as INPUT TO review, not as review itself
- "[X] resumes / contracts / clauses structurally extracted in [time], pending human review"
- "drafting time reduced; review time unchanged and required"
- "triage scaffolding produced for human evaluator"

The differentiating principle: the output is **input to the expert's review**, never **a substitute for it**. Phrasings that preserve that distinction are acceptable.

> *Relocated 2026-08-15 (DR-2026-262): worked example (non-normative; every Prohibited/Acceptable phrasing rule remains above) — full text in the companion roi-display.md (sibling of this rules directory; imposes nothing, relaxes nothing).*


---

## Operating Principle

> "The workforce reports nothing about its own value. Hours are computed from the owner-affirmed activity table and shown where aggregation belongs — the dashboard and the weekly email."
