#!/usr/bin/env python3
"""expectations.py — the 11 golden expectations + edge expectations.

Each entry declares, for one frozen fixture, exactly what the extractor MUST
yield. The runner (`run_tests.py`) computes the ACTUAL receipts and asserts the
declared fields by diff. We assert on STABLE, load-bearing fields only (count,
slug, format, source, decision_records.present, roi.minutes, authors, tool_use_id)
plus, for fixture 1, the full canonical receipt (committed as
`fixtures/01_subagent_tool_result.expected.json`) to lock the entire schema shape.

Authoring note (QA, 2026-05-30): expectations are hand-derived from the design
§4 MUST-yield table, NOT copied from a tool run. They are the spec. The runner
proves the build conforms to them.
"""

# Per-fixture expectation.
#   file:            frozen fixture filename under fixtures/
#   include_at:      pass --include-assistant-text equivalent
#   count:           number of receipts MUST yield
#   receipts:        ordered list of partial dicts; each asserted field-by-field
#                    against the actual receipt at the same index. Omitted fields
#                    are not asserted (e.g. block_hash, ts — stable but noisy).
EXPECTATIONS = [
    {
        "id": 1,
        "name": "subagent-receipt-in-tool_result (P0 happy path)",
        "file": "01_subagent_tool_result.jsonl",
        "include_at": False,
        "count": 1,
        "receipts": [{
            "agent_slug": "chief-architect",
            "format": "v2",
            "source": "tool_result",
            "tool_use_id": "toolu_0001",
            "authors": ["chief-architect"],
            "decision_records.present": True,
            "roi.minutes": 180,
            "roi.tokens": 58000,
            "roi.value_usd": 300,
            "roi.measured_tokens": 58000,
            "roi.drift": 1.0,
            "loads.preload_packs.count": 3,
            "loads.skill_md.ok": True,
        }],
    },
    {
        "id": 2,
        "name": "clean v2 assistant emission (only with --include-assistant-text)",
        "file": "02_assistant_text.jsonl",
        "include_at": False,
        "count": 0,
        "receipts": [],
        "also": {  # second assertion with the flag ON
            "include_at": True,
            "count": 1,
            "receipts": [{
                "agent_slug": "qa-engineer",
                "format": "v2",
                "source": "assistant-text",
                "tool_use_id": None,
                "decision_records": {},   # ET block: DR section omitted -> empty dict (§3.1)
                "roi.minutes": 120,
            }],
        },
    },
    {
        "id": 3,
        "name": "v1-legacy Pre-Execution Self-Check",
        "file": "03_v1_legacy.jsonl",
        "include_at": False,
        "count": 1,
        "receipts": [{
            "agent_slug": "product-manager",
            "format": "v1-legacy",
            "source": "tool_result",
            "tool_use_id": "toolu_0003",
            "roi.minutes": None,
        }],
    },
    {
        "id": 4,
        "name": "pure-decoy (Read tool_result with valid block, NO Agent spawn)",
        "file": "04_pure_decoy.jsonl",
        "include_at": False,
        "count": 0,
        "receipts": [],
    },
    {
        "id": 5,
        "name": "mixed (genuine + decoy) -> exact genuine count",
        "file": "05_mixed.jsonl",
        "include_at": False,
        "count": 1,
        "receipts": [{
            "agent_slug": "chief-architect",
            "format": "v2",
            "source": "tool_result",
            "tool_use_id": "toolu_0005a",
            "decision_records.present": True,
        }],
    },
    {
        "id": 6,
        "name": "joint-authoring -> 1, format joint + authors[]",
        "file": "06_joint.jsonl",
        "include_at": False,
        "count": 1,
        "receipts": [{
            "format": "joint",
            "source": "tool_result",
            "tool_use_id": "toolu_0006",
            "authors": ["director-product-marketing", "copywriter"],
            "roi.minutes": 240,
        }],
    },
    {
        "id": 7,
        "name": "cross-file duplicate tool_use_id -> 1 written (write-layer idempotency)",
        # Idempotency is a WRITE-layer property (design R4: ".telemetry-dedup gates
        # the WRITE"). The raw extractor yields one receipt per file (2); the
        # writer collapses the duplicate tool_use_id to ONE persisted line. The
        # runner asserts this via the dedup-write check, NOT via raw receipt count.
        "write_dedup": {
            "files": ["07a_dup.jsonl", "07b_dup.jsonl"],
            "expected_written_lines": 1,
            "dup_key": "toolu_DUP777",
        },
    },
    {
        "id": 8,
        "name": "truncated block (no [Post-Execution ROI]) -> 1, roi.minutes None",
        "file": "08_truncated.jsonl",
        "include_at": False,
        "count": 1,
        "receipts": [{
            "agent_slug": "product-manager",
            "format": "v2",
            "source": "tool_result",
            "tool_use_id": "toolu_0008",
            "roi.minutes": None,
            "roi.value_usd": None,
        }],
    },
    {
        "id": 9,
        "name": "malformed-JSON line mid-transcript -> skip + continue, exit 0",
        "file": "09_malformed.jsonl",
        "include_at": False,
        "count": 1,
        "receipts": [{
            "agent_slug": "chief-architect",
            "format": "v2",
            "tool_use_id": "toolu_0009",
            "decision_records.present": True,
        }],
    },
    {
        "id": 10,
        "name": "block inside Read/Bash tool_result -> 0 (tool-name join rejects)",
        "file": "10_block_in_read.jsonl",
        "include_at": False,
        "count": 0,
        "receipts": [],
    },
    {
        "id": 11,
        "name": "OS block WITH [Decision Records] -> 1, decision_records.present True",
        "file": "11_os_with_dr.jsonl",
        "include_at": False,
        "count": 1,
        "receipts": [{
            "agent_slug": "chief-architect",
            "format": "v2",
            "source": "tool_result",
            "tool_use_id": "toolu_0011",
            "decision_records.present": True,
        }],
    },
    {
        "id": 13,
        "name": "FX-1 sensitive-skill number-first ROI -> roi.minutes 240",
        "file": "13_sensitive_roi_number_first.jsonl",
        "include_at": False,
        "count": 1,
        "receipts": [{
            "agent_slug": "contracts-counsel",
            "format": "v2",
            "source": "tool_result",
            "tool_use_id": "toolu_SENS13",
            "roi.minutes": 240,           # "~4 hrs saved on drafting and triage"
            "roi.value_usd": 400,
        }],
    },
    {
        "id": 14,
        "name": "A4 genuine spawn, prose name-drops header, no [section] -> 0",
        "file": "14_prose_header_only.jsonl",
        "include_at": False,
        "count": 0,
        "receipts": [],
    },
    {
        "id": 15,
        "name": "A5 BOM-prefixed transcript -> line 1 not dropped -> 1 receipt",
        "file": "15_bom_prefixed.jsonl",
        "include_at": False,
        "count": 1,
        "receipts": [{
            "agent_slug": "chief-architect",
            "format": "v2",
            "source": "tool_result",
            "tool_use_id": "toolu_BOM15",
            "decision_records.present": True,
        }],
    },
]

# FX-5: TWO distinct blocks in ONE tool_result (one tool_use_id) MUST both
# persist to the canonical jsonl. The composite dedup key (tool_use_id:hash)
# distinguishes them; a tool_use_id-only key would collapse them to one line.
FX5_TWO_BLOCKS = {
    "file": "12_two_blocks_one_result.jsonl",
    "shared_tool_use_id": "toolu_TWO12",
    "raw_receipt_count": 2,        # extractor yields 2 blocks from the one result
    "written_lines": 2,           # writer persists BOTH (composite key)
}

# Anti-regression (Phase 2): validator blind vs role-aware count on one fixture.
ANTI_REGRESSION = {
    "file": "AR_anti_regression.jsonl",
    "blind_count": 3,        # legacy blind scan over-counts prose decoys
    "role_aware_count": 1,   # join keeps only the genuine tool_result receipt
}

# Edge fixtures asserted only for "exit 0 + no crash + count".
EDGE = [
    {"name": "zero-byte file", "file": "zero_byte.jsonl", "count": 0},
    {"name": "missing path", "file": "__DOES_NOT_EXIST__.jsonl", "count": 0},
    {"name": "text-mode", "file": "text_mode.txt", "mode": "text", "count": 1},
]
