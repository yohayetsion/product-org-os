---
pack: a2a-architecture
consumers:
- ai-architect
- security-architect
---
# A2A Architecture (V2V Knowledge Pack)

**Adapted from**:
  - Google A2A Protocol v1.2 (Apache-2.0, donated to Linux Foundation March 2026)
  - NIST CAISI AI Agent Standards Initiative (public, Feb 2026)
**Source licence**: Apache-2.0 (A2A) + public (NIST CAISI)
**V2V refinements**:
- Translated A2A v1.2 spec to product-organization integration guidance (not a re-statement of the wire spec)
- Cross-mapped A2A primitives to V2V Phase 4 (Execution) decision interfaces
- Held the MCP-vs-A2A boundary explicitly (sibling protocols, different roles, common confusion in 2026 adoption)
- Added structural placeholder for cross-refs to Q2-5.1 `mcp-architecture.md` and Q2-5.3 `agentic-security.md` per M40 Wave-2 stitching pass

---

## What A2A Is (and what it isn't)

A2A (Agent-to-Agent) is a **peer-to-peer collaboration protocol for autonomous agents**. It standardizes how one agent delegates a task to another, exchanges structured messages mid-task, returns artifacts, and surfaces status. Agents are independent processes with their own identity, memory, and tool access — A2A is the wire format and lifecycle that lets them work together without a shared runtime.

A2A is **not** a tool-call protocol — that role belongs to MCP. It is **not** a model-serving protocol (Inference API, vLLM, TGI handle that layer). It is **not** an orchestration framework — A2A is the protocol; orchestration patterns (star/mesh/hybrid, below) sit on top of it. The boundary matters because in 2026 a recurring adoption failure is teams reaching for A2A when MCP would be simpler: if one side is a tool or data source, use MCP; if both sides are agents with autonomous behavior, use A2A.

## A2A vs MCP — Sibling Protocols, Different Roles

| Aspect | MCP (Q2-5.1) | A2A (this pack) |
|---|---|---|
| Direction | Client → tool/data server (asymmetric) | Agent ↔ Agent (bidirectional, symmetric) |
| Primitives | Resources, Tools, Prompts | Tasks, Messages, Artifacts, Agent Cards |
| Lifecycle | Stateless call/response | Stateful task lifecycle (multi-turn) |
| Use case | AI uses external capabilities | AI agents collaborate on work |
| Identity | Client identity (one-way) | Mutual agent identity (two-way, cross-ref `agent-identity.md`) |
| Failure mode | Tool unavailable / wrong schema | Peer non-responsive / task abandoned / artifact disputed |

The protocols compose: an agent invoked over A2A almost always uses MCP internally to reach its tools. The two are sibling layers, not competing standards.

## A2A v1.2 Spec — Core Primitives

### Tasks
The unit of delegated work. Lifecycle states: `created → assigned → in-progress → (completed | failed | cancelled)`. Tasks carry a structured goal, optional deadline, and a reference back to the requesting agent. The receiving agent owns task execution; the requesting agent owns acceptance of the result. State transitions are auditable — every transition is an event the orchestrator can record.

### Messages
Structured payloads exchanged mid-task. Messages are threaded against a task ID and ordered. They carry intermediate updates ("I'm 60% through, here's what I have"), clarifying questions, and partial artifacts. Messages are NOT how tasks are created — they are how agents communicate during an in-flight task.

### Artifacts
Outputs an agent produces and shares with peers. Artifacts are typed (text, structured data, file references, links) and can be partial (streamed) or final. An agent may return multiple artifacts per task; the requester decides which constitutes acceptance.

### Agent Cards
Discovery + capability declaration. Each agent publishes an Agent Card describing its identity, the task types it accepts, input/output schemas, auth requirements, and version. Cards are the routing primitive — an orchestrator selects a peer by matching task requirements against published cards.

## Transport + Auth

A2A v1.2 uses HTTP with JSON-RPC 2.0 as the carrier. Auth is OAuth2 with mutual agent identity per the V2V `agent-identity.md` pack — both sides verify, not just the client. Tokens are short-lived and scoped to a task or task class, not blanket peer access. TLS termination is at the agent boundary; intermediate proxies must not unwrap A2A payloads.

## Multi-Agent Orchestration Patterns

### Star (centralized coordinator)
One coordinator agent decomposes a goal and dispatches sub-tasks to peers. Coordinator owns the task DAG, aggregates artifacts, and presents the final result. Simple to reason about. Single point of failure for the workflow — if the coordinator crashes mid-task, recovery requires task-state durability.

### Mesh (peer-to-peer)
Agents negotiate task ownership directly. No central coordinator; routing happens via Agent Cards plus a discovery service. Resilient to single-agent failure. Hard to reason about, hard to audit (multi-party causality), and prone to deadlocks where two peers each wait on the other.

### Hybrid (coordinator + peer escalation)
Most production deployments. A coordinator owns the top-level task and the audit trail; peers may delegate sub-tasks directly to other peers when they have local context the coordinator lacks. V2V's default recommendation: **hybrid**. It preserves the audit clarity of star while letting specialist agents do specialist hand-offs without coordinator round-trips.

## NIST CAISI Alignment

NIST CAISI (AI Agent Standards Initiative, Feb 2026) defines a reference architecture for safe multi-agent systems: identity, capability declaration, task lifecycle, observability, and policy enforcement. A2A v1.2 maps cleanly onto **identity** (mutual auth), **capability declaration** (Agent Cards), and **task lifecycle** (Tasks). Convergence is strong on these three layers.

The current gaps where NIST CAISI exceeds what A2A v1.2 specifies: **observability** (A2A defines events but not a standard telemetry schema — implementations diverge), **policy enforcement** (CAISI envisions a policy layer that approves task delegation against an org-level rulebook; A2A leaves this to the orchestrator), and **cross-organization trust** (CAISI anticipates inter-org agent traffic; A2A v1.2 assumes single-org trust domain). Treat the gaps as known; expect v1.3+ to close them.

## Implementation Guidance

A product org adopting A2A should: declare Agent Cards in source control (not runtime-only — review them like API contracts); make task-lifecycle events flow to the same audit log as MCP tool calls and human decisions (cross-ref `decision-quality-audit`); pick **hybrid** orchestration unless the system is genuinely small (star) or genuinely federated (mesh); and run a per-task policy check at the coordinator before dispatch (capability scope + data sensitivity + counterparty trust). Don't expose A2A endpoints outside the trust domain in v1.2 — the cross-org story is not yet defensible.

## Anti-Patterns / Common Failures

- **Star coordinator as SPOF without task-state durability** — coordinator crash loses all in-flight work. Persist task state; resume on restart.
- **Agent-card staleness** — a peer's published capability drifts from its actual behavior. Sign cards and version them; reject peers with unverifiable cards.
- **Missing task-lifecycle audit** — state transitions happen but aren't logged. Reconstructing what an agent did becomes impossible. Log every transition.
- **A2A used where MCP would do** — peer-call between an agent and a thing-that's-really-a-tool. Adds peer-identity overhead with no collaboration value. If the receiver is stateless and tool-shaped, use MCP.
- **Mesh adopted for clean-architecture reasons** — looks elegant; produces deadlocks and unauditable causality in production. Choose mesh only when star/hybrid genuinely cannot meet the workload.

## V2V Cross-References

**Sibling Q2-3 packs**:
- **`agent-identity.md` (Q2-3.1)** — mutual agent identity layer A2A v1.2 depends on. A2A's mutual-auth pattern is the peer-symmetric instantiation of Pattern 3 (OAuth-style delegation with `act_as`) extended for two-way verification; Agent Card identity binding consumes that pack's system-identity surface.
- **`mcp-governance.md` (Q2-3.2)** — governance pattern (registry, approval workflow, audit-trail standards, supply-chain assessment) applies to A2A peer-call boundaries as well as MCP integration boundaries. Agent Cards published in source control are the A2A analog of MCP-server intake records.
- **`csa-ai-controls-matrix.md` (Q2-3.3)** — AICM control taxonomy applies to A2A operating posture; domain 9 (Identity & Access Management) and domain 11 (Logging & Monitoring) operationalize on A2A task-lifecycle events.
- **`eu-ai-act-annex-iv.md` (Q2-3.4)** — Annex IV §1 (architecture) and §3 (monitoring, functioning, control) documentation cites A2A topology choices (star / mesh / hybrid) for multi-agent high-risk systems.
- **`ai-bom.md` (Q2-3.5)** — AI BOM §2.6 (Third-Party Components) consumes Agent Cards directly when third-party components are A2A peer agents (not just MCP servers).

**Sibling Q2-5 packs**:
- **`mcp-architecture.md` (Q2-5.1)** — **sibling protocol; pair-read**. MCP is asymmetric agent→tool/data-server; A2A is symmetric agent↔agent. The two compose: an A2A peer almost always uses MCP internally to reach its tools. See the A2A-vs-MCP table in §"A2A vs MCP — Sibling Protocols, Different Roles" of this pack.
- **`agentic-security.md` (Q2-5.3)** — A2A-specific threat surfaces: task injection at the Tasks-primitive boundary, Agent Card spoofing (named explicitly in that pack's Pattern 2 "Agent-card spoofing" attack vector), cross-peer privilege escalation through `act_as` chains.
- **`subagent-driven-development.md` (Q2-5.4)** — how product teams adopt agent-to-agent patterns in their delivery workflow; when sub-agents delegate to other sub-agents, A2A is the wire.

**Existing packs**:
- `api-design.md` — broader API design patterns A2A's JSON-RPC over HTTPS sits on top of.
- `security-frameworks.md` — enterprise security context that A2A trust-domain decisions (single-org v1.2; cross-org gap pending v1.3+) operate within.

**Sensitive-skill applicability**: Not sensitive per `sensitive-skill-guardrails.md` §2 (protocol architecture and integration guidance; no legal/HR/compliance output). Skills built on top of A2A that automate delegated decisions inherit sensitive-skill scaffolding independently.

## Sensitive-skill applicability

**Not sensitive.** This is a technical-reference pack — protocol architecture and integration guidance. Skills that build *on* A2A may be sensitive (e.g., a delegated-decision skill that uses A2A as carrier), and those skills inherit the sensitive-skill scaffolding from `sensitive-skill-guardrails.md` independently. The protocol layer itself does not require the Findings / Reviewer Checklist / Cannot Assess Without structure.

## A2A 2026 Governance + GA Status (added 2026-06-24, PBAW Wave 1 — `chief-architect`)

**Adapted from**:
  - Linux Foundation — "A2A Protocol Surpasses 150 Organizations… Enterprise Production Use in First Year" (linuxfoundation.org/press)
  - Linux Foundation — "Launches the Agent2Agent Protocol Project" (linuxfoundation.org/press)
  - a2a-protocol.org (latest)
**Source licence**: A2A Protocol (Apache-2.0, under Linux Foundation stewardship)
**V2V refinements**: governance/adoption framing layered over the pack's existing v1.2 technical baseline; explicitly reconciles the version lineage rather than overwriting the pack's assumed spec version.

> **Version-string reconciliation (important):** the technical sections of this pack are written against **A2A v1.2** (the pack's assumed spec baseline; see "A2A v1.2 Spec — Core Primitives" above) and anticipate **v1.3+** to close the cross-org / observability / policy gaps. Public LF/adoption reporting describes the protocol's GA lineage in terms of a **v0.3 → v1.0** production-grade milestone (gRPC support, signable Agent Cards, **version negotiation** guaranteeing backward-compatible migration). These are **not contradictory** — they describe different release tracks/labels reported by different sources. **Do not assert a single canonical version number here; verify the current spec version at a2a-protocol.org before depending on a specific string.** What matters architecturally is below.

### Governance: now Linux Foundation, not Google-owned
A2A was developed by Google and **donated to the Linux Foundation** (the pack already notes the March 2026 donation). It is now stewarded under **LF AI & Data** by a Technical Steering Committee with representation across AWS, Cisco, Google, IBM Research, Microsoft, Salesforce, SAP, and ServiceNow. **Design implication:** A2A is vendor-neutral governance, not a single-vendor protocol — a point in its favor when choosing it as an integration contract, and it lowers the "betting on one vendor" risk the pack's adoption guidance otherwise has to weigh.

### ACP convergence
**IBM's Agent Communication Protocol (ACP) merged into A2A under LF AI & Data.** **Design implication:** if a counterparty system or a prior evaluation pointed at ACP, treat A2A as the consolidated target — there is one fewer competing agent-comms standard to track. (MCP remains the sibling tool-call protocol — the boundary in this pack's "A2A vs MCP" section is unchanged.)

### Production-grade GA + version negotiation
The protocol crossed into **enterprise production use** in its first year (LF reports 150+ supporting organizations and integrations across Google, Microsoft, and AWS platforms). The GA line added **version negotiation** with a spec-level backward-compatibility guarantee across releases. **Design implication:** the "is this production-ready?" hesitation in early adoption guidance is weaker now — but the pack's standing caution still holds: **do not expose A2A endpoints outside your trust domain** until the cross-org trust story (the v1.3+ gap noted above) is defensible for your specific deployment. **Verify** the current cross-org posture against the live spec before any inter-org A2A traffic.

## Operating Principle

> *Agents collaborate; tools serve. A2A is the contract for collaboration — keep the boundary with MCP clean and the protocol stays useful.*
