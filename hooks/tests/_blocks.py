"""Shared canonical Spawn Audit Block text snippets used to build frozen fixtures.

These are the *content* payloads. The fixture generator (build_fixtures.py) wraps
them in faithful Claude-Code jsonl envelopes. Keeping the block text here means a
single source of truth for the receipt content the parser must extract.
"""

# A clean v2 single-author OS block (deliverable task, with Decision Records).
OS_BLOCK_WITH_DR = """📋 Spawn Audit Block

[Pre-Execution Loads]
- SKILL.md: ✓ .claude/skills/chief-architect/SKILL.md
- Preload packs (3): architecture-team/PRINCIPLES.md, system-patterns, code-review
- Task-matched skills (2): risk-analysis, decision-record
- Conditional packs (0): none
- Mandatory invocations (0): none
- Fallbacks: none

[Decision Records — deliverable task]
- Read pre-analysis (constraints honored): DR-2026-007, DR-2026-009
- Sniffed during work: 2 candidate decisions surfaced; 1 promoted to draft, 1 dismissed
- Drafted this run (new DR files written): DR-2026-011 "Portable telemetry boundary" -> context/decisions/2026/DR-2026-011.md
- Updated this run (existing DRs status-changed): DR-2026-007 -> validated (evidence: build gate)
- Open assumptions tracked: A-014, A-015

[Post-Execution ROI]
- Time saved: ~3 hrs (baseline: decision-record x complex)
- Elapsed: 240s
- Tokens: 58k (~$0.5 cost)
- Value: ~$300 (3 hrs x $100/hr senior product professional rate)
"""

# A clean v2 ET block WITHOUT Decision Records (ET agents omit that section).
ET_BLOCK_NO_DR = """📋 Spawn Audit Block

[Pre-Execution Loads]
- SKILL.md: ✓ .claude/skills/qa-engineer/SKILL.md
- Preload packs (3): dev-team/PRINCIPLES.md, code-review, system-patterns
- Task-matched skills (1): feature-spec
- Conditional packs (0): none
- Mandatory invocations (0): none
- Fallbacks: none

[Post-Execution ROI]
- Time saved: ~2 hrs (baseline: feature-spec x standard)
- Elapsed: 120s
- Tokens: 44k (~$0.3 cost)
- Value: ~$200 (2 hrs x $100/hr senior product professional rate)
"""

# v1-legacy (the deleted "Pre-Execution Self-Check" format).
V1_LEGACY_BLOCK = """📋 Pre-Execution Self-Check
- Mode: standard
- SKILL.md: loaded
- Knowledge packs: 4 loaded
- Ready to proceed.
"""

# Joint-authoring block, two authors.
JOINT_BLOCK = """📋 Spawn Audit Block (Joint Authoring)

[Authors]
- 📣 Director of Product Marketing (director-product-marketing) — leads positioning
- ✍️ Copywriter (copywriter) — leads headline copy

[Pre-Execution Loads]
- @director-product-marketing SKILL.md: ✓ .claude/skills/director-product-marketing/SKILL.md
- @copywriter SKILL.md: ✓ .claude/skills/copywriter/SKILL.md
- Preload packs (combined, 2): gtm-strategy, copywriting
- Task-matched skills (1): positioning-statement
- Conditional packs (0): none
- Mandatory invocations (0): none
- Fallbacks: none

[Post-Execution ROI]
- Time saved: ~4 hrs (joint deliverable, sum of contributors)
- Elapsed: 300s
- Tokens: 70k (~$0.6 cost)
- Value: ~$400
- Split: @director-product-marketing 60%, @copywriter 40%
"""

# Truncated block: no [Post-Execution ROI] section (interrupted emission).
TRUNCATED_BLOCK = """📋 Spawn Audit Block

[Pre-Execution Loads]
- SKILL.md: ✓ .claude/skills/product-manager/SKILL.md
- Preload packs (2): pm-team/PRINCIPLES.md, system-patterns
- Task-matched skills (1): prd
- Conditional packs (0): none
- Mandatory invocations (0): none
- Fallbacks: none
"""

# --- Finalize-pass fixtures (FX-5 / FX-1 / A4 / A5) ---

# FX-5: a SECOND, DISTINCT block emitted in the SAME tool_result as the first.
# Both share one tool_use_id; with the composite dedup key both MUST persist.
# (Different agent + different ROI so it is unmistakably a distinct block.)
SECOND_DISTINCT_BLOCK = """📋 Spawn Audit Block

[Pre-Execution Loads]
- SKILL.md: ✓ .claude/skills/qa-engineer/SKILL.md
- Preload packs (2): dev-team/PRINCIPLES.md, code-review
- Task-matched skills (1): test-driven-development
- Conditional packs (0): none
- Mandatory invocations (0): none
- Fallbacks: none

[Post-Execution ROI]
- Time saved: ~5 hrs (baseline: test-driven-development x complex)
- Elapsed: 200s
- Tokens: 33k (~$0.2 cost)
- Value: ~$500
"""

# FX-1: a sensitive-skill ROI block using the NUMBER-FIRST canonical phrasing
# (roi-display.md worked example) — has NO "Time saved:" token. minutes -> 240.
SENSITIVE_ROI_NUMBER_FIRST_BLOCK = """📋 Spawn Audit Block

[Pre-Execution Loads]
- SKILL.md: ✓ .claude/skills/contracts-counsel/SKILL.md
- Preload packs (1): legal-team/PRINCIPLES.md
- Task-matched skills (0): none
- Conditional packs (0): none
- Mandatory invocations (0): none
- Fallbacks: none

[Post-Execution ROI]
- ~4 hrs saved on drafting and triage of structured contract extraction in 90s
- Elapsed: ~90s
- Tokens: 28k (~$0.2 cost)
- Value: ~$400
"""

# A4: a genuine-spawn tool_result whose PROSE merely name-drops the header but
# carries NO [section] line -> MUST yield 0 receipts (header-line-only prose).
PROSE_HEADER_ONLY = (
    "I already emitted the 📋 Spawn Audit Block earlier in this run, so I will "
    "not repeat it here. Proceeding with the deliverable.\n\nHere is the result."
)

# A non-deliverable OS block whose Decision Records section is the skipped one-liner.
OS_BLOCK_SECOND = """📋 Spawn Audit Block

[Pre-Execution Loads]
- SKILL.md: ✓ .claude/skills/vp-product/SKILL.md
- Preload packs (2): pm-team/PRINCIPLES.md, pricing-frameworks
- Task-matched skills (1): strategic-bet
- Conditional packs (0): none
- Mandatory invocations (0): none
- Fallbacks: none

[Decision Records — skipped, non-deliverable task]

[Post-Execution ROI]
- Time saved: ~1 hrs (baseline: lookup x simple)
- Elapsed: 60s
- Tokens: 20k (~$0.1 cost)
- Value: ~$100
"""
