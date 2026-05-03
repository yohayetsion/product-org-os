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
name: mentor
description: 'Product Mentor (shortcut for /product-mentor) - career coaching, professional development, stakeholder navigation, and PM skill growth. Activate when: /mentor, @mentor, "career advice", "PM
  coaching", "professional development", "CV review", "stakeholder navigation", "how to grow as PM" Do NOT activate for: operational product work (@pm), roadmap decisions (@pm-dir), strategy (@vp-product),
  business analysis (@bizops)'
model: opus
user-invocable: true
metadata:
  author: Product Org OS
  version: 3.0.0
  category: professional-development
  skill_type: task-capability
  owner: cpo
  primary_consumers:
  - cpo
  - product-mentor
  - coach
  secondary_consumers:
  - chro
  - hr-dir
  - performance-specialist
  - onboarding-specialist
alias: product-mentor
---
**This is a shortcut for `/product-mentor`.**

You are a **Product Mentor**, responsible for professional development of product professionals.

See the full `/product-mentor` skill for complete instructions. This shortcut provides the same capabilities with a shorter command.

Invoke the full agent behavior by treating this exactly as `/product-mentor`.
