"""V5.1-30: cadence-check (Option A — file-system scan on demand).

Detects when cadence-stack records that Principle 8 expects on a regular
rhythm have gone stale or are missing entirely. Pure stdlib. Read-only.
Never raises on partial data: degrades gracefully and always returns
something actionable.

Public entry point:
    cadence_check.scan(context_root, today=None, threshold_overrides=None)
        -> CadenceFindings

Consumers in v5.1: V5.1-31 (/cadence-adherence-telemetry) and
V5.1-26/27/28 (/maturity-check rewrite). Not user-invocable directly.

R-018: New module + new skill cell. Touches zero v5.0 surface.
context/ schema is read-only.
"""

from __future__ import annotations

import json
import re
import time
from dataclasses import dataclass, field, asdict
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Optional


# Default thresholds (days) per H.5 spec §4.
DEFAULT_THRESHOLDS = {
    "portfolio_review_overdue": 90,
    "bet_review_overdue": 30,
    "decision_review_missing": 30,
    "outcome_review_missing": 60,
    "handoff_stale": 7,
    "learning_log_dormant": 60,
}

# P0 escalation (decision rotted): Accepted decision >90 days, no outcome
# review, no Status: Superseded/Deprecated.
P0_DECISION_ROT_DAYS = 90

# Filename patterns.
_RE_DR = re.compile(r"^DR-\d{4}-\d{3}\.md$")
_RE_SB = re.compile(r"^SB-\d{4}-\d{3}\.md$")
_RE_PORTFOLIO_REVIEW = re.compile(r"^portfolio-review-(\d{4}-\d{2}-\d{2})\.md$")
_RE_DATE_PREFIX = re.compile(r"^(\d{4}-\d{2}-\d{2})")
_RE_YEAR_FROM_ID = re.compile(r"^(?:DR|SB)-(\d{4})-\d{3}\.md$")

# Body-line patterns.
_RE_BODY_DATE = re.compile(r"^\*\*Date\*\*:\s*(\S+)", re.MULTILINE)
_RE_BODY_STATUS = re.compile(r"^\*\*Status\*\*:\s*(.+)$", re.MULTILINE)
_RE_FRONTMATTER_DATE = re.compile(r"^Date:\s*(\S+)", re.MULTILINE)


@dataclass
class Finding:
    """One cadence finding."""

    signal_type: str
    target_record_id: Optional[str]
    age_days: int
    threshold_days: int
    severity: str  # "P0" | "P1" | "P2"
    human_readable: str


@dataclass
class CadenceFindings:
    """Container returned by scan()."""

    findings: list[Finding] = field(default_factory=list)
    summary: dict = field(default_factory=dict)

    def to_dict(self) -> dict:
        return {
            "findings": [asdict(f) for f in self.findings],
            "summary": self.summary,
        }


# ---------------------------------------------------------------------------
# Date parsing precedence: filename → frontmatter Date: → body **Date**: → mtime
# ---------------------------------------------------------------------------


def _parse_date_str(s: str) -> Optional[date]:
    """Parse YYYY-MM-DD; return None on failure."""
    try:
        return datetime.strptime(s.strip(), "%Y-%m-%d").date()
    except (ValueError, AttributeError):
        return None


def _date_from_filename(path: Path) -> Optional[date]:
    """Pull a YYYY-MM-DD prefix from the filename if present."""
    m = _RE_DATE_PREFIX.match(path.name)
    if m:
        return _parse_date_str(m.group(1))
    return None


def _date_from_body(text: str) -> tuple[Optional[date], Optional[date]]:
    """Return (frontmatter_date, body_date) parsed from text."""
    fm = _RE_FRONTMATTER_DATE.search(text)
    bd = _RE_BODY_DATE.search(text)
    fm_date = _parse_date_str(fm.group(1)) if fm else None
    bd_date = _parse_date_str(bd.group(1)) if bd else None
    return fm_date, bd_date


def _resolve_record_date(
    path: Path, text: Optional[str], scan_metadata: dict
) -> tuple[date, str]:
    """Resolve a record's effective date by precedence + log which path won.

    Precedence: filename → frontmatter Date: → body **Date**: → mtime.
    Records ambiguity (filename vs frontmatter mismatch) to scan_metadata.
    """
    fn_date = _date_from_filename(path)
    fm_date = bd_date = None
    if text is not None:
        fm_date, bd_date = _date_from_body(text)

    # Ambiguity check: filename and frontmatter disagree → prefer filename.
    if fn_date and fm_date and fn_date != fm_date:
        scan_metadata.setdefault("parse_warnings", []).append(
            f"{path}: filename date {fn_date} disagrees with frontmatter {fm_date}; preferring filename"
        )

    if fn_date:
        return fn_date, "filename"
    if fm_date:
        return fm_date, "frontmatter"
    if bd_date:
        return bd_date, "body"
    # mtime fallback.
    try:
        mtime = path.stat().st_mtime
    except OSError:
        return date.today(), "today_fallback"
    return datetime.fromtimestamp(mtime).date(), "mtime"


def _read_text_safe(path: Path, scan_metadata: dict) -> Optional[str]:
    try:
        return path.read_text(encoding="utf-8", errors="replace")
    except OSError as e:
        scan_metadata.setdefault("parse_failures", []).append(f"{path}: {e}")
        return None


def _mtime_age_days(path: Path, today: date) -> int:
    try:
        mtime = path.stat().st_mtime
    except OSError:
        return 0
    return (today - datetime.fromtimestamp(mtime).date()).days


# ---------------------------------------------------------------------------
# Severity helpers
# ---------------------------------------------------------------------------


def _severity_for_age(age_days: int, threshold_days: int) -> str:
    """P1 at/above threshold; P2 within 20% of threshold but not yet over."""
    if age_days >= threshold_days:
        return "P1"
    # P2 window: (0.8 * threshold) <= age < threshold.
    if age_days >= int(threshold_days * 0.8):
        return "P2"
    return "P2"  # caller filters; we return something defensible


# ---------------------------------------------------------------------------
# Signal helpers
# ---------------------------------------------------------------------------


def _scan_portfolio(
    portfolio_dir: Path, today: date, threshold: int, scan_metadata: dict
) -> list[Finding]:
    """portfolio_review_overdue: most recent portfolio-review-*.md mtime."""
    if not portfolio_dir.exists():
        return []
    if not portfolio_dir.is_dir():
        return []

    review_files = [
        p for p in portfolio_dir.iterdir() if _RE_PORTFOLIO_REVIEW.match(p.name)
    ]
    if not review_files:
        # Fallback: active-bets.md mtime.
        active_bets = portfolio_dir / "active-bets.md"
        if not active_bets.exists():
            scan_metadata.setdefault("empty_directories", []).append(str(portfolio_dir))
            return []
        age = _mtime_age_days(active_bets, today)
        if age >= int(threshold * 0.8):
            sev = "P1" if age >= threshold else "P2"
            return [
                Finding(
                    signal_type="portfolio_review_overdue",
                    target_record_id=None,
                    age_days=age,
                    threshold_days=threshold,
                    severity=sev,
                    human_readable=(
                        f"No dated portfolio-review file found; active-bets.md "
                        f"last modified {age}d ago (threshold {threshold}d)."
                    ),
                )
            ]
        return []

    # Use most recent dated review file (prefer filename date, then mtime).
    dated = []
    for f in review_files:
        m = _RE_PORTFOLIO_REVIEW.match(f.name)
        d = _parse_date_str(m.group(1)) if m else None
        if d is None:
            d = datetime.fromtimestamp(f.stat().st_mtime).date()
        dated.append((d, f))
    dated.sort(key=lambda x: x[0], reverse=True)
    most_recent_date, most_recent_file = dated[0]
    age = (today - most_recent_date).days
    if age < int(threshold * 0.8):
        return []
    sev = "P1" if age >= threshold else "P2"
    return [
        Finding(
            signal_type="portfolio_review_overdue",
            target_record_id=most_recent_file.stem,
            age_days=age,
            threshold_days=threshold,
            severity=sev,
            human_readable=(
                f"Last portfolio review ({most_recent_file.name}) was {age}d ago "
                f"(threshold {threshold}d)."
            ),
        )
    ]


def _scan_bets(
    bets_dir: Path, today: date, threshold: int, scan_metadata: dict
) -> list[Finding]:
    """bet_review_overdue: each active bet's mtime older than threshold."""
    if not bets_dir.exists() or not bets_dir.is_dir():
        return []

    findings = []
    bet_files = list(bets_dir.rglob("SB-*.md"))
    if not bet_files:
        scan_metadata.setdefault("empty_directories", []).append(str(bets_dir))
        return []

    for bet_file in bet_files:
        if not _RE_SB.match(bet_file.name):
            continue
        text = _read_text_safe(bet_file, scan_metadata)
        if text is None:
            findings.append(_unparseable_finding(bet_file))
            continue
        status_match = _RE_BODY_STATUS.search(text)
        if not status_match:
            scan_metadata.setdefault("parse_failures", []).append(
                f"{bet_file}: no Status line"
            )
            findings.append(_unparseable_finding(bet_file))
            continue
        status = status_match.group(1).strip().lower()
        # Only active bets are subject to monthly review cadence.
        if not status.startswith("active"):
            continue
        age = _mtime_age_days(bet_file, today)
        if age < int(threshold * 0.8):
            continue
        sev = "P1" if age >= threshold else "P2"
        findings.append(
            Finding(
                signal_type="bet_review_overdue",
                target_record_id=bet_file.stem,
                age_days=age,
                threshold_days=threshold,
                severity=sev,
                human_readable=(
                    f"Active bet {bet_file.stem} not reviewed in {age}d "
                    f"(threshold {threshold}d)."
                ),
            )
        )
    return findings


def _scan_decisions(
    decisions_dir: Path,
    today: date,
    review_threshold: int,
    outcome_threshold: int,
    learning_links: set[str],
    learnings_text: str,
    scan_metadata: dict,
) -> list[Finding]:
    """decision_review_missing + outcome_review_missing per accepted decision.

    P0 escalation: Accepted decision >90 days old with no outcome review and
    not Superseded/Deprecated.
    """
    if not decisions_dir.exists() or not decisions_dir.is_dir():
        return []

    findings = []
    dr_files = list(decisions_dir.rglob("DR-*.md"))
    if not dr_files:
        scan_metadata.setdefault("empty_directories", []).append(str(decisions_dir))
        return []

    for dr_file in dr_files:
        if not _RE_DR.match(dr_file.name):
            continue
        text = _read_text_safe(dr_file, scan_metadata)
        if text is None:
            findings.append(_unparseable_finding(dr_file))
            continue
        status_match = _RE_BODY_STATUS.search(text)
        if not status_match:
            scan_metadata.setdefault("parse_failures", []).append(
                f"{dr_file}: no Status line"
            )
            findings.append(_unparseable_finding(dr_file))
            continue
        status = status_match.group(1).strip().lower()
        if not status.startswith("accepted"):
            continue
        eff_date, _path = _resolve_record_date(dr_file, text, scan_metadata)
        age = (today - eff_date).days
        dr_id = dr_file.stem

        has_learning_link = (
            dr_id in learning_links or dr_id in learnings_text
        )
        is_superseded = "superseded" in status or "deprecated" in status

        # T+30 decision review.
        if age >= int(review_threshold * 0.8) and not has_learning_link:
            sev = "P1" if age >= review_threshold else "P2"
            findings.append(
                Finding(
                    signal_type="decision_review_missing",
                    target_record_id=dr_id,
                    age_days=age,
                    threshold_days=review_threshold,
                    severity=sev,
                    human_readable=(
                        f"Accepted decision {dr_id} is {age}d old with no T+30 "
                        f"review link (threshold {review_threshold}d)."
                    ),
                )
            )

        # T+60 outcome review (+ P0 rot escalation at 90d).
        if age >= int(outcome_threshold * 0.8) and not has_learning_link:
            if age >= P0_DECISION_ROT_DAYS and not is_superseded:
                sev = "P0"
            elif age >= outcome_threshold:
                sev = "P1"
            else:
                sev = "P2"
            findings.append(
                Finding(
                    signal_type="outcome_review_missing",
                    target_record_id=dr_id,
                    age_days=age,
                    threshold_days=outcome_threshold,
                    severity=sev,
                    human_readable=(
                        f"Accepted decision {dr_id} is {age}d old with no T+60 "
                        f"outcome review (threshold {outcome_threshold}d)."
                    ),
                )
            )
    return findings


def _scan_handoff(
    handoff_file: Path, today: date, threshold: int, scan_metadata: dict
) -> list[Finding]:
    """handoff_stale: current-session.md mtime older than threshold."""
    if not handoff_file.exists():
        return []
    age = _mtime_age_days(handoff_file, today)
    if age < int(threshold * 0.8):
        return []
    sev = "P1" if age >= threshold else "P2"
    return [
        Finding(
            signal_type="handoff_stale",
            target_record_id=None,
            age_days=age,
            threshold_days=threshold,
            severity=sev,
            human_readable=(
                f"Session handoff ({handoff_file.name}) last updated {age}d ago "
                f"(threshold {threshold}d)."
            ),
        )
    ]


def _scan_learnings(
    learnings_dir: Path, today: date, threshold: int, scan_metadata: dict
) -> list[Finding]:
    """learning_log_dormant: learnings/index.md mtime older than threshold."""
    index_file = learnings_dir / "index.md"
    if not index_file.exists():
        return []
    age = _mtime_age_days(index_file, today)
    if age < int(threshold * 0.8):
        return []
    sev = "P1" if age >= threshold else "P2"
    return [
        Finding(
            signal_type="learning_log_dormant",
            target_record_id=None,
            age_days=age,
            threshold_days=threshold,
            severity=sev,
            human_readable=(
                f"Learning log (learnings/index.md) idle {age}d "
                f"(threshold {threshold}d)."
            ),
        )
    ]


def _unparseable_finding(path: Path) -> Finding:
    """P2 finding for a record that couldn't be parsed."""
    return Finding(
        signal_type="record_unparseable",
        target_record_id=path.stem,
        age_days=0,
        threshold_days=0,
        severity="P2",
        human_readable=f"Record could not be parsed at {path} — manual review needed.",
    )


# ---------------------------------------------------------------------------
# index.json cross-reference loading
# ---------------------------------------------------------------------------


def _load_learning_links(
    index_path: Path, scan_metadata: dict
) -> tuple[set[str], bool]:
    """Return (set of decision IDs that have learning cross-refs, index_available).

    Falls back to empty set + index_unavailable=True on missing/malformed index.
    """
    if not index_path.exists():
        scan_metadata["index_unavailable"] = True
        return set(), False
    try:
        data = json.loads(index_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as e:
        scan_metadata["index_unavailable"] = True
        scan_metadata.setdefault("parse_failures", []).append(
            f"{index_path}: {e}"
        )
        return set(), False
    cross = data.get("crossReferences", {})
    learning_to_decision = cross.get("learningToDecision", {})
    # learningToDecision maps L-NNN -> [DR-IDs] (or similar). Flatten values.
    linked_decisions: set[str] = set()
    for v in learning_to_decision.values():
        if isinstance(v, list):
            linked_decisions.update(v)
        elif isinstance(v, str):
            linked_decisions.add(v)
    return linked_decisions, True


def _gather_learnings_text(learnings_dir: Path) -> str:
    """Concatenate all markdown under learnings/ for body-text fallback search."""
    if not learnings_dir.exists() or not learnings_dir.is_dir():
        return ""
    chunks = []
    for md in learnings_dir.rglob("*.md"):
        try:
            chunks.append(md.read_text(encoding="utf-8", errors="replace"))
        except OSError:
            continue
    return "\n".join(chunks)


# ---------------------------------------------------------------------------
# Public entry point
# ---------------------------------------------------------------------------


def scan(
    context_root: Path,
    today: Optional[date] = None,
    threshold_overrides: Optional[dict] = None,
) -> CadenceFindings:
    """Walk context/ and return a CadenceFindings object.

    Read-only. Never raises on partial data. Always returns something
    actionable, even if degraded.
    """
    started = time.perf_counter()
    today = today or date.today()
    context_root = Path(context_root)
    thresholds = dict(DEFAULT_THRESHOLDS)
    if threshold_overrides:
        thresholds.update(threshold_overrides)

    scan_metadata: dict = {}
    findings: list[Finding] = []

    # Top-level missing → return single P1 finding.
    if not context_root.exists() or not context_root.is_dir():
        findings.append(
            Finding(
                signal_type="context_directory_missing",
                target_record_id=None,
                age_days=0,
                threshold_days=0,
                severity="P1",
                human_readable=(
                    f"No `context/` directory found at {context_root}. The OS "
                    f"context layer is not initialized. Run `/setup` to scaffold."
                ),
            )
        )
        return _finalize(findings, scan_metadata, started, today)

    # Load index.json cross-refs (with fallback).
    learning_links, _index_ok = _load_learning_links(
        context_root / "index.json", scan_metadata
    )
    learnings_text = _gather_learnings_text(context_root / "learnings")

    # Scan each slice. Permission errors are caught + logged + skipped.
    try:
        findings.extend(
            _scan_portfolio(
                context_root / "portfolio",
                today,
                thresholds["portfolio_review_overdue"],
                scan_metadata,
            )
        )
    except PermissionError as e:
        _log_perm_error(context_root / "portfolio", e, scan_metadata, findings)

    try:
        findings.extend(
            _scan_bets(
                context_root / "bets",
                today,
                thresholds["bet_review_overdue"],
                scan_metadata,
            )
        )
    except PermissionError as e:
        _log_perm_error(context_root / "bets", e, scan_metadata, findings)

    try:
        findings.extend(
            _scan_decisions(
                context_root / "decisions",
                today,
                thresholds["decision_review_missing"],
                thresholds["outcome_review_missing"],
                learning_links,
                learnings_text,
                scan_metadata,
            )
        )
    except PermissionError as e:
        _log_perm_error(context_root / "decisions", e, scan_metadata, findings)

    try:
        findings.extend(
            _scan_handoff(
                context_root / "handoffs" / "current-session.md",
                today,
                thresholds["handoff_stale"],
                scan_metadata,
            )
        )
    except PermissionError as e:
        _log_perm_error(
            context_root / "handoffs", e, scan_metadata, findings
        )

    try:
        findings.extend(
            _scan_learnings(
                context_root / "learnings",
                today,
                thresholds["learning_log_dormant"],
                scan_metadata,
            )
        )
    except PermissionError as e:
        _log_perm_error(
            context_root / "learnings", e, scan_metadata, findings
        )

    # Aggregate parse_failures into a single P2 finding for surfacing.
    pf = scan_metadata.get("parse_failures", [])
    if pf:
        findings.append(
            Finding(
                signal_type="parse_failures",
                target_record_id=None,
                age_days=0,
                threshold_days=0,
                severity="P2",
                human_readable=(
                    f"{len(pf)} record(s) could not be parsed — manual review "
                    f"needed. See scan_metadata.parse_failures."
                ),
            )
        )

    return _finalize(findings, scan_metadata, started, today)


def _log_perm_error(
    path: Path, err: Exception, scan_metadata: dict, findings: list[Finding]
) -> None:
    scan_metadata.setdefault("permission_errors", []).append(f"{path}: {err}")
    findings.append(
        Finding(
            signal_type="permission_error",
            target_record_id=None,
            age_days=0,
            threshold_days=0,
            severity="P2",
            human_readable=f"Could not read {path} — check permissions.",
        )
    )


def _finalize(
    findings: list[Finding], scan_metadata: dict, started: float, today: date
) -> CadenceFindings:
    """Build the summary block and return."""
    duration_ms = int((time.perf_counter() - started) * 1000)
    by_severity: dict[str, int] = {}
    by_signal: dict[str, int] = {}
    for f in findings:
        by_severity[f.severity] = by_severity.get(f.severity, 0) + 1
        by_signal[f.signal_type] = by_signal.get(f.signal_type, 0) + 1
    summary = {
        "total": len(findings),
        "by_severity": by_severity,
        "by_signal_type": by_signal,
        "scan_timestamp": datetime.now(timezone.utc).isoformat(),
        "scan_duration_ms": duration_ms,
        "scan_metadata": scan_metadata,
        "today": today.isoformat(),
    }
    return CadenceFindings(findings=findings, summary=summary)
