---
name: agent-runtime-patterns
owner: ai-architect
consumers: [ai-architect]
sensitive: false
---

<!-- TIER: Tier-2 CONDITIONAL knowledge pack — NOT preloaded. Read on trigger only.
     Kept out of `ai-architect` Tier-1 (already 27,247 tokens, over the 20k nominal cap per
     agent-metadata-schema.md D14). This pack must not be added to preload_knowledge_packs. -->

# Agent Runtime Patterns — Memory Architecture & Framework Selection

**Adapted from**:
- LangGraph (github.com/langchain-ai/langgraph) — stateful graph orchestration, checkpointer/persistence model
- CrewAI (github.com/crewAIInc/crewAI) — role-based crew orchestration
- Microsoft AutoGen (github.com/microsoft/autogen) — conversable multi-agent runtime
- OpenAI Agents SDK (github.com/openai/openai-agents-python; openai.github.io/openai-agents-python) — lightweight agents + handoffs
- MetaGPT (github.com/geekan/MetaGPT) — SOP-encoded software-company multi-agent
- MemGPT / Letta (research + github.com/letta-ai/letta) — hierarchical/OS-style agent memory paging

**Source licence**: LangGraph (MIT), CrewAI (MIT), AutoGen (MIT/CC-BY per-repo-terms), OpenAI Agents SDK (MIT), MetaGPT (MIT), Letta/MemGPT (Apache-2.0). Framework capabilities described qualitatively; verify current version specifics against each repo (capabilities noted as of 2026).

**V2V refinements**:
- Added the **agent long-term memory decision guide** (episodic vs semantic, checkpointer scoping, compaction ladder, memory-read-vs-RAG boundary, write/eviction policy) — the existing `ai-ml-patterns.md` has zero memory content.
- Added the **multi-agent framework selection axes** (control vs autonomy, topology, statefulness/checkpointing, human-in-loop, maturity/lock-in) mapping abstract patterns to production frameworks.
- Cross-referenced into `ai-ml-patterns.md` (`### Agent Orchestration Patterns`) rather than duplicating its pattern taxonomy; deferred wire-level agent-to-agent protocol detail to `a2a-architecture.md`.

> **Scope note.** This pack sits *on top of* `ai-ml-patterns.md → ### Agent Orchestration Patterns`, which already defines the abstract patterns (ReAct, Plan-and-Execute, Supervisor, Consensus, Debate, Assembly Line, Parallel Fan-Out). Read that section first for the *what*; read this for *how to persist agent state over time* and *which framework to build on*. For the wire-level agent-to-agent / A2A protocol, see `a2a-architecture.md` — not repeated here.

---

## 1. Agent Long-Term Memory Architecture

An agent's "memory" is not one thing. Conflating the kinds is the most common design error: teams bolt a vector store onto a chat loop, call it memory, and then wonder why the agent forgets commitments, re-derives facts, and bloats context. Separate the concerns first.

### 1.1 Two axes: what kind, and how long

**Kind (borrowed from cognitive science):**
- **Episodic memory** — the record of *what happened*: prior turns, tool calls and their results, decisions taken, events in order. Time-stamped, append-mostly. Answers "what did we do / say / decide?"
- **Semantic memory** — distilled *facts and preferences* independent of when they were learned: "the user prefers metric units," "customer X is on the enterprise plan," "the API base URL is Y." Answers "what is true?"
- (**Procedural memory** — learned *how-to* / updated instructions the agent applies. Least common in practice; usually collapses into the system prompt or a skills registry.)

Episodic is a *log you retrieve slices of*; semantic is a *store you upsert into and read the current value from*. They have different write policies and different staleness behavior (below).

**Duration / scope:**
- **Thread-scoped (short-term)** — state that lives for one conversation/run. Backed by a **checkpointer** (LangGraph's term) or run/session state. Contains the working context: message history, scratchpad, intermediate tool outputs. Dies (or is archived) when the thread ends.
- **Long-term / cross-session** — state that outlives any single thread, keyed by user/org/entity rather than thread id. This is where durable semantic facts and reusable episodic summaries live.

The decision that trips people up: **thread-scoped ≠ short-lived-only.** A checkpointer persists a thread durably (you can resume it days later, replay it, fork it for human-in-the-loop). "Thread-scoped" is about *keying*, not *lifetime*. Long-term memory is a *different key space* (user/entity), not merely "the same store but bigger."

### 1.2 Persistence: checkpointer vs memory store

| Concern | Checkpointer (thread state) | Long-term memory store |
|---|---|---|
| Keyed by | thread/run id | user / org / entity id |
| Holds | full working state (messages, scratchpad, pending tool calls) | distilled facts, preferences, episodic summaries |
| Read pattern | load the whole checkpoint to resume/replay/fork | query/retrieve the relevant slice |
| Write pattern | snapshot after each step (enables replay, time-travel, HIL pause/resume) | deliberate upsert under a write policy (§1.4) |
| Lifetime | one thread (resumable, forkable) | indefinite, spans threads |
| Typical backing | SQLite/Postgres/Redis checkpoint | vector store, KV store, or relational rows |

Design rule: use a **checkpointer** to get durability, resumability, and human-in-the-loop pause/resume *for the current thread*; use a **separate long-term store** for anything a *future* thread must see. Don't try to make one serve both — the read patterns (load-whole vs retrieve-slice) are incompatible.

### 1.3 Compaction: keeping the working context bounded

Thread state grows unboundedly; the context window does not. Choose a compaction strategy by how much of the *literal* history the task needs:

- **Buffer (window) — keep the last N turns verbatim, drop the rest.** Cheapest, lossy, no LLM cost. Use when only recent context matters (support chat, simple task loops). Fails when an early commitment must survive.
- **Running summary — maintain one rolling summary; fold each turn into it.** Bounded size, one extra LLM call per compaction. Use for long single-threaded conversations where the *gist* matters more than exact wording. Risk: silent drift and loss of specifics (numbers, names) as they get summarized away — pin critical facts to semantic memory (§1.1) rather than trusting the summary.
- **Hierarchical — buffer of recent turns + running mid-level summaries + a stable long-term summary (and/or paging older detail out to a store you can recall on demand).** The MemGPT/Letta "OS-style paging" shape: hot context in-window, warm summaries a tier down, cold detail retrievable. Most expensive to build; the right answer when both recency *and* recall of old specifics matter (long-running assistants, multi-day agents).

Practical default: **buffer + pinned semantic facts** for most agents; escalate to running-summary when threads routinely exceed the window; reach for hierarchical only when you have a genuine long-horizon agent.

### 1.4 Memory read vs RAG — when a read is retrieval, when it's just RAG

This distinction is muddy in most codebases and worth making sharp:

- It's a **first-class memory read** when the agent looks up state it (or the system) *deliberately wrote about this specific user/entity/thread* — "what did the user tell me their name was," "what did we decide last session," "what's this customer's plan." The store is *authored by the agent's own operation*; the read is keyed and often exact (KV/relational), or a semantic lookup over a *small, self-written* corpus.
- It's **RAG** when the agent retrieves from a *large corpus it did not author* to ground a generation — docs, knowledge base, product catalog. The point is grounding against external knowledge, not recalling the agent's own history.

Why it matters: they have different failure modes and different write ownership. Memory reads fail by *staleness and wrong-key* (you read an outdated preference); RAG fails by *retrieval quality* (wrong chunks, poor reranking — see `ai-ml-patterns.md` RAG section). Memory is write-owned by the agent under a policy (§1.4); RAG corpora are owned by an ingestion pipeline. When "memory" is really RAG over a self-written store, apply RAG hygiene (chunking, reranking) to it; when it's a keyed fact, don't vector-search it — read it by key.

### 1.5 Write policy: what to persist, and eviction

Memory quality is governed by *what you choose to write*, far more than by the store. Undisciplined writes are the real failure mode — an agent that persists everything ends up retrieving noise.

- **What to persist (semantic):** durable, reusable facts and preferences; decisions with future consequence; entity attributes. *Not* every utterance. A cheap heuristic: persist a fact only if a *future* thread would be wrong without it.
- **What to persist (episodic):** summaries of completed sub-tasks and decisions, not raw turn logs. Keep raw logs in the checkpointer (thread-scoped) and promote only distilled episodes to long-term.
- **Staleness / eviction:** semantic facts can be *superseded* (user changed their preference) — model this as **upsert-by-key with last-write-wins**, not append, so a read never returns a stale value alongside the fresh one. For episodic summaries, use **recency + relevance decay** (or explicit TTL) so old, unreferenced episodes age out of retrieval. Flag conflicting writes (two different values for the same key close in time) rather than silently overwriting when the stakes are high.
- **Confidence & provenance:** tag written facts with source (user-stated vs inferred) and let inferred facts be overridden by stated ones. This prevents an agent's guess from ossifying into "truth."

**Decision guide (one line):** *Thread state → checkpointer. Durable facts → semantic store, upsert-by-key. Reusable history → episodic summaries with decay. Large external knowledge → RAG, not memory.*

---

## 2. Multi-Agent Framework Selection

The abstract orchestration patterns live in `ai-ml-patterns.md → ### Agent Orchestration Patterns` (Supervisor, Consensus, Debate, Assembly Line, Parallel Fan-Out, plus ReAct and Plan-and-Execute). This section answers the next question: **which production framework do you build those patterns on?** Don't re-derive the pattern taxonomy here — pick the runtime that expresses your chosen pattern with the least friction.

### 2.1 The selection axes

Score a framework on these axes against your workload, not on GitHub stars:

1. **Control / determinism vs autonomy.** Do you need an explicit, auditable flow (edges you drew) or do you want agents to figure out the path? High-control favors graphs; high-autonomy favors conversational/role runtimes.
2. **Topology: graph vs conversation vs role-based.** *Graph* = nodes+edges you define (deterministic control flow, branching, loops). *Conversation* = agents exchange messages until a stop condition (emergent flow). *Role-based / crew* = you define roles + tasks and the framework sequences them.
3. **Statefulness & checkpointing.** Does the runtime persist state natively (resume, replay, time-travel, human-in-the-loop pause), or is state your problem to bolt on? This is the axis most correlated with production-readiness for long or interruptible workflows (ties directly to §1.2).
4. **Human-in-the-loop support.** First-class interrupt/approve/resume, or DIY? Matters for any workflow with an approval gate.
5. **Maturity / lock-in / ecosystem.** How much of your architecture becomes coupled to the framework's abstractions, and how painful is exit? Lightweight libraries lock you in less than opinionated end-to-end frameworks.

### 2.2 Framework map (qualitative, as of 2026)

| Framework | Topology | Determinism | Native state / checkpointing | Human-in-loop | Best fit / trade |
|---|---|---|---|---|---|
| **LangGraph** | Graph (nodes + edges) | **High** — you draw the control flow | **Strong** — built-in checkpointer, resume/replay/time-travel, thread persistence | First-class (interrupt/resume) | Auditable, stateful, branching/looping workflows where control and durability matter. Trade: more upfront wiring; graph abstraction to learn. |
| **CrewAI** | Role-based crew (roles + tasks; sequential or hierarchical process) | Medium | Lighter; add your own for durable long-term state | Supported, less central | Fast to stand up a "team of roles" for a bounded task. Trade: less explicit control than a graph; state/persistence is more your responsibility. |
| **AutoGen** (Microsoft) | Conversation (conversable agents exchanging messages) | Lower — flow emerges from dialogue | Conversation state; durable persistence is your design | Supported (human proxy agent) | Research-y, flexible multi-agent conversations, group chat, code-writing loops. Trade: emergent flow is harder to make deterministic/auditable. |
| **OpenAI Agents SDK** | Lightweight agents + **handoffs** + guardrails | Medium (explicit handoffs, otherwise agent-driven) | Minimal/lightweight by design; sessions for short-term | Guardrails + tracing; HIL is DIY-ish | Small, clean primitive set; low lock-in; good when you want thin orchestration close to the model API. Trade: fewer batteries (durable state, complex graphs) included. |
| **MetaGPT** | Role-based with **encoded SOPs** (software-company metaphor) | Medium-high *within its SOP* | Workflow-scoped | Limited | Opinionated, strong for its target domain (multi-agent software generation) where the SOP fits. Trade: high conceptual lock-in; bends other domains to its metaphor. |

### 2.3 Choose-between decision aid

```
Need explicit, auditable control flow + durable resumable state (approvals, long/interruptible runs)?
    → LangGraph  (graph + checkpointer; ties to §1.2 persistence)

Want a "team of named roles" to knock out a bounded task, fast, minimal wiring?
    → CrewAI

Exploring emergent multi-agent conversation / group-chat / code-gen loops, control-flow rigor secondary?
    → AutoGen

Want the thinnest orchestration primitive, low lock-in, hug the model API, add your own state?
    → OpenAI Agents SDK  (agents + handoffs + guardrails)

Target is multi-agent software generation and the SOP metaphor genuinely fits?
    → MetaGPT

Cross-cutting rules:
  - The more your workflow needs determinism + durability → move up the "graph + native checkpointing" axis.
  - The more it's exploratory / conversational → conversation runtimes are fine, but plan your own persistence.
  - Weigh lock-in explicitly: opinionated end-to-end frameworks (MetaGPT, to a lesser degree CrewAI) couple your
    architecture to their abstractions; lightweight SDKs (OpenAI Agents SDK) keep exit cheap.
  - Statefulness is not free: if the framework doesn't persist it, YOU own §1 memory architecture end-to-end.
```

> **Boundary reminders.** This section selects a *runtime*; it does not restate the pattern taxonomy (see `ai-ml-patterns.md`) and it does not cover the *wire protocol* by which heterogeneous agents talk across a boundary — for agent-to-agent / A2A protocol design, MCP tool-calling, and interop, defer to `a2a-architecture.md` and `mcp-architecture.md`. Pick the pattern (ai-ml-patterns) → pick the framework (here) → design cross-agent protocol (a2a-architecture) → design memory (§1 here).
