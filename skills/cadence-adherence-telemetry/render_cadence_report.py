"""V5.1-31: render cadence_check.scan() output as a markdown report.

Pure stdlib helper. Consumes the CadenceFindings contract from V5.1-30
(skills/cadence-check/cadence_check.py SHA 7f0dc89) and emits the
cadence-adherence-telemetry markdown document that V5.1-31 surfaces to
the user and persists to context/telemetry/.

Public entry points:
    render(findings: CadenceFindings, today: date | None = None) -> str
    suggested_next_step(signal_type: str) -> str

Sort order: severity (P0 < P1 < P2) then age_days descending. Findings
are grouped by signal_type within each severity tier so the reader sees
all P0 outcome-reviews-missing together, then all P1 bet-review-overdue
together, etc.

R-018: V5.1-31 is a NEW skill cell. Touches zero v5.0 surface. Consumes
V5.1-30's stable contract.
"""

from __future__ import annotations

from datetime import date, datetime
from typing import Iterable


# Severity sort weight (lower = surfaces first).
_SEVERITY_WEIGHT = {"P0": 0, "P1": 1, "P2": 2}

# Signal type display order within a severity tier (most actionable first).
_SIGNAL_DISPLAY_ORDER = [
    "outcome_review_missing",
    "decision_review_missing",
    "portfolio_review_overdue",
    "bet_review_overdue",
    "handoff_stale",
    "learning_log_dormant",
    "context_directory_missing",
    "record_unparseable",
    "parse_failures",
    "permission_error",
]

# Suggested next step per signal_type. Surfaced inline beneath each finding.
_NEXT_STEP = {
    "outcome_review_missing": (
        "Run /outcome-review against this decision to close the T+60 loop, "
        "or update the decision Status: Superseded if the call has changed."
    ),
    "decision_review_missing": (
        "Run /context-recall on this decision and link a learning record "
        "(L-NNN) once the T+30 review is filed."
    ),
    "portfolio_review_overdue": (
        "Run /portfolio-status and produce a dated portfolio-review-YYYY-MM-DD.md "
        "in context/portfolio/."
    ),
    "bet_review_overdue": (
        "Run /bet-invalidation-checkpoint (or update the bet's Status line) so "
        "the monthly review cadence resumes."
    ),
    "handoff_stale": (
        "Run /handoff at the next session boundary. Stale handoff often signals "
        "a dormant project that needs a parking decision."
    ),
    "learning_log_dormant": (
        "Run /context-save with a learning record, or capture a recent retrospective "
        "via /retrospective. 60+ days idle suggests learnings are being lost."
    ),
    "context_directory_missing": "Run /setup to scaffold the context layer.",
    "record_unparseable": "Open the record manually and verify date + Status: lines parse.",
    "parse_failures": "Inspect scan_metadata.parse_failures and repair affected records.",
    "permission_error": "Check filesystem permissions on the affected directory.",
}


def suggested_next_step(signal_type: str) -> str:
    """Return the suggested next step for a given signal_type."""
    return _NEXT_STEP.get(signal_type, "Manual review needed.")


def _signal_sort_key(signal_type: str) -> int:
    try:
        return _SIGNAL_DISPLAY_ORDER.index(signal_type)
    except ValueError:
        return len(_SIGNAL_DISPLAY_ORDER)


def _sort_findings(findings: Iterable) -> list:
    """Sort by severity then signal_type display order then age_days desc."""
    return sorted(
        findings,
        key=lambda f: (
            _SEVERITY_WEIGHT.get(f.severity, 99),
            _signal_sort_key(f.signal_type),
            -f.age_days,
        ),
    )


def _format_finding(f) -> str:
    target = f.target_record_id or "—"
    return (
        f"#### [{f.severity}] {f.signal_type}\n\n"
        f"- **Target**: `{target}`\n"
        f"- **Age**: {f.age_days}d (threshold: {f.threshold_days}d)\n"
        f"- **Detail**: {f.human_readable}\n"
        f"- **Suggested next step**: {suggested_next_step(f.signal_type)}\n"
    )


def _format_summary_block(summary: dict, today: date) -> str:
    by_sev = summary.get("by_severity", {})
    by_sig = summary.get("by_signal_type", {})
    total = summary.get("total", 0)
    scan_ts = summary.get("scan_timestamp", "")
    duration_ms = summary.get("scan_duration_ms", 0)
    metadata = summary.get("scan_metadata", {})

    lines = [
        f"**Scan date**: {today.isoformat()}",
        f"**Scan timestamp (UTC)**: {scan_ts}",
        f"**Scan duration**: {duration_ms}ms",
        f"**Total findings**: {total}",
        "",
        "**By severity**:",
    ]
    if by_sev:
        for sev in ("P0", "P1", "P2"):
            count = by_sev.get(sev, 0)
            if count:
                lines.append(f"- {sev}: {count}")
    else:
        lines.append("- (none)")

    if by_sig:
        lines.append("")
        lines.append("**By signal type**:")
        for sig in sorted(by_sig.keys(), key=_signal_sort_key):
            lines.append(f"- {sig}: {by_sig[sig]}")

    # Surface degraded-scan flags so the reader knows the scan was partial.
    degraded_flags = []
    if metadata.get("index_unavailable"):
        degraded_flags.append("`context/index.json` unavailable — cross-ref check ran in body-text fallback mode.")
    if metadata.get("permission_errors"):
        degraded_flags.append(
            f"{len(metadata['permission_errors'])} permission error(s) — see scan metadata."
        )
    if metadata.get("parse_failures"):
        degraded_flags.append(
            f"{len(metadata['parse_failures'])} parse failure(s) — see scan metadata."
        )
    if metadata.get("parse_warnings"):
        degraded_flags.append(
            f"{len(metadata['parse_warnings'])} parse warning(s) (date precedence ambiguity)."
        )
    if metadata.get("empty_directories"):
        degraded_flags.append(
            f"{len(metadata['empty_directories'])} empty directory slice(s) — no records yet."
        )

    if degraded_flags:
        lines.append("")
        lines.append("**Scan health**:")
        for flag in degraded_flags:
            lines.append(f"- {flag}")
    else:
        lines.append("")
        lines.append("**Scan health**: clean (no degraded signals).")

    return "\n".join(lines)


def render(findings_obj, today: date | None = None) -> str:
    """Render a CadenceFindings object as a markdown report."""
    today = today or date.today()
    sorted_findings = _sort_findings(findings_obj.findings)
    summary_block = _format_summary_block(findings_obj.summary, today)

    parts = [
        f"# Cadence Adherence Telemetry — {today.isoformat()}",
        "",
        "Principle 8 cadence-stack adherence scan. Surfaces overdue items "
        "across the four-layer cadence stack (portfolio review, bet review, "
        "decision T+30 / outcome T+60, handoff freshness, learning log "
        "activity).",
        "",
        "## Summary",
        "",
        summary_block,
        "",
    ]

    if not sorted_findings:
        parts.append("## Findings")
        parts.append("")
        parts.append(
            "No cadence findings. The four-layer cadence stack is on rhythm "
            "across all scanned slices."
        )
        parts.append("")
    else:
        # Group by severity for readable section headers.
        current_severity = None
        parts.append("## Findings")
        parts.append("")
        for f in sorted_findings:
            if f.severity != current_severity:
                current_severity = f.severity
                tier_label = {
                    "P0": "P0 — Blocker (decision rotted in place)",
                    "P1": "P1 — Important (over threshold)",
                    "P2": "P2 — Notice (within 20% of threshold)",
                }.get(current_severity, current_severity)
                parts.append(f"### {tier_label}")
                parts.append("")
            parts.append(_format_finding(f))

    parts.append("---")
    parts.append("")
    parts.append(
        "_Generated by `/cadence-adherence-telemetry` (V5.1-31) consuming "
        "`cadence_check.scan()` (V5.1-30). Read-only sensor; never mutates "
        "`context/`. Persists to `context/telemetry/cadence-adherence-{date}.md` "
        "for audit trail._"
    )
    parts.append("")
    return "\n".join(parts)


# ---------------------------------------------------------------------------
# Inline self-test (dict-built fake CadenceFindings)
# ---------------------------------------------------------------------------


def _self_test() -> None:
    """Smoke-test render() with a hand-built fake CadenceFindings."""
    from dataclasses import dataclass
    from typing import Optional

    @dataclass
    class _FakeFinding:
        signal_type: str
        target_record_id: Optional[str]
        age_days: int
        threshold_days: int
        severity: str
        human_readable: str

    @dataclass
    class _FakeFindings:
        findings: list
        summary: dict

    sample = _FakeFindings(
        findings=[
            _FakeFinding(
                "outcome_review_missing", "DR-2026-014", 120, 60, "P0",
                "Accepted decision DR-2026-014 is 120d old with no T+60 outcome review (threshold 60d)."
            ),
            _FakeFinding(
                "bet_review_overdue", "SB-2026-003", 45, 30, "P1",
                "Active bet SB-2026-003 not reviewed in 45d (threshold 30d)."
            ),
            _FakeFinding(
                "handoff_stale", None, 8, 7, "P1",
                "Session handoff (current-session.md) last updated 8d ago (threshold 7d)."
            ),
            _FakeFinding(
                "decision_review_missing", "DR-2026-019", 26, 30, "P2",
                "Accepted decision DR-2026-019 is 26d old with no T+30 review link (threshold 30d)."
            ),
        ],
        summary={
            "total": 4,
            "by_severity": {"P0": 1, "P1": 2, "P2": 1},
            "by_signal_type": {
                "outcome_review_missing": 1,
                "bet_review_overdue": 1,
                "handoff_stale": 1,
                "decision_review_missing": 1,
            },
            "scan_timestamp": "2026-05-03T12:00:00+00:00",
            "scan_duration_ms": 47,
            "scan_metadata": {"index_unavailable": False},
            "today": "2026-05-03",
        },
    )
    output = render(sample, today=date(2026, 5, 3))
    assert "# Cadence Adherence Telemetry" in output
    assert "[P0] outcome_review_missing" in output
    assert "[P1] bet_review_overdue" in output
    assert "[P2] decision_review_missing" in output
    assert "DR-2026-014" in output
    assert "/outcome-review" in output  # next-step text surfaced
    assert "P0 — Blocker" in output
    print("self-test OK")
    print("---OUTPUT PREVIEW---")
    print(output[:1200])


if __name__ == "__main__":
    _self_test()
