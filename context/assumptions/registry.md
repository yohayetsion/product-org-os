# Assumption Registry

*Last updated: 2026-03-08*

## All Tracked Assumptions

| ID | Assumption | Source | Product | Confidence | Validation Method | Status | Outcome |
|----|------------|--------|---------|------------|-------------------|--------|---------|
| A-001 | CISOs will pay for judgment over enforcement | DR-2026-005, DOC-2026-027 | AXIA | Medium | Pilot conversion, win/loss analysis | Pending | — |
| A-002 | $3.2B IRM market sustains a 4-person team | DOC-2026-027 | AXIA | Medium | Revenue per customer x customer count | Pending | — |
| A-003 | "Understanding WHY" is defensible vs legacy DLP | DOC-2026-027 | AXIA | Medium | Competitive displacement data | Pending | — |
| A-004 | Platform expansion to HRI viable post-PMF | DOC-2026-027 | AXIA | Low | Customer demand for adjacent use cases | Pending | — |
| A-005 | API-based deployment wins over endpoint agents | DOC-2026-027 | AXIA | Medium | POC completion rates vs competition | Pending | — |
| A-006 | LLM inference economics work at scale | DOC-2026-027 | AXIA | Medium | Cost per event analysis at 10K+ events/day | Pending | — |
| A-007 | Users will connect Legionis as MCP server in external tools | SB-2026-005 | Legionis | Medium | Track MCP key generation + external invocations | Pending | — |
| A-008 | Context accessed from external tools increases platform retention | SB-2026-005 | Legionis | Medium | Compare retention: MCP vs web-only users | Pending | — |
| A-009 | Integration brokering reduces setup friction for new user adoption | SB-2026-005 | Legionis | Medium | Connection rate for MCP-first vs web-first | Pending | — |
| A-010 | Users prefer centralized integration management over per-tool config | SB-2026-005 | Legionis | Medium | Survey + usage data | Pending | — |
| A-011 | MCP protocol adoption continues growing in major AI/dev tools | SB-2026-005 | Legionis | High | Monitor ecosystem quarterly | Pending | — |

## By Status

### Pending Validation

| ID | Assumption | Product | Source | Validation Method |
|----|------------|---------|--------|-------------------|
| A-001 | CISOs will pay for judgment over enforcement | AXIA | DR-2026-005, DOC-2026-027 | Pilot conversion, win/loss analysis |
| A-002 | $3.2B IRM market sustains a 4-person team | AXIA | DOC-2026-027 | Revenue per customer x customer count |
| A-003 | "Understanding WHY" is defensible vs legacy DLP | AXIA | DOC-2026-027 | Competitive displacement data |
| A-004 | Platform expansion to HRI viable post-PMF | AXIA | DOC-2026-027 | Customer demand for adjacent use cases |
| A-005 | API-based deployment wins over endpoint agents | AXIA | DOC-2026-027 | POC completion rates vs competition |
| A-006 | LLM inference economics work at scale | AXIA | DOC-2026-027 | Cost per event analysis at 10K+ events/day |
| A-007 | Users will connect Legionis as MCP server in external tools | Legionis | SB-2026-005 | Track MCP key generation + external invocations |
| A-008 | Context accessed from external tools increases platform retention | Legionis | SB-2026-005 | Compare retention: MCP vs web-only users |
| A-009 | Integration brokering reduces setup friction for new user adoption | Legionis | SB-2026-005 | Connection rate for MCP-first vs web-first |
| A-010 | Users prefer centralized integration management over per-tool config | Legionis | SB-2026-005 | Survey + usage data |
| A-011 | MCP protocol adoption continues growing in major AI/dev tools | Legionis | SB-2026-005 | Monitor ecosystem quarterly |

### Validated
*No assumptions validated yet*

| ID | Assumption | Validated Date | Outcome |
|----|------------|----------------|---------|
| — | — | — | — |

### Invalidated
*No assumptions invalidated yet*

| ID | Assumption | Invalidated Date | Actual Finding | Affected Decisions |
|----|------------|------------------|----------------|-------------------|
| — | — | — | — | — |

---

## By Product

### AXIA
A-001, A-002, A-003, A-004, A-005, A-006

### Legionis
A-007, A-008, A-009, A-010, A-011

---

## How Assumptions Flow

1. **Created**: When a `/strategic-bet` or `/decision-record` includes explicit assumptions
2. **Extracted**: `/context-save` pulls assumptions into this registry
3. **Tracked**: Each assumption has a validation method and timeline
4. **Validated**: `/outcome-review` updates status based on real data
5. **Surfaced**: Invalidated assumptions trigger re-decision alerts

## Assumption ID Format

`A-[NNN]` where NNN is a sequential number across all assumptions.
