# Conformance Reporter API Contract — POST /v2v/conformance/charter-escalation

**Authors**: 🤖 AI Architect + 🛠️ Backend Dev + 🏗️ Chief Architect
**Date**: 2026-04-30 (v1.0); v1.1 amendment 2026-04-30 — see Amendment Log at end of file
**Status**: Locked at v1.1 for Stream D dispatch (Stream G cleanup pass)
**Spec version**: 1.1.0 (matches OpenAPI YAML `info.version`)
**Gates**: Phase 3 Stream D Day 4 implementation; Stream E cross-stream conformance check
**Cross-references**: 0.5.B Interface Contract §6.3 (signal vocabulary); Mode-Drift sub-spec FINAL Layer 3 (audit-cadence binding); Phase 3 dispatch plan v1.1 §M1

---

> ⚠️ **Not legal advice.** This spec is a drafting and triage aid produced by simulated architecture agents in a product-organization scaffolding workflow. It defines the wire contract for one runnable primitive in the OS skill bundle; it does not declare conformance with any regulation or standards body and creates no attorney-client relationship.
>
> **Jurisdiction Assumed:** U.S. federal + Delaware (primary); UK / EU AI Act / Israel (named secondaries per 0.5.B §1). Where deployer jurisdiction differs, treat the auth model and rate-limiting defaults as hypotheses to verify with local counsel and IT-governance review.

---

## Endpoint

```
POST /v2v/conformance/charter-escalation
```

**Purpose.** Single-write endpoint by which a deployer-side Conformance Reporter emits a Charter-level escalation event (Layer-1 soft-flag-rate breach, Layer-2 audit-hook breach, Layer-3 peer-review demotion, Layer-4 attestation refusal, or Charter `escalation_rule` invocation per 0.5.B Interface Contract §3.2) into the Standard's escalation surface. The endpoint records process; it does not certify a Charter as compliant or grade conformance level. Grading is the conformance-level reporter's separate read surface (out of scope for this contract).

**Bound to substrates.** §3 Charter state model (`charter_id`, `escalation_rule`); §6 conformance-signal vocabulary (signals listed in §6 below are the fixed enumeration the `evidence_metric` field validates against); Mode-Drift sub-spec Layer 3 audit-cadence binding (escalation events emitted by the peer-review primitive use this endpoint).

---

## 1. Auth Model

**Choice: Deployer-side OAuth 2.0 client_credentials flow (RFC 6749 §4.4) over TLS 1.3.**

- Token endpoint: `POST /v2v/oauth2/token` (separate from this contract).
- Scope required on access token: `conformance:write`.
- Bearer presented in `Authorization: Bearer <token>` header.
- Token TTL: 1 hour. Refresh via re-issuance against client_credentials (no refresh token — short TTL acceptable because escalation traffic is bursty + low volume).
- Client identity (`client_id`) MUST be provisioned per deployer organization, never per Charter. Deployers may emit escalations for any Charter whose `accountable_owner` is registered under the deployer's `client_id`.

**Rationale.**

1. **API keys rejected** because (a) static keys leak silently and Charter-escalation events carry `accountable_owner` identity that should not be implicitly bound to a leaked credential, and (b) client_credentials gives the deployer a structural rotation path without re-provisioning the Charter binding.
2. **Deployer-side, not user-side.** The Reporter is a deployer-operated component running inside the deployer's environment; it asserts the deployer's own identity, not an end-user's. User-delegated flows (authorization_code) would couple Charter-level events to individual end-user sessions, which is the wrong granularity.
3. **TLS 1.3 not negotiable.** Lower TLS versions rejected at the listener.

**Rejected alternative.** Static `Authorization: ApiKey <key>` was considered for Phase 3 simplicity. Rejected because the Layer-4 named-attestor binding upstream depends on identity-bound provenance that survives credential rotation; static keys conflate "rotated last week" with "different deployer," which corrupts the audit trail.

---

## 2. Idempotency

**Required header on every POST: `Idempotency-Key: <uuid-v4>`.**

- The `Idempotency-Key` is generated client-side by the Reporter, scoped to the deployer + Charter + escalation event.
- Server retains the `(client_id, Idempotency-Key)` tuple for **24 hours** in a dedup cache.
- On replay within the window with identical request body hash → server returns the original response (status code, body, headers) verbatim. No side effects.
- On replay within the window with **divergent** request body hash → server returns `409 Conflict` with `error_code: idempotency_key_reuse_with_divergent_body`. This catches the Reporter-bug case where the same `Idempotency-Key` accidentally attaches to two distinct events.
- Beyond 24 hours, the same `Idempotency-Key` is treated as fresh (deployers MUST NOT rely on cross-day dedup; the SLO is one operational day).

**Server-side request-hash dedup window.** Independent of `Idempotency-Key`, server hashes `(client_id, charter_id, escalation_type, evidence_window_start, evidence_window_end, escalation_timestamp)` and rejects identical hash within **5 minutes** as `409 Conflict` with `error_code: duplicate_escalation_in_dedup_window`. This catches Reporter retry storms where the client forgot to set `Idempotency-Key`.

**Retry semantics.** Reporters MUST retry on 5xx + 429 with exponential backoff (initial 1s, factor 2, max 60s, max 6 attempts). Reporters MUST NOT retry 4xx (except 429); 4xx responses indicate a contract violation that retrying does not resolve.

---

## 3. Response Shape

**Choice: Synchronous ack-only.** No async pattern; no `status_url`; no polling.

**Success response (201 Created):**

```json
{
  "escalation_id": "esc_01HXYZ...",
  "charter_id": "ch-pmm-positioning-lock",
  "accepted_at": "2026-05-12T14:33:18.421Z",
  "received_signals": ["soft_flag_rate_breach", "no_silent_mode_drift_in_sample"],
  "schema_version": "v1.0"
}
```

- `escalation_id`: server-generated stable identifier (ULID), opaque to the Reporter; used by the conformance-level reporter's read surface to back-reference the event into the schedule of records.
- `accepted_at`: server timestamp of acceptance (ISO 8601 with milliseconds, UTC).
- `received_signals`: echoes the conformance signals (per 0.5.B §6.3) that the server parsed from `evidence_metric`. Any unrecognized signal in the request is rejected at validation (§4 below) — this echo is for the Reporter's own audit trail.
- `schema_version`: pinned `v1.0` for the lifetime of this contract.

**Rationale.** Async with status URL was rejected because:
1. The escalation event is itself a recorded process artifact; it is NOT a long-running computation. The server's only work is validate + persist + acknowledge.
2. Async forces the Reporter to maintain polling state and re-attach the result to its own audit trail, which adds a class of "lost-poll" failure modes the sync contract does not have.
3. Stream E's cross-stream conformance check walks synthetic Charters and verifies escalation events round-trip; sync makes that test deterministic in a single request.

The endpoint is bounded to ≤ 500ms p99 server-side. If a deployer's Reporter cannot accept a 500ms blocking call, the Reporter should batch escalations into its own background queue and call this endpoint from the queue worker (the deployer's design choice, not this contract's concern).

---

## 4. Error Semantics

**Standardized error envelope (every 4xx + 5xx response):**

```json
{
  "error_code": "invalid_evidence_metric",
  "error_message": "evidence_metric 'mode_certified_compliant' is not a recognized conformance signal. Reference 0.5.B Interface Contract §6.3.",
  "error_field": "evidence_metric",
  "retry_after": null,
  "trace_id": "trc_01HXYZ...",
  "schema_version": "v1.0"
}
```

| Status | When | `error_code` examples | `retry_after` |
|---|---|---|---|
| 400 Bad Request | Malformed JSON, missing required field, schema-validation failure (per §6 below) | `invalid_evidence_metric`, `missing_required_field`, `malformed_json`, `unknown_escalation_type` | null |
| 401 Unauthorized | Missing / expired / malformed bearer token | `token_missing`, `token_expired`, `token_malformed` | null |
| 403 Forbidden | Token valid but `client_id` not authorized for the asserted `charter_id` (Charter `accountable_owner` not registered to this deployer) | `charter_not_owned_by_client`, `scope_insufficient` | null |
| 409 Conflict | Idempotency-key reuse with divergent body; duplicate escalation within 5-minute server-side dedup window | `idempotency_key_reuse_with_divergent_body`, `duplicate_escalation_in_dedup_window` | null |
| 422 Unprocessable Entity | Request structurally valid but semantically inconsistent (e.g., `escalation_timestamp` later than `evidence_window_end`; `evidence_threshold` outside the metric's defined range) | `timestamp_outside_evidence_window`, `evidence_threshold_out_of_range`, `escalation_type_metric_mismatch` | null |
| 429 Too Many Requests | Per-deployer token bucket exhausted (per §5) | `rate_limit_exceeded` | seconds (integer) until next refill |
| 500 Internal Server Error | Server fault; persistence failure | `internal_error` | null |
| 502 Bad Gateway | Upstream persistence layer unreachable | `persistence_unreachable` | null |
| 503 Service Unavailable | Maintenance window or graceful degradation | `service_unavailable` | seconds (integer) |

**Error envelope discipline.**
- `trace_id` MUST be present on every error response so the deployer can correlate against server-side logs without exposing internal log identifiers.
- `error_message` is human-readable but stable per `error_code` (Reporters may match on `error_code`, never on `error_message` substring).
- `retry_after` populated only on 429 + 503; null elsewhere (NOT zero — null signals "do not retry on this error class").

---

## 5. Rate Limiting

**Per-deployer token bucket.**

- **Default**: 60 escalations per minute, burst 120 (token bucket capacity 120, refill 1 per second).
- **Override mechanism**: per-`client_id` rate-limit override is a server-side configuration; deployers request increases via the deployer-onboarding ticket process (out of band — not exposed via API). The override request requires (a) a Charter-count justification (deployers with > 50 active Charters typically need a higher floor) and (b) a Layer-1 soft-flag rate forecast (deployers with high anticipated drift detection need higher burst).
- **Override ceiling**: 600/min, burst 1200. Above the ceiling, the deployer's traffic shape suggests Reporter misconfiguration or batch-emit anti-pattern — IT-governance review required before further increase.

**Bucket scope.** `client_id`, NOT `(client_id, charter_id)`. A deployer with a noisy Charter does not consume rate-limit budget that a different deployer would otherwise have.

**429 behavior.** Server returns `Retry-After: <seconds>` as both an HTTP header and the `retry_after` field in the error envelope (redundant by design; Reporters parse whichever they prefer). The seconds value is the time until the bucket has at least 1 token, rounded up.

**Rationale.** 60/min is well above the expected steady-state escalation rate for a single deployer (Layer-1 hard flags are bounded by 5%-of-records-sampled-at-15%; Layer-2 hook breaches and Layer-3 peer-review demotions are bursty but low-volume). The 120 burst handles end-of-cadence batches (e.g., a deployer's monthly Charter audit firing many escalations in a window). Above 600/min, the Reporter is probably emitting one event per record rather than aggregated Charter-level escalations, which violates the contract's intent.

---

## 6. Request Payload Schema

**Content-Type: `application/json`. UTF-8.**

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "additionalProperties": false,
  "required": [
    "schema_version",
    "charter_id",
    "escalation_type",
    "evidence_window",
    "evidence_metric",
    "evidence_threshold",
    "escalation_timestamp",
    "accountable_owner_ref"
  ],
  "properties": {
    "schema_version": {
      "type": "string",
      "const": "v1.0"
    },
    "charter_id": {
      "type": "string",
      "pattern": "^[a-z0-9][a-z0-9-]{2,127}$",
      "description": "Stable Charter slug per 0.5.B Interface Contract §3.2."
    },
    "escalation_type": {
      "type": "string",
      "enum": [
        "layer_1_soft_flag_rate_breach",
        "layer_1_hard_flag_record",
        "layer_2_audit_hook_breach",
        "layer_3_peer_review_demotion",
        "layer_4_attestation_refusal",
        "charter_escalation_rule_invoked",
        "disclosure_review_cadence_overdue",
        "schedule_of_records_exception",
        "peer_reviewer_pool_underflow"
      ]
    },
    "evidence_window": {
      "type": "object",
      "additionalProperties": false,
      "required": ["start", "end"],
      "properties": {
        "start": {"type": "string", "format": "date-time"},
        "end": {"type": "string", "format": "date-time"}
      }
    },
    "evidence_metric": {
      "type": "string",
      "description": "MUST be a named signal from 0.5.B Interface Contract §6.3 (Level 1, 2, or 3 signal vocabulary). Free-text values rejected.",
      "enum": [
        "charter_state_is_fields_completed",
        "mode_declaration_populated",
        "schedule_of_records_committed",
        "record_location_resolvable",
        "accountable_owner_named",
        "re_decision_triggers_minimum_met",
        "every_record_carries_mode_declaration",
        "every_mode_2_record_has_disclosure_block",
        "every_mode_1_edge_case_record_has_disclosure_block",
        "disclosure_block_required_fields_populated",
        "no_silent_mode_drift_in_sample",
        "re_decision_triggers_firing_on_schedule",
        "escalation_rule_records_present_when_invoked",
        "disclosure_review_cadence_current",
        "schedule_of_records_queryable",
        "conformance_level_reporter_output_recent",
        "soft_flag_rate_breach"
      ]
    },
    "evidence_threshold": {
      "type": "object",
      "additionalProperties": false,
      "required": ["operator", "value", "observed"],
      "properties": {
        "operator": {"type": "string", "enum": ["gt", "gte", "lt", "lte", "eq", "neq"]},
        "value": {"type": ["number", "string", "boolean"]},
        "observed": {"type": ["number", "string", "boolean"]},
        "unit": {"type": "string"}
      }
    },
    "escalation_timestamp": {
      "type": "string",
      "format": "date-time",
      "description": "When the Reporter detected the escalation. MUST fall within evidence_window.start ≤ ts ≤ evidence_window.end + 24h. 422 if outside."
    },
    "accountable_owner_ref": {
      "type": "string",
      "description": "Reference to the Charter's accountable_owner per 0.5.B §3.2. Server verifies (a) reference resolves and (b) the accountable_owner is registered under the asserted client_id."
    },
    "narrative": {
      "type": "string",
      "maxLength": 2000,
      "description": "Optional. Reporter-supplied human-readable context. Indexed for downstream peer reviewer surface; never authoritative."
    },
    "linked_record_ids": {
      "type": "array",
      "items": {"type": "string"},
      "maxItems": 200,
      "description": "Optional. Decision record IDs this escalation pertains to. Bounded at 200 — for larger sets, emit a Charter-level escalation and link the schedule export."
    },
    "classifier_metadata": {
      "type": "object",
      "description": "Required when escalation_type is layer_1_*. Per Mode-Drift sub-spec Layer 1 corpus-version provenance.",
      "additionalProperties": false,
      "properties": {
        "classifier_version": {"type": "string"},
        "corpus_version": {"type": "string"},
        "confidence": {"type": "number", "minimum": 0, "maximum": 1}
      }
    }
  },
  "allOf": [
    {
      "if": {"properties": {"escalation_type": {"pattern": "^layer_1_"}}},
      "then": {"required": ["classifier_metadata"]}
    }
  ]
}
```

**Validation strictness.** `additionalProperties: false` at every object level. Unknown fields rejected with `400 unknown_field`. The conformance signal enumeration in `evidence_metric` is the contract's tightest binding to 0.5.B §6.3 — any signal not in the enum is a contract violation, not a pass-through.

**Field-pair semantic checks (422-class):**
- `escalation_timestamp` MUST satisfy `evidence_window.start ≤ ts ≤ evidence_window.end + 24h` (24h grace allows post-window detection).
- `escalation_type` and `evidence_metric` MUST be a recognized pair (e.g., `layer_1_soft_flag_rate_breach` → `soft_flag_rate_breach`; `schedule_of_records_exception` → `schedule_of_records_queryable` or `every_record_carries_mode_declaration`). Mismatches return `422 escalation_type_metric_mismatch`.
- `evidence_threshold.operator` + `value` + `observed` MUST yield a true comparison consistent with the threshold being breached (e.g., if `operator=gt`, `value=0.05`, `observed=0.07` is consistent; `observed=0.03` is inconsistent → `422 evidence_threshold_not_breached`).

---

## Open Questions for Stream D Implementation

The lock above fixes the wire contract. The following items are deliberately preserved for Stream D Backend Dev / Chief Architect implementation judgment, with named bounds:

1. **Persistence layer choice**: append-only event log vs. relational + audit-trigger pattern. Either acceptable provided the `(escalation_id, accepted_at)` tuple is stable and queryable by `client_id` and `charter_id` from day one. Stream E's cross-stream conformance walk reads via a separate read API (out of scope for this contract).
2. **`trace_id` format**: ULID, UUID v4, or W3C `traceparent`-derived. Stream D may pick; the only binding is opacity and stability per request.
3. **OAuth client_credentials issuer co-location**: same service or separate identity-provider service. Either acceptable; the bearer-token validation contract is the same.
4. **Layer-1 `classifier_metadata` schema versioning**: this contract pins `classifier_version` + `corpus_version` as opaque strings. The internal taxonomy of those strings is a Layer-1 implementation concern (Mode-Drift sub-spec FINAL §Layer 1 corpus provenance) and may evolve without breaking this contract.
5. **`narrative` indexing strategy**: full-text vs. metadata-only. Indexing choice is downstream; the field is delivered to peer-reviewer surfaces via the read API.
6. **Webhook fan-out for Stream E**: whether Stream E subscribes to escalation events via a separate webhook or polls the read API. Out of scope for this contract; both patterns can be layered atop the persisted event log.

Items NOT preserved (locked): everything in §§1-6 above. Deviations require a v1.1 contract amendment with `ai-architect` + `backend-dev` + `chief-architect` co-sign, NOT a Stream D runtime workaround.

---

## Cross-References

- **0.5.B Interface Contract §3.2** — Charter state model; `charter_id`, `accountable_owner`, `escalation_rule` field semantics.
- **0.5.B Interface Contract §6.3** — Conformance-signal vocabulary; the `evidence_metric` enum is bound 1:1 to this section's signal names.
- **Mode-Drift sub-spec FINAL Layer 1** — Statistical detection; `classifier_metadata.classifier_version` + `corpus_version` provenance.
- **Mode-Drift sub-spec FINAL Layer 3** — Audit-cadence binding; `escalation_type: layer_3_peer_review_demotion` is the canonical Layer 3 surface for this endpoint.
- **Phase 3 dispatch plan v1.1 §M1** — This spec satisfies M1.
- **Phase 3 dispatch plan v1.1 §D.3** — Stream D skill bundle's Conformance Reporter implements against this contract.

---

*Locked for Phase 3 Stream D dispatch. Co-signed: 🤖 AI Architect + 🛠️ Backend Dev + 🏗️ Chief Architect, 2026-04-30.*

---

## Amendment Log

### v1.1.0 — 2026-04-30 (Stream G cleanup pass)

**Change**: Added `peer_reviewer_pool_underflow` to the `escalation_type` enum (now 9 values, previously 8).

**Rationale**: Stream E Finding 3 surfaced that Layer 3 documentation (`mode-drift/layer-3-mode-confirmation.md`) lists `peer_reviewer_pool_underflow` as a valid `escalation_type` emitted to the reporter API, but the v1.0 enum did not include it. A deployer's Reporter implementing Layer 3's documented escalation surface would have been rejected at the API with `400 unknown_escalation_type`. Synthetic Charter 5 (`peer-reviewer-pool-underflow`) in the test apparatus is designed to exercise this exact path. Extending the enum is cleaner than rerouting through `charter_escalation_rule_invoked` or `schedule_of_records_exception`, both of which would have required ad-hoc narrative on every pool-underflow event.

**Scope**: This amendment touches the wire contract (`escalation_type` enum). Per the v1.0 spec's "Items NOT preserved (locked): everything in §§1-6 above" rule, any deviation from §6 requires an M1 amendment with three-way co-sign. The amendment is additive (no value removed; one value added), so existing v1.0 Reporter implementations remain valid against v1.1.

**Co-signed by**:
- 🤖 **AI Architect**: Approved. The signal `peer_reviewer_pool_underflow` is already specified by Layer 3's peer-reviewer designation rule (sub-rule 4: pool minimum 3). The wire contract was the only place the value was missing. Approved as additive amendment.
- 🛠️ **Backend Dev**: Approved. Wire contract change is additive, no breaking behavior for existing v1.0 clients. Server-side validator updates straightforward (one entry added to the enum constant). OpenAPI YAML `info.version` bumped 1.0.0 → 1.1.0 to reflect the additive enum change.
- 🏗️ **Chief Architect**: Approved. The amendment closes a documented inconsistency between Layer 3 prose and the OpenAPI binding that Stream E surfaced. Locking-the-contract-as-is would have required Layer 3 doc rewrite to reroute pool-underflow through a generic escalation type, which obscures the audit trail. Extending the enum preserves the 1:1 mapping between Layer 3 documented escalation events and reporter API enum values.

**OpenAPI binding updated**: `reporter-api.openapi.yaml` `info.version` 1.0.0 → 1.1.0; enum extended to 9 values.

**Locked at v1.1.0 for Phase 3 Day 10 tag.**
