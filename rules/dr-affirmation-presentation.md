# Decision-Record Affirmation Presentation (MANDATORY)

How decision records (DRs) are presented to the accountable owner **for affirmation** — whether inline or as a review deck. This governs *presentation for the human-affirmation gate*, not how DRs are authored (`/decision-record`) or the DPS itself.

**Why:** the owner is the named accountable authority who closes every DR (DPS: agent drafts → human affirms to `closed`). If he can't readily understand what he's affirming, the gate degrades into rubber-stamping — which defeats the DPS. **Affirmation requires comprehension.** Source: FB-2026-030 (2026-06-14).

---

## The Rule (NON-NEGOTIABLE)

When surfacing ANY DR for affirmation, present it in **TWO layers, in this order**:

### Layer 1 — Plain language (lead with this, ALWAYS)
Three short beats, in business/plain terms — no engine/architecture/methodology jargon (or jargon defined in one clause):
1. **What this is** — what changed, in plain terms.
2. **Why** — the reason / the problem it solves.
3. **What affirming commits** — what the owner is signing off on (and whether it's already been built/executed).

### Layer 2 — The DPS structure (the close-block the standard dictates)
Present each DR in the structure from `../knowledge/os-support/standard/v5.0/state-machines/decision-record-state-machine.md`:
- **Decision** (one line)
- **Record State** (§6.2): `dispatched` | `drafted` | `review-required` | `closed` — show the current state and that it's *awaiting affirmation*.
- **Dispatch Mode**: `mode-1` (human-led) | `mode-2` (AI worker drafted, human affirms) | `mode-1-with-embedded-mode-2-summary`.
- **Layer-2 substantive-authorship gate** (mode-1 only): the human-authorship basis.
- **Layer-4 attestation / accountable-owner signoff** (required at `closed`).
- **Supersedes / Implements / Evidence / Links** as applicable.
- **§5.1 lifecycle**: `draft` → `reviewed` → `affirmed`.

---

## Format specifics
- **One DR per slide/section** in a review deck (so each gets its own affirmation chip / inline comment anchor). Generate the deck via `agent-output-handler.py --brand <project-brand>` (per `agent-output-automation.md`).
- **Show already-affirmed DRs** in the same review marked `AFFIRMED → closed` (with the signoff line) so the owner sees the full slate, not only the pending ones.
- **Affirmation ask** per DR: a one-line, explicit "affirm / affirm-with-changes / decline" prompt.
- On affirmation: populate the Layer-4 attestation + accountable-owner signoff with the owner's identity + timestamp, set Record State → `closed`, §5.1 → `affirmed`. Never auto-close; never fabricate a `seal_hash` — record the affirmation event in prose.

## What a worked instance looks like

A slate of related DRs presented as ONE deck — one DR per slide, each slide carrying its own
affirmation ask, and the already-affirmed records shown alongside the pending ones so the owner
sees the full slate rather than only what is outstanding. Per slide:

```
DR-YYYY-NNN — <the decision in one line>

WHAT THIS IS      <plain terms, no jargon>
WHY               <the problem it solves>
AFFIRMING COMMITS <what the owner is signing off on; whether it is already built>

Record State: drafted -> awaiting affirmation   |   Dispatch Mode: <mode>
Supersedes / Implements / Evidence: <ids, or none>

Affirm  /  Affirm with changes  /  Decline
```

Where instances exist locally they live **beside the work they governed**, as
`dr-affirmation-review-YYYY-MM-DD.md` in that project's `Product/` folder — **not** in
`context/decisions/`, which indexes the decision records themselves, not the review decks.

---

> "An affirmation the owner doesn't understand isn't governance — it's a signature. Plain language earns the signature; the DPS structure makes it auditable."
