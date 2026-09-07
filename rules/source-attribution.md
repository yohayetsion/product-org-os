# Source Attribution (MANDATORY)

When a V2V OS / Extension Teams knowledge pack or skill absorbs framework, structure, or content from a named external source, the source MUST be attributed in the pack/skill itself.

**Owner**: 🏗️ Chief Architect (rule maintenance) + ✒️ Vision to Value editorial (book/manuscript references)
**Status**: Active as of 2026-05-18 (Q2-0.5 Wave 1B)

---

> *Relocated 2026-08-15 (DR-2026-262): why-this-rule-exists rationale (intellectual honesty / CC-BY 4.0 inheritance / absorb-and-add-value legibility) — full text in the companion source-attribution.md (sibling of this rules directory; imposes nothing, relaxes nothing).*

---

## Required Format

Every knowledge pack that actually adapts protected source expression carries this block near the top of the file (in the YAML frontmatter as a comment, or as the first prose paragraph after the title):

```
**Adapted from**: [source name + URL or citation]
**Source licence**: [CC-BY 4.0 / Apache-2.0 / MIT / no-license-but-publicly-cited / per-source-terms / etc.]
**V2V refinements**: [bulleted list of what V2V added, changed, or refined relative to the source]
```

Where a pack is original V2V expression that only describes a public method, standard, fact, or software pattern, use this block instead:

```
**Sources consulted**: [source name + URL or citation]
**Source licence**: [the source's own licence or published terms]
**Our determination**: describes-public-method
**V2V refinements**: [what V2V's original treatment contributes]
```

`Source licence` reports a fact about the named source. It does not state which licence governs the V2V file. Do not use the legacy field name `License:` for source credit, and do not add a file-level proprietary stamp to this block.

No paraphrasing of the field names and no "light" versions. If the source has multiple components, list each source separately. Use `Adapted from` only when protected expression was actually adapted; otherwise use `Sources consulted` and record the determination.

---

## What Requires Attribution

| Source Type | Examples |
|---|---|
| Public frameworks | MITRE ATLAS, OWASP LLM Top 10, NIST CAISI, NIST AI RMF, CSA AICM / Agentic Trust Framework, ISO 42001, EU AI Act, NYC AEDT, Texas TRAIGA, PMBOK 8th Edition + Appendix X3, BPMN 2.0 |
| OSS repos and codebases | dbt MetricFlow, LF SQLMesh, GrowthBook, DeepEval, Braintrust, Promptfoo, CopilotKit AG-UI, shadcn/ui, Anthropic MCP spec, Google A2A spec, Google A2UI |
| Anthropic vertical plugins | Legal, Financial Services, HR, Customer Success, Operations, Product Management, Investment Banking, SMB (shipped Feb-May 2026) |
| Industry analyst frameworks | TSIA Value Score, Gartner / Forrester maturity models, Camunda 2026 Process Orchestration report |
| Academic papers | Cite paper + venue + DOI when available |
| Named methodologies | April Dunford positioning, Cagan / SVPG product, Teresa Torres opportunity-solution trees, Wickman EOS, Wardley Mapping, Helmer 7 Powers |

---

## What Does NOT Require Attribution

- **Generic concepts in common use** — RICE, MoSCoW, RACI, OKRs, SWOT, kanban. These are too widely used to need attribution unless we're explicitly invoking a specific commercial framework variant.
- **V2V's own derivative work that goes beyond a recognizable source** — once a refinement is substantively V2V (e.g., V2V's six-phase decision/portfolio/value flow, the sensitive-skill scaffolding pattern), no source attribution is needed for the V2V layer itself. Cite when V2V builds ON something; don't cite when V2V invented something.
- **Common terminology** — "stakeholder map," "value chain," "user story," "definition of done."

If a concept is in three or more textbooks under the same name with no proprietary owner, it's common. If one source coined it and others reuse it, attribute the coiner.

---

## Where Attribution Goes

1. **Top of the knowledge pack file** — first prose section after the title, OR as a YAML frontmatter block if the pack uses frontmatter.
2. **In the skill SKILL.md frontmatter** as an optional `metadata.sources` field — list of source citation strings. Non-blocking if absent on existing skills, but new sensitive packs added in Q2 2026 onward should populate this.
3. **In V2V book / manuscript references** — every chapter that draws on absorbed material lists sources in the chapter end-notes or the consolidated bibliography. CC-BY 4.0 publication makes this a license condition for sources that require it.

---

## Edge Case — Anthropic Vertical Plugins

Per the maintainer's 2026-05-18 stance (D5): **absorb plugin structure + attribute in technical docs; no marketing surface**.

- **Where we adapt structure from an Anthropic plugin into a V2V knowledge pack**: attribute in the pack body (the technical doc) using the required format above.
- **Where V2V markets itself externally**: do NOT name Anthropic plugins. The V2V positioning is its own narrative; we don't lean on plugin co-mention for marketing leverage.
- **Q2 2026 refresh — named Anthropic-adapted packs**: `hr-ai-governance.md` (HR Plugin), `ai-act-readiness.md` (claude-for-legal), `value-score-design.md` (CS Plugin), `mcp-architecture.md` (MCP spec), `generative-ui.md` (MCP Apps), and others listed in the 2026 Q2 refresh runbook §3.0.C. Each carries its attribution block.

---

## Example Attribution Block

For `hr-ai-governance.md` (HR knowledge pack absorbing Anthropic HR Plugin structure):

```
**Adapted from**: Anthropic HR Plugin (released 2026-02-24, claude.com/plugins/human-resources)
**Source licence**: per Anthropic plugin terms (no formal OSS license; publicly documented patterns)
**V2V refinements**:
- Added per-pack `## Findings` + `## Reviewer Checklist` + `## Cannot Assess Without` scaffolding per `sensitive-skill-guardrails.md`
- Added FCRA structural treatment per `sensitive-skill-guardrails.md` §1.4 (Eightfold AI class action 2026-01-20)
- Added EU AI Act high-risk HR coverage (Article 6 + Annex III)
- Added NYC AEDT + Texas TRAIGA jurisdiction-specific obligations
- Added ISO 42001 HR module reference
```

For a pack absorbing multiple sources (e.g., `agentic-security.md`):

```
**Adapted from**:
  - MITRE ATLAS v5.4 (atlas.mitre.org)
  - OWASP LLM Top 10 v2.0 (genai.owasp.org/llm-top-10/)
  - NIST CAISI (nist.gov/ai-safety-institute)
**Source licence**: MITRE ATLAS (CC-BY 4.0), OWASP (CC-BY-SA 4.0), NIST (public domain)
**V2V refinements**:
- Cross-mapped ATLAS tactics to V2V architecture review gates
- Integrated with `/ai-control-audit` skill invocation
- Added agentic-specific failure modes from CSA Agentic Trust Framework
```

For a pack written as original V2V prose that describes a public method:

```
**Sources consulted**: Simon Wardley, Wardley Mapping (published work under CC BY-SA 4.0)
**Source licence**: CC BY-SA 4.0 applies to Simon Wardley's published work
**Our determination**: describes-public-method
**V2V refinements**: Original V2V decision workflow, application guidance, and output structure
```

---

## Operating Principle

> "Absorption with attribution is intellectual honesty. The V2V program is published under CC-BY 4.0 to inherit and contribute to the same commons we draw from."
