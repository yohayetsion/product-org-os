---
pack: agent-identity
owner: it-security-policy
co_owner: chief-architect
consumers: [it-security-policy, chief-architect, security-architect, enterprise-systems, cio]
sensitive: false
token_budget_variance_rationale: "D14 cases (a) joint-authoring 🛡️+🏗️ and (b) multi-consumer (4 primary + 1 secondary); the four-source absorption plus the load-bearing §Agent-to-Agent Authentication section that Q2-5.3 will cite verbatim requires headroom above the 2000-token preload norm. Pack is reference material, not preload."
v2v_wave: q2-3.1
related_packs_status: TBC-after-wave-2-stitching-pass
---

# Agent Identity (V2V Knowledge Pack)

**Adapted from**:
  - Microsoft Entra Agent ID (publicly documented pattern, learn.microsoft.com/azure/active-directory/develop/)
  - Cisco Agentic Zero Trust (publicly documented pattern, cisco.com)
  - Google Agent Identity in Gemini Enterprise (publicly documented pattern, cloud.google.com/agent-identity)
  - CSA Agentic Trust Framework Feb 2026 (CC-BY 4.0, cloudsecurityalliance.org/research/agentic-trust-framework)

**Source licence**: per-source-terms (commercial sources, publicly documented patterns absorbed under fair-use technical-reference norms) + CC-BY 4.0 (CSA Agentic Trust Framework)

**V2V refinements**:
- Mapped commercial-source system-identity patterns to V2V's existing **Identity Registry** semantics (per `.claude/rules/agent-spawn-protocol.md` §1) — distinguishing **in-conversation display identity** (the registry's emoji + display-name surface, runtime-only, no system-level trust grant) from **system identity** (the commercial-source patterns: a credentialed principal that authenticates to APIs, holds capability tokens, and produces audit trail entries). Conflation of the two is the most common failure mode in product-org adoption, and V2V's Anti-Patterns section names it.
- Cross-mapped the **CSA Agentic Trust Framework's 7 MCP risk classes** to product-organization governance touchpoints — identifying which the identity layer mitigates directly (1, 2, 3, 6) and which require layered controls handled by Q2-3.2 mcp-governance.md (4, 5, 7).
- Added a product-org-specific Anti-Patterns section absent from the enterprise-IT source material (over-broad capability tokens, silent inheritance from spawning agent, missing revocation on agent retirement, identity drift between conversation-display and system-credential surfaces).
- Added structural cross-reference placeholders for Q2-3.2 (mcp-governance.md), Q2-5.3 (agentic-security.md), and Q2-5.1 (mcp-architecture.md) per M40 Wave 2 stitching pass.
- Drew an explicit boundary contract (per M38) declaring what this pack does NOT cover — transport mechanics, server governance, threat models — so consuming packs can rely on scope discipline.

---

## What Agent Identity Is

Three identity types coexist in modern enterprise systems:

| Type | Subject | Lifecycle | Trust Anchor |
|---|---|---|---|
| **User identity** | A human | Long-lived (employment) | HR system + IdP (Okta, Entra, Workspace) |
| **Workload identity** | A service, function, or pod | Tied to deployment | Service principal, IAM role, Workload Identity Federation |
| **Agent identity** | An autonomous or semi-autonomous AI agent | Variable — minutes to months | Agent-identity service (Entra Agent ID, Cisco Agentic ZT, Google Agent Identity) |

Agent identity emerged as a distinct concern in 2026 because agents do not fit either of the existing categories. A workload identity assumes deterministic behaviour bound to deployment topology — an agent's behaviour is non-deterministic and its capability surface changes per-turn. A user identity assumes a single human accountable principal — an agent has no human at the wheel for the in-flight tool call, even when a human supervises the outcome.

The 2026 zero-trust posture treats agents as a fourth identity class with its own provisioning, runtime authentication, capability scoping, and revocation lifecycle. This pack codifies the patterns that converged across Microsoft, Cisco, and Google between Q4 2025 and Q2 2026, anchored by the CSA Agentic Trust Framework's open taxonomy.

---

## The 2026 Landscape

| Vendor | Product | Distinctive Angle | Where It Converges |
|---|---|---|---|
| **Microsoft** | Entra Agent ID | Agents as first-class principals in Entra ID; conditional-access policies apply directly; capability tokens issued as scoped OAuth artifacts | Lifecycle, revocation, audit |
| **Cisco** | Agentic Zero Trust | Continuous verification at the network layer; agent-fleet observability; policy decision points (PDPs) evaluate every agent action against current posture | Continuous-verification model |
| **Google** | Agent Identity in Gemini Enterprise | Tight coupling to Workload Identity Federation; agents inherit GCP IAM primitives with agent-specific scopes | Capability tokens, federation |
| **CSA** | Agentic Trust Framework Feb 2026 (open) | Vendor-neutral taxonomy: 7 MCP risk classes, control categories, maturity model | The shared vocabulary all three commercial frameworks now reference |

**Convergence**: all three commercial frameworks issue **scoped, time-bounded capability tokens** rather than static credentials; all three support **agent-to-agent delegation** with capability narrowing on each hop; all three produce **per-action audit trail** linking agent identity, capability token, and tool call.

**Divergence**: identity-provider integration (Entra-native vs Workload Identity Federation vs Cisco's network-layer overlay) is genuinely different. Product orgs should NOT assume cross-cloud portability of agent identity without an explicit federation design.

---

## Core Patterns

### Agent-to-Agent Authentication

**[Owner: 🏗️]** *This section is load-bearing for Q2-5.3 agentic-security.md per M34. The threat-model section in agentic-security.md cites the patterns named here.*

When an agent spawns or delegates to another agent, the receiving agent must authenticate the caller and verify the caller's authority to delegate the specific capability requested. Four patterns are in use in 2026:

1. **Capability-token forwarding with narrowing** — the spawning agent passes a token to the sub-agent that is a strict subset of its own. The sub-agent cannot escalate. This is the default pattern in Microsoft Entra Agent ID and Google Agent Identity.
2. **Mutual TLS with agent certificates** — each agent holds a short-lived certificate identifying its agent-identity record; the receiving agent validates the certificate against the agent-identity service before accepting the call. Cisco Agentic Zero Trust emphasises this at the network layer.
3. **OAuth-style delegation flow** — the spawning agent requests a delegation grant from the identity service on behalf of the sub-agent, the identity service evaluates policy, and the resulting token names both principals (`act_as` claim). Microsoft Entra Agent ID supports this for cross-tenant delegation.
4. **Workload Identity Federation bridging** — when an agent crosses a cloud boundary, the receiving environment exchanges the source-cloud token for a local token via federation. Google Agent Identity is the reference implementation; AWS and Azure equivalents exist.

In all four patterns the **principle of least capability** applies: the sub-agent receives the narrowest token that allows it to complete its task, not the broadest that the spawning agent could grant.

### Capability Tokens & Scoped Delegation

**[Owner: 🛡️]**

A capability token is a time-bounded, narrowly-scoped credential that names: (a) the issuing agent identity, (b) the holding agent identity, (c) the specific capabilities granted (which tools, which data scopes, which actions), (d) the expiration timestamp, (e) optional constraints (rate limits, geographic restrictions, per-action approval requirements).

V2V product-org guidance:

- **Default expiration is short** — minutes to hours, not days. Long-lived agent tokens recreate the static-credential anti-pattern that agent identity was invented to escape.
- **Capability narrowing is non-optional on delegation** — if a sub-agent is spawned to read one document, its token grants read access to that document, not to the document corpus.
- **Per-action approval gates** for high-impact capabilities (financial transactions, data exfiltration-capable tools, customer-facing communications) are encoded in the capability token itself, not bolted on at the application layer.
- **Revocation must be immediate and propagated** — when an agent identity is deactivated, all outstanding capability tokens it holds or has issued become invalid within seconds, not at next refresh.

### Agent Lifecycle Management

**[Owner: 🛡️]**

| Phase | Required Controls |
|---|---|
| **Provisioning** | Agent identity created via identity service with named human owner, declared purpose, declared capability scope, declared retirement criteria |
| **Runtime authentication** | Every tool call presents a valid capability token; token validation happens at the policy decision point, not at the tool |
| **Capability adjustment** | Capability scope changes flow through the identity service with audit; agents cannot self-elevate |
| **Deactivation** | Triggered by retirement criteria, owner request, or security event; immediate token revocation; preservation of audit trail |
| **Log retention** | Per-action audit retained per the org's data-retention schedule, minimum 1 year for compliance-adjacent agents, longer if regulated (see ai-act-readiness.md for EU AI Act high-risk-system retention requirements) |

### CSA Agentic Trust Framework Integration

**[Owner: 🛡️ + 🏗️]**

The CSA framework names 7 MCP risk classes. Mapping to agent-identity controls:

| # | CSA Risk Class | Mitigated By This Pack | Defer To |
|---|---|---|---|
| 1 | Data exfiltration | Capability tokens scoped to specific data resources; mTLS prevents lateral data flow | — |
| 2 | Unauthorized actions | Per-action approval gates encoded in capability tokens; agent-to-agent auth prevents spoofing | — |
| 3 | Overprivileged access | Capability narrowing on delegation; least-capability default | — |
| 4 | Supply chain (compromised MCP servers) | — | **Q2-3.2 mcp-governance.md** (server allow-listing, integrity verification) |
| 5 | Missing audit trails | Identity-bound audit per action | **Q2-3.2 mcp-governance.md** (audit-pipeline architecture, retention) |
| 6 | Privilege escalation | Cryptographic narrowing prevents self-elevation; revocation propagates | — |
| 7 | Shadow AI sprawl | — | **Q2-3.2 mcp-governance.md** (discovery, inventory, allow-list enforcement) |

Risk classes 1, 2, 3, 6 are mitigated by correct agent-identity implementation. Risk classes 4, 5, 7 require governance controls layered on top of identity — see Q2-3.2.

---

## Implementation Guidance

**[Owner: 🏗️]**

Product orgs adopting agent identity in 2026 face three architecture decisions:

1. **Cloud-native vs cross-cloud** — if the org is single-cloud, adopt the cloud's native agent-identity service. If multi-cloud, design federation explicitly. Do not assume portability.
2. **Identity service vs application-layer identity** — agent identity belongs in the identity service, not in the application. Application-layer "agent IDs" maintained by the product team are an anti-pattern: they do not integrate with conditional-access, do not produce identity-bound audit trail, and do not revoke.
3. **Conversation-display identity vs system identity** — V2V's Identity Registry (per `.claude/rules/agent-spawn-protocol.md` §1) governs in-conversation display identity (emoji, display name, RACI surface) and is runtime-only with no system-level trust grant. The system identity governed by this pack is a separate concern. The two MUST map cleanly: a single agent in the Identity Registry corresponds to a single system identity in the identity service, with a documented binding. They are not interchangeable.

Practical sequencing for product orgs:

- Start by inventorying every agent already running in the org (almost always more than expected — shadow AI is real).
- Onboard each agent into the identity service with a named human owner before granting any new capability.
- Treat the first 90 days as a discovery-and-cleanup phase, not a control-tightening phase. Tightening prematurely creates incident-by-policy.
- Wire revocation testing into the agent retirement workflow before scaling.

---

## Anti-Patterns / Common Failures

**[Owner: 🛡️]**

| Anti-Pattern | Why It Fails | What V2V Does Instead |
|---|---|---|
| **Conflating Identity Registry with system identity** | The V2V Identity Registry is in-conversation display (emoji + display name); commercial-source agent identity is a credentialed principal. Treating them as one means either the display surface leaks credential semantics or the credential surface lacks proper governance. | Maintain both surfaces with a documented binding; Identity Registry stays runtime-only, system identity stays in the identity service. |
| **Silent identity inheritance** | A sub-agent inherits the spawning agent's full token by default. The sub-agent now has more capability than its task requires; if compromised, blast radius is the parent's, not its own. | Capability narrowing is non-optional on every delegation hop. |
| **Over-broad capability tokens** | Token grants `read:*` instead of `read:document:12345`. Convenient at issue time, catastrophic on compromise. | Default to narrowest scope; widen only with explicit justification recorded against the agent identity. |
| **Missing revocation on agent retirement** | The agent is removed from the runtime but its capability tokens remain valid until expiration. A still-valid token in a deactivated agent is a credential in the wild. | Deactivation triggers immediate token revocation; retirement workflow includes revocation verification. |
| **Application-layer "agent IDs"** | The product team maintains a database of agent IDs separate from the identity service. No integration with conditional-access, no identity-bound audit, no revocation propagation. | Agent identity lives in the identity service. Application references it; does not duplicate it. |
| **Long-lived agent tokens** | Token expires in 30 days. The token IS the credential; a 30-day token is a 30-day credential. | Minutes-to-hours expiration; refresh through the identity service. |
| **No named human owner** | The agent runs autonomously with no accountable human. When something goes wrong, there is no one to escalate to and no one with authority to deactivate. | Every agent identity has a named human owner recorded at provisioning. |

---

## V2V Cross-References

**Sibling Q2-3 packs (governance + regulatory layer over identity)**:
- **Q2-3.2 `mcp-governance.md`** — governance controls layered on agent identity (server allow-listing, audit pipeline, shadow-AI discovery, supply-chain integrity). Handles CSA risk classes 4, 5, 7 that this pack defers per §CSA Agentic Trust Framework Integration table.
- **Q2-3.3 `csa-ai-controls-matrix.md`** — AICM domain 9 (AI Identity & Access Management) is the canonical control library this pack's lifecycle and capability-token patterns map into; AICM domain 14 (AI Supply Chain) applies when agent identities cross third-party provenance boundaries.
- **Q2-3.4 `eu-ai-act-annex-iv.md`** — Annex IV §3 (monitoring, functioning, control) evidence requirements consume agent-identity audit trail per §Agent Lifecycle Management; high-risk agent systems must produce identity-bound audit per Article 11.
- **Q2-3.5 `ai-bom.md`** — when AI BOM §2.1 (Models) and §2.6 (Third-Party Components) inventories an agent that authenticates via this pack's patterns, identity binding is a required BOM disclosure field.

**Sibling Q2-5 packs (architecture + threat surfaces over identity)**:
- **Q2-5.1 `mcp-architecture.md`** — MCP auth handshake mechanics. §4.2 of that pack explicitly defers identity semantics to this pack's §Agent-to-Agent Authentication patterns; capability tokens travel over MCP transport per Pattern 1 above.
- **Q2-5.2 `a2a-architecture.md`** — A2A v1.2 mutual agent identity at the agent-to-agent collaboration layer. A2A's OAuth2 + mutual-identity pattern is the agent-to-agent peer instantiation of Pattern 3 (`act_as` delegation) extended for symmetric peer relationships.
- **Q2-5.3 `agentic-security.md`** — **load-bearing per M34**: cites this pack's §Agent-to-Agent Authentication patterns by name and verbatim. The four patterns (capability-token forwarding with narrowing / mTLS with agent certificates / OAuth-style delegation with `act_as` / Workload Identity Federation) anchor every defensive control in the agentic-security threat model.
- **Q2-5.4 `subagent-driven-development.md`** — sub-agent driven dev's identity-and-access discussion (org-wide adoption) consumes this pack's Identity Registry-vs-system-identity distinction; sub-agent-authored code that takes autonomous action needs the agent-identity binding established at this pack's lifecycle layer.

**Existing packs**:
- `compliance-frameworks.md` — SOC 2 + ISO 27001 + ISO 42001 identity-and-access control mapping (this pack contributes agent-specific application of those controls).
- `security-frameworks.md` — NIST CSF 2.0 IDENTIFY + PROTECT functions that this pack's identity controls participate in.
- `it-governance.md` — `cio`-owned IT-portfolio governance that agent-identity service operations plug into.

**Rule files**:
- `.claude/rules/agent-spawn-protocol.md` §1 — the V2V **Identity Registry** (in-conversation display identity, runtime-only). Different surface from this pack's system identity per §Anti-Patterns row 1.

---

## Sensitive-skill applicability

This pack is **NOT sensitive** per `.claude/rules/sensitive-skill-guardrails.md` §2. It is technical reference material: descriptions of identity patterns and their implementation guidance. It does not produce legal, HR, compliance, or regulatory output. It does not advise on decisions with material liability consequences.

Cross-references from this pack to sensitive packs (e.g., Q2-3.3 it-compliance, Q2-3.4 hr-ai-governance, Q2-3.5 procurement-controls when Wave 2 lands) are mechanical pointers, not load-bearing substance. Consuming sensitive packs must still satisfy their own scaffolding requirements (Disclaimer + Findings + Reviewer Checklist + Cannot Assess Without) regardless of what this pack says.

---

## Operating Principle

> *Agent identity is not a feature of any one cloud. It is the precondition for any zero-trust posture in an agentic-AI organization — and the surface where the V2V Identity Registry meets the wider enterprise control plane.*
