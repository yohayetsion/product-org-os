# Decision-Record State Machine — v5.0 Runnable Primitive

**Authority**: Standard §5 (Required Artifact Set) + 0.5.B Interface Contract §5
**Naming**: "Vision to Value Standard" full spelling in prose; `v2v_decision_record_state` in code identifiers

---

## States

```
   dispatched ──> drafted ──> closed
                      │
                      └──> review-required (interrupt)
                              │
                              ├──> closed
                              └──> re-opened-with-mode-migration ──> drafted
```

---

## Two State Families (Standard §5.1 vs §6.2)

The Standard maintains two distinct, non-conflated state families for a decision record:

- **§6.2 schema dispatch states** — carried on the `record_state` field: `dispatched` / `drafted` / `review-required` / `closed` / `re-opened-with-mode-migration`. These drive the dispatch/close workflow above.
- **§5.1 record lifecycle** — `draft` / `reviewed` / `affirmed`. This is NOT a separate enum field; it is expressed through population of `affirmation_record` + `seal_hash` (a record is in the `affirmed` lifecycle state once those carry a valid affirmation event and integrity seal per §5.1(3)).

Per A5-bis the two families are deliberately distinct and MUST NOT be conflated or normalized into one enum. The cross-stream conformance check (Category I/B) verifies BOTH families exist: the §6.2 states on `record_state`, and the §5.1 lifecycle via `affirmation_record`/`seal_hash` population. This note exists so the gate does not false-positive the deliberate two-family design as a divergence.

---

## Lifecycle

| State | Mode 1 behavior | Mode 2 behavior |
|---|---|---|
| `dispatched` | Human author opens decision under a Charter in `fields-completed`. AI worker prepares conformance-signal scaffold. | AI worker opens decision. Reads Charter state, decision context, prior records. Prepares substantive draft + disclosure metadata block. |
| `drafted` | Human writes substantive content. AI worker monitors conformance-signal completeness. | AI worker writes substantive content. Disclosure metadata block populates with `declaring_authority`, `ai_system_identity`, `jurisdictional_applicability`, `disclosure_text_pointer`. |
| `review-required` (interrupt) | Layer 1/2/3 routed flag. Holds at this state until peer reviewer disposition. | Same routing, plus the standard Mode 2 reviewer sign-off path. |
| `closed` | Layer 2 audit hook fires; all answers `Yes` → close authorized. Layer 4 attestation captured. AI worker writes final conformance signals. Record archives to schedule of records. | Human reviewer signs off; disclosure metadata block finalizes (`last_reviewed_at` set); Layer 4 attestation captured; record archives. |

---

## Required Fields at Close

Per `../schemas/decision-record.schema.json`:

- `decision_id` (stable identifier, format `DR-YYYY-NNN`; renamed from `record_id` in v5.1.0 reconciliation)
- `charter_id` (back-reference)
- `dispatch_mode` (`mode-1` | `mode-2` | `mode-1-with-embedded-mode-2-summary`; inherited from Charter `mode_declaration` at `dispatched`; may differ post-migration)
- `disclosure_metadata_pointer` (required when `dispatch_mode` ∈ {`mode-2`, `mode-1-with-embedded-mode-2-summary`} OR per-record edge case fires)
- `mode_classification_attestation` (Layer 4 structured object — required at `closed`; see `../mode-drift/layer-4-attestation.schema.json`)
- `layer_2_audit_trail` (the 10 fields per Layer 2 sub-spec)
- `peer_reviewer_disposition` (required when `review-required` was traversed)

---

## Layer 2 Hard Gate at Close

Before transitioning from `drafted` to `closed`, the dispatch state machine MUST:

1. Present the 4-question Mode-1 Substantive-Authorship Challenge to the declaring authority (Mode 1 records only — Mode 2 records skip Layer 2; their gate is the human reviewer sign-off + Layer 4).
2. Collect 4 answers + identity-bound attestation (Layer 2 attestation language verbatim).
3. If any answer is `No` or `Uncertain`, OR declaring authority declines, OR Layer-1-vs-Layer-2 inconsistency detected → route to `review-required`.
4. If all 4 answers `Yes` AND no Layer 1 inconsistency → proceed to `closed` AND require Layer 4 attestation.

Layer 2 does not itself authorize Mode classification — it gates the close transition. Mode classification is a downstream consequence via Layers 3 and 4.

---

## Conformance Signal Emissions

This state machine emits the following signals (per `../conformance/signal-vocabulary.md`):

**Level 1**:
- `every_record_carries_mode_declaration` — fires on transition into `closed` (validation: `dispatch_mode` populated)

**Level 2**:
- `every_mode_2_record_has_disclosure_block` — fires on transition into `closed` for Mode 2 records
- `every_mode_1_edge_case_record_has_disclosure_block` — fires on transition into `closed` for Mode 1 records carrying embedded-summary edge case
- `disclosure_block_required_fields_populated` — fires on transition into `closed` (validation: 5 required Article 50 disclosure fields all populated)
- `no_silent_mode_drift_in_sample` — sample-level signal; fires on Layer 3 audit cadence per Seam 3 convergence lock (NOT every record)
- `every_affirmed_record_carries_affirmation_event` — fires at the §5.1 `affirmed` lifecycle promotion (validation: `affirmation_record` populated)
- `every_affirmed_record_carries_seal_hash` — fires at the §5.1 `affirmed` lifecycle promotion (validation: `seal_hash` populated)
- `every_mode_2_record_carries_drafting_authority` — fires at `affirmed`/`closed` for Mode 2 records (validation: `drafting_authority.deployer_role_pointer` populated)
- `no_passive_promotion_to_affirmed_in_sample` — sample-level signal; audits a sample of `affirmed` records for §5.2 affirmative-human-act compliance (NOT every record)
- `every_redaction_event_carries_operational_store_deletion_attestation` — sample-level signal; reads field population of `operational_store_deletion_attestation` on `record_type: redaction_event` records per Seam 3 cadence (§4.8.2)
- `altitude_to_consent_posture_binding_enforced` — sample-level signal; audits `altitude: individual-professional` records for consent-posture binding per §6.2.3.1 (emitted in conjunction with the access-policy layer)

**Level 3**:
- `escalation_rule_records_present_when_invoked` — fires when Charter `escalation_rule` fires AND a corresponding decision record exists
- `disclosure_review_cadence_current` — fires when `last_reviewed_at` within Privacy Counsel's review-cadence threshold per Section 4
- `superseded_records_retained_in_full` — reporter/Level-3 signal; fires on-demand/every-transition (validation: superseded records remain in schedule, immutable; current record carries `supersedes` reference per §5.1(3))

---

## Mode Migration Backpointers

When a record's mode migrates (Mode 1 → Mode 2 or Mode 2 → Mode 1), `prior_state_archive` captures the pre-migration state with `demotion_path` enum: `review-driven` | `audit-driven` | `escalation-driven`. The original draft is preserved; the migrated record has a `migration_reference` field pointing back to the prior state archive.

---

*Locked for v5.0. Layer 2 hard gate at close is the load-bearing structural mitigation that catches latent-influence drift before Layer 4 attestation binds the named human.*
