---
pack: generative-ui
consumers:
- interaction-designer
- ui-designer
- frontend-dev
- user-researcher
- product-manager
- prodops
---
# Generative UI (V2V Knowledge Pack)

**Adapted from**:
  - Claude Design (Anthropic Labs, April 17 2026)
  - A2UI v0.9 (Google, April 17 2026; Vercel / AG2 / Oracle integration)
  - CopilotKit AG-UI ($27M Series A, May 2026)
  - Anthropic MCP Apps / SEP-1865 (ratified MCP extension `ext-apps`; MCP spec Release Candidate announced 2026-05-21, final dated 2026-07-28)
  - shadcn/ui CLI v4 (March 2026, MIT)
  - Figma Make (closed beta, 2026-05-28) and Vercel v0 repositioning (~2026-05-13) — added in 2026-06 delta
**Source licence**: per-source-terms (Anthropic, Google, CopilotKit, Anthropic MCP, Figma, Vercel) + MIT (shadcn/ui)
**V2V refinements**:
- Translated the three Generative UI patterns into product-organization Design adoption guidance, not vendor-product documentation.
- Codified the layered-not-picked principle as the 2026 default posture.
- Cross-referenced shadcn/ui as the de facto AI-native component vocabulary and the substrate all three patterns increasingly emit toward.
- Added product-org-specific anti-patterns (Gen-UI as feature instead of substrate; picking when layering would work; accessibility regression in generated output; under-investing in the component vocabulary).
- M32 scope discipline: this pack is a standalone Design knowledge asset, not pre-authored content for a Decision Interface Charter.
- 2026-06 delta: resolved the open status of Pattern 3 MCP Apps (SEP-1865 ratified as official `ext-apps` extension; MCP core went stateless) and added the design-tool-commits-PRs trajectory (Figma Make, Vercel v0).

> **Scope note (M32)**: This pack is a standalone Design knowledge asset. It is NOT pre-authored content for any V5.2 Decision Interface Charter. D10's locked four-Charter composition (Data / Engineering / PMM / Customer-Outcome) does not include Design. If a Design Charter is added later, this pack becomes additive composition material; until then it stands on its own as Interaction + UI reference.

---

## What Generative UI Is

The 2026 inflection: user interface is no longer entirely designed up-front and shipped as a fixed surface. AI agents can now generate, declare, or compose UI at runtime — choosing components, assembling layouts, or in some cases synthesizing new UI from scratch in response to a task or context. Between January and May 2026 the market sorted this capability into three distinct patterns, each with a different control posture and a different failure mode. The patterns are not competing vendor frameworks dressing up the same idea; they answer different questions about who decides what the user sees. By April 2026 the leading vendor implementations (Claude Design, A2UI, AG-UI, MCP Apps) had stabilized enough that Design teams in product organizations can adopt them with reasonable confidence — but only if they understand the three patterns are meant to be layered, not chosen between.

Generative UI is not "AI-generated screens." It is a runtime capability that sits between the agent and the rendered surface. The Design organization's job in 2026 is to choose how much of the surface the agent controls, to design the component vocabulary the agent draws from, and to enforce accessibility and brand discipline on output that is materialized at runtime rather than at build time.

## The Three Generative UI Patterns

### Pattern 1: Controlled (developer-bounded)

Exemplar: CopilotKit AG-UI ($27M Series A, May 2026).

The developer pre-declares the set of UI components the agent may use. The agent selects from that set and composes them — it cannot invent new components or render arbitrary markup. The application embeds the agent inside an existing product surface (a copilot in a CRM, a sidebar in a help center, a configurator inside a SaaS app). Behavior is predictable, auditable, and constrained. Failure modes are bounded: the agent might pick the wrong component, but it cannot produce a UI the design system has not vetted.

When it fits: embedded copilots in existing products where the surrounding UI is already designed and the agent is augmenting rather than replacing it. Enterprise SaaS, internal tools, and any context where audit, accessibility certification, and brand control matter more than expressive flexibility.

### Pattern 2: Declarative (agent declares UI; app renders)

Exemplar: A2UI v0.9 (Google, April 17 2026), with announced integration paths through Vercel, AG2, and Oracle.

The agent describes the desired UI in a declarative protocol — a serialized description of intent and structure — and the rendering application interprets that description against its own component library and rendering rules. The agent does not own pixels; the renderer does. This separates concerns cleanly: agents become portable across apps, apps become portable across agents. The protocol is the contract.

When it fits: cross-app agent workflows where the same agent must surface inside multiple products with different visual systems, or where the organization wants to remain vendor-agnostic on either the agent or the renderer. A2UI is the most explicitly portability-oriented of the three patterns and is the one to watch if the long-tail bet is that agents become commodities and rendering becomes the differentiator.

### Pattern 3: Open-ended (LLM generates UI on the fly)

Exemplars: Anthropic MCP Apps (an MCP spec extension that lets an LLM produce a complete app-shaped UI in response to a task) and Claude Design (Anthropic Labs, April 17 2026, a product-level instantiation of the same capability). As of the 2026-06 delta, MCP Apps' status is no longer open: SEP-1865 was ratified as an official MCP extension (`ext-apps`), explicitly NOT folded into MCP core — see the 2026-06 Delta Update below.

The LLM generates complete UI components — sometimes complete screens — at runtime, given a task and a context. There is no pre-declared component set the model must draw from; the model produces whatever shape best fits the task. This is the highest-flexibility pattern and also the weakest-guardrails pattern. The model can invent novel layouts that no designer would have produced and that no design system has approved.

When it fits: long-tail tasks, exploratory work, and surfaces where the cost of a fixed UI is higher than the risk of an unconventional one. Internal research tools, custom report builders, one-off analytical workflows. The model produces a surface that exists for one task and one user and is discarded after.

## The 2026 Playbook: Layer, Don't Pick

The single most important framing the Design organization should adopt this year: the three patterns are not alternatives. They answer different questions about different surfaces of the same product. A mature 2026 deployment uses Pattern 1 for the predictable core (the surfaces that ship in every release, that customers expect to look the same way every time, that compliance and accessibility teams sign off on), Pattern 2 for cross-app and cross-vendor workflows (where portability is the design goal and the protocol is the contract), and Pattern 3 for the exploratory edge (the long-tail tasks, the research workflows, the one-off configurations that don't justify a designed surface).

Picking one pattern as "the Generative UI strategy" is almost always wrong. Pattern 1 alone leaves the long-tail unaddressed. Pattern 3 alone leaves the predictable core under-designed and risks accessibility regression at scale. Pattern 2 alone is portable but offers nothing that pure server-rendered components don't already offer if you don't have the cross-app problem. The 2026 default is layered.

The corollary: the Design organization's planning unit is not "which Gen-UI vendor do we choose," it is "for each surface in our product, which of the three patterns fits and what component vocabulary do all three emit toward."

## shadcn/ui as De Facto Substrate

shadcn/ui CLI v4 (March 2026, MIT-licensed) is becoming the AI-native component vocabulary in 2026. Four properties drove the convergence: components are composable rather than monolithic (the agent can recombine pieces); components are AI-readable (the source is in the repo, not behind a build wall, and LLMs can reason about it directly); the distribution model is copy-paste rather than imported (the agent or developer takes ownership of the components, no upgrade contract to honor); and the v4 CLI made adoption a single command. Together those properties mean that when an agent in Pattern 1 selects components, when an agent in Pattern 2 declares components, or when an LLM in Pattern 3 generates components, the output increasingly converges on shadcn-shaped primitives.

This matters for Design organizations in a practical way: the component vocabulary the team curates is no longer an internal-only artifact. It is the substrate the agents emit toward. A design system maintained in shadcn shape — with composition primitives, accessible defaults, and a token system the agent can read — directly improves the quality of Pattern 1 selection, Pattern 2 declaration, and Pattern 3 generation. A design system that is closed, monolithic, or build-time-only does the opposite.

The "becoming the substrate" framing should be read as a trajectory, not a finished state. shadcn is not the only vocabulary in production use, and large enterprises with prior investments in Material, Carbon, or proprietary systems are not abandoning them. But the direction of pull through Q2 2026 is consistent enough that new design-system work in product organizations that have not yet picked a vocabulary should default to shadcn-shape unless there is a specific reason not to.

## Implementation Guidance

This is practical posture by maturity stage, not a step-by-step recipe.

**Early adoption (one surface, one pattern)**: pick the single surface in the product where Generative UI is most defensibly useful (an embedded copilot, a configurator, a research tool), pick the pattern that fits that surface (Pattern 1 for embedded copilots; Pattern 3 for research; Pattern 2 only if the cross-app problem is real today), and ship. Do not pre-plan the other two patterns. Learn what the failure modes feel like before extending.

**Maturity (two patterns layered)**: most product organizations land here in 2026. Pattern 1 covers the in-product copilot or assistant; Pattern 3 covers a research, analytics, or admin surface where exploratory output is the point. The Design organization invests in the shadcn-shaped vocabulary that both patterns draw from. Accessibility and brand QA is treated as a runtime concern, not a build-time one.

**Full-stack (three patterns at appropriate surfaces)**: enterprises and platform-shaped products. Pattern 1 in the core product. Pattern 2 in the agent-to-third-party-app workflows where portability is the explicit goal. Pattern 3 in the exploratory and long-tail surfaces. The Design organization at this stage is doing meta-design: designing the vocabulary, the protocols, and the runtime guardrails rather than the individual screens.

The mistake to avoid at every stage: treating "Generative UI" as a feature to ship rather than a runtime substrate that changes how surfaces are produced. The feature framing leads to a single AI-generated screen that nobody knows where to put. The substrate framing leads to a vocabulary, three patterns, and a posture.

## Accessibility in Generative UI

Generated UI must still meet WCAG 2.2 — the standard does not care whether the button was designed in Figma in February or synthesized by an LLM in May. The accessibility risk in Generative UI is regression at scale: a single designed button gets reviewed once and shipped; a million generated buttons across a million sessions might each individually fail keyboard navigation, contrast, or semantic-role assignment.

The load-bearing accessibility work in a Generative UI deployment is at three places. First, the component vocabulary itself must be accessible — shadcn primitives have reasonable defaults, but any custom additions to the vocabulary need accessibility review at the vocabulary level, because they will be emitted thousands of times. Second, Pattern 1 controlled mode benefits most directly from this because the agent can only emit what the vocabulary allows; accessibility certification of the vocabulary is roughly equivalent to certification of the output. Third, Pattern 3 open-ended mode needs runtime accessibility checks (semantic role validation, contrast verification, focus order assertion) because the model can generate components that have never been certified — without runtime checks, accessibility becomes probabilistic.

Detailed accessibility audit methodology is the territory of the sibling pack `accessibility-audit.md`. That pack defines the WCAG 2.2 audit posture, the test toolchain, and the certification cadence. The Generative UI pack defers to it on those concerns and stays on the question of how the three patterns each create distinct accessibility risk profiles. The cross-reference is load-bearing — a Gen-UI deployment without an accessibility-audit posture is exposed.

## Anti-Patterns / Common Failures

**Treating Gen-UI as a feature instead of as substrate.** The team builds "the AI-generated screen" as a discrete product feature, ships it, and nobody knows what to do with it. The right framing is that Generative UI is a runtime capability that changes how many surfaces are produced, not one more surface.

**Picking one pattern when layering would work.** "We're going to use AG-UI" or "We're going to use MCP Apps" — singular. The team commits to one vendor's pattern, then discovers six months in that the other two patterns address surfaces this one can't. The 2026 default is layered; commit to a pattern per surface, not to a pattern for the product.

**Ignoring accessibility in generated output.** Generated buttons must still be keyboard-navigable. Generated forms must still have semantic labels. The output not having been designed by a human does not exempt it from WCAG 2.2. Without runtime accessibility validation in Pattern 3 deployments, this regresses quickly and quietly.

**Over-relying on Pattern 3 for predictable workflows.** The team uses open-ended LLM generation for a workflow that ships in every release and that customers do the same way every time. Output drifts session-over-session, support tickets cite "the screen looks different now," and the team retrofits Pattern 1 controls over the top. Predictable surfaces want controlled patterns.

**Under-investing in the component vocabulary.** The team adopts Generative UI without first investing in a shadcn-shaped, accessible, AI-readable design system. All three patterns then emit toward inconsistent vocabularies, the output looks incoherent across surfaces, and Design ends up doing pixel-level QA on agent output. The vocabulary is the leverage point; if the vocabulary is weak, no pattern saves it.

**Treating the three patterns as competing vendor pitches.** Marketing materials from each vendor naturally position their pattern as "the" Generative UI approach. Reading them in isolation produces vendor capture; reading them together produces the layering insight. The patterns are complementary in 2026, regardless of how the vendors frame them.

## 2026-06 Delta Update (as of 2026-06-06)

**MCP Apps status resolved — the Pattern 3 open question is closed.** The MCP spec Release Candidate (announced 2026-05-21, final dated 2026-07-28) settled the open status this pack previously assigned to MCP Apps:

- **MCP Apps (SEP-1865) is ratified as an official MCP EXTENSION, `ext-apps`** — a reverse-DNS extension ID, negotiated via an `extensions` capability map. It exposes sandboxed-iframe interactive HTML UIs through `ui://` resources declared ahead of time, and lives in its own `ext-apps` repo. It is explicitly **NOT folded into MCP core**.
- **MCP core went stateless** in the same Release Candidate — the handshake and session headers were eliminated.
- The May "three-horse race" framing (A2UI / AG-UI / MCP Apps) still holds across the three patterns. What changed is only that the MCP-Apps leg now has definite ratified-extension status rather than the "MCP spec extension, 2026 (status open)" framing this pack carried.

**Design-tool-commits-PRs trajectory — design→code is collapsing into one agentic loop.** Two May 2026 product moves point the same direction (see also the sibling `design-dev-handoff.md` delta, which owns the handoff-practice implication):

- **Figma Make (closed beta, 2026-05-28)** connects to your local codebase, lets you prompt contextually on elements, and has an AI coding agent commit changes / open a PR (via Figma MCP) against your real design system.
- **Vercel v0 (~2026-05-13)** was repositioned in Vercel's own docs from "shadcn/ui component generator" to "an AI agent for creating real code, full-stack apps, and agents." AI Elements added Voice & Code components (2026-05-11).

For this pack, the v0 repositioning reinforces the shadcn-as-substrate framing (§"shadcn/ui as De Facto Substrate"): the tool that popularized shadcn-shape generation is now an agent that emits real full-stack code, not just components.

**Sources (2026-06 delta)**:
- https://github.com/modelcontextprotocol/ext-apps/
- https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/
- https://github.com/modelcontextprotocol/modelcontextprotocol/pull/1865
- https://www.figma.com/release-notes/
- https://vercel.com/blog/working-with-figma-and-custom-design-systems-in-v0

## 2026-06-24 Delta Update (Vercel AI SDK 6 + AI Elements)

**Adapted from**: Vercel AI SDK 6 (vercel.com/blog/ai-sdk-6; ai-sdk.dev) + AI Elements (elements.ai-sdk.dev; vercel.com/changelog/introducing-ai-elements; github.com/vercel/ai-elements).
**Source licence**: Apache-2.0 (AI SDK) / open-source component registry (AI Elements, built on shadcn/ui).
**V2V refinements**: scoped this pack to the UI/streaming surface; framed AI Elements as the shadcn-registry-distributed streaming layer; no fabricated adoption metrics.

The generative-UI surface for the AI SDK 6 era (the UI/streaming layer):

- **AI Elements** (`elements.ai-sdk.dev`) — an open-source, headless-first component library + custom registry **built on top of shadcn/ui** for AI-native React apps, distributed via the shadcn registry (copy-in, composable). It is the now-shipped product name for what earlier notes called "Vercel AI SDK UI Elements." Prebuilt streaming components wire to `useChat`/`streamText`/`streamObject`: token-streaming text, structured-object rendering via `useObject`, tool-call views, and agent-run views.
- **Boundary (load-bearing):** frontend/generative-UI owns the **UI/streaming surface** (AI Elements, `useChat`-style components). Backend agent-loop mechanics remain outside this pack.
- **Convergence note:** v0.app + AI Elements + shadcn are converging on one foundation (shadcn registry as the distribution mechanism); the existing v0/shadcn coverage stands, this just names the shipped AI Elements layer on top of it.

## V2V Cross-References

**Sibling Q2-8 packs**:
- **`ai-research-synthesis.md` (Q2-8.2)** — UX research practice in an AI-native workflow. Pairs with Generative UI for the research-surface use case (Pattern 3 exploratory tools that AI research synthesis informs and consumes); the voice-flattening risk from that pack applies to Pattern 3 outputs that surface synthesized findings.
- `accessibility-audit.md` — accessibility methodology that applies to all three patterns; **load-bearing cross-reference for Pattern 3 deployments** per §"Accessibility in Generative UI" above. The runtime accessibility validation that Pattern 3 requires is operationalized through that pack's audit posture.

**Sibling Q2-5 packs**:
- **`mcp-architecture.md` (Q2-5.1)** — MCP transport layer underlying MCP Apps (Pattern 3 protocol path). When the LLM generates UI via MCP Apps, the transport variants, capability negotiation, and the three primitives (resources, tools, prompts) from that pack are the carrier. Note (2026-06 delta): MCP core went stateless in the Release Candidate (handshake + session headers eliminated), and MCP Apps now lives as the ratified `ext-apps` extension negotiated via the `extensions` capability map — the transport carrier framing still holds, but the capability negotiation path is now extension-scoped.
- **`a2a-architecture.md` (Q2-5.2)** — when generative UI is invoked across agent boundaries (one agent renders UI on behalf of another), A2A artifacts can carry the declarative UI description (Pattern 2 declarative pattern over A2A wire).
- **`agentic-security.md` (Q2-5.3)** — Pattern 3 open-ended LLM generation creates a novel attack surface (LLM01 prompt-injection-via-rendered-component); runtime-generated UI inherits that pack's threat model.

**Sibling Q2-3 packs**:
- **`agent-identity.md` (Q2-3.1)** — when generative UI invokes tools on behalf of a user, the identity binding for those tool calls per that pack's Pattern 1 (capability-token forwarding with narrowing) governs what the rendered UI can do.
- **`mcp-governance.md` (Q2-3.2)** — MCP Apps (Pattern 3) inherit MCP-server governance posture; registry, approval workflow, and audit-trail standards apply.

**Sibling Q2-6 packs**:
- **`llm-seo.md` (Q2-6.3)** — when product surfaces are runtime-generated, the AI-citation discipline applies inside the product surface (LLMs that render content within Pattern 2 / Pattern 3 surfaces consume the same citation hierarchy as external AI search engines).

**Existing packs**:
- `design-systems.md` — vocabulary curation guidance; this Gen-UI pack extends it with the AI-native shadcn substrate framing.
- `ui-patterns.md` — pattern-level guidance for non-Generative surfaces; complement to this pack.
- `design-dev-handoff.md` — handoff posture changes when surfaces are runtime-generated rather than build-time-designed; this Gen-UI pack flags the implication, design-dev-handoff owns the practice change.

**Sensitive-skill applicability**: NOT sensitive. Technical design reference; no legal/HR/compliance output. Standard ROI framing applies.

## Sensitive-skill applicability

NOT sensitive. This is a technical and design reference pack. It does not produce legal, HR, compliance, or regulated output. Output is design guidance for product organizations adopting Generative UI capabilities. Standard knowledge-pack treatment — no Findings / Reviewer Checklist / Cannot Assess Without scaffolding required.

## Operating Principle

> *Generative UI in 2026 is not a feature to ship — it is a runtime substrate that changes how surfaces are produced. The decision is not whether to adopt it; it is how to layer the three patterns across the surfaces of the product, and what component vocabulary all three emit toward.*
