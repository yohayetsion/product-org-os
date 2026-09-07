---
name: context-harvest
description: 'Review a completed piece of work or session and fan it out into BOTH memory layers — the OS context registry (Documents, Decisions, Strategic Bets, Assumptions, Learnings, Feedback) AND the Claude Code harness recall memory (topic file + MEMORY.md pointer). Activate when: "harvest this into context", "process this into all context types", "debrief this session", "capture everything from this work", "document it for later recall", "document for later recall" (full sweep). Do NOT activate for: saving a single known record (/context-save), recalling context (/context-recall), capturing only feedback (/feedback-capture).'
argument-hint: '[optional: topic or scope hint, e.g. "the «Security Vendor» v1->v2 mapping work"]'
user-invocable: true
metadata:
  author: ProductBeacon AI Workforce
  category: context-layer
  skill_type: task-capability
  owner: product-operations
  primary_consumers:
    - product-operations
  secondary_consumers:
    - vp-product
    - director-product-management
    - bizops
  sensitive: false
  work_shape: operator-loop
  phases:
    - name: Review the work
      description: Reconstruct what actually happened across every lens — what was produced, chosen, committed, assumed, learned, and told to you — and recall both memory layers first so nothing is duplicated.
    - name: Decide what to keep
      description: Judgment-led and automatic. Create the records that clear the bar; never present a candidate menu, never invent records to fill a category.
    - name: Write the records
      description: Write the organizational records (documents, decisions, bets, assumptions, learnings, feedback) through their canonical tools, and the recall-memory entry plus its index pointer.
    - name: Update indexes and cross-references
      description: Update each index and the context index file, then build bidirectional cross-references between the newly born records.
    - name: Surface drafted decisions
      description: State plainly that every drafted decision record needs the named owner affirmation to close. Never self-close.
    - name: Report the harvest
      description: Close with a summary across both layers listing every record created, the cross-links, and what was deliberately skipped.
---

Review a completed piece of work (the current session, a deliverable, a decision discussion) and **process it into every memory surface at once**, so nothing of value is left only in conversation or in a single scratch note.

This is the **full-sweep** counterpart to `/context-save` (which persists one known record at a time). `/context-harvest` does the *review-and-route* step across **both** memory layers the workspace keeps.

## The Two Memory Layers It Covers

| Layer | What it is | Reader | IDs / form |
|-------|-----------|--------|-----------|
| **A — Organizational memory** | The OS `context/` registry | Agents, `/context-recall`, the org over time | `DOC-`, `DR-`, `SB-`, `A-`, `L-`, `FB-` |
| **B — Recall memory** | The Claude Code **harness memory** — what "document it for later recall" produces | The assistant, every future session (auto-injected at session start) | A topic `.md` file + a one-line `MEMORY.md` pointer |

A harvest writes to **both**. They serve different readers and rarely duplicate: Layer A is the durable, queryable *organizational* record; Layer B is the assistant's cross-session *continuity* note that often **points at** the Layer-A records ("drafted DR-2026-NNN; converter at …") plus the non-obvious gotchas worth recalling. Capturing one but not the other is the gap this skill exists to close.

### Layer A — the six organizational context types

| Type | ID | What to harvest | Written via |
|------|----|-----------------|-------------|
| **Document** | `DOC-[YYYY]-[NNN]` | Any file/deliverable produced or substantially updated (PRD, spec, analysis, plan, script + its doc, report, model) | Register in `context/documents/index.md` + `context/index.json` |
| **Decision** | `DR-[YYYY]-[NNN]` | A choice with long-tail consequences; an approach picked among real alternatives; a prior decision now contradicted | `/decision-record` → **drafted** (DPS human-gate, see below) |
| **Strategic Bet** | `SB-[YYYY]-[NNN]` | A resource commitment or directional wager that rests on an explicit key assumption | `/strategic-bet` |
| **Assumption** | `A-[NNN]` | A load-bearing, not-yet-validated belief the work depends on | `/assumption-map` → status `Pending` |
| **Learning** | `L-[NNN]` | A generalizable lesson worth carrying to future work (not a one-off fact) | `/context-save learning` |
| **Feedback** | `FB-[YYYY]-[NNN]` | A user correction, stated preference, market signal, or customer quote encountered during the work | `/feedback-capture` (MANDATORY when present) |

**Auto-handled in Layer A (do not duplicate):** Interactions (`IX-`) and session summaries are logged automatically by `tools/hooks/os-tracker.py`. Themes (`TH-`) update automatically when feedback is linked (see `rules/context-graph.md`). `/context-harvest` references these; it does not re-create them.

### Layer B — the recall memory entry

One file per durable fact in the session's Claude Code memory directory (`~/.claude/projects/<project>/memory/`), plus a one-line pointer in that directory's `MEMORY.md` index (the file auto-injected into context at session start). Convention (per the harness memory spec):

- **Frontmatter:** `name` (kebab-case slug), `description` (one line — used to judge relevance on recall), `metadata.type` ∈ `user` | `feedback` | `project` | `reference`.
- **Body:** the fact. For `feedback`/`project`, follow with **Why:** and **How to apply:** lines. Link related memories with `[[other-name]]`.
- **Pointer:** append one line to `MEMORY.md` in the form below (never put memory content in the index):

  ```
  - [Title](file.md) — one-line hook
  ```
- **Type mapping from this work:** who the user is → `user`; how they want you to work (corrections/approved approaches) → `feedback`; ongoing work/goals/constraints → `project`; pointer to an artifact/resource (a script, doc, dashboard, the OS records just filed) → `reference`.

Layer B captures **what would be non-obvious or expensive to reconstruct next session** — not a verbatim copy of Layer A. A good recall entry names the artifacts and the gotcha, and links to the Layer-A IDs rather than restating them.

## Path Resolution & Auto-Initialization (local, every deployment)

Both targets resolve to the **local** operator, never to authoring-side paths:
- **Layer A** writes under `context/` **relative to the current workspace root** — i.e. the operator's own registry in their own deployment.
- **Layer B** writes to the **active session's own** Claude Code memory directory (`~/.claude/projects/<project>/memory/` for whoever is running this session) and that directory's `MEMORY.md`.

Before writing Layer A, ensure the registry exists (it ships scaffold-on-install, so a fresh deployment may not have it yet). If `context/` or a needed index is missing, create the minimal structure (`context/{documents,decisions,bets,assumptions,portfolio,learnings,feedback}/` + their index files + `context/index.json`) — mirror `/context-save`'s auto-initialization. Never stop and ask the operator to run something; the layer is yours to create. Never assume the authoring environment's paths or IDs; always read the *local* indexes to find the next number.

## Process

### 1. Review the work (reconstruct, don't assume)

Reconstruct what actually happened in the scope under review, through every lens:
- **What was produced** — files created or substantially changed (Layer A **Documents**; Layer B **reference**).
- **What was chosen** — decisions, approaches selected over alternatives, defaults set (**Decisions**).
- **What was committed** — directional wagers, resource commitments (**Strategic Bets**).
- **What it rests on** — beliefs the work depends on, not yet validated (**Assumptions**).
- **What was learned** — generalizable lessons, gotchas, reusable patterns (**Learnings**; strong Layer B candidates).
- **What the user told you** — corrections, preferences, signals, quotes (**Feedback**; Layer B `feedback`).
- **What future-you would need to continue** — the non-obvious continuity hook (**Recall memory**, Layer B).

If a scope hint was passed as an argument, focus there; otherwise sweep the current session. Before drafting, run `/context-recall {topic}` **and** check the recall-memory directory for an existing entry on this topic, so new records cross-link to (and don't duplicate) existing ones.

### 2. Create the records (judgment-led, automatic — NO approval gate)

Use your judgment to decide what is genuinely worth keeping across both layers, and **create those records now**. Do **not** present a candidate table and wait for the user to pick — the skill's value is its judgment; exercise it. The user asked for a harvest, not a menu to approve.

- **Auto-create** Documents, Assumptions, Learnings, Feedback, and the recall-memory entry for everything that clears the bar below.
- **Auto-draft** Decision Records — draft them without asking permission to draft. (DRs are surfaced for affirmation in §5; per the Decision Provenance Standard that affirmation *closes* the decision — it is the **only** human gate, and it concerns closing, not whether to record.)

**Judgment bar (quality over volume):** record what a future agent or session would genuinely need or benefit from — the load-bearing decisions, the reusable lessons, the real feedback, the artifacts produced, and the continuity hook. Skip the trivial, the obvious, and anything already in the registry or recall memory (you recalled in §1, so you know). Never invent records to fill a category — if a type has nothing worth keeping, skip it silently. A lean, high-signal harvest beats an exhaustive one. Report what you created afterward (§6); don't ask first.

### 3. Write each record

**Layer A** — follow the established per-type mechanics; do not reinvent them:
- **Document** → append a row to `context/documents/index.md` (`ID | Title | Date | Type | Owner | Product | Location | Tags`) and add the entry to `context/index.json`.
- **Decision** → `/decision-record`. Per the **DPS human-gate**, write at **`Record State: drafted`** with attestation + accountable-owner-signoff fields **`[PENDING HUMAN AFFIRMATION]`**. **Never** self-close. Surface for affirmation (§5).
- **Strategic Bet** → `/strategic-bet`; add to `context/portfolio/active-bets.md` if Active; extract its key assumption.
- **Assumption** → `/assumption-map`; `A-NNN` from `tools/allocate-id.py --ns A`; status `Pending`; link to source.
- **Learning** → `/context-save learning`; `L-NNN` from `tools/allocate-id.py --ns L`; categorize; link to source.
- **Feedback** → `/feedback-capture`; `FB-YYYY-NNN` from `tools/allocate-id.py --ns FB`; link related decisions; update theme strength.

**Layer B** — write the recall memory:
1. Check the memory directory for an existing file covering this fact. If found, **update it** rather than creating a duplicate; if it's now wrong, correct or delete it.
2. Otherwise create `~/.claude/projects/<project>/memory/<slug>.md` with the frontmatter + body convention above. Choose `type` per the mapping. Reference the Layer-A IDs and artifact paths; link related entries with `[[name]]`.
3. Append the one-line pointer to `MEMORY.md`.
4. Keep it to the non-obvious continuity hook — do not restate Layer-A content verbatim.

### 4. Update indexes + cross-references

1. Update each Layer-A type's index file (for example `context/documents/index.md`) and bump its "Last updated".
2. Update `context/index.json` — `entries`, `topicIndex`, `typeIndex`, `phaseIndex`, `lastUpdated`.
3. Build **bidirectional cross-references** per `rules/context-graph.md`: scan each new Layer-A record for `DR-*/SB-*/FB-*/A-*/L-*/DOC-*` references and link them in `crossReferences`.
4. Confirm the `MEMORY.md` pointer is present for the Layer-B entry. A harvest is the highest-value moment for cross-linking because the records are born together.

### 5. Surface drafted Decisions for affirmation (MANDATORY when any DR was drafted)

A DR this skill drafts is at most DPS `drafted` — not a closed decision. State plainly, in prose:

> "I've recorded **DR-YYYY-NNN** at `context/decisions/YYYY/DR-YYYY-NNN.md`. Per the Decision Provenance Standard it's at `drafted` and needs your affirmation to close — you're the accountable owner. Approve it as written, or want changes first?"

Only after the user approves do you populate the affirmation fields (user identity + timestamp) and set `Record State: closed`.

### 6. Report the harvest

Close with a summary across both layers:

```
Context harvest complete — "[scope]"
Layer A — organizational registry:
- DOC-2026-0NN  "Title"        → context/documents/index.md
- L-0NN         "Lesson"       → context/learnings/index.md
- DR-2026-0NN   "Decision"     → context/decisions/2026/ (drafted — awaiting your affirmation)
- A-0NN         "Assumption"   → context/assumptions/registry.md (Pending)
- FB-2026-0NN   "Feedback"     → context/feedback/2026/
- Cross-links:  DR-0NN↔A-0NN, DOC-0NN↔L-0NN, FB-0NN→DR-0NN
Layer B — recall memory:
- <slug>.md created + MEMORY.md pointer added
Skipped: Strategic Bet (none surfaced)
```

## Instructions

1. Determine scope (argument hint, or the current session).
2. Run `/context-recall {scope}` AND scan the recall-memory directory to anchor against both layers.
3. Reconstruct the work across all lenses, both layers (§1).
4. Use your judgment to decide what clears the bar and **create those records directly** (§2) — no approval gate, no candidate menu.
5. Read each affected index/file before editing; preserve existing entries; reserve every ID with `tools/allocate-id.py` (see ID Generation) — never by reading the current max and adding one.
6. Write the Layer-A records (canonical mechanics) and the Layer-B recall entry (§3).
7. Update all indexes + cross-references; confirm the MEMORY.md pointer (§4).
8. Surface any drafted DRs for human affirmation (§5).
9. Report what was saved, by layer (§6).

## ID Generation

`DOC-[YYYY]-[NNN]` · `DR-[YYYY]-[NNN]` · `SB-[YYYY]-[NNN]` · `A-[NNN]` · `L-[NNN]` · `FB-[YYYY]-[NNN]`. (Layer B uses a kebab-case slug, not a numeric ID.)

**Reserve every one of them with the allocator — never by reading the index for the highest number and adding one:**

```bash
python tools/allocate-id.py --ns DOC --note "<short reason>"     # then DR, SB, A, L, FB as needed
```

Use each printed id verbatim. **If it exits non-zero, do NOT guess a number** — re-run it; it refuses exactly when it cannot prove the id is free.

**This skill is the highest-risk minting site in the workspace: one harvest mints up to five ids across five namespaces**, so it holds a stale view of every index for the whole run. Read-the-index-and-add-one is what collided five ids on 2026-08-02, two of them *during* the cleanup fixing the first three. Call the allocator once per id, **at the moment you write that record** — not all six up front.

(Collision-safe across concurrent sessions on one machine, not across machines. If `tools/allocate-id.py` is absent from this workspace, fall back to reading the index — and verify each id is still free immediately before **and after** the write.)

## Guardrails

- **Both layers, every harvest.** Capturing the org registry but not the recall memory (or vice-versa) is the failure mode this skill prevents. If the operator doesn't use harness recall memory at all, they may skip Layer B — but offer it by default.
- **Judgment-led and automatic.** Don't present a candidate table or ask permission per record — decide what's worth keeping and create it, then report (§6). The only human gate is DR affirmation (§5), per DPS.
- **DPS human-gate on Decisions.** Draft at `drafted`/`[PENDING HUMAN AFFIRMATION]`; never self-close. (`rules/agent-spawn-protocol.md` Phase 1.5; the Decision Provenance Standard.)
- **No fabrication.** Do not manufacture records to fill rows, and do not invent financials/timelines (`rules/no-estimates.md`). `— none surfaced —` is correct when a type or layer has no candidate.
- **No duplicates.** Recall both layers first; if a near-identical record/entry exists, update it instead of creating a new one.
- **Layer B is a hook, not a copy.** The recall entry names artifacts + the non-obvious gotcha and links to Layer-A IDs; it does not restate them.
- **Feedback is mandatory when present.** Any customer/user signal encountered MUST be captured (`rules/context-management.md`).
- **Methodology-bound (Layer A).** Extension-Team-only work has no `context/` registry; harvest Layer B only in that case.

## Relationship to Adjacent Skills

| Skill | Difference |
|-------|------------|
| `/context-save` | Persists ONE already-identified Layer-A record. `/context-harvest` reviews the whole work and routes to ALL types across BOTH layers. |
| `/context-recall` | Reads Layer-A memory. `/context-harvest` writes both layers (and recalls first to avoid duplication). |
| `/feedback-capture` | Captures only feedback. `/context-harvest` calls it as one leg. |
| `/handoff` | Briefs the next agent (transient). `/context-harvest` persists durable records + recall memory. |
| `/decision-record`, `/strategic-bet`, `/assumption-map` | Single-type Layer-A authoring tools `/context-harvest` orchestrates. |
