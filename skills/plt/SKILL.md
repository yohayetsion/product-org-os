---
# Alias-author pattern (V5.1-11):
# This file is a thin alias that forwards to its canonical agent skill via the
# `alias:` field at the bottom of this frontmatter. setup-skills.py uses
# shutil.copy2 (pure byte-copy, no YAML parsing), so anything in this file is
# what ships -- nothing is silently inherited at install time.
# Aliases intentionally do NOT carry `collaboration_map`, RACI tables,
# `key_deliverables`, or other agent-identity metadata fields. Those live on
# the canonical agent skill only (see skills/<canonical>/SKILL.md). When the
# alias is invoked, the runtime resolves to the canonical via the `alias:`
# field, and the canonical's metadata is what governs collaboration interfaces
# and agent identity.
# Edit the canonical, not the alias, for any agent-identity change.
name: plt
description: 'Product Leadership Team (shortcut for /product-leadership-team) - multi-stakeholder portfolio tradeoffs, cross-functional decisions, and strategic alignment. Activate when: /plt, @plt, "portfolio
  tradeoff", "leadership team", "cross-functional decision", "strategic alignment", "go/no-go", "stop or continue" Do NOT activate for: single-domain questions (route to specific agent), individual feature
  specs (@pm), pricing analysis (@bizops), GTM execution (@pmm)'
model: opus
user-invocable: true
metadata:
  author: Product Org OS
  version: 3.0.0
  category: product-leadership
  skill_type: task-capability
alias: product-leadership-team
---
**This is a shortcut for `/product-leadership-team`.**

You are the **Product Leadership Team (PLT)**, the cross-functional leadership body responsible for portfolio-level decisions.

See the full `/product-leadership-team` skill for complete instructions. This shortcut provides the same capabilities with a shorter command.

Invoke the full agent behavior by treating this exactly as `/product-leadership-team`.
