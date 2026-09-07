#!/usr/bin/env python3
"""Reserve the next free context id ATOMICALLY, before the record is written.

WHY THIS EXISTS
---------------
Context ids are minted by "read the highest number, add one". Two sessions
that read before either writes both compute the same number. On 2026-08-02
that produced five collisions across five namespaces in one day -- two of them
DURING the cleanup task -- and one let an owner affirmation attach to a record
he never affirmed.

`check-dr-ids.py` and `check-context-ids.py` DETECT that after the fact.
This script PREVENTS it, for callers that use it, by making read-max and
claim-it a single critical section guarded by an O_EXCL lockfile, and by
recording the claim in `context/ids/reservations.jsonl` BEFORE the record
file exists.

THE GUARANTEE, HONESTLY -- do not overclaim this
------------------------------------------------
    Collision-safe across concurrent sessions on ONE machine, for callers
    that use the allocator. NOT safe across machines. Non-cooperating callers
    are caught by the Phase 0.3 post-write detector, not prevented.

Cross-machine is not fixable by this route: two machines share the registry
through Google Drive File Stream, whose sync is eventually consistent and
offers no cross-host exclusion primitive. An O_EXCL create on machine A is
invisible to machine B until sync catches up.

USAGE
    python context/allocate-id.py --ns DR
    python context/allocate-id.py --ns A --note "capability-embed assumption"
    python context/allocate-id.py --ns DOC --json
    python context/allocate-id.py --ns DR --year 2027

    ID=$(python context/allocate-id.py --ns DR) || exit 1   # fail-closed

EXIT CODES
    0  allocated -- the id is on stdout, and ONLY the id
    1  refused   -- lock unobtainable, lock stolen mid-flight, or an internal
                    error. NOTHING is written to stdout. Never guesses.
    2  usage error (argparse). Also not an allocation.

FAIL-CLOSED IS THE POINT. If this script cannot prove it holds the lock, it
refuses rather than handing back a number it cannot vouch for.
"""
from __future__ import annotations

import json
import os
import re
import sys
import time
import uuid
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent          # <workspace>/context
IDS_DIR = HERE / "ids"
LOCK = IDS_DIR / ".allocate.lock"
RESERVATIONS = IDS_DIR / "reservations.jsonl"

# How old a lockfile must be before it is treated as abandoned and broken.
#
# Set from measurement, not taste. The critical section is a few filesystem
# scans of the live registry over Google Drive File Stream; the slowest
# namespace (DR, the only one with hundreds of record files) measured 641ms
# before the os.walk change below and ~40ms after, and it grows with the
# record count. 120s is >1000x the measured worst case with room for the
# registry to grow an order of magnitude.
#
# Getting this wrong is deliberately not dangerous in the direction that
# matters: assert_still_ours() re-proves ownership immediately before the
# reservation is committed, so a lock broken too eagerly produces a loud
# REFUSAL from the stalled holder, never a duplicate id. The timeout tunes
# liveness; the token check is what provides safety.
#
# Deliberately NOT configurable: a flag that shortens it is a flag that
# defeats the lock. Tests age the lockfile with os.utime() instead, which
# exercises the real production path rather than a test-only branch.
STALE_SECONDS = 120.0

# How long to wait for a lock held by a LIVE process before refusing.
DEFAULT_WAIT_SECONDS = 10.0
POLL_SECONDS = 0.05


# --------------------------------------------------------------------------
# Namespace adapters
# --------------------------------------------------------------------------
# The six namespaces are three different storage shapes, not one:
#   DR, FB   -- one file per record under <dir>/YYYY/ AND a row in an index
#   SB       -- rows in an index today; the per-year record dir is specified
#               (context-management.md) but not yet created
#   A, L     -- rows inside one markdown index file, no year in the id
#   DOC      -- rows inside one markdown index file, year in the id
#
# Every adapter is given BOTH a records dir and an index, uniformly. Where a
# namespace has no record files the rglob simply returns nothing -- that costs
# one cheap directory walk and removes six special cases, and it means the day
# someone starts writing `context/bets/2026/SB-*.md` the allocator already
# sees them.

class Namespace:
    def __init__(self, prefix: str, yearly: bool, index_rel: str, records_rel: str):
        self.prefix = prefix
        self.yearly = yearly
        self.index = HERE / index_rel
        self.records_dir = HERE / records_rel

        # DELIBERATELY WIDER THAN THE DETECTORS. See "Blind spots" below.
        num = r"(\d+)"
        if yearly:
            self._file_re = re.compile(rf"^{prefix}-(\d{{4}})-{num}")
            self._cell_re = re.compile(rf"\b{prefix}-(\d{{4}})-{num}")
        else:
            self._file_re = re.compile(rf"^{prefix}-{num}")
            self._cell_re = re.compile(rf"\b{prefix}-{num}")

    # -- the three claim readers ------------------------------------------
    def _from_files(self, year: str) -> set[int]:
        """Every record file on disk claiming this namespace.

        Walks EVERY subdirectory, not only the ones whose name is a 4-digit
        year. check-dr-ids.py only walks `name.isdigit()` dirs, so a record
        parked in `decisions/archive/` is invisible to it. The allocator
        scanning the superset means it can never hand out a number that an
        unpoliced file already claims.
        """
        out: set[int] = set()
        if not self.records_dir.is_dir():
            return out
        # os.walk, not Path.rglob: rglob calls is_file() on every hit, which is
        # one stat syscall each. Over Google Drive File Stream that measured
        # 641ms for the 207 DR files; os.walk yields filenames already split
        # into dirs/files by the directory read, so the stats disappear.
        for _root, _dirs, files in os.walk(self.records_dir):
            for name in files:
                m = self._file_re.match(name)
                if not m:
                    continue
                if self.yearly:
                    if m.group(1) != year:
                        continue
                    out.add(int(m.group(2)))
                else:
                    out.add(int(m.group(1)))
        return out

    def _from_index(self, year: str) -> set[int]:
        """Every id registered in the index — as a leading TABLE CELL or a HEADING.

        ⛔ Table rows alone were not enough, and the gap collided a real id.
        `assumptions/registry.md` and `learnings/index.md` each begin as a table
        and then switch to `## A-137 — …` / `## L-370 — …` section headings for
        newer entries. Scanning only table cells, this method saw A-001..A-118
        and missed everything after — so on 2026-08-20 the allocator handed out
        **A-137, which the registry already held**, having been written by a
        session that did not reserve it.

        Reservations alone cannot cover that case: they record what THIS tool
        handed out, never what someone wrote by hand. The index is the only
        source that sees a hand-written id, so it has to read the index the way
        the index is actually written.

        Adding a source can only ever WIDEN the claimed set, so this is strictly
        the conservative direction: it can refuse a free number, never hand out
        a taken one.
        """
        out: set[int] = set()
        if not self.index.is_file():
            return out
        text = self.index.read_text(encoding="utf-8", errors="replace")
        for line in text.splitlines():
            stripped = line.lstrip()          # tolerate indented rows
            if stripped.startswith("#"):
                m = self._cell_re.search(stripped.lstrip("#").strip())
                if m:
                    if self.yearly:
                        if m.group(1) == year:
                            out.add(int(m.group(2)))
                    else:
                        out.add(int(m.group(1)))
                continue
            if not stripped.startswith("|"):
                continue
            parts = stripped.split("|")
            if len(parts) < 3:
                continue
            first_cell = parts[1]
            m = self._cell_re.search(first_cell)   # search, not fullmatch:
            if not m:                              # a bolded/decorated cell
                continue                           # still registers an id
            if self.yearly:
                if m.group(1) != year:
                    continue
                out.add(int(m.group(2)))
            else:
                out.add(int(m.group(1)))
        return out

    def _from_reservations(self, year: str) -> set[int]:
        """Ids this allocator has already handed out.

        Without this, two allocations with no intervening record write return
        the same number -- which is the exact defect, reintroduced one layer up.
        """
        out: set[int] = set()
        if not RESERVATIONS.is_file():
            return out
        for line in RESERVATIONS.read_text(encoding="utf-8", errors="replace").splitlines():
            line = line.strip()
            if not line:
                continue
            try:
                row = json.loads(line)
            except (ValueError, TypeError):
                continue          # torn/garbage line -- see append_reservation
            if row.get("ns") != self.prefix:
                continue
            m = self._cell_re.search(str(row.get("id", "")))
            if not m:
                continue
            if self.yearly:
                if m.group(1) != year:
                    continue
                out.add(int(m.group(2)))
            else:
                out.add(int(m.group(1)))
        return out

    def claimed(self, year: str) -> tuple[set[int], dict[str, int]]:
        files = self._from_files(year)
        index = self._from_index(year)
        resv = self._from_reservations(year)
        return files | index | resv, {
            "files": len(files), "index": len(index), "reservations": len(resv)
        }

    def format(self, n: int, year: str) -> str:
        # Always >= 3 digits. This is what keeps every id this script mints
        # inside the set the detectors police -- check-dr-ids.py's ID_RE
        # requires \d{3,} and would silently skip a 2-digit id.
        return f"{self.prefix}-{year}-{n:03d}" if self.yearly else f"{self.prefix}-{n:03d}"


NAMESPACES = {
    "DR":  Namespace("DR",  True,  "decisions/index.md",      "decisions"),
    "FB":  Namespace("FB",  True,  "feedback/index.md",       "feedback"),
    "SB":  Namespace("SB",  True,  "bets/index.md",           "bets"),
    "DOC": Namespace("DOC", True,  "documents/index.md",      "documents"),
    "A":   Namespace("A",   False, "assumptions/registry.md", "assumptions"),
    "L":   Namespace("L",   False, "learnings/index.md",      "learnings"),
}


# --------------------------------------------------------------------------
# The lock
# --------------------------------------------------------------------------
# ONE global lock, not one per namespace. Namespaces are independent, so
# per-namespace locks would be more concurrent -- but allocations happen a
# handful of times an hour and take tens of milliseconds, so the contention
# saved is zero, while a single lock also serialises the shared reservations
# append for free. One lock is the smaller correct design.

class LockRefused(Exception):
    pass


class LockStolen(Exception):
    pass


def _break_if_stale(now: float) -> bool:
    """Atomically remove the lock IF it is older than STALE_SECONDS.

    The break is a rename to a caller-unique path. os.replace is atomic, so if
    two processes both decide the lock is stale exactly one rename finds the
    source present; the loser gets FileNotFoundError and simply retries the
    O_EXCL create. That is what stops "recover from a stale lock" turning into
    "two processes proceed at once".
    """
    try:
        age = now - os.stat(LOCK).st_mtime
    except FileNotFoundError:
        return True                     # already gone; retry the create
    if age <= STALE_SECONDS:
        return False
    steal = LOCK.with_name(f"{LOCK.name}.steal-{os.getpid()}-{uuid.uuid4().hex[:8]}")
    try:
        os.replace(LOCK, steal)
    except OSError:
        return False                    # someone else broke it, or it is busy
    try:
        os.remove(steal)
    except OSError:
        pass
    sys.stderr.write(f"allocate-id: broke a stale lock (age {age:.1f}s > {STALE_SECONDS:.0f}s)\n")
    return True


def acquire(wait_seconds: float) -> str:
    """Take the lock. Return our ownership token. Raise LockRefused on timeout."""
    IDS_DIR.mkdir(parents=True, exist_ok=True)
    token = f"{os.getpid()}-{uuid.uuid4().hex}"
    body = json.dumps({
        "token": token,
        "pid": os.getpid(),
        "host": os.environ.get("COMPUTERNAME") or os.environ.get("HOSTNAME") or "",
        "acquired_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
    }).encode("utf-8")

    deadline = time.time() + max(wait_seconds, 0.0)
    while True:
        try:
            fd = os.open(str(LOCK), os.O_CREAT | os.O_EXCL | os.O_WRONLY)
        except FileExistsError:
            pass
        else:
            try:
                os.write(fd, body)
            finally:
                os.close(fd)
            return token

        now = time.time()
        _break_if_stale(now)
        if now >= deadline:
            raise LockRefused(
                f"could not take {LOCK} within {wait_seconds:g}s -- another allocation "
                f"is in flight. Refusing rather than guessing an id."
            )
        time.sleep(POLL_SECONDS)


def assert_still_ours(token: str) -> None:
    """Re-prove ownership before committing.

    The stale-break path is the one way two processes could ever both believe
    they hold the lock (holder stalls past STALE_SECONDS, another breaks it).
    Re-reading the token immediately before the reservation is appended turns
    that from a silent duplicate into a loud refusal.
    """
    try:
        held = json.loads(LOCK.read_text(encoding="utf-8")).get("token")
    except (OSError, ValueError, TypeError):
        raise LockStolen("the lockfile vanished or was rewritten mid-allocation")
    if held != token:
        raise LockStolen("the lock was taken over by another process mid-allocation")


def release(token: str) -> None:
    try:
        held = json.loads(LOCK.read_text(encoding="utf-8")).get("token")
    except (OSError, ValueError, TypeError):
        return                          # not ours to remove
    if held == token:
        try:
            os.remove(LOCK)
        except OSError:
            pass


# --------------------------------------------------------------------------
# The reservation ledger
# --------------------------------------------------------------------------

def append_reservation(row: dict) -> None:
    """Append one JSON line, durably, healing a torn trailing line first.

    A crash between os.write and fsync can leave a partial line. That is SAFE
    here in a way worth stating: a process that died mid-append also never
    wrote the record, so re-issuing that number later is correct, not a
    collision. What is NOT safe is the partial line corrupting the NEXT
    append, so if the file does not end in a newline we add one first.
    """
    line = json.dumps(row, ensure_ascii=True, sort_keys=True) + "\n"
    prefix = ""
    if RESERVATIONS.is_file() and RESERVATIONS.stat().st_size:
        with open(RESERVATIONS, "rb") as fh:
            fh.seek(-1, os.SEEK_END)
            if fh.read(1) != b"\n":
                prefix = "\n"
    fd = os.open(str(RESERVATIONS), os.O_CREAT | os.O_APPEND | os.O_WRONLY)
    try:
        os.write(fd, (prefix + line).encode("utf-8"))
        os.fsync(fd)
    finally:
        os.close(fd)


# --------------------------------------------------------------------------

def backfill_unreserved(ns, ns_key: str, year: str) -> list[str]:
    """Write a ledger row for every id the records/index claim but the ledger
    does not. Returns the ids back-filled (usually empty after the first run).

    Called with the lock held, from `allocate()`. Marked `"source": "backfill"`
    so it is never mistaken for evidence that this tool granted the number --
    it is evidence that something else did.
    """
    seen = ns._from_files(year) | ns._from_index(year)
    have = ns._from_reservations(year)
    missing = sorted(seen - have)
    now = datetime.now(timezone.utc).isoformat(timespec="seconds")
    out = []
    for n in missing:
        _id = ns.format(n, year)
        append_reservation({
            "id": _id, "ns": ns_key, "year": year if ns.yearly else None,
            "reserved_at": now, "pid": os.getpid(),
            "host": os.environ.get("COMPUTERNAME") or os.environ.get("HOSTNAME") or "",
            "note": "backfill: claimed in the records/index, never reserved",
            "source": "backfill",
        })
        out.append(_id)
    return out


def allocate(ns_key: str, year: str, note: str, wait_seconds: float) -> dict:
    ns = NAMESPACES[ns_key]
    token = acquire(wait_seconds)
    try:
        claimed, sources = ns.claimed(year)
        nxt = (max(claimed) + 1) if claimed else 1
        new_id = ns.format(nxt, year)

        assert_still_ours(token)          # last check before we commit

        # ── SELF-HEALING: remember ids this tool never handed out ───────────
        # Reservations record what the ALLOCATOR granted. They are blind to an
        # id a session wrote by hand -- and hand-minting is always possible,
        # because ids are assigned by a language model reading prose in another
        # process. On 2026-08-17 six ids were hand-minted; the scanners could
        # not see their shape, so this allocator granted the same six numbers to
        # a cooperating caller and produced six collisions.
        #
        # Widening the scanners fixed that shape. This fixes the CLASS: every id
        # visible in the records or the index but absent from the ledger is
        # back-filled now, marked `backfill`, so the ledger converges on the
        # truth and a LATER scanner blind spot still cannot resurrect a number
        # that some file already claims. Costs one pass over data already read.
        backfilled = backfill_unreserved(ns, ns_key, year)

        row = {
            "id": new_id,
            "ns": ns_key,
            "year": year if ns.yearly else None,
            "reserved_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
            "pid": os.getpid(),
            "host": os.environ.get("COMPUTERNAME") or os.environ.get("HOSTNAME") or "",
            "note": note or "",
        }
        append_reservation(row)
        return {"id": new_id, "ns": ns_key, "year": row["year"],
                "claimed": len(claimed), "sources": sources,
                "backfilled": backfilled,
                "reservations_file": str(RESERVATIONS)}
    finally:
        release(token)


def main(argv: list[str]) -> int:
    import argparse
    ap = argparse.ArgumentParser(
        prog="allocate-id.py",
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    ap.add_argument("--ns", required=True, choices=sorted(NAMESPACES),
                    help="id namespace to allocate from")
    ap.add_argument("--year", default=str(datetime.now().year),
                    help="year namespace for DR/FB/SB/DOC (default: current year)")
    ap.add_argument("--note", default="", help="why this id was reserved (recorded)")
    ap.add_argument("--wait-seconds", type=float, default=DEFAULT_WAIT_SECONDS,
                    help="how long to wait for a live lock before refusing")
    ap.add_argument("--json", action="store_true", help="emit the full record as JSON")
    ap.add_argument("--backfill-only", action="store_true",
                    help="record ids already claimed in the records/index into the "
                         "ledger, WITHOUT allocating a new one")
    args = ap.parse_args(argv)

    if not re.fullmatch(r"\d{4}", args.year):
        sys.stderr.write(f"allocate-id: --year must be 4 digits, got {args.year!r}\n")
        return 1

    if args.backfill_only:
        # Converge the ledger without burning a number. Same lock, same writer.
        ns = NAMESPACES[args.ns]
        token = acquire(args.wait_seconds)
        try:
            assert_still_ours(token)
            done = backfill_unreserved(ns, args.ns, args.year)
        finally:
            release(token)
        if args.json:
            print(json.dumps({"ns": args.ns, "backfilled": done}, indent=2))
        else:
            print(f"{args.ns}: back-filled {len(done)} id(s) into the ledger"
                  + (f" — {done[0]} … {done[-1]}" if done else ""))
        return 0

    try:
        result = allocate(args.ns, args.year, args.note, args.wait_seconds)
    except LockRefused as e:
        sys.stderr.write(f"allocate-id: REFUSED -- {e}\n")
        return 1
    except LockStolen as e:
        sys.stderr.write(
            f"allocate-id: REFUSED -- {e}. No id was reserved; nothing was written. "
            f"Re-run.\n")
        return 1
    except Exception as e:                                  # noqa: BLE001
        sys.stderr.write(
            f"allocate-id: REFUSED -- {type(e).__name__}: {e}. "
            f"No id was reserved. A broken allocator must never look like a working one.\n")
        return 1

    print(json.dumps(result, indent=2) if args.json else result["id"])
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
