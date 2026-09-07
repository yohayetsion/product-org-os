# CHANGELOG entry — to be appended to the distribution changelog at Day 10 tag

**Note for DevOps**: Insert these entries at the top of `the distribution changelog` at Day 10 tag.

---

## [5.1.0] - 2026-05-29 — Standard↔Substrate Reconciliation

v5.1.0 reconciles the Product Org OS substrate to the Decision Provenance Standard rev 7. The Standard manuscript is authoritative and unchanged; the substrate was brought into 1:1 field-and-signal alignment with it via the 18-change reconciliation list. The directory path stays `standard/v5.0/` (the v5.x line lives under `v5.0/`; the path is unchanged so the manuscript's `standard/v5.0/...` references remain valid). Full detail: `standard/v5.0/release/RELEASE-NOTES-v5.1.0.md`.

### Added
- 7 Standard-mandated conformance signals to `signal-vocabulary.md` + the OpenAPI `evidence_metric` enum (`every_affirmed_record_carries_affirmation_event`, `every_affirmed_record_carries_seal_hash`, `no_passive_promotion_to_affirmed_in_sample`, `superseded_records_retained_in_full`, `every_redaction_event_carries_operational_store_deletion_attestation`, `every_mode_2_record_carries_drafting_authority`, `altitude_to_consent_posture_binding_enforced`). Signal vocabulary is now 23 signals (6 L1 + 13 L2 + 4 L3).
- `charter.schema.json`: `use_case_scope_limit_declaration`, `works_council_consultation_record` (rev6 Wave 0d, conditional).
- `article-50-disclosure-metadata.json`: `content_type_tag`, `generation_timestamp` (both required; the Standard §4.6.2 five are now correct).
- `decision-record.schema.json`: §5.1/§6.2.3 lifecycle fields (`affirmation_record`, `seal_hash`, `seal_algorithm`, `supersedes`, `review_log`, `revision_history`), `altitude` + `consent_posture`, `drafting_authority`, the §6.2.3.2 redaction-event family (`record_type` discriminator + 9 fields), and the §6.2 dispatched/drafted/closed-state fields.

### Changed
- `decision-record.schema.json`: `dispatch_mode` enum extended to the exhaustive 3-value Standard enum (added `mode-1-with-embedded-mode-2-summary`); `record_id` renamed to `decision_id` (format `DR-YYYY-NNN`).
- Decision-record + Charter state machines: firing-authority bindings, dispatch_mode prose, two-state-family note, and the two new Charter fields on the `fields-completed` transition.
- README + RELEASE-NOTES-v5.0.0: signal count 8 → 23; corrected the Article-50 "five fields" enumeration; Naming Bridge updated to rev 7 / v5.1.0.

### Removed
- Orphan `soft_flag_rate_breach` value from the OpenAPI `evidence_metric` enum (duplicated the `escalation_type` concept; no signal-vocabulary home).

### Breaking Changes
None. Additive at the schema/enum level; new required fields are conditional (wired via `allOf`/`if-then`). Reporter wire contract (`schema_version: v1.0`) unchanged.

---

## [5.0.0] - 2026-05-XX (Phase 3 Day 10 target)

v5.0.0 is a major-version release marking Product Org OS's alignment to the Decision Provenance Standard v1.0. The version jump from v4.0.1 to v5.0.0 (skipping the v4.x release line) reflects the load-bearing nature of the Standard alignment: the OS now ships the runnable substrate (`standard/v5.0/`) for the Conformance Level 3 claim, which is a substantive scope expansion beyond the v4.x line, not a feature drop within it.

### Added — Vision to Value Standard Alignment Bundle

- **`standard/v5.0/`** — new top-level directory with the runnable substrate that supports the Conformance Level 3 claim:
  - `state-machines/charter-state-machine.md` — 5 forward-only states + `review-required` RECORD-state interrupt
  - `state-machines/decision-record-state-machine.md` — `dispatched` / `drafted` / `closed` + `review-required` interrupt
  - `schemas/article-50-disclosure-metadata.json` — 5 required Article 50 disclosure metadata fields per Section 4 §4.6 + 0.5.D (`declaring_authority`, `ai_system_identity`, `jurisdictional_applicability`, `content_type_tag`, `generation_timestamp`; corrected in v5.1.0)
  - `schemas/charter.schema.json` — Charter object schema (JSON Schema Draft 2020-12)
  - `schemas/decision-record.schema.json` — Decision-record object schema (JSON Schema Draft 2020-12)
  - `conformance/reporter-api-spec.md` — POST /v2v/conformance/charter-escalation contract per locked M1 spec
  - `conformance/reporter-api.openapi.yaml` — OpenAPI 3.1 wire contract
  - `conformance/signal-vocabulary.md` — signal vocabulary across Levels 1, 2, 3 + Seam 3 cadence binding
  - `mode-drift/layer-1-detection.md` — statistical detection scaffolding (D.2.1 sub-track owns enforcement post-launch)
  - `mode-drift/layer-2-audit-hook.md` — 4-question challenge prompt at Mode-1 record close (hot day-one)
  - `mode-drift/layer-3-mode-confirmation.md` — `review-required` RECORD-state interrupt + 5-rule peer-reviewer designation (hot day-one)
  - `mode-drift/layer-4-attestation.md` + `layer-4-attestation.schema.json` — `mode_classification_attestation` structured object with 8 required sub-fields, 4 jurisdictional variants (US/UK/EU/IL) (hot day-one — load-bearing for Day-3 binary scope-check)
  - `tests/cross-stream-conformance-check.md` — 9-category test matrix for Stream E
  - `tests/synthetic-charter-library.md` — 8 synthetic Charters covering all jurisdictions and edge cases

### Changed — 8 Named Structural-Primitive Skills

The following skills are aligned to emit Vision to Value Standard conformance signals (Level 1, 2, 3 vocabulary):

- `/decision-charter` — output schema matches Standard Section 3 (5-state lifecycle + 15 fields + 3-value mode-declaration enum)
- `/decision-record` — schema matches Standard Section 5 + adds `dispatch_mode` + `disclosure_metadata_pointer` fields
- `/escalation-rule` — aligns with Layer 3 Mode-Confirmation Audit primitive
- `/ownership-map` — emits `accountable_owner_named` Level 1 signal
- `/customer-value-trace` — emits Level 2 signal stub
- `/collaboration-check` — emits Level 2 signal stub
- `/scale-check` — emits Level 2 signal stub
- `/phase-check` — emits Level 1 + Level 2 signals

### Documentation

- README updated for Vision to Value Standard alignment + Conformance Level 3 claim per Conformance Framing Locked Language Table §A.4 (verbatim canonical claim)
- CLAUDE.md updated with Standard ↔ OS Interface Contract pointer (`standard/v5.0/`)
- Naming Directive Distribution Pack applied to all human-facing artifacts: "Vision to Value" full spelling in prose; "v2v" retained in API endpoint paths, code identifiers, file system paths only

### Deferred to v5.1 (4-6 weeks post-launch)

- ~125 ancillary OS skills receive Mode-awareness + disclosure metadata field alignment
- Layer 1 enforcement-mode activation (technically OS v5.0 lifecycle Week 7+)
- v5.1 release artifacts: skill-by-skill alignment patches, conformance coverage report, v5.1 CHANGELOG

v5.1 is NOT load-bearing for the Conformance Level 3 claim — it improves coverage breadth, not conformance depth.

### Breaking Changes

None for end users. The 8 named structural-primitive skills retain existing invocation syntax. For deployers integrating with the conformance reporter API: wire contract is new; no prior version exists.

### Authority

- Phase 3 dispatch plan v1.1 §M4
- Stream D scope spec v1
- M1 conformance reporter API contract (locked)
- Mode-Drift composed mitigation sub-spec FINAL
- 0.5.B Standard ↔ OS Interface Contract
- Conformance Framing Locked Language Table + Naming Directive Distribution Pack
