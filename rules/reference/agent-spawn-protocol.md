# Companion — agent-spawn-protocol (relocated reference)

> Relocated rationale/reference — the binding rule is `.claude/rules/agent-spawn-protocol.md`;
> this file imposes nothing and relaxes nothing. Moved VERBATIM 2026-08-15
> (DR-2026-262). Do not edit here
> without the same review the rule itself requires.

---

<!-- from agent-spawn-protocol · REFERENCE-MOVE · v1→v2 + 2026-08-01 changelog blocks -->

**2026-08-01 change (hours-only switch, O1+O2)**:
- **DELETED**: `[Post-Execution ROI]` from every Audit Block schema (single, non-deliverable, ET, joint). Agents report NOTHING about their own value or time saved. Hours are computed downstream from the owner-affirmed activity table — see §3.

**v2 changes from v1**:
- **DELETED**: `Mode:` field. `lightweight_spawn` exception (entire section). All escape hatches.
- **REPLACED**: `📋 Pre-Execution Self-Check` telemetry block → unified `📋 Spawn Audit Block` covering loads + decision records (+ ROI, until its 2026-08-01 retirement).
- **NEW**: Phase 1.5 DR Context Check for OS agents on deliverable tasks (READ → SNIFF → DRAFT/UPDATE).
- **NEW**: Multi-Agent DR Ownership Rule — synthesis owner carries DRs; sub-agents skip.
- **NEW**: Verify-Before-Declaring-Missing step (no fabricated ✗).
- **NEW**: Inline-Persona Exclusion (no Audit Block when there is no Task-tool spawn).
- **NEW**: Joint-Authoring schema with N-author support + mandatory attribution rule.
- **NEW**: Machine-checkable schema; validator at `tools/hooks/audit-block-validator.py`.

---

<!-- from agent-spawn-protocol · DUPLICATE-POINTER · §3 computed-hours ROI model restatement (canonical: .claude/rules/roi-display.md) -->

**Agents report nothing about their own value.** The per-spawn `[Post-Execution ROI]` section left the Audit Block schema on 2026-08-01. No agent — single, joint, sub-agent, gateway, or synthesizer — emits time-saved figures, token counts, cost figures, or value figures about its own work, and no synthesizer emits an aggregate ROI footer.

How ROI is produced and shown instead:

- **Hours come from the owner-affirmed activity table**, resolved per canonical agent slug by the telemetry pipeline: each spawn's receipt is priced from the table's per-seat time basis (`baseMinutes`), with the frozen alias map supplying the canonical slug (identity for unmapped slugs). A spawn whose seat has no affirmed table row is **counted, not priced** — visible with its spawn count, contributing zero hours, never estimated and never given a default.
- **Aggregation and presentation are the dashboard's and the weekly email's job**, never the agent's or the synthesizer's. Coverage (priced spawns / receipts) is stated wherever hours are shown.
- **Hours only.** There is no dollar value figure, no rate table, and no $/hr anywhere in the value chain.
- **Sensitive framing** on any displayed hours follows `.claude/rules/roi-display.md` → Sensitive Skill ROI Framing ("drafting and triage", never "review") — that control is unchanged and binds the dashboard, the weekly email, and any user-facing surface.
