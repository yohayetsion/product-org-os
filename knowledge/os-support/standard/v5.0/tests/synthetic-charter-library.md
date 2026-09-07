# Synthetic Charter Library — Cross-Stream Test Fixtures

**Purpose**: Test fixtures for cross-stream conformance check (`cross-stream-conformance-check.md`)
**Status**: v5.0 pre-staged

---

## Charter 1 — `pmm-positioning-lock` (Mode 1, single-jurisdiction)

| Field | Value |
|---|---|
| `charter_id` | `pmm-positioning-lock` |
| `decision_class` | "Quarterly positioning lock" |
| `accountable_owner` | "Director of Product Marketing" |
| `mode_declaration` | `mode-1` |
| `cadence` | quarterly |
| `re_decision_triggers` | 1 outcome (NPS Δ > 5pt) + 1 market (competitor major launch) |
| `peer_reviewer_pool` | 3 named DPMM-level peers |
| `conformance_level_declared` | 3 |
| Jurisdiction | US-DE |

Use to validate clean Mode 1 round-trip + Layer 2 hard gate + Layer 4 attestation in US-DE jurisdiction.

## Charter 2 — `pricing-decision` (Mode 2, EU jurisdiction)

| Field | Value |
|---|---|
| `charter_id` | `pricing-decision` |
| `decision_class` | "Enterprise pricing exception approval" |
| `accountable_owner` | "VP Product" |
| `mode_declaration` | `mode-2` |
| `disclosure_metadata_pointer` | populated (5 Article 50 fields) |
| `peer_reviewer_pool` | 4 named peers |
| `conformance_level_declared` | 3 |
| Jurisdiction | EU (German entity) |

Use to validate Mode 2 disclosure block + EU jurisdictional variant in Layer 4 attestation + Article 50 disclosure metadata schema completeness.

## Charter 3 — `roadmap-cycle` (Mode 1 with embedded Mode 2 summary)

| Field | Value |
|---|---|
| `charter_id` | `roadmap-cycle` |
| `mode_declaration` | `mode-1-with-embedded-mode-2-summary` |
| Per-record edge case | Some records embed AI-authored summaries; others don't |
| `peer_reviewer_pool` | 3 named peers |
| Jurisdiction | UK |

Use to validate per-record disclosure attachment for Mode 1 edge case + UK jurisdictional variant.

## Charter 4 — `escalation-driven-demotion` (Mode 2 → Mode 1 demotion)

| Field | Value |
|---|---|
| `charter_id` | `escalation-driven-demotion` |
| `mode_declaration` | `mode-2` |
| `escalation_rule` | Triggers on disclosure-cadence overdue |

Use to validate escalation-driven Mode demotion + `prior_state_archive` population + reporter API `escalation_type: charter_escalation_rule_invoked`.

## Charter 5 — `peer-reviewer-pool-underflow` (failure case)

| Field | Value |
|---|---|
| `charter_id` | `peer-reviewer-pool-underflow` |
| `peer_reviewer_pool` | Initially 3, reduces to 2 mid-Charter |

Use to validate `peer_reviewer_pool_underflow` escalation emits when pool drops below 3.

## Charter 6 — `idempotency-replay` (API contract failure case)

Charter for testing reporter API idempotency:

- Same `Idempotency-Key` + same body → original response returned verbatim
- Same `Idempotency-Key` + divergent body → 409 `idempotency_key_reuse_with_divergent_body`
- Different `Idempotency-Key` + same body within 5-minute server-side dedup window → 409 `duplicate_escalation_in_dedup_window`

## Charter 7 — `israel-jurisdiction` (IL variant)

| Field | Value |
|---|---|
| `charter_id` | `israel-jurisdiction` |
| Jurisdiction | IL |
| Layer 4 attestation | Hebrew variant: "במסגרת תפקידי" + Israeli Companies Law §252-§254 reference |

Use to validate IL jurisdictional variant in Layer 4 attestation.

## Charter 8 — `latent-influence-catch` (Layer 2 catches drift Layer 1 missed)

Use case: declaring authority answers Q1-Q3 `No` (clean Mode 1) but Q4 `Uncertain` (counterfactual trap fires) → Layer 2 routes to Layer 3 → peer reviewer migrates to Mode 2.

Validates the load-bearing latent-influence catch the 4-question structure exists to deliver.

---

## Test Coverage Matrix

| Category | Charter 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|
| A — Charter lifecycle | ✓ | ✓ | ✓ | ✓ | ✓ | | ✓ | ✓ |
| B — Record lifecycle | ✓ | ✓ | ✓ | ✓ | | | ✓ | ✓ |
| C — Layer 2 hard gate | ✓ | | ✓ | | | | ✓ | ✓ |
| D — Layer 3 mode confirmation | ✓ | ✓ | ✓ | ✓ | ✓ | | ✓ | ✓ |
| E — Layer 4 attestation | ✓ | ✓ | ✓ | ✓ | | | ✓ | ✓ |
| F — Reporter API | | | | ✓ | ✓ | ✓ | | |
| G — Signal vocabulary | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| H — Naming directive | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| I — Field alignment | ✓ | ✓ | ✓ | ✓ | | | ✓ | |

---

*Library locked for Stream E test apparatus. Additional fixtures may be added in v5.1.*
