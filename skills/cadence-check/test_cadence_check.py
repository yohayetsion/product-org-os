"""Tests for V5.1-30 cadence_check module.

Pytest-based. Pure stdlib + pytest. Builds a tmp_path-based context/ tree
with known stale and fresh records and asserts each signal type fires
correctly. Also covers failure modes (missing dir, malformed record,
missing index.json fallback to body-text scan).
"""

from __future__ import annotations

import json
import os
import time
from datetime import date, datetime, timedelta
from pathlib import Path

import pytest

import cadence_check
from cadence_check import scan, Finding, CadenceFindings


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _set_mtime(path: Path, days_ago: int) -> None:
    """Backdate a file's mtime by N days."""
    target = time.time() - days_ago * 86400
    os.utime(path, (target, target))


def _write_decision(
    dir_: Path, dr_id: str, status: str, days_ago: int, body_date: str | None = None
) -> Path:
    """Write a DR-YYYY-NNN.md record. days_ago is age relative to today."""
    dir_.mkdir(parents=True, exist_ok=True)
    body_date = body_date or (date.today() - timedelta(days=days_ago)).isoformat()
    f = dir_ / f"{dr_id}.md"
    f.write_text(
        f"# {dr_id}: Test\n\n"
        f"**Date**: {body_date}\n"
        f"**Status**: {status}\n\n"
        f"## Summary\nTest decision.\n",
        encoding="utf-8",
    )
    _set_mtime(f, days_ago)
    return f


def _write_bet(
    dir_: Path, sb_id: str, status: str, days_ago: int
) -> Path:
    dir_.mkdir(parents=True, exist_ok=True)
    f = dir_ / f"{sb_id}.md"
    f.write_text(
        f"# {sb_id}: Test\n\n"
        f"**Date**: {(date.today() - timedelta(days=days_ago)).isoformat()}\n"
        f"**Status**: {status}\n\n"
        f"## Summary\nTest bet.\n",
        encoding="utf-8",
    )
    _set_mtime(f, days_ago)
    return f


def _write_index_json(context: Path, learning_to_decision: dict) -> None:
    (context / "index.json").write_text(
        json.dumps(
            {
                "version": "3.0",
                "crossReferences": {"learningToDecision": learning_to_decision},
            }
        ),
        encoding="utf-8",
    )


@pytest.fixture
def context_root(tmp_path: Path) -> Path:
    """A scaffolded but mostly empty context/ root."""
    root = tmp_path / "context"
    for sub in ("decisions/2026", "bets/2026", "portfolio", "learnings", "handoffs"):
        (root / sub).mkdir(parents=True)
    (root / "learnings" / "index.md").write_text("# Learnings\n", encoding="utf-8")
    _set_mtime(root / "learnings" / "index.md", 1)
    (root / "handoffs" / "current-session.md").write_text(
        "# Handoff\n", encoding="utf-8"
    )
    _set_mtime(root / "handoffs" / "current-session.md", 1)
    (root / "portfolio" / "active-bets.md").write_text(
        "# Active Bets\n", encoding="utf-8"
    )
    _set_mtime(root / "portfolio" / "active-bets.md", 1)
    _write_index_json(root, {})
    return root


# ---------------------------------------------------------------------------
# Tests: one per signal type
# ---------------------------------------------------------------------------


def test_portfolio_review_overdue(context_root: Path) -> None:
    # Drop a stale dated review file (100 days old > 90d threshold).
    stale_date = (date.today() - timedelta(days=100)).isoformat()
    f = context_root / "portfolio" / f"portfolio-review-{stale_date}.md"
    f.write_text("# Stale review\n", encoding="utf-8")
    _set_mtime(f, 100)

    result = scan(context_root)
    sigs = [f.signal_type for f in result.findings]
    assert "portfolio_review_overdue" in sigs
    pf = next(f for f in result.findings if f.signal_type == "portfolio_review_overdue")
    assert pf.severity == "P1"
    assert pf.age_days >= 90


def test_bet_review_overdue(context_root: Path) -> None:
    # Stale active bet (45d > 30d threshold).
    _write_bet(context_root / "bets" / "2026", "SB-2026-001", "Active", 45)
    # Fresh active bet — should NOT fire.
    _write_bet(context_root / "bets" / "2026", "SB-2026-002", "Active", 5)
    # Stale closed bet — should NOT fire (only active bets count).
    _write_bet(context_root / "bets" / "2026", "SB-2026-003", "Closed", 200)

    result = scan(context_root)
    bet_findings = [f for f in result.findings if f.signal_type == "bet_review_overdue"]
    assert len(bet_findings) == 1
    assert bet_findings[0].target_record_id == "SB-2026-001"
    assert bet_findings[0].severity == "P1"


def test_decision_review_missing_no_learning_link(context_root: Path) -> None:
    # Accepted decision 35 days old, no learning link → P1 decision_review_missing.
    _write_decision(context_root / "decisions" / "2026", "DR-2026-001", "Accepted", 35)

    result = scan(context_root)
    drm = [f for f in result.findings if f.signal_type == "decision_review_missing"]
    assert len(drm) == 1
    assert drm[0].target_record_id == "DR-2026-001"
    assert drm[0].severity == "P1"


def test_outcome_review_missing_p0_decision_rot(context_root: Path) -> None:
    # 100-day-old Accepted decision, no learning link, not Superseded → P0.
    _write_decision(context_root / "decisions" / "2026", "DR-2026-002", "Accepted", 100)

    result = scan(context_root)
    orm = [f for f in result.findings if f.signal_type == "outcome_review_missing"]
    assert len(orm) == 1
    assert orm[0].severity == "P0"
    assert orm[0].age_days >= 90


def test_outcome_review_missing_superseded_drops_to_p1(context_root: Path) -> None:
    # 100d old but Superseded → not P0, falls back to P1.
    _write_decision(
        context_root / "decisions" / "2026",
        "DR-2026-099",
        "Accepted; later Superseded",
        100,
    )
    result = scan(context_root)
    orm = [f for f in result.findings if f.signal_type == "outcome_review_missing"]
    assert len(orm) == 1
    assert orm[0].severity == "P1"


def test_handoff_stale(context_root: Path) -> None:
    handoff = context_root / "handoffs" / "current-session.md"
    _set_mtime(handoff, 10)  # > 7d threshold

    result = scan(context_root)
    hs = [f for f in result.findings if f.signal_type == "handoff_stale"]
    assert len(hs) == 1
    assert hs[0].severity == "P1"


def test_learning_log_dormant(context_root: Path) -> None:
    idx = context_root / "learnings" / "index.md"
    _set_mtime(idx, 70)  # > 60d threshold

    result = scan(context_root)
    ll = [f for f in result.findings if f.signal_type == "learning_log_dormant"]
    assert len(ll) == 1
    assert ll[0].severity == "P1"


# ---------------------------------------------------------------------------
# Failure-mode tests
# ---------------------------------------------------------------------------


def test_missing_context_directory_returns_one_finding(tmp_path: Path) -> None:
    nonexistent = tmp_path / "does-not-exist"
    result = scan(nonexistent)
    assert len(result.findings) == 1
    assert result.findings[0].signal_type == "context_directory_missing"
    assert result.findings[0].severity == "P1"


def test_malformed_record_handled_gracefully(context_root: Path) -> None:
    # Decision file with no Status: line.
    bad = context_root / "decisions" / "2026" / "DR-2026-666.md"
    bad.write_text("# DR-2026-666\n\nMalformed — no status.\n", encoding="utf-8")
    _set_mtime(bad, 35)

    result = scan(context_root)
    # Should not raise. Should produce a parse_failures aggregate finding (P2).
    pf = [f for f in result.findings if f.signal_type == "parse_failures"]
    assert len(pf) == 1
    assert pf[0].severity == "P2"
    # And scan_metadata should record the specific failure.
    assert "parse_failures" in result.summary["scan_metadata"]


def test_missing_index_json_falls_back_to_body_text(context_root: Path) -> None:
    # Remove the index, write a learning that mentions DR-2026-007.
    (context_root / "index.json").unlink()
    learning_file = context_root / "learnings" / "L-001.md"
    learning_file.write_text(
        "# L-001\n\nSee DR-2026-007 for context.\n", encoding="utf-8"
    )
    _set_mtime(learning_file, 1)

    # An Accepted decision 35 days old. With body-text fallback, the L-001
    # mention should suppress decision_review_missing for DR-2026-007.
    _write_decision(context_root / "decisions" / "2026", "DR-2026-007", "Accepted", 35)

    result = scan(context_root)
    drm = [
        f for f in result.findings
        if f.signal_type == "decision_review_missing" and f.target_record_id == "DR-2026-007"
    ]
    assert drm == [], "body-text fallback should have suppressed this finding"
    assert result.summary["scan_metadata"].get("index_unavailable") is True
