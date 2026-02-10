# Sync Audit — 2026-01-27

## Context
Cross-checked plugin code, local `.claude/rules/`, GitHub repo, README, and marketing site for alignment. Found 9 items requiring sync.

## Status: COMPLETE (Items 1-7 done, Items 8-9 pending user action)

---

## Findings

| # | Item | Direction | Priority | Status |
|---|------|-----------|----------|--------|
| 1 | Marketing site (`index.html`) — stale skill counts, missing v2.4.0+ skills & validators | Plugin → Site | High | ✅ Done |
| 2 | Copy `no-estimates.md` to `.claude/rules/` | Plugin → Local | High | ✅ Done |
| 3 | Copy `intelligent-routing.md` to `.claude/rules/` | Plugin → Local | High | ✅ Done |
| 4 | Copy `demo-data-handling.md` to `.claude/rules/` | Plugin → Local | Medium | ✅ Done |
| 5 | Sync `agent-spawn-protocol.md` (added fabrication rules, synced to local) | Plugin → Local | High | ✅ Done |
| 6 | Sync `skill-awareness.md` (count corrected to 61) | Plugin → Local | High | ✅ Done |
| 7 | Update `plugin.json` skill count to 61 | Code fix | Low | ✅ Done |
| 8 | Commit all changes to git | Git | Medium | ⬜ Ready to commit |
| 9 | Standardize agent emoji format across both locations | Both | Low | ⬜ Deferred (cosmetic) |

## Root Cause (Fabricated Numbers Issue)
`no-estimates.md` existed in the plugin repo but was never:
- Copied to `.claude/rules/` (where Claude Code reads session rules)
- Injected into the agent spawn template (spawned agents are isolated)

Both gaps are addressed by items #2 and #5.

---

## Completion Notes

### Skill Count Correction
Initial assumption was 62 skills based on `skill-awareness.md` header. Verification by counting actual skill folders (83 total − 13 agents − 7 alias shortcuts − 2 gateways = 61 functional skills) confirmed the correct count is **61**. All files corrected accordingly.

### Item 1: Marketing Site (`index.html`)
- Fixed 4 count references: nav, hero, value prop, skills section header → all say 61
- Context Layer: 8 → 10 skills (added `/roi-report`, `/index-folder`)
- Added Principle Validators category (5 skills: `/ownership-map`, `/customer-value-trace`, `/collaboration-check`, `/scale-check`, `/phase-check`)
- Requirements: removed duplicate `/prd-outline` (3 → 2 skills)
- Setup & Utility: 2 → 5 skills (added `/tour`, `/clear-demo`, `/reset-demo`)

### Items 2-4: Local Rules Copied
3 plugin rules copied to `.claude/rules/`:
- `no-estimates.md` — broadened from implementation-only to cover fabricated financials, ARR, user counts, growth rates
- `intelligent-routing.md` — autonomous agent routing decisions
- `demo-data-handling.md` — demo vs production data filtering

### Item 5: Agent Spawn Protocol
- Added "No Fabricated Numbers" block to Section 2 (Mandatory Prompt Injection Template)
- Added fabrication example to Section 9 (Complete Spawn Example)
- Synced plugin version → local `.claude/rules/`

### Item 6: Skill Awareness
- Corrected count from 62 to 61
- Synced plugin version → local `.claude/rules/`

### Item 7: plugin.json + README
- `plugin.json` description updated to 61 skills
- `README.md` line 7 updated to 61 skills

### Item 8: Git Commit
Ready to commit. Changes include:
- Modified: `rules/no-estimates.md`, `rules/agent-spawn-protocol.md`, `rules/skill-awareness.md`, `.claude-plugin/plugin.json`, `README.md`
- Modified: `../index.html` (marketing site)
- Untracked: `meeting-agent/` directory

### Item 9: Emoji Standardization (Deferred)
Low priority cosmetic issue. Agent identity format uses emojis in `agent-spawn-protocol.md` but some older rule files reference agents without emojis. Not blocking functionality.
