#!/usr/bin/env python3
"""make_aux.py — generate the auxiliary frozen artifacts the runner needs:

  1. fixtures/AR_anti_regression.jsonl   — 1 genuine tool_result receipt + 3
                                           assistant-text prose decoys. Proves the
                                           validator blind-vs-role-aware count gap.
  2. fixtures/01_subagent_tool_result.expected.json — the FULL canonical receipt
                                           for fixture 1, locking the entire
                                           schema shape (committed, diffed).

Deterministic. Run after build_fixtures.py. Idempotent.
"""
import importlib.util
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
HOOKS = HERE.parent
FX = HERE / "fixtures"

sys.path.insert(0, str(HERE))
import build_fixtures as bf  # noqa: E402
from _blocks import OS_BLOCK_WITH_DR, ET_BLOCK_NO_DR, JOINT_BLOCK  # noqa: E402


def build_anti_regression():
    objs = [
        bf.spawn_msg("toolu_AR1", "chief-architect"),
        bf.result_msg("toolu_AR1", OS_BLOCK_WITH_DR),          # genuine (blind can't see it)
        bf.assistant_text_msg("Here is my analysis. " + ET_BLOCK_NO_DR),  # prose decoy
        bf.assistant_text_msg(JOINT_BLOCK),                     # prose decoy (leads)
        bf.assistant_text_msg("Narrating: " + OS_BLOCK_WITH_DR),  # prose decoy
    ]
    bf.write_jsonl("AR_anti_regression.jsonl", objs)


def build_canonical_expected():
    spec = importlib.util.spec_from_file_location(
        "telemetry_extract", HOOKS / "telemetry-extract.py")
    te = importlib.util.module_from_spec(spec)
    sys.modules["telemetry_extract"] = te
    spec.loader.exec_module(te)
    cands = list(te.iter_receipts_from_jsonl(FX / "01_subagent_tool_result.jsonl"))
    receipt = te.build_receipt(cands[0])
    out = FX / "01_subagent_tool_result.expected.json"
    out.write_text(json.dumps(receipt, ensure_ascii=True, indent=2) + "\n",
                   encoding="utf-8")


if __name__ == "__main__":
    build_anti_regression()
    build_canonical_expected()
    print("Wrote AR fixture + canonical expected json to", FX)
