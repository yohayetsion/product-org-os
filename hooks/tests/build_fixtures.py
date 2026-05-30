#!/usr/bin/env python3
"""build_fixtures.py — (re)generate the 11 FROZEN telemetry fixtures.

Each fixture is a static, hand-built `.jsonl` (or `.txt` for text mode) under
`fixtures/`. They do NOT reference the live `~/.claude/projects/<project>` dir,
so transcript-ID recycling (the c0e15e9f->0 anchor going stale) cannot break them.

The Claude-Code envelope shapes here were verified against a real transcript
(c0e15e9f) on 2026-05-30:
  - tool_use (name=Agent|Task) lives in an `assistant`-role message; carries
    `input.prompt` with the identity sentinel + `input.description` ([slug] convention).
  - tool_result is wrapped in a `user`-role message; `content` is a LIST whose
    text part(s) carry the subagent's emitted audit block.

Run: python build_fixtures.py   (idempotent; overwrites fixtures/*.jsonl)
"""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
FX = os.path.join(HERE, "fixtures")
os.makedirs(FX, exist_ok=True)

import sys
sys.path.insert(0, HERE)
from _blocks import (
    OS_BLOCK_WITH_DR, ET_BLOCK_NO_DR, V1_LEGACY_BLOCK, JOINT_BLOCK,
    TRUNCATED_BLOCK, OS_BLOCK_SECOND,
    SECOND_DISTINCT_BLOCK, SENSITIVE_ROI_NUMBER_FIRST_BLOCK, PROSE_HEADER_ONLY,
)

SENTINEL_PROMPT = (
    "## Agent Identity & Operating Protocol\n\n"
    "You are **{emoji} {name}** {prep} a simulated Product Organization.\n"
    "### REQUIRED FIRST ACTIONS...\n"
)


def spawn_msg(tool_id, slug, name="Chief Architect", emoji="🏗️", prep="in",
              tool_name="Agent"):
    """An assistant-role message carrying a genuine Agent/Task tool_use."""
    prompt = SENTINEL_PROMPT.format(emoji=emoji, name=name, prep=prep)
    return {
        "type": "assistant",
        "message": {
            "role": "assistant",
            "content": [
                {"type": "text", "text": "Spawning the agent now."},
                {
                    "type": "tool_use",
                    "id": tool_id,
                    "name": tool_name,
                    "input": {
                        "description": f"[{slug}] do the task",
                        "subagent_type": "general-purpose",
                        "prompt": prompt,
                    },
                },
            ],
        },
        "timestamp": "2026-05-30T09:15:00Z",
    }


def result_msg(tool_id, block_text, usage=None):
    """A user-role message wrapping a tool_result whose text carries the block."""
    msg = {
        "type": "user",
        "message": {
            "role": "user",
            "content": [
                {
                    "type": "tool_result",
                    "tool_use_id": tool_id,
                    "content": [{"type": "text", "text": block_text}],
                }
            ],
        },
        "timestamp": "2026-05-30T09:18:00Z",
    }
    if usage is not None:
        msg["message"]["usage"] = usage
    return msg


def result_msg_two_blocks(tool_id, block_a, block_b, usage=None):
    """A tool_result whose text carries TWO distinct audit blocks (FX-5). They
    share one tool_use_id; both must be extracted AND both must persist (the
    composite dedup key keys on tool_use_id:block_hash, not tool_use_id alone)."""
    combined = block_a + "\n\n" + block_b
    return result_msg(tool_id, combined, usage=usage)


def decoy_tool_msg(tool_id, tool_name, block_text):
    """A genuine NON-Agent tool_use (Read/Bash) + its result carrying a block.

    The tool_use_id is NOT in the spawn map (its tool_use named Read/Bash), so the
    join must reject the block. This is the hard-decoy class.
    """
    use = {
        "type": "assistant",
        "message": {
            "role": "assistant",
            "content": [
                {"type": "tool_use", "id": tool_id, "name": tool_name,
                 "input": {"file_path": "x.md"} if tool_name == "Read"
                          else {"command": "cat x.md"}},
            ],
        },
        "timestamp": "2026-05-30T09:20:00Z",
    }
    res = {
        "type": "user",
        "message": {
            "role": "user",
            "content": [
                {"type": "tool_result", "tool_use_id": tool_id,
                 "content": [{"type": "text", "text": block_text}]},
            ],
        },
        "timestamp": "2026-05-30T09:21:00Z",
    }
    return [use, res]


def assistant_text_msg(block_text):
    """An assistant message that LEADS with the audit block as plain text."""
    return {
        "type": "assistant",
        "message": {
            "role": "assistant",
            "content": [{"type": "text", "text": block_text}],
        },
        "timestamp": "2026-05-30T09:25:00Z",
    }


def user_text_msg(text):
    return {"type": "user", "message": {"role": "user", "content": text},
            "timestamp": "2026-05-30T09:10:00Z"}


def write_jsonl(name, objs):
    path = os.path.join(FX, name)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        for o in objs:
            if isinstance(o, str):           # raw line (for malformed-JSON fixture)
                f.write(o + "\n")
            else:
                f.write(json.dumps(o, ensure_ascii=True) + "\n")
    return path


def write_jsonl_bom(name, objs):
    """Like write_jsonl but prepends a UTF-8 BOM to line 1 (A5 fixture). Written
    as raw bytes so the BOM lands verbatim ahead of the first JSON object."""
    path = os.path.join(FX, name)
    lines = [json.dumps(o, ensure_ascii=True) for o in objs]
    body = "\n".join(lines) + "\n"
    with open(path, "wb") as f:
        f.write("﻿".encode("utf-8"))   # BOM
        f.write(body.encode("utf-8"))
    return path


def write_text(name, text):
    path = os.path.join(FX, name)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    return path


def build():
    # 1 — subagent receipt in tool_result (P0 happy path)
    write_jsonl("01_subagent_tool_result.jsonl", [
        user_text_msg("Please run the architecture review."),
        spawn_msg("toolu_0001", "chief-architect"),
        result_msg("toolu_0001", OS_BLOCK_WITH_DR, usage={
            "input_tokens": 40000, "output_tokens": 18000}),
    ])

    # 2 — clean v2 assistant emission (only counted with --include-assistant-text)
    write_jsonl("02_assistant_text.jsonl", [
        user_text_msg("Adopt the QA persona inline."),
        assistant_text_msg(ET_BLOCK_NO_DR),
    ])

    # 3 — v1-legacy Pre-Execution Self-Check (in a genuine spawn's tool_result)
    write_jsonl("03_v1_legacy.jsonl", [
        spawn_msg("toolu_0003", "product-manager", name="Product Manager",
                  emoji="📝"),
        result_msg("toolu_0003", V1_LEGACY_BLOCK),
    ])

    # 4 — pure decoy: a Read tool_result carrying a valid block, NO Agent spawn -> 0
    objs = [user_text_msg("Read the design note.")]
    objs += decoy_tool_msg("toolu_0004", "Read", OS_BLOCK_WITH_DR)
    write_jsonl("04_pure_decoy.jsonl", objs)

    # 5 — mixed: genuine spawn + decoy in same file -> exactly the genuine count (1)
    objs = [
        spawn_msg("toolu_0005a", "chief-architect"),
        result_msg("toolu_0005a", OS_BLOCK_WITH_DR),
    ]
    objs += decoy_tool_msg("toolu_0005b", "Bash", ET_BLOCK_NO_DR)  # decoy, rejected
    objs.append(assistant_text_msg(JOINT_BLOCK))  # prose narration, OFF by default
    write_jsonl("05_mixed.jsonl", objs)

    # 6 — joint-authoring block
    write_jsonl("06_joint.jsonl", [
        spawn_msg("toolu_0006", "director-product-marketing",
                  name="Director of Product Marketing", emoji="📣"),
        result_msg("toolu_0006", JOINT_BLOCK),
    ])

    # 7 — cross-file duplicate tool_use_id (idempotency). Two files, SAME id.
    write_jsonl("07a_dup.jsonl", [
        spawn_msg("toolu_DUP777", "chief-architect"),
        result_msg("toolu_DUP777", OS_BLOCK_WITH_DR),
    ])
    write_jsonl("07b_dup.jsonl", [
        spawn_msg("toolu_DUP777", "chief-architect"),
        result_msg("toolu_DUP777", OS_BLOCK_WITH_DR),
    ])

    # 8 — truncated block (no [Post-Execution ROI]) -> 1, roi.minutes=None
    write_jsonl("08_truncated.jsonl", [
        spawn_msg("toolu_0008", "product-manager", name="Product Manager",
                  emoji="📝"),
        result_msg("toolu_0008", TRUNCATED_BLOCK),
    ])

    # 9 — malformed-JSON line mid-transcript -> skip + continue, still yields 1
    write_jsonl("09_malformed.jsonl", [
        spawn_msg("toolu_0009", "chief-architect"),
        "{ this is not valid json at all >>>",          # raw broken line
        result_msg("toolu_0009", OS_BLOCK_WITH_DR),
    ])

    # 10 — audit block inside a Read tool_result (HARD decoy) -> 0
    #      (identical idea to 4 but isolated; only the tool-name join rejects it)
    objs = [user_text_msg("just reading a file with an example block")]
    objs += decoy_tool_msg("toolu_0010", "Read", ET_BLOCK_NO_DR)
    write_jsonl("10_block_in_read.jsonl", objs)

    # 11 — OS block WITH [Decision Records] -> 1, decision_records.present True
    write_jsonl("11_os_with_dr.jsonl", [
        spawn_msg("toolu_0011", "chief-architect"),
        result_msg("toolu_0011", OS_BLOCK_WITH_DR),
    ])

    # 12 — FX-5: TWO distinct blocks in ONE tool_result (one tool_use_id).
    #      Composite dedup key -> BOTH must persist (2 written lines).
    write_jsonl("12_two_blocks_one_result.jsonl", [
        spawn_msg("toolu_TWO12", "chief-architect"),
        result_msg_two_blocks("toolu_TWO12", OS_BLOCK_WITH_DR, SECOND_DISTINCT_BLOCK),
    ])

    # 13 — FX-1: sensitive-skill NUMBER-FIRST ROI phrasing -> roi.minutes 240.
    write_jsonl("13_sensitive_roi_number_first.jsonl", [
        spawn_msg("toolu_SENS13", "contracts-counsel", name="Contracts Counsel",
                  emoji="📜", prep="on"),
        result_msg("toolu_SENS13", SENSITIVE_ROI_NUMBER_FIRST_BLOCK),
    ])

    # 14 — A4: genuine spawn whose tool_result PROSE name-drops the header but
    #      has NO [section] line -> 0 receipts (header-line-only prose rejected).
    write_jsonl("14_prose_header_only.jsonl", [
        spawn_msg("toolu_PROSE14", "chief-architect"),
        result_msg("toolu_PROSE14", PROSE_HEADER_ONLY),
    ])

    # 15 — A5: a UTF-8 BOM prefixes line 1 of the transcript. utf-8-sig must
    #      consume it so line 1 (the spawn) is not dropped -> 1 receipt.
    write_jsonl_bom("15_bom_prefixed.jsonl", [
        spawn_msg("toolu_BOM15", "chief-architect"),
        result_msg("toolu_BOM15", OS_BLOCK_WITH_DR),
    ])

    # Supplementary frozen inputs for the explicit edge tests:
    write_text("zero_byte.jsonl", "")                       # zero-byte file
    write_text("text_mode.txt", "intro prose\n" + OS_BLOCK_SECOND + "\ntrailer")

    print("Wrote frozen fixtures to", FX)


if __name__ == "__main__":
    build()
