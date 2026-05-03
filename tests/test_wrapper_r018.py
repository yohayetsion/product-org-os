"""
R-018 wrapper-pattern attestation harness.

Converts the R-018 promise ("v5.0 callers reach v5.0 behavior unambiguously,
v5.0 logic block preserved byte-identical to v5.0.0") from documentary to
mechanical. Every test in this file is a structural check on the wrapper
SKILL.md against a frozen v5.0.0 snapshot baseline.

Baseline SHA: 29e54c3 (origin/main, v5.0.0 ship)
Spec: G:/My Drive/Claude/Vision to Value/Content/Book/reviews-v5.2-final-review/
      working/phase-3.5/wave-2/H.5-wrapper-pattern-mode-spec-2026-05-02.md §8

Wave 3 surface: /phase-check (V5.1-23 + V5.1-24).
Wave 4+ surface: /decision-charter, /business-case (V5.2-S43) — when v5.2 lands.
"""

from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent
SKILL_PATH = REPO_ROOT / "skills" / "phase-check" / "SKILL.md"
SNAPSHOT_PATH = REPO_ROOT / "tests" / "snapshots" / "v5.0" / "phase-check-skill-md.md"


def _read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def _normalize(text: str) -> str:
    """Whitespace-only normalization: strip trailing whitespace per line, normalize line endings."""
    lines = text.replace("\r\n", "\n").replace("\r", "\n").split("\n")
    return "\n".join(line.rstrip() for line in lines)


def _extract_v50_logic_block(skill_md: str) -> str:
    """
    Anchor-based extraction of the v5.0 logic block from the wrapper SKILL.md.

    The v5.0 block runs from the first `## Gotchas` heading (the original v5.0
    body's first heading) through the v5.0 `## Operating Principle` block (which
    ends with the quoted line about 'risk debt'). We extract by anchor rather
    than by hardcoded line number because the wrapper preamble length may evolve.
    """
    start_marker = "## Gotchas"
    end_marker = "> \"You can't skip phases without accumulating risk debt"
    start_idx = skill_md.find(start_marker)
    end_idx = skill_md.find(end_marker)
    assert start_idx != -1, "v5.0 anchor `## Gotchas` not found in wrapper SKILL.md"
    assert end_idx != -1, "v5.0 anchor (Operating Principle quote) not found in wrapper SKILL.md"
    # Find end of the Operating Principle line
    end_of_line = skill_md.find("\n", end_idx)
    return skill_md[start_idx : end_of_line + 1]


def _extract_v50_body_from_snapshot(snapshot: str) -> str:
    """The v5.0 snapshot has frontmatter at the top; extract from `## Gotchas` onward."""
    start_idx = snapshot.find("## Gotchas")
    end_marker = "> \"You can't skip phases without accumulating risk debt"
    end_idx = snapshot.find(end_marker)
    assert start_idx != -1, "v5.0 snapshot missing `## Gotchas` anchor"
    assert end_idx != -1, "v5.0 snapshot missing Operating Principle anchor"
    end_of_line = snapshot.find("\n", end_idx)
    return snapshot[start_idx : end_of_line + 1]


# ---------------------------------------------------------------------------
# Test 1 — v5.0 logic block preserved byte-identical (modulo whitespace)
# ---------------------------------------------------------------------------


def test_phase_check_v50_logic_block_preserved():
    """
    The v5.0 logic block in the wrapper SKILL.md must match the v5.0.0 baseline
    snapshot byte-for-byte (after whitespace normalization). This is the core
    R-018 attestation.
    """
    current_block = _normalize(_extract_v50_logic_block(_read(SKILL_PATH)))
    baseline_block = _normalize(_extract_v50_body_from_snapshot(_read(SNAPSHOT_PATH)))
    assert current_block == baseline_block, (
        "R-018 VIOLATION: v5.0 logic block in /phase-check has drifted from "
        "the v5.0.0 baseline (SHA 29e54c3). The wrapper-pattern contract "
        "requires the v5.0 block to remain byte-identical so v5.0 callers "
        "reach v5.0 behavior unambiguously. Re-baseline the wrapper or "
        "restore the v5.0 block."
    )


# ---------------------------------------------------------------------------
# Test 2 — Default mode is v5.0
# ---------------------------------------------------------------------------


def test_phase_check_default_mode_is_v50():
    """
    The dispatch block must declare `v5.0` as the default mode. Per the spec,
    a caller that does NOT pass `mode:` MUST reach v5.0 behavior. The wrapper
    SKILL.md must say so explicitly.

    Assertion form: 'default' and 'v5.0' must appear within a 200-char window
    of each other in the dispatch section. This catches both the prose form
    ('the default is v5.0') and the imperative form ('default → v5.0').
    """
    body = _read(SKILL_PATH)
    # Locate the dispatch section
    dispatch_start = body.find("Dispatch")
    assert dispatch_start != -1, "Wrapper SKILL.md missing Dispatch section"
    dispatch_section = body[dispatch_start : dispatch_start + 3000]

    # Find every 'default' occurrence and check there's 'v5.0' within 200 chars
    found_pairing = False
    search_start = 0
    while True:
        idx = dispatch_section.lower().find("default", search_start)
        if idx == -1:
            break
        window = dispatch_section[max(0, idx - 200) : idx + 200]
        if "v5.0" in window:
            found_pairing = True
            break
        search_start = idx + 1

    assert found_pairing, (
        "R-018 VIOLATION: dispatch section does not declare v5.0 as the "
        "default mode. The wrapper-pattern contract requires that a caller "
        "who does not pass `mode:` reaches v5.0 behavior."
    )


# ---------------------------------------------------------------------------
# Test 3 — Dispatch block present (per H.5 spec §4)
# ---------------------------------------------------------------------------


def test_phase_check_dispatch_block_present():
    """
    The wrapper SKILL.md must contain the dispatch block per H.5 spec §4:
    a block that reads `mode:` from invocation context, validates against
    [v5.0, v5.1, v5.2], and routes execution.

    Canonical phrases the dispatch block must contain (any is sufficient,
    we require at least 3 of 5 to allow phrasing flexibility while catching
    a removed dispatch block):
    """
    body = _read(SKILL_PATH)
    canonical_phrases = [
        "args:",
        "mode=",
        "selected_mode",
        "v5.0",
        "v5.1",
    ]
    found = sum(1 for phrase in canonical_phrases if phrase in body)
    assert found >= 3, (
        f"R-018 VIOLATION: wrapper SKILL.md missing dispatch block. "
        f"Only {found}/5 canonical dispatch phrases found: "
        f"{[p for p in canonical_phrases if p in body]}. "
        f"The dispatch block per H.5 §4 is required."
    )

    # Stronger check: the dispatch logic must mention validation against allowed modes
    assert "Validate" in body or "validate" in body, (
        "Dispatch block must validate `mode:` against allowed values "
        "[v5.0, v5.1, v5.2] per H.5 §4."
    )


# ---------------------------------------------------------------------------
# Test 4 — v5.1 extensions appended, not interleaved
# ---------------------------------------------------------------------------


def test_phase_check_v51_extensions_appended_not_inline():
    """
    The v5.1 hard-gate sections (Phase 2→3 and Phase 3→4) must appear AFTER
    the v5.0 logic block, not interleaved into it. The structural marker is
    that `# v5.1 Hard-Gate Extensions` (or equivalent) must appear after the
    v5.0 `## Operating Principle` quote line.
    """
    body = _read(SKILL_PATH)
    v50_end_anchor = "> \"You can't skip phases without accumulating risk debt"
    v51_extension_anchor_options = [
        "# v5.1 Hard-Gate Extensions",
        "## v5.1 Hard-Gate Extensions",
        "Phase 2 → Phase 3 Hard-Gate",
        "Phase 2→3 Hard-Gate",
    ]

    v50_end_idx = body.find(v50_end_anchor)
    assert v50_end_idx != -1, "v5.0 Operating Principle anchor not found"

    v51_idx = -1
    for anchor in v51_extension_anchor_options:
        candidate = body.find(anchor)
        if candidate != -1 and (v51_idx == -1 or candidate < v51_idx):
            v51_idx = candidate

    assert v51_idx != -1, (
        f"v5.1 hard-gate extensions not found. Looked for any of: "
        f"{v51_extension_anchor_options}"
    )
    assert v51_idx > v50_end_idx, (
        "R-018 VIOLATION: v5.1 hard-gate extensions appear BEFORE the v5.0 "
        "Operating Principle. The wrapper-pattern contract requires v5.1 "
        "extensions to be appended AFTER the v5.0 logic block, not "
        "interleaved into it. v5.0 callers must see only v5.0 output."
    )

    # Also: the v5.0 block should not contain v5.1 hard-gate language
    v50_block = _extract_v50_logic_block(body)
    forbidden_in_v50 = [
        "Phase 2→3 Hard-Gate",
        "Phase 3→4 Hard-Gate",
        "Five Signals Verdict",
        "continuation_threshold_declared",
    ]
    leaked = [phrase for phrase in forbidden_in_v50 if phrase in v50_block]
    assert not leaked, (
        f"R-018 VIOLATION: v5.1 hard-gate language has leaked into the v5.0 "
        f"logic block. Found: {leaked}. The v5.0 block must remain "
        f"byte-identical to v5.0.0."
    )


# ---------------------------------------------------------------------------
# Test 5 — No v5.2 block yet (forward-compat guard)
# ---------------------------------------------------------------------------


def test_phase_check_no_v52_block_yet():
    """
    Forward-compat guard. V5.2-S43 has not landed on `v5.1-prep`. The wrapper
    SKILL.md should not yet contain a dedicated v5.2 hard-gate block — only
    the dispatch-level mention that `mode: v5.2` is reserved.

    This test flips intent when V5.2-S43 lands on `v5.2-prep`: at that point,
    update the assertion to require the v5.2 block to exist.

    Allowed today:
      - `mode: v5.2` mentioned in dispatch table / dispatch logic (reserved)
      - `# TODO v5.2:` reservation note
    Forbidden today:
      - A `## v5.2 Sub-Series-C Lane` section (or equivalent dedicated v5.2
        execution block)
      - A `# v5.2 Extensions` block parallel to the v5.1 block
    """
    body = _read(SKILL_PATH)
    forbidden_v52_block_anchors = [
        "## v5.2 Sub-Series-C Lane",
        "# v5.2 Extensions",
        "## v5.2 Hard-Gate Extensions",
        "# v5.2 Hard-Gate Extensions",
        "## V5.2-S43 Sub-Series-C Block",
    ]
    found = [anchor for anchor in forbidden_v52_block_anchors if anchor in body]
    assert not found, (
        f"Forward-compat guard FIRED: wrapper SKILL.md contains a v5.2 "
        f"execution block ({found}) but V5.2-S43 has not landed on "
        f"`v5.1-prep`. If V5.2-S43 has landed and this test should flip, "
        f"update test_phase_check_no_v52_block_yet to require the block."
    )


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
