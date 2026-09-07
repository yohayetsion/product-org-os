# Product Org OS v5.1.0 — Standard↔Substrate Reconciliation Release

**Release Date**: 2026-05-29
**Tag**: `v5.1.0`
**Authority**: Chief Architect (owner of Decision Provenance Standard conformance integrity + v5.0 substrate schemas), per maintainer sign-off on the 18-change reconciliation list (2026-05-29)
**Directory path**: `standard/v5.0/` — UNCHANGED. The v5.x substrate line continues to live under the `v5.0/` directory so the Decision Provenance Standard manuscript's `standard/v5.0/...` references remain valid. v5.1.0 is the version *label* of the substrate; the *path* stays `v5.0/`.

---

## What This Release Is

v5.1.0 reconciles the Product Org OS substrate to the **Decision Provenance Standard rev 7** (rev7-WORKING-2026-05-29). The Standard manuscript is authoritative and was NOT changed. Every one of the 18 reconciliation changes brings the substrate into 1:1 field-and-signal alignment with what the Standard already mandates. No deployer behavior breaks (the substrate had not shipped to a real deployer; the reporter wire contract is brand-new). All changes are additive at the JSON-schema and enum level.

This flips the cross-stream conformance-check gate (Categories G + I) from NO-GO → GO without any manuscript edit. The Standard remains v1.0-conformance-stable.

---

## Changes Applied (18)

### Category G — Signal Vocabulary 1:1 Binding (8 changes)

The signal set is reconciled to **23 signals** (was: 16 in `signal-vocabulary.md`, 17 in the OpenAPI enum with one orphan). Added 7 Standard-mandated signals, moved 1 between levels, removed 1 orphan enum value.

- **G1** — Added `every_affirmed_record_carries_affirmation_event` (Level 2) to `signal-vocabulary.md` + OpenAPI enum.
- **G2** — Added `every_affirmed_record_carries_seal_hash` (Level 2).
- **G3** — Added `no_passive_promotion_to_affirmed_in_sample` (Level 2, sample-level).
- **G4** — Added `superseded_records_retained_in_full` (Level 3).
- **G5** — Added `every_redaction_event_carries_operational_store_deletion_attestation` (Level 2, sample-level).
- **G6** — Moved `re_decision_triggers_firing_on_schedule` from Level 2 to Level 3 (per Standard §7.4.2).
- **G7** — Removed orphan `soft_flag_rate_breach` from the OpenAPI `evidence_metric` enum (it duplicated the `escalation_type` concept and had no signal-vocabulary home).
- **G8** — Added `every_mode_2_record_carries_drafting_authority` + `altitude_to_consent_posture_binding_enforced` (both Level 2; from the Standard §7.1 integrated lifecycle-signals table).

Post-change: `signal-vocabulary.md` and the OpenAPI `evidence_metric` enum are the identical 23-signal union. Level split: 6 L1 + 13 L2 + 4 L3.

### Category I — Standard↔OS Field Alignment (13 changes)

- **I1** — `charter.schema.json`: added `use_case_scope_limit_declaration` (conditional, rev6 Wave 0d).
- **I2** — `charter.schema.json`: added `works_council_consultation_record` (conditional, rev6 Wave 0d).
- **I3** — `article-50-disclosure-metadata.json`: added `content_type_tag` (required, controlled vocabulary).
- **I4** — `article-50-disclosure-metadata.json`: added `generation_timestamp` (required; distinct from the substrate-extra `attached_at`).
- **I5** — `disclosure_text_pointer` / `attached_at` retained as permitted substrate extras (not removed; gate tolerates extras). The Standard-required five are now correct: `declaring_authority`, `ai_system_identity`, `jurisdictional_applicability`, `content_type_tag`, `generation_timestamp`. The §4.6.3 4-of-5 anonymization rule now maps correctly.
- **I6** — `decision-record.schema.json`: `dispatch_mode` enum extended to the 3-value Standard enum `["mode-1", "mode-2", "mode-1-with-embedded-mode-2-summary"]` (was 2-value; the charter schema already had 3).
- **I7** — `decision-record.schema.json`: added §5.1/§6.2.3 lifecycle fields `affirmation_record`, `seal_hash`, `seal_algorithm`, `supersedes`, `review_log`, `revision_history`.
- **I8** — `decision-record.schema.json`: added `altitude` (required from draft) + `consent_posture` (conditional on altitude).
- **I9** — `decision-record.schema.json`: added `drafting_authority` (conditional-required on Mode 2 / mode-1-with-embedded-mode-2-summary).
- **I10** — `decision-record.schema.json`: added the §6.2.3.2 redaction-event family (`record_type` discriminator + `target_record_hash`, `target_decision_id`, `redacted_fields`, `redaction_basis`, `redaction_basis_detail`, `redaction_authority`, `redaction_timestamp`, `operational_store_deletion_attestation` [4 sub-fields], `archival_record_retention_basis`), conditional-required on `record_type == redaction_event`.
- **I11** — `decision-record.schema.json`: renamed `record_id` → `decision_id` (format `DR-YYYY-NNN`); added the dispatched/drafted/closed-state §6.2 fields (`accountable_owner`, `decision_class`, `dispatched_at`, `decision_statement`, `context_at_decision`, `options_considered`, `required_inputs_used`, `assumptions_depended_on`, `success_criteria`, `accountable_owner_signoff`, `re_decision_trigger`, `record_location`, `related_decisions`), wired conditional-required via `allOf`/`if-then` on `record_state`. Mode-Drift fields (`mode_classification_attestation`, `layer_2_audit_trail`, `peer_reviewer_disposition`, `prior_state_archive`) preserved.
- **I12** — No enum change to `record_state`: the §5.1 lifecycle and §6.2 dispatch states are the deliberate two distinct families (A5-bis). A prose mapping note was added to the decision-record state machine (SM3) so the gate does not false-positive.
- **I13** — Verification only: G1–G8 close Category I check #4 (each §6/§7 criterion now has ≥1 signal).

### State-machine + doc-sync (SM1–SM4)

- **SM1** — `decision-record-state-machine.md`: bound firing authority for the 7 new signals in Conformance Signal Emissions.
- **SM2** — `decision-record-state-machine.md`: patched the 2-value `dispatch_mode` prose to 3-value; renamed `record_id` → `decision_id`.
- **SM3** — `decision-record-state-machine.md`: added the §5.1-vs-§6.2 two-state-family mapping note.
- **SM4** — `charter-state-machine.md`: added the two new Charter fields to the `fields-required → fields-completed` transition row.

### Doc/release surfaces (D-1 to D-3)

- **D-1** — README signal count `8-signal` → `23-signal`.
- **D-2** — README + RELEASE-NOTES-v5.0.0 Article-50 "five fields" enumeration corrected to the right five.
- **D-3** — README Naming Bridge updated: Book → "Decision Provenance Standard rev 7"; Substrate → "v5.1.0 ... at Conformance Level 3 (path: `standard/v5.0/`)"; reconciliation recorded as executed.

---

## Version Decision

**v5.1.0 (minor).** Selected by the maintainer 2026-05-29 to read the reconciliation as a visible milestone rather than a quiet patch. (The Chief Architect's engineering recommendation in the change-list was v5.0.1 patch on erratum-alignment grounds; the maintainer's framing call to v5.1.0 governs.) The change is additive at the schema/enum level and breaks no shipped deployer; the load-bearing claim — *"Product Org OS implements the Decision Provenance Standard's reporter protocol at Conformance Level 3"* — remains true and is now structurally backed by the full signal set and field set the Standard mandates.

---

## Directory Path Handling

The directory remains `standard/v5.0/`. It was NOT renamed. The Decision Provenance Standard manuscript references `standard/v5.0/...` paths and must not be edited; renaming the directory would break those references. The v5.x substrate line therefore lives under the `v5.0/` path with v5.1.0 as the version label. This is recorded in the README Status line and Naming Bridge.

---

## Breaking Changes

None. Schema additions are additive; new required fields are conditional (wired via `allOf`/`if-then` on state/mode/altitude/record_type) and do not retroactively invalidate the existing Mode-Drift-focused records. The OpenAPI enum gained 7 values and lost 1 orphan that no conformant emitter referenced. The reporter wire contract (`schema_version: v1.0`) is unchanged.

---

*v5.1.0 release notes authored 2026-05-29 by 🏗️ Chief Architect as part of the Standard↔substrate reconciliation. The Standard manuscript (rev7-WORKING) is authoritative and unchanged.*
