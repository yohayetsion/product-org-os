# Layer 1 — Statistical Detection (Scaffolding-Only in v5.0)

**Owner**: AI Architect (substantive) + Privacy Counsel (consent/UX) + Chief Architect (Layer C corpus + integration)
**Authority**: Mode-Drift sub-spec FINAL Layer 1 + D.2.1 sub-track
**Status**: v5.0 ships **detection-only scaffolding**. Enforcement gates phase in via D.2.1 sub-track at OS v5.0 lifecycle Week 7+ (NOT Phase 3 dispatch weeks).

---

## What Layer 1 Does

An independent Mode-2-trained classifier samples Mode-1-declared closed decision records, re-classifies against substantive-content features (not metadata), and routes drift candidates above threshold to Layer 3.

## Sampling Configuration

| Charter type | Baseline rate | Override |
|---|---|---|
| Standard Mode-1 Charters | 15% stratified | First-100-records-per-Charter rule overrides to 100% until 100 closed records exist |
| `mode-1-with-embedded-mode-2-summary` Charters | 30% stratified | Same first-100 override |

The 15% baseline threads the needle: below it, drift-rate confidence intervals at the Charter level are too wide to be useful; above 30% the human-review queue load saturates available reviewer capacity.

## Three-Corpus Training Design

**Each corpus is disjoint from any AI worker output that would later be classified.**

| Corpus | Source | Authoring window | Status in v5.0 |
|---|---|---|---|
| **Layer A** — Authoritative Mode 2 records | ~200 peer-reviewed Mode-2 decision records from Vision to Value early-adopter cohort | OS v5.0 lifecycle Weeks 1-3 | Available at v5.0 launch |
| **Layer B** — Synthetic Mode 2 examples | Hand-authored from Section 4 worked examples + 0.5.D Article 50 pre-draft + Charter primer documents | OS v5.0 lifecycle Weeks 1-3 | Available at v5.0 launch |
| **Layer C** — Adversarial negative examples | Mode-1 records with deliberately injected Mode-2 substantive content; AI Architect + Privacy Counsel + Chief Architect joint authorship | **OS v5.0 lifecycle Weeks 4-6** (NOT Phase 3 dispatch weeks) | NOT available at v5.0 launch — authoring runs post-launch |

The classifier training pipeline emits `corpus_id` + `corpus_version` provenance fields. The classifier outputs `classifier_version` + `corpus_version` on every flag so a downstream auditor can verify training-set independence at any point.

## Drift-Flagging Threshold

| Confidence | Action |
|---|---|
| ≥ 0.75 | **Hard flag** — routes to Layer 3 (in enforcement mode) or surfaces in conformance reporter (in detection-only mode) |
| 0.50 - 0.75 | **Soft flag** — surfaces in per-Charter drift-rate aggregate; does NOT interrupt record lifecycle |

If a Charter's soft-flag rate exceeds 5% over a rolling 30-day window, the reporter emits a Charter-level escalation independent of any single record's hard flag (`escalation_type: layer_1_soft_flag_rate_breach`).

## Phased Deployment (D.2.1 Sub-Track)

| Phase | Lifecycle Window | Activity | Layer 1 mode |
|---|---|---|---|
| Phase 1 | OS Weeks 1-3 | Layer A + B corpus assembly; classifier trained on A+B; validation against held-out Layer A subset | **Detection-only** |
| Phase 2 | OS Weeks 4-6 | Layer C adversarial-corpus authoring (joint AI Architect + Privacy Counsel + Chief Architect); classifier retrained on full A+B+C corpus; validation against held-out adversarial subset | **Detection-only** continues |
| Phase 3 | OS Week 7+ | Enforcement-mode activation | **Enforcement** — hard flags trigger Layer 3 peer-review interrupt |

**"Weeks" refers to OS v5.0 lifecycle weeks, NOT Phase 3 dispatch weeks.** Phase 3 finishes Day 10 (~2 calendar weeks). Layer 1 phased deployment runs on its own multi-week cadence that overlaps Phase 3 close + post-launch. Layer 1 enforcement activation at Week 7+ falls 7 weeks AFTER v5.0 release, NOT 7 weeks after Phase 3 kickoff.

## R-001 Closure Note

R-001 closes day-one of v5.0 because **Layers 2, 3, and 4 fire hot day-one**. Layer 1's Phase 1-2 detection-only mode means the `no_silent_mode_drift_in_sample` Level 2 signal emits in a known-conservative posture during OS Weeks 1-6 (false-negatives possible due to incomplete Layer C corpus). The composition closes R-001; Layer 1's full firing authority arrives at Week 7+ and adds population-level signal — it does not gate R-001 closure.

## D.2.1 Sub-Track Day 1 Kickoff

Per Phase 3 plan v1.1 §D.2.1: AI Architect + Privacy Counsel + Chief Architect joint authorship begins Phase 3 Day 1. Layer C corpus authoring scheduled OS v5.0 lifecycle Weeks 4-6.

**Tracking**: Program Manager M/W/F standups. Quality bar: precision ≥ 0.85, recall ≥ 0.75 against held-out adversarial subset before enforcement mode activation.

---

*Layer 1 ships scaffolding only at v5.0. Enforcement deferred to Week 7+ via D.2.1 sub-track. R-001 closure preserved by Layers 2/3/4 firing hot day-one.*
