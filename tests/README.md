# tests/

Mechanical attestation harness for the v5.0-aligned wrapper pattern.

## Purpose

Per Vision to Value v5.1, the requirement R-018 mandates that v5.0.0 stays tag-ready: any caller that does not pass an explicit `mode:` parameter to a wrapped skill MUST receive output byte-identical to what they received before v5.1 shipped. This harness converts that promise from documentary to mechanical. If any wrapper drifts from the v5.0.0 baseline, the test fails and the wrapper cannot merge into `v5.1-prep`.

The wrapper pattern is specified in `H.5-wrapper-pattern-mode-spec-2026-05-02.md` (Vision to Value review working dir, Phase 3.5 Wave 2). §8 of that spec is the test plan this harness implements.

## What lives here

- `test_wrapper_r018.py` — pytest suite. Five tests covering: v5.0 logic block preservation, default-to-v5.0 dispatch, dispatch block presence, v5.1 extensions appended (not interleaved), forward-compat guard against premature v5.2 blocks.
- `snapshots/v5.0/` — frozen v5.0.0 baseline files extracted from `git show 29e54c3:skills/<skill>/SKILL.md`. SHA 29e54c3 is the v5.0.0 ship pin on `origin/main`; that pin is contractually frozen and must not be re-baselined under normal evolution.

## Today's coverage

- `/phase-check` (V5.1-23 + V5.1-24 wrapper) — full coverage in `test_wrapper_r018.py`.

## Coming with v5.2

When V5.2-S43 lands on `v5.2-prep`, two more wrapper surfaces (`/decision-charter`, `/business-case`) need the same five-test treatment. Add `test_wrapper_r018_v5_2.py` with parametrized tests over the two new surfaces, capture their v5.0.0 baselines from SHA 29e54c3, and flip `test_phase_check_no_v52_block_yet` to require a v5.2 block instead of forbid one.

## How to run

```
cd C:/dev/product-org-os
python -m pytest tests/test_wrapper_r018.py -v
```

All tests must pass green. A red test indicates a real R-018 violation; do not paper over it.

## Re-baselining policy

You should not need to re-baseline. The whole point of pinning v5.0.0 to SHA 29e54c3 is that the v5.0 surface is frozen. The only legitimate reason to update `snapshots/v5.0/` is if v5.0.0 is itself re-tagged (which the v5.0 standard explicitly forbids barring a critical-defect repin). If you ever need to do this, document the reason in the same commit and require a Director-level sign-off per `sensitive-skill-guardrails.md` two-pass gate.

## What this harness does NOT verify

This harness verifies the SKILL.md body contract — the markdown structure, the dispatch declarations, the preserved v5.0 logic block. It does NOT verify live agent invocation behavior (no Claude Code runtime in CI). The substantive R-018 promise that "a v5.0 caller passing no `mode:` parameter receives byte-identical v5.0 output" is enforced structurally here (the v5.0 block is byte-identical and the dispatch defaults to v5.0) but the runtime equivalence is enforced by the dispatch logic the agent reads, not by these tests.

In practice, structural enforcement is sufficient for R-018 because the wrapper-pattern is implemented entirely in markdown that the agent executes verbatim — there is no separate runtime layer that could diverge.
