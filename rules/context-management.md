---
globs:
  - "**/*"
---

# Context Management Rules

Organizational memory across sessions and agents. Auto-context injection (`auto-context.md`) and cross-references (`context-graph.md`) enhance this layer.

---

## Core Behaviors

### Auto-Registration of Strategic Documents (MANDATORY)

ALL skill outputs producing strategic documents MUST be auto-registered to `context/documents/index.md` with metadata (ID: `DOC-[YYYY]-[NNN]`, title, type, skill, date, owner, product, location, tags).

### After Creating Decisions or Bets

Auto-register → run `/context-save` → extract assumptions → update portfolio.

### Before Making Decisions

Run `/context-recall [topic]` → incorporate relevant context → flag conflicts with past decisions.

### When Encountering Feedback (MANDATORY)

ALL agents MUST capture feedback immediately via `/feedback-capture`.

### After Retrospectives and Outcome Reviews

Offer to save learnings → mark assumptions validated/invalidated → flag re-decision triggers.

---

## Principle Enforcement

| Trigger | Validators |
|---------|-----------|
| Creating commitments | `/ownership-map`, `/commitment-check` |
| Making decisions | `/customer-value-trace`, `/collaboration-check` |
| Committing resources | `/scale-check` |
| Phase transitions | `/phase-check` |

Before Phase 2→3 commitments: require `/ownership-map`, verify Phase 1-2 deliverables exist.

---

## ROI Display

See `roi-display.md` for all ROI calculation and display rules.

---

## Telemetry: `[Context Records]` (spawn-protocol §2.5)

The Spawn Audit Block's **`[Context Records]`** section (OS deliverable spawns) reports the non-DR context types created/updated this spawn — Assumptions (`A-`), Learnings (`L-`), Feedback (`FB-`), Strategic Bets (`SB-`), Documents (`DOC-`) — and cross-references `[Decision Records]` for DRs (never re-lists them). `os-tracker.py` prefers these structured sections over its blind scrape when an `[Outputs]` section is present, then registers the ids here. This makes context-type coverage auditable per spawn rather than convention-dependent.

---

## Context File Locations

| Type | Index | Records |
|------|-------|---------|
| Documents | `context/documents/index.md` | (by path) |
| Decisions | `context/decisions/index.md` | `context/decisions/[YYYY]/` |
| Strategic Bets | `context/bets/index.md` | `context/bets/[YYYY]/` |
| Assumptions | `context/assumptions/registry.md` | (in registry) |
| Portfolio | `context/portfolio/active-bets.md` | (in file) |
| Learnings | `context/learnings/index.md` | (in index) |
| Feedback | `context/feedback/index.md` | `context/feedback/[YYYY]/` |
| Interactions | `context/interactions/index.json` | `context/interactions/[YYYY]/` |

## ID Conventions

Documents: `DOC-[YYYY]-[NNN]` | Decisions: `DR-[YYYY]-[NNN]` | Bets: `SB-[YYYY]-[NNN]` | Assumptions: `A-[NNN]` | Learnings: `L-[NNN]` | Feedback: `FB-[YYYY]-[NNN]` | Themes: `TH-[NNN]` | Interactions: `IX-[YYYY]-[NNNNN]`

---

> "Organizational memory is a competitive advantage. Document decisions not for bureaucracy, but for learning velocity."
