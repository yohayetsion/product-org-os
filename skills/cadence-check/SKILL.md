---
name: cadence-check
description: Internal cadence-stack scanner. Walks context/ and detects when Principle 8 cadence records (portfolio review, bet review, decision T+30/T+60, handoff, learning log) have gone stale or missing. Read-only. Not user-invocable directly — V5.1-31 (/cadence-adherence-telemetry) is the user-facing entry point.
user-invocable: false
metadata:
  author: Product Org OS
  version: 5.1.0
  category: cadence
  skill_type: task-capability
  owner: tech-lead
  primary_consumers:
    - cadence-adherence-telemetry
    - maturity-check
  sensitive: false
---

# cadence-check (V5.1-30)

Internal cadence-enforcement triggers skill. Implements Option A from the
H.5 V5.1-30 architecture spec: file-system scan on demand, no daemon, no
cron, no event bus.

The Python module `cadence_check.py` exposes one public entry point:

```python
from cadence_check import scan
findings = scan(context_root, today=None, threshold_overrides=None)
```

The returned `CadenceFindings` object carries a `findings` list (one
`Finding` per stale/missing cadence signal) and a `summary` block (totals
by severity and signal type, scan duration, and `scan_metadata` recording
which date-precedence path each record used plus any parse failures).

V5.1-31 (`/cadence-adherence-telemetry`) is the user-facing wrapper that
formats findings into a markdown document and persists it to
`context/telemetry/`. `/maturity-check` (V5.1-26/27/28 rewrite) reads
P0/P1 counts from this scan as input to the Three Tiers cadence
dimension.

This skill is **read-only**: it never writes to `context/`, never mutates
the index, and degrades gracefully on missing or malformed inputs. R-018
holds — V5.1-30 introduces a new module + new skill cell and touches zero
v5.0 surface.

See `cadence_check.py` for implementation and
`test_cadence_check.py` for the test suite.
