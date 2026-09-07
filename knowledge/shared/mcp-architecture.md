---
pack: mcp-architecture
consumers:
- ai-architect
- chief-architect
- tech-lead
- backend-dev
- pm-dir
- product-manager
---
# MCP Architecture Pack — V2V technical reference for Model Context Protocol transport, schema, and client/server patterns

**Version**: 1.0.0
**Type**: knowledge-pack (technical reference, not sensitive)
**Owner**: ai-architect (primary) + chief-architect (substantive co-owner)
**Last updated**: 2026-06-06 (Q2 delta refresh — MCP Release Candidate; prior: 2026-05-18 Q2-5.1, Wave 2)
**Consumers**: `ai-architect`, `chief-architect`, `security-architect`, `tech-lead`, `backend-dev`, `data-architect`, `enterprise-systems`; downstream skills `/api-design`, `/code-review`, `/ai-control-audit` (when `--framework=mcp` and only for control mapping into the sibling pack)
**Sibling pack (WHAT-CONTROLS counterpart)**: `mcp-governance.md` (Q2-3.2, Wave 1 — covers controls, registry, approval workflow, audit requirements, vendor risk, ISO 42001 + CSA AICM mapping, incident response)
**Sensitive**: false (technical reference; not legally or operationally sensitive per `sensitive-skill-guardrails.md` §2)
**Re-verification cadence**: quarterly (next: 2026-08-18; mandatory re-read on each material Anthropic MCP spec revision or new transport pattern reaching production maturity)
**token_budget_variance_rationale**: D14 case (a) joint-authoring 🤖 AI Architect + 🏗️ Chief Architect AND case (b) multi-consumer (five primary consumers across Architecture, Security, Engineering). The pack's central authoring constraint is the M38 boundary contract with `mcp-governance.md`, which requires explicit per-section `Out of scope` redirects that exceed the 2000-token nominal budget without losing boundary clarity. Pack is reference material, not preload.

---

**Adapted from**:
- Anthropic Model Context Protocol specification (modelcontextprotocol.io) — the protocol specification; canonical source for JSON-RPC framing, capability negotiation, the three primitives (resources, tools, prompts), and transport variants. Initial public spec November 2024; substantial revisions through 2025-2026.
- Structurizr MCP Server (community-maintained, publicly documented through 2026, structurizr.com) — exemplar of structured-output MCP servers: declares typed resources, returns deterministic JSON over JSON-RPC, demonstrates the "MCP server as architectural integration surface" pattern.
- Claude Code C4 Skill (Anthropic, Feb 2026) — exemplar of skill-defined MCP client patterns: declarative capability discovery, structured tool invocation, error-handling and retry expressed at the skill layer rather than the transport layer.
- MCP transport patterns — stdio (local subprocess), SSE (Server-Sent Events for streaming), Streamable HTTP (the 2026 bidirectional pattern). All three documented in the Anthropic MCP specification.
- MCP Release Candidate (announced 2026-05-21, final dated 2026-07-28, blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/) — stateless transport core, extensions framework, Tasks demotion, formal deprecation policy.
- MCP 2026 roadmap (blog.modelcontextprotocol.io/posts/2026-mcp-roadmap/) — four priority areas replacing dated milestones.
- MCP Apps extension `ext-apps` / SEP-1865 (github.com/modelcontextprotocol/ext-apps/) — sandboxed-iframe interactive HTML UIs via `ui://` resources, ratified as an official extension.

**Source licence**:
- Anthropic MCP specification: Apache-2.0 (open protocol).
- Structurizr MCP Server: MIT (community OSS).
- Claude Code C4 Skill: per Anthropic Claude Code publication terms (publicly documented; reference and summary).
- MCP transport patterns: documented in the Apache-2.0 specification.
- MCP Release Candidate, 2026 roadmap, and `ext-apps` extension: Apache-2.0 (open protocol) / publicly documented Anthropic + MCP-community sources.

**V2V refinements**:
- Authored the **explicit boundary contract** with `mcp-governance.md` (M38): this pack covers HOW MCP works; the sibling pack covers WHAT-CONTROLS. Each major body section ends with an `Out of scope (see mcp-governance.md)` redirect naming the governance dimension deliberately deferred. The boundary is visible to the reader, not just enforced by authoring discipline.
- Cross-mapped MCP primitives (resources, tools, prompts) to **V2V Phase 4 (Execution) decision interfaces** — resources surface execution-context evidence, tools execute decisions, prompts carry decision framing into agent runtime. This is a V2V-specific architectural lens not present in the source specification.
- Added **implementation guidance for product organizations adopting MCP-server architecture** (server-design patterns, client-design patterns, transport-selection heuristics) distinct from vendor-selection or registry governance, which live in the sibling pack.
- Added structural cross-reference placeholders for the auth-handshake identity layer (Q2-3.1 `agent-identity.md`) and the agentic threat model that cites MCP attack surfaces (Q2-5.3 `agentic-security.md`).
- Drew the M38 boundary contract explicitly so consuming packs (Q2-5.3 in particular) can cite mechanics from this pack and controls from the sibling pack without ambiguity.
- **2026-06 delta**: corrected the Streamable HTTP / stateless framing from "emerging direction / H2-2026 roadmap" to the locked MCP Release Candidate (RC 2026-05-21, final 2026-07-28) and added §2.4 + a dated Delta Update section covering the stateless transport core, extensions framework, Tasks demotion, `ext-apps` (SEP-1865) ratification, the formal deprecation policy (Roots/Sampling/Logging, 12-month windows), and the roadmap reorganization into four priority areas.

---

**Boundary contract** (M38): This pack covers **HOW MCP works** — JSON-RPC framing, the three transport variants (stdio, SSE, Streamable HTTP), the three primitives (resources, tools, prompts), capability negotiation, the tool-call invocation flow, auth-handshake mechanics at the protocol level, server architecture patterns (stateless vs stateful, multi-server orchestration), client architecture patterns (capability discovery, error handling, retry logic), and multi-server session-graph mechanics. For **WHAT-CONTROLS** — shadow-AI sprawl controls, audit-trail and log-retention requirements, privilege-escalation defenses at the governance layer, server registry and approval workflows, vendor and supply-chain risk on MCP servers, ISO 42001 + CSA AICM control mapping, incident response for MCP-server breaches — see the sibling pack `mcp-governance.md` (Q2-3.2). Each major section below ends with an explicit `Out of scope (see mcp-governance.md)` note naming the controls deliberately deferred. The boundary should be visible to the reader, not just enforced by the authors.

---

## 1. What MCP Is (architecturally)

The Model Context Protocol is a protocol layer between AI clients (LLM-driven assistants, agents, IDE integrations) and tool-or-data servers (databases, SaaS APIs, internal services, file systems). The protocol standardizes three concerns that, before MCP, every AI-integration project re-invented: **what the server exposes** (resources, tools, prompts), **how the client discovers it** (capability negotiation), and **how the client invokes it** (typed JSON-RPC calls over a transport).

MCP's architectural shape is a JSON-RPC 2.0 message bus with capability-typed endpoints. The client and server perform a handshake that exchanges supported capabilities, then operate over typed messages whose schema is declared in the specification. The protocol is transport-agnostic: the same message schema runs over a local subprocess (stdio), over a streaming HTTP connection (SSE), or over the 2026 Streamable HTTP variant. Transport selection is an architectural decision driven by deployment topology, not a protocol decision.

The design value of MCP is **standardization with latitude**. A single AI client implementation can consume any compliant MCP server without per-integration code. A single server implementation can serve any compliant AI client. The latitude is in how the client composes capabilities — the same set of tools can be invoked in patterns the server author did not anticipate, which is also where governance attention concentrates.

**Out of scope** (see mcp-governance.md): the controls that operate on this latitude — server approval, shadow-AI sprawl detection, privilege scoping, and the broader registry and lifecycle governance — are the sibling pack's territory.

---

## 2. MCP Transport Patterns

The MCP specification defines three transports. Each has a distinct architectural fit, and the choice is consequential for deployment topology, latency profile, scaling characteristics, and security posture.

### 2.1 stdio Transport

The stdio transport runs the MCP server as a local subprocess of the client. Communication is over the subprocess's stdin and stdout, framed as line-delimited JSON-RPC messages. This is the original MCP transport and remains the canonical pattern for **desktop**, **CLI-tool**, and **single-user-agent** deployments.

Architectural properties: zero network surface (no listening port, no certificate, no transport-layer auth); process lifecycle bound to the client (server terminates when client exits); credential inheritance from the spawning user; latency in the sub-millisecond range (no network hop). The server's identity is established by file-system path of the binary plus whatever credentials the spawning user already holds; no protocol-layer authentication beyond that.

Best fit: a personal AI assistant invoking local tools (filesystem, git, local databases), an IDE integration where the MCP server ships with the IDE extension, a developer-tooling MCP server consumed by a CLI agent. Worst fit: any multi-tenant or shared-service deployment, because stdio is fundamentally one-process-per-client.

**Out of scope** (see mcp-governance.md): which categories of MCP servers should be permitted to operate under stdio deployment for a given product organization, and the registry-policy controls on stdio-deployed servers.

### 2.2 SSE (Server-Sent Events) Transport

The SSE transport runs the MCP server as a long-lived HTTP service. The client opens a streaming HTTP connection; the server sends responses over the SSE event stream; the client sends requests over POST to a separate endpoint. SSE became the canonical pattern for **remote MCP servers** through 2025 and remains widely deployed in mid-2026.

Architectural properties: standard HTTP/HTTPS network surface (firewall and load-balancer behavior is conventional); server can serve many clients concurrently; latency profile dominated by network hop plus server processing (typically tens to hundreds of milliseconds); backpressure handled by the SSE stream's natural flow-control; the asymmetric request-response shape (POST for requests, SSE for responses) requires correlation identifiers that the protocol carries in JSON-RPC `id` fields.

Implementation notes: the SSE connection holds open indefinitely; reconnection logic on the client is essential because intermediate proxies, load balancers, and network conditions terminate long-lived connections unpredictably. Connection-pool sizing on the server side reflects concurrent-client expectations rather than per-request load.

**Out of scope** (see mcp-governance.md): the network-policy controls (egress filtering, TLS-certificate management, IP-allowlisting) that wrap remote MCP-server deployment, and the registry-policy controls on which remote servers a product organization permits.

### 2.3 Streamable HTTP Transport

The Streamable HTTP transport carries full bidirectional streaming over a single HTTP connection. It replaces SSE's asymmetric POST-plus-SSE shape with a single duplex channel, simplifying client implementation and reducing the cardinality of connection state. Streamable HTTP is the direction the MCP protocol is moving; new MCP-server implementations through 2026 increasingly default to it. (Update: the MCP Release Candidate locked 2026-05-21, final dated 2026-07-28, takes Streamable HTTP further — it makes the transport core *stateless* by eliminating the `initialize`/`initialized` handshake and `Mcp-Session-Id` headers, so servers route through standard load balancers and scale horizontally. See §2.4 and the 2026-06 Delta Update at the end of this pack.)

Architectural properties: similar to SSE for network-surface and latency, but bidirectional in a single connection; supports server-initiated messages (resource-change notifications, capability-update notifications) that SSE supported awkwardly via the always-open response channel; simpler client implementation (no separate POST endpoint to correlate). Backpressure handling is more explicit and follows standard HTTP/2 flow-control semantics where the underlying transport is HTTP/2.

> **Superseded re: server-initiated messaging (MCP 2026-07-28 RC) — see the 2026-06-24 Delta §B.** The "always-open response channel" framing above no longer holds under the RC: SEP-2260 restricts server-initiated requests to *during active processing of a client request*, and SEP-2322 replaces the held-open SSE stream with the `InputRequiredResult` / `inputResponses` re-issue pattern. Treat this paragraph as historical context for pre-`2026-07-28` transports.

Architectural posture for 2026: Streamable HTTP is the recommended choice for new MCP-server implementations targeting multi-tenant deployment. SSE-deployed servers do not need urgent migration but should be migrated opportunistically. stdio-deployed servers are a different architectural category and not affected by the SSE-to-Streamable-HTTP transition.

**Out of scope** (see mcp-governance.md): the migration-management controls for an organization shifting an MCP-server fleet from SSE to Streamable HTTP, and the registry-update workflow that tracks transport variant per server.

### 2.4 Stateless Transport Core (RC, dated 2026-07-28)

The MCP Release Candidate (announced 2026-05-21, final publication dated 2026-07-28) locks a **stateless transport core** as the protocol direction — superseding the earlier framing of statelessness as an H2-2026 aspiration. The handshake-bearing `initialize`/`initialized` exchange and the `Mcp-Session-Id` headers are ELIMINATED from the core. The architectural consequence is direct: a server that holds no transport-layer session can be placed behind a standard HTTP load balancer with no session affinity, and scaled horizontally like any conventional stateless service. This collapses the operational distance between "MCP server" and "ordinary stateless microservice" (see §5.1) at the transport layer.

What survives and what moves: capability discovery as a concept persists, but the stateful handshake is gone from the core; anything that genuinely needs negotiated session state moves into the new **extensions framework** (§2.4 of the Delta Update) rather than living in the transport core. Servers that today rely on the `initialize` handshake for session establishment must re-architect toward the stateless core or declare the relevant behavior as an extension.

**Out of scope** (see mcp-governance.md): the migration-governance controls for moving a server fleet onto the stateless RC core, and the registry-policy decision on whether to require RC-conformant statelessness for newly-approved servers.

---

## 3. MCP Message Schema

The MCP message schema is JSON-RPC 2.0 with a constrained set of method names declared by the specification. The schema is the contract between every MCP client and every MCP server, and is the surface that capability negotiation discovers.

### 3.1 The Three Primitives: Resources, Tools, Prompts

MCP servers expose three categories of capability. Each has a distinct schema and a distinct invocation pattern.

**Resources** are addressable read-only content. A resource has a URI, a MIME type, and content. The client discovers available resources via `resources/list`, reads a specific resource via `resources/read`, and subscribes to change notifications via `resources/subscribe` if the server declares the subscription capability. Resources map architecturally to the **read side** of the integration boundary: documents, database query results, file contents, API responses framed as content.

**Tools** are typed invocable functions. A tool has a name, a JSON-Schema-typed parameter contract, and a typed result contract. The client discovers available tools via `tools/list`, invokes a tool via `tools/call` with parameters matching the declared schema, and receives a result whose schema matches the declared result contract. Tools map architecturally to the **write side** plus **compute side** of the integration boundary: state-changing operations, parametric queries, function-call evaluations.

**Prompts** are reusable prompt templates the server provides to the client. A prompt has a name, a parameter list, and a templated message sequence the server returns when invoked. Prompts are the protocol's mechanism for the server to suggest task-shaped interactions the client can offer to its user. Prompts map architecturally to the **interaction-template side**: the server contributes prompt scaffolding rather than the client inventing it.

In V2V architectural terms: resources surface execution-context evidence into V2V Phase 4 (Execution); tools execute decisions made in V2V Phases 1-3; prompts carry decision framing from V2V Phase 0 (Vision) and Phase 1 (Discovery) into agent runtime. This mapping is V2V-specific and is the architectural lens product organizations use to evaluate whether an MCP-server design serves the underlying product decision flow.

**Out of scope** (see mcp-governance.md): which primitives a given MCP server should be permitted to expose to which agent persona or user role; the registry policy on primitive declaration; the data-classification controls on resource content (the WHAT — this pack describes HOW resources are declared and read, not what may be exposed).

### 3.2 Capability Negotiation

The protocol's handshake begins with `initialize`: the client sends its supported protocol version and capability declarations; the server responds with the negotiated protocol version and the capabilities it supports. Capability declarations cover the three primitives plus optional features (subscriptions, logging, completions, sampling). After `initialize`, both sides operate under the negotiated capability set; calls outside that set are protocol errors.

> **Superseded for the stateless transport core (RC locked 2026-05-21, final 2026-07-28).** The MCP Release Candidate ELIMINATES the `initialize`/`initialized` handshake and `Mcp-Session-Id` headers from the transport core to make servers stateless and horizontally scalable behind standard load balancers. Capability negotiation as a *concept* persists, but the stateful handshake described above is removed in the RC core. See the 2026-06 Delta Update at the end of this pack for the full set of RC changes (extensions framework, Tasks demotion, `ext-apps` ratification, deprecation policy).

The architectural significance of capability negotiation is that **the client knows up-front what the server can do**, and conversely. This eliminates the runtime-discovery-or-fail pattern that bedevils ad-hoc API integrations. It also means that a client cannot probe for capabilities the server did not declare — capability declaration is the surface the server commits to support.

Implementation guidance: clients should cache the negotiated capability set per server connection and re-negotiate on reconnection. Servers should declare capabilities truthfully — declaring a capability the server cannot reliably serve creates downstream client errors that are hard to diagnose because the protocol surface implied the capability was available.

**Out of scope** (see mcp-governance.md): the registry policy on how server capability declarations are reviewed at intake, and the change-management controls when a server's declared capability set changes.

### 3.3 The Tool-Call Invocation Flow

A tool call is a single JSON-RPC `tools/call` request from client to server, carrying the tool name and the parameter object. The server validates parameters against the declared tool schema, executes the tool's implementation, and returns a `tools/call` response containing the result object plus a status (success / error / partial). The client treats the response as typed per the declared result contract.

Error semantics: protocol-layer errors (malformed JSON-RPC, unknown tool name, parameter schema violation) are distinguished from tool-layer errors (the tool ran but produced an error result). Protocol-layer errors travel as JSON-RPC error responses; tool-layer errors travel as structured `isError: true` results within an otherwise-successful JSON-RPC response. Clients must handle both layers; conflating them is a common implementation defect.

Timeout semantics: the protocol does not mandate a tool-call timeout; the client decides. Servers should treat long-running tools as a design choice and document their expected latency; clients should configure timeouts per tool category (sub-second for read-only lookups, seconds for compute, longer with explicit user awareness for batch operations). Timeouts that expire mid-execution leave the server's tool implementation potentially still running — the protocol does not provide a cancellation primitive in the base specification, though servers may expose explicit cancellation tools.

Multi-step tool sequences are an emergent pattern, not a primitive: the client orchestrates the sequence, holding result data between calls, choosing the next tool based on the previous result. The protocol does not natively express transactions across multiple tool calls.

**Out of scope** (see mcp-governance.md): the alerting and circuit-breaker controls on state-changing tool invocations, the rate-limiting policy on tool calls, and the audit-trail completeness standard that every tool invocation must meet.

---

## 4. Auth Mechanics

Authentication in MCP operates at two levels: the transport-layer auth that establishes the client-server connection, and the identity-binding that the auth handshake carries. This section covers the transport-layer mechanics. The identity layer — which agent is invoking, with what authority, under whose delegation — is the territory of `agent-identity.md` (Q2-3.1).

### 4.1 OAuth Flow at the Protocol Level

The Anthropic MCP specification defines an OAuth 2.1 authorization flow for remote MCP servers (SSE and Streamable HTTP transports). The flow is the standard OAuth authorization-code-with-PKCE shape: the client initiates authorization at the server's well-known authorization endpoint, the user (or the agent operating on the user's behalf) authenticates and authorizes the requested scopes, the authorization server returns an authorization code, the client exchanges the code for an access token at the token endpoint, and subsequent MCP JSON-RPC calls carry the access token in an `Authorization: Bearer` header.

Architectural points worth naming:

- **Scope semantics are protocol-defined at the MCP layer, not invented per server.** The MCP specification declares the scope names that map to capability sets (resource read, tool call categories, subscription). Servers do not invent novel scope names; they map their declared capabilities to the standard scopes.
- **Token refresh is standard OAuth 2.1.** Access tokens are short-lived; refresh tokens are long-lived. Clients implement standard refresh logic. The protocol does not extend OAuth 2.1 token mechanics.
- **The authorization server may or may not be the MCP server.** Larger MCP deployments separate the authorization server (an identity-provider-fronted authorization endpoint) from the MCP servers themselves (resource servers in OAuth terms). Smaller MCP deployments may collocate them.

stdio transport does not use OAuth at the MCP layer because stdio inherits credentials from the spawning process. The auth surface for stdio is the local-user-credential surface plus whatever the spawned server binary chooses to do with those credentials.

**Out of scope** (see mcp-governance.md): the credential-rotation policy that operates on MCP-server tokens, the just-in-time credential elevation governance, and the periodic credential-scope review cadence. These are control-layer concerns; see also `agent-identity.md` (Q2-3.1) for the identity-binding patterns the auth handshake carries.

### 4.2 Client Identity Binding

Every MCP JSON-RPC call carries (implicitly via transport) the client's identity as established at auth time. **Which** identity it carries is the layered question that `agent-identity.md` answers: is it the human user's identity, a delegated agent identity, a workload identity, or a hybrid with `act_as` claims? This pack describes the **mechanism** — the access token in the `Authorization` header — and defers the **semantics** to the identity pack.

The protocol-level identity binding is therefore not the MCP specification's invention; it is OAuth's standard `sub` claim plus any extension claims the authorization server chooses to issue. Cross-reference: `agent-identity.md` §Agent-to-Agent Authentication (load-bearing per M34) names the four 2026 patterns for delegation (capability-token forwarding with narrowing, mutual TLS with agent certificates, OAuth-style delegation flow, Workload Identity Federation bridging) — all four interact with the MCP auth handshake but the identity semantics live in that pack.

**Out of scope** (see mcp-governance.md): the registry policy on which identity types may invoke which MCP servers, and the audit-trail requirements that link MCP-layer caller identity to upstream agent or user identity. See also `agent-identity.md` (Q2-3.1) for the identity-layer patterns.

---

## 5. Server Architecture Patterns

MCP server architecture is dominated by a single decision: stateless or stateful. The decision shapes deployment topology, scaling characteristics, and operational complexity.

### 5.1 Stateless Servers

A stateless MCP server holds no per-client state between requests. Every JSON-RPC request is processed independently; resource reads and tool calls produce results from the server's underlying systems without server-side memory of prior calls. This is the simpler architecture and is the right default for most product-organization MCP-server implementations.

Operational properties: trivial horizontal scaling (any server instance can handle any request); no session-affinity requirements at the load balancer; failure recovery is per-request (a failed request can be retried without state-consistency concerns); deployment topology can be conventional stateless-microservice patterns (Kubernetes deployments, Cloud Run services, Lambda functions for short-lived calls).

Idempotency matters: stateless servers should make tool calls idempotent where the underlying operation permits (use natural keys, accept idempotency-key parameters, design tool semantics to be retry-safe). Idempotent tool implementations let the client retry on transport failure without risking duplicate side effects.

Caching at the server side is permitted (resource content cached behind the server's own logic) without making the server stateful in the MCP-protocol sense — MCP statefulness is about per-client session state, not about server-internal caching.

**Out of scope** (see mcp-governance.md): the operational controls on stateless server deployment (rate-limiting, circuit-breaker, alerting policy), and the registry classification of stateless versus stateful servers.

### 5.2 Stateful Servers

A stateful MCP server holds per-client session state — typically because the server's underlying domain requires it (database transactions, long-running computations, multi-step workflows where intermediate state must persist). Stateful servers are architecturally more complex and should be used only when the underlying domain justifies it.

Operational properties: session-affinity at the load balancer (a given client's calls must reach the same server instance, or session state must be externalized to a shared store); session-expiration policy (idle sessions must be reaped; session state must not accumulate indefinitely); failure recovery requires session-state durability (in-memory session state lost on instance failure must either be reconstructable or acceptable to lose).

The most common stateful pattern in 2026 is the **server-side conversation state** pattern: the MCP server holds a conversation graph that aggregates tool-call results across a session and exposes derived resources or prompt scaffolding based on the accumulated state. Structurizr's MCP server is an exemplar — the server holds the architecture-model state across a session of model-mutation tool calls and exposes the current model as a resource.

Design heuristic: if a stateful design is being chosen for performance (caching) reasons rather than domain (transactional, multi-step-workflow) reasons, reconsider stateless with a shared cache layer.

**Out of scope** (see mcp-governance.md): the session-state-retention policy, the session-audit-trail standard, and the registry-policy controls on stateful-server approval (stateful servers typically tier higher in the approval workflow).

### 5.3 Multi-Server Orchestration

Many production MCP deployments involve clients consuming several MCP servers concurrently. The client orchestrates: discovers capabilities across all connected servers, routes tool calls and resource reads to the appropriate server, and composes results across servers in service of the user task. This is the dominant pattern for production agent deployments in 2026.

Architectural patterns:

- **Federated capability namespace**: the client unions tool names and resource URIs across servers, with a server-identifier prefix to disambiguate. The user (or the agent operating on the user's behalf) sees a single capability set that is the union of all connected servers.
- **Session-graph mechanics**: a single user task may invoke tools across multiple servers in sequence; the client holds session-graph state that links tool calls to user task. The protocol does not natively express cross-server session graphs; client implementations do.
- **Cross-server result composition**: results from one server become inputs to a tool call on another server, with the client (or the orchestrating LLM) responsible for the composition. There is no protocol-level transaction across servers; partial failure is possible and the client must handle it.

Inter-server isolation matters: an MCP server in the federation should not directly invoke another MCP server in the federation. Cross-server flows route through the orchestrating client (and its LLM) under the client's authorization context. Direct server-to-server invocation under a single caller identity is an architecture anti-pattern and is the protocol-level shape of one of the privilege-escalation vectors named in the governance sibling.

**Out of scope** (see mcp-governance.md): the inter-server isolation controls at the governance layer, the registry policy on which servers may federate, and the anomaly-detection controls on session-graph composition patterns.

---

## 6. Client Architecture Patterns

MCP client implementations are dominated by three responsibilities: capability discovery and caching, error handling across the two error layers (protocol versus tool), and retry-with-backoff for transport-layer failures.

### 6.1 Capability Discovery and Caching

After the `initialize` handshake, the client queries `resources/list`, `tools/list`, and `prompts/list` (where supported) to enumerate the server's exposed capabilities. The client caches the result per server connection. Cache invalidation triggers: server-initiated `notifications/list_changed` notifications, client-initiated reconnection, explicit user request to refresh.

The cache shape matters for the client's downstream behavior. An LLM-driven agent client typically projects the cached capability set into the LLM's context as a tool manifest; the manifest format depends on the LLM's tool-calling convention (OpenAI function-calling, Anthropic tools, Google function-calling) and is the client's responsibility to translate. The MCP specification standardizes the source representation, not the LLM-facing representation.

### 6.2 Error Handling Across Two Layers

The two error layers from §3.3 demand distinct handling at the client. Protocol-layer errors (JSON-RPC `error` responses) indicate that the call did not reach the server's tool implementation: malformed parameters, unknown tool, server unavailable, transport failure. The client's response is typically to surface a system-level error to the user or to the agent's reasoning loop, with the call treated as not-attempted from the underlying-system perspective.

Tool-layer errors (responses with `isError: true`) indicate that the call reached the server's tool implementation but the tool itself produced an error result: invalid input semantics, downstream system failure, business-logic refusal. The client's response is typically to surface the error to the LLM as a tool-result, allowing the agent to reason about the failure and choose a follow-up action.

Conflating the two layers is a common defect. A client that treats every `isError: true` as a protocol failure loses the LLM's ability to reason about the failure; a client that treats every JSON-RPC error as a tool failure exposes the LLM to protocol-internal noise that does not belong in its reasoning context.

### 6.3 Retry and Backoff

Transport-layer failures on remote MCP servers (SSE, Streamable HTTP) are normal and demand client-side retry with exponential backoff. Standard patterns apply: exponential base with jitter, retry budget per session, circuit-break to surface persistent failure to the user rather than retrying forever. The protocol does not specify retry behavior; clients implement it.

Idempotency matters again: clients should retry calls whose underlying tool is documented idempotent more aggressively than calls whose tool is not. Clients without per-tool idempotency knowledge default to conservative retry on read-only operations (resource reads, `tools/list`, `resources/list`) and human-confirmation-required retry on state-changing operations.

Connection-pool sizing on the client side reflects server-fan-out: a client consuming five MCP servers concurrently needs five connection slots minimum; clients in long-running agent runtimes typically pool more aggressively.

**Out of scope** (see mcp-governance.md): the alerting policy when client-side retry budgets are exhausted, and the operational controls that surface persistent MCP-server failure to the broader product operations function.

---

## 7. Anti-Patterns / Common Architectural Failures

This section names architecture-level failure modes V2V has observed in MCP-adopting product organizations. Each entry names the failure pattern and the mitigation. Governance-level failure modes (registry sprawl, audit-trail gaps, approval-workflow rubber-stamping) are named in the sibling pack's Anti-Patterns section.

### 7.1 Tightly-Coupled Tool Calls Without Capability Negotiation

**Pattern**: A client hard-codes assumptions about which tools a server exposes, skipping the `initialize` and `tools/list` handshake or treating it as ceremony. When the server's capability set changes (a tool removed, renamed, or re-scoped), the client fails opaquely. The protocol's capability-negotiation surface was precisely designed to prevent this; bypassing it discards a load-bearing property of the protocol.
**Mitigation**: Treat capability negotiation as architectural truth, not setup overhead. The client's tool-invocation paths consume the cached capability set, not hard-coded tool names; a tool the server did not declare is an unsupported operation, not a 500 from a hard-coded call.

### 7.2 Missing Timeout Handling on Tool Calls

**Pattern**: The client invokes a tool with no timeout, or with a per-process default that does not match the tool's expected latency profile. A long-running tool call holds the client's request slot indefinitely; a stuck server holds the client's session indefinitely. The agent runtime degrades to apparent unresponsiveness.
**Mitigation**: Per-tool-category timeout configuration on the client. Read-only resource reads timeout sub-second; conventional tool calls timeout in seconds; explicitly long-running tools are categorized and given longer timeouts with explicit user awareness. Timeouts surface as protocol-layer errors with retry semantics; tool implementations that legitimately run long expose explicit progress or cancellation tools.

### 7.3 Ignoring Session-State Expiration on Stateful Servers

**Pattern**: A client holds a session reference to a stateful MCP server indefinitely, assuming the session persists. The server reaps idle sessions per its policy; subsequent client calls fail because the session is gone. The client's session-recovery logic is absent; the user experiences mysterious failure.
**Mitigation**: Stateful-server clients track session-state freshness explicitly, refresh sessions on idle, and handle session-expired-error responses with re-initialization rather than surfacing them as protocol failures. Server-side: the session-expiration policy is documented in the server's capability declaration where the protocol surface permits.

### 7.4 stdio Transport for Production Multi-Tenant Use

**Pattern**: An MCP server is implemented for stdio (because the developer prototyped on a desktop client) and then deployed to production as a multi-tenant service by wrapping the stdio binary in a process-per-request shell. Concurrency is bounded by process-launch latency; per-request resource overhead is high; credential handling becomes ad-hoc because stdio's credential-inheritance pattern does not match the multi-tenant context.
**Mitigation**: Multi-tenant MCP servers are implemented for SSE or Streamable HTTP from the start. Migrating a stdio-only server to a network transport is a re-architecture, not a deployment change. Choose the transport during initial server design, not after.

### 7.5 Federated Capability Namespace Collision

**Pattern**: A client federates several MCP servers without a server-identifier prefix on tool names and resource URIs. Two servers expose tools with the same name; collisions resolve unpredictably in the client's tool-invocation routing. The agent runtime occasionally invokes the wrong server's tool.
**Mitigation**: The federated capability namespace always carries a server-identifier prefix at the client level. Server-side tool names remain bare (server authors do not coordinate); the prefix is the client's federation responsibility.

### 7.6 Confusing Protocol-Layer and Tool-Layer Errors

**Pattern**: §6.2's conflation pattern, in concrete form. A client's error path treats every error as a single category, losing the LLM's ability to reason about tool-layer failures and exposing the LLM to protocol-layer noise.
**Mitigation**: Two explicit error paths at the client, with distinct downstream behavior. Protocol-layer errors surface to system telemetry and user-visible error messages; tool-layer errors surface to the LLM's reasoning loop as structured tool-result payloads.

### 7.7 Stateless-by-Default Drift to Accidental Statefulness

**Pattern**: An MCP server is designed stateless but accumulates de facto session state through server-internal caching that conflates "this caller" with "this session." Two clients with the same access token (or two sessions of the same user) interfere because the cache key is too coarse. The server appears to behave correctly under single-client testing and incorrectly under load.
**Mitigation**: Server-internal caching is keyed at the granularity below the session — by stable inputs to the operation, not by caller identity. Where per-caller caching is legitimate, the server declares itself stateful and adopts stateful-server discipline (§5.2).

---

## 8. V2V Cross-References

**Sibling Q2-3 packs**:
- **`mcp-governance.md` (Q2-3.2)** — **explicit M38 boundary partner**. The WHAT-CONTROLS counterpart to this pack's HOW-IT-WORKS. Each `Out of scope (see mcp-governance.md)` note in this pack is a forward reference; each `Out of scope (see mcp-architecture.md)` note in that pack is the reciprocal. Boundary enforced visibly from both sides.
- **`agent-identity.md` (Q2-3.1)** — the identity layer that the MCP auth handshake carries. §4.2 of this pack defers identity semantics to that pack; §Agent-to-Agent Authentication in that pack names the four 2026 delegation patterns (capability-token forwarding with narrowing / mTLS with agent certificates / OAuth-style delegation with `act_as` / Workload Identity Federation) that interact with the MCP auth handshake.
- **`csa-ai-controls-matrix.md` (Q2-3.3)** — the AICM control library that the governance sibling maps to. This pack does NOT duplicate the mapping; readers needing controls-to-MCP-mechanics traceability use the governance sibling.
- **`eu-ai-act-annex-iv.md` (Q2-3.4)** — Annex IV §1 (architecture) and §2 (design specifications) documentation for high-risk systems cites this pack's transport variant, capability negotiation, and server architecture decisions.
- **`ai-bom.md` (Q2-3.5)** — AI BOM §2.6 (Third-Party Components) inventory cites the MCP transport variant and server architecture posture per integrated component.

**Sibling Q2-5 packs**:
- **`a2a-architecture.md` (Q2-5.2)** — the agent-to-agent collaboration protocol, parallel to MCP at a different layer. MCP is the agent-to-tool-or-data-server protocol (asymmetric); A2A is the agent-to-agent orchestration protocol (symmetric, peer-to-peer). The two compose: an agent invoked over A2A almost always uses MCP internally to reach its tools. Client architecture (§6 of this pack) is where the two interact.
- **`agentic-security.md` (Q2-5.3)** — the threat model for agentic systems. MCP-server compromise and MCP-protocol-level attack surfaces are one attack vector among several. That pack cites mechanics from this pack (transport-level attack surfaces: capability tokens on the wire, mTLS at transport, federation across MCP servers) and controls from `mcp-governance.md` per the M38 boundary discipline.
- **`subagent-driven-development.md` (Q2-5.4)** — sub-agent driven dev sits on MCP as its plumbing layer; tool-integration architecture for sub-agent dev consumes the transport and primitive patterns documented here.

**Existing packs**:
- `api-design.md` — broader API design patterns that MCP server design draws on (idempotency, error semantics, capability declaration); MCP is a constrained shape on top of conventional API-design discipline.
- `ai-ml-patterns.md` — broader AI/ML system patterns that consume MCP at the tool-integration layer; agent-runtime architectures reference MCP as the standard tool-integration surface.
- `cloud-patterns.md` — deployment-topology patterns (stateless microservices, session affinity, autoscaling) that the §5 server architecture decisions sit on top of.

**Anti-Patterns scope-discipline note**: this pack's §7 anti-patterns cover architecture-layer failures (capability-negotiation bypass, timeout handling, session expiration, stdio-for-production, namespace collision, error-layer conflation, statefulness drift). Governance-layer failures (registry sprawl, audit-trail blind spots, approval-workflow rubber-stamping, credential drift, internal-only loophole, IT-handoff) live in the governance sibling §7. M38 boundary preserved — no architecture failure pattern is duplicated in the governance pack and vice versa.

## 2026-06 Delta Update (as of 2026-06-06)

The MCP Release Candidate was **announced 2026-05-21** and carries a **final publication date of 2026-07-28**, with a ~10-week SDK validation window between RC lock and final. This supersedes any earlier "H2-2026 roadmap" framing of stateless servers / server cards: the relevant primitives are now locked in an RC, not aspirational. The concrete changes:

1. **Stateless transport core.** The `initialize`/`initialized` handshake and the `Mcp-Session-Id` headers are ELIMINATED from the core. This is the load-bearing change: stateless servers route through standard load balancers and scale horizontally without session affinity. See §2.4 and the §3.2 superseded note.

2. **Extensions framework introduced.** Behavior that genuinely needs negotiated session state, or any optional capability that does not belong in the core, moves into a formal extensions framework. Extensions are identified by **reverse-DNS extension IDs** and negotiated via an `extensions` capability map. This replaces the previous pattern of bolting optional features onto the core capability declaration.

3. **Tasks demoted.** What was an experimental core feature is **demoted from the core to an opt-in extension**. Tasks now live behind the extensions framework rather than being assumed present in every conformant implementation.

4. **MCP Apps ratified as official extension `ext-apps` (SEP-1865).** Interactive HTML UIs delivered through MCP are now an official extension, NOT folded into the core. The mechanism: sandboxed-iframe interactive HTML UIs surfaced via `ui://` resources that the server declares ahead of time. `ext-apps` lives in its own repository (`modelcontextprotocol/ext-apps`), keeping the UI surface explicitly separate from the protocol core. This is the canonical way to ship generative/interactive UI over MCP going forward (cross-reference: `generative-ui.md` if present).

5. **Formal deprecation policy added.** The RC introduces an explicit deprecation policy with stated removal windows. Under it, **Roots, Sampling, and Logging are marked deprecated, each with a 12-month removal window.** Consumers depending on these should plan migration within that window.

6. **Roadmap reorganization.** The 2026 MCP roadmap blog moved AWAY from dated milestones and toward **four priority areas**: Transport/Scalability, Agent Communication, Governance, and Enterprise Readiness. This is why "dated H2-2026 roadmap item" framing is no longer accurate — the roadmap is now organized by priority area, with the RC carrying the concrete dated commitments.

**Sources:**
- MCP Release Candidate announcement: https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/ (URL slug = the final-spec date 2026-07-28; the RC was announced/locked 2026-05-21)
- 2026 MCP roadmap (four priority areas): https://blog.modelcontextprotocol.io/posts/2026-mcp-roadmap/
- `ext-apps` extension repository (SEP-1865): https://github.com/modelcontextprotocol/ext-apps/
- MCP specification repository: https://github.com/modelcontextprotocol/modelcontextprotocol

## 2026-06-24 Delta Update (MCP 2026-07-28 RC — full breaking-change + migration detail)

**Adapted from**: MCP 2026-07-28 Specification Release Candidate, blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/ (authors David Soria Parra + Den Delimarsky, Lead Maintainers; published 2026-05-21, RC locked 2026-05-21, final spec dated 2026-07-28). SEP references per the same post and the spec repo (github.com/modelcontextprotocol/modelcontextprotocol).
**Source licence**: Apache-2.0 (open protocol) / publicly documented Anthropic + MCP-community sources.
**V2V refinements**:
- Re-verified the RC against the primary source on 2026-06-24 and added the concrete migration mechanics the 2026-06-06 delta summarized at headline level only (routing headers, `_meta` transport of clientInfo/capabilities, `server/discover`, the multi-round-trip elicitation flow, caching + trace propagation, the six auth-hardening SEPs, full JSON Schema 2020-12 for tools, and the `-32002`→`-32602` error-code break).
- Added a **serverless/edge deployment topology** subsection (the V2V product-org adoption lens), framing the stateless core as what finally makes MCP servers viable on Lambda / Cloud Run / Vercel-style platforms with no session store.
- Flagged the §2.3 server-initiated-messaging framing as superseded by SEP-2260 + SEP-2322 (annotated inline at §2.3).

This section is additive to the 2026-06-06 delta (which remains correct at the headline level). Nothing there is contradicted; the detail below is the migration-grade elaboration. The RC "is the largest revision of the protocol since launch" and "contains breaking changes" — treat the items marked **[BREAKING]** as code-impacting before 2026-07-28.

### A. Stateless core — the request shape that replaces the session (six SEPs)

The stateless core is delivered by six coordinated SEPs completing the December 2025 "Future of MCP Transports" plan:

- **[BREAKING] `initialize`/`initialized` handshake removed (SEP-2575).** Protocol version, client info, and client capabilities no longer exchange once at connection time — they travel in `_meta` on *every* request (e.g. `_meta["io.modelcontextprotocol/clientInfo"]`). A new **`server/discover`** method lets a client fetch server capabilities up front when it needs them.
- **[BREAKING] `Mcp-Session-Id` header and protocol-level session removed (SEP-2567).** With both the handshake and the session gone, any request can land on any server instance. Sticky routing and shared session stores are no longer required at the protocol layer.
- **Routing headers now required (SEP-2243).** Streamable HTTP requests MUST carry `Mcp-Method` and `Mcp-Name` headers so load balancers, gateways, and rate-limiters route on the operation without inspecting the body. Servers MUST reject requests where headers and body disagree.
- **List/read results carry `ttlMs` + `cacheScope` (SEP-2549).** Modeled on HTTP `Cache-Control`. A client knows how long a `tools/list` (or resource-read) response is fresh and whether it is safe to share across users — a long-lived SSE stream is no longer the only way to learn a list changed.
- **W3C Trace Context propagation in `_meta` documented (SEP-414).** `traceparent`, `tracestate`, and `baggage` key names are now fixed, so a trace follows a tool call through client SDK → MCP server → downstream as one span tree in any OpenTelemetry backend.

**Stateful applications on a stateless protocol (the explicit-handle pattern).** Removing the protocol-level session does NOT force application statelessness. A server that needs cross-call state mints an explicit handle from a tool (`basket_id`, `browser_id`) and the model passes it back as an ordinary argument on later calls — visible to the model, which can compose and hand off handles across tools. **Architectural consequence for §5.2 (Stateful Servers):** prefer the explicit-handle pattern over server-held session state for new designs; reserve true stateful-server discipline for domains (transactions, durable workflows) that genuinely require server-side session durability.

### B. Server-to-client requests restructured — SUPERSEDES the §2.3 always-open-channel framing

- **Server-initiated requests only during active processing (SEP-2260).** A server may issue a request to the client (e.g. an elicitation prompt) ONLY while it is actively processing a client request. Earlier spec versions recommended this; it is now required.
- **Multi Round-Trip Requests replace the held-open SSE stream (SEP-2322).** Instead of holding an SSE stream open, the server returns an `InputRequiredResult` (`resultType: "inputRequired"`) carrying `inputRequests` plus an opaque echoed `requestState`. The client gathers answers and **re-issues the original call** with `inputResponses` and the echoed `requestState`. Any server instance can pick up the retry.

Net: long-lived SSE streams are no longer the mechanism for server→client interaction or list-change discovery (`ttlMs`/`cacheScope` covers the latter). Clients targeting `2026-07-28` implement the `InputRequiredResult` re-issue loop, not an always-open response-channel reader.

### C. Tools: full JSON Schema 2020-12 + the error-code break

- **[BREAKING-ish] Tool `inputSchema`/`outputSchema` lifted to full JSON Schema 2020-12 (SEP-2106).** Input schemas keep the `type: "object"` root but allow composition (`oneOf`, `anyOf`, `allOf`), conditionals, and references (`$ref`, `$defs`). Output schemas are unrestricted; `structuredContent` may be any JSON value. **Security constraints:** implementations MUST NOT auto-dereference external `$ref` URIs, and SHOULD bound schema depth and validation time (untrusted-schema DoS surface).
- **[BREAKING] Missing-resource error code changes `-32002` → `-32602` (SEP-2164).** Any client matching on the literal `-32002` value MUST be updated. Affects §3.3 error semantics and §6.2 client error handling.

### D. Extensions framework — formal process (SEP-2133), two official extensions

**SEP-2133** makes extensions first-class — reverse-DNS extension IDs, negotiated through an `extensions` map on client/server capabilities, living in their own `ext-*` repos with delegated maintainers, versioning independently of the spec. Two official extensions ship with the RC: **MCP Apps (SEP-1865)** — server-declared HTML UI templates (hosts prefetch/cache/security-review; UI-initiated actions hit the same audit/consent path as a direct tool call); and the **Tasks extension** — `tools/call` may return a task handle driven by `tasks/get`/`tasks/update`/`tasks/cancel`, creation is server-directed, and **`tasks/list` is removed because it cannot be scoped safely without sessions**. Anyone on the `2025-11-25` experimental Tasks API migrates.

### E. Serverless / edge deployment topology (V2V product-org adoption lens)

The stateless core's practical payoff: a remote MCP server that previously needed sticky sessions, a shared session store, and deep-packet inspection at the gateway now runs behind a plain round-robin load balancer, routes on the `Mcp-Method` header, and lets clients cache `tools/list` for the server's `ttlMs`. This makes MCP servers a clean fit for **function-as-a-service and edge platforms** (AWS Lambda, Cloud Run, Cloudflare Workers, Vercel functions). Heuristic: default to a stateless function behind the platform's standard load balancer; use the explicit-handle pattern (§A) for cross-call state; reach for a durable store only when the domain demands it.


### F. Migration checklist (for any MCP server/client we ship or consume before 2026-07-28)

- [ ] **Client:** stop matching on error code `-32002`; handle `-32602` for missing resource (SEP-2164).
- [ ] **Client:** move clientInfo + capabilities into `_meta` per request; drop reliance on the `initialize` handshake; use `server/discover` when up-front capabilities are needed (SEP-2575).
- [ ] **Client + Server:** drop `Mcp-Session-Id`; design for any-instance request landing (SEP-2567).
- [ ] **Server (Streamable HTTP):** emit/require `Mcp-Method` + `Mcp-Name` headers; reject header/body disagreement (SEP-2243).
- [ ] **Client:** replace always-open-SSE server-initiated handling with the `InputRequiredResult` → `inputResponses` + echoed `requestState` re-issue loop (SEP-2260, SEP-2322).
- [ ] **Client:** honor `ttlMs`/`cacheScope` on list/read results (SEP-2549).
- [ ] **Both:** adopt W3C Trace Context key names in `_meta` (SEP-414).
- [ ] **Server (tools):** upgrade schemas to JSON Schema 2020-12; do NOT auto-dereference external `$ref`; bound schema depth/validation time (SEP-2106).
- [ ] **Both:** migrate any `2025-11-25` experimental Tasks usage to the Tasks extension lifecycle; drop `tasks/list`.
- [ ] **Both:** plan migration off Roots / Sampling / Logging within the 12-month deprecation window (SEP-2577).

## 9. Operating Principle

> *MCP is the cable, not the policy — and the cable spec must be precise enough that the policy can layer on top of it without re-inventing transport. Architecture authors the cable; governance authors what travels through it.*
