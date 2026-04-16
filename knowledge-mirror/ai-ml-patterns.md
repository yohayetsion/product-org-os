# AI/ML Architecture — Frameworks & Methods

<!-- Attribution:
  LLM patterns section informed by:
  - Anthropic best practices — RAG patterns, agent orchestration, prompt engineering, context window management
  - RAGAS (github.com/explodinggradients/ragas) — RAG evaluation methodology
  - DeepEval (github.com/confident-ai/deepeval) — LLM evaluation framework
  Adapted and expanded for Product Org OS agents.
-->

## Overview

AI/ML architecture is the discipline of designing systems where probabilistic models operate within deterministic product requirements. The core challenge is not building AI — it is building AI that is reliable, cost-effective, measurable, and safe enough for production use.

This reference covers the practical patterns for integrating AI into products, with emphasis on LLM-based systems (RAG, agents, function calling) that dominate current product development. The patterns are organized from simplest to most complex. Start simple and escalate only when measurement proves the simpler approach insufficient.

AI architecture differs from traditional software architecture in one fundamental way: the output is probabilistic. Every pattern in this document addresses that reality through evaluation, guardrails, fallbacks, and cost management.

---

## Frameworks

### RAG Architecture Patterns

**When to use**: When AI needs to answer questions or generate content based on your organization's specific data, documents, or knowledge base.

**Three RAG Tiers**:

| Tier | Description | Complexity | Quality | Cost |
|------|-------------|-----------|---------|------|
| **Naive RAG** | Embed, retrieve top-k, generate | Low | Baseline | Low |
| **Advanced RAG** | Optimized chunking, hybrid search, reranking | Medium | +30-50% over naive | Medium |
| **Agentic RAG** | Query planning, multi-step retrieval, self-correction | High | +20-30% over advanced | High |

**Naive RAG Template**:
```
1. INGEST
   Documents → Chunking → Embedding → Vector Store

2. RETRIEVE
   User Query → Embed Query → Vector Search (top-k) → Relevant Chunks

3. GENERATE
   System Prompt + Retrieved Chunks + User Query → LLM → Response
```

**Advanced RAG Template**:
```
1. INGEST (enhanced)
   Documents → Smart Chunking (semantic boundaries, overlap)
   → Embedding (domain-tuned model)
   → Vector Store + Keyword Index (hybrid)
   → Metadata extraction (source, date, type)

2. RETRIEVE (enhanced)
   User Query → Query Expansion/Rewriting
   → Hybrid Search (semantic + keyword)
   → Reranking (cross-encoder)
   → Contextual Compression (remove noise)
   → Top-k relevant, deduplicated chunks

3. GENERATE (enhanced)
   System Prompt + Retrieved Chunks + User Query
   → LLM with citation instructions
   → Response with source references
   → Faithfulness check (optional)
```

**Agentic RAG Template**:
```
1. PLAN
   User Query → Query Analyzer
   → Determine if single or multi-step retrieval needed
   → Generate sub-queries for complex questions

2. RETRIEVE (iterative)
   For each sub-query:
     → Route to appropriate data source
     → Retrieve and evaluate relevance
     → If insufficient: reformulate query and retry

3. SYNTHESIZE
   All retrieved context → LLM synthesis
   → Self-evaluation of answer completeness
   → If incomplete: generate follow-up retrieval
   → Final response with citations and confidence

4. VERIFY
   Response → Fact-check against sources
   → Flag unsupported claims
   → Present with confidence indicators
```

**Chunking Strategy Decision**:

| Strategy | When to Use | Chunk Size |
|----------|-------------|-----------|
| Fixed-size | Simple documents, uniform structure | 500-1000 tokens with 100-200 overlap |
| Semantic | Documents with clear section boundaries | By paragraph or section headers |
| Recursive | Mixed content types | Split by headers, then paragraphs, then sentences |
| Document-level | Short documents (emails, tickets) | Entire document as one chunk |

**Limitations**: RAG quality is bounded by retrieval quality. If the right chunks are not retrieved, the LLM cannot produce the right answer. Invest more in retrieval optimization (hybrid search, reranking) than in prompt engineering.

---

### LLM Integration Patterns

**When to use**: When integrating LLM capabilities into product features.

**Pattern Catalog**:

| Pattern | Description | Use When | Complexity |
|---------|-------------|----------|-----------|
| **Single Prompt** | One call, one response | Simple generation, classification | Low |
| **Chain of Thought** | Prompt instructs step-by-step reasoning | Complex reasoning, math, logic | Low |
| **Function Calling** | LLM invokes defined functions with structured args | Structured data extraction, API actions | Medium |
| **Sequential Chain** | Output of one LLM call feeds into the next | Multi-step processing pipelines | Medium |
| **Router** | LLM or classifier routes to specialized prompts | Multi-domain queries, varied response types | Medium |
| **Agent Loop** | LLM iteratively plans, acts, observes, decides | Complex tasks requiring multiple tools | High |

**Function Calling Template**:
```json
{
  "tools": [
    {
      "type": "function",
      "function": {
        "name": "search_knowledge_base",
        "description": "Search the product knowledge base for information",
        "parameters": {
          "type": "object",
          "properties": {
            "query": {
              "type": "string",
              "description": "Search query"
            },
            "category": {
              "type": "string",
              "enum": ["product", "billing", "technical"],
              "description": "Category to filter results"
            }
          },
          "required": ["query"]
        }
      }
    }
  ]
}
```

**Agent Loop Template**:
```
While (task not complete AND iterations < max_iterations):
  1. OBSERVE: Current state, available information
  2. THINK: Analyze what is known, what is needed
  3. PLAN: Select next action from available tools
  4. ACT: Execute the selected tool/function
  5. EVALUATE: Did the action produce useful results?
  6. DECIDE: Continue, escalate to human, or complete

Guardrails:
  - Max iterations: [5-10 depending on complexity]
  - Token budget: [max tokens per loop]
  - Timeout: [max wall-clock time]
  - Escalation: If stuck for 2+ iterations, request human input
```

**Limitations**: Agent loops are powerful but expensive and unpredictable. Every iteration costs tokens. Set strict iteration limits, token budgets, and timeout constraints. Log every step for debugging.

---

### Embedding Strategy & Vector DB Selection

**When to use**: When building any semantic search, RAG, or recommendation system.

**Embedding Model Selection**:

| Model Type | Examples | Dimensions | Best For |
|-----------|---------|-----------|----------|
| **General-purpose** | text-embedding-3-small, all-MiniLM-L6 | 384-1536 | Default starting point |
| **Large general** | text-embedding-3-large, BGE-large | 1024-3072 | Higher accuracy, higher cost |
| **Domain-specific** | Fine-tuned on your data | Variable | Best accuracy for your domain |
| **Multilingual** | multilingual-e5-large, Cohere multilingual | 768-1024 | Multi-language content |

**Vector Database Selection**:

| Database | Type | Best For | Scaling |
|----------|------|---------|---------|
| **Pinecone** | Managed | Quick start, serverless option | Automatic |
| **Weaviate** | Open source / managed | Hybrid search (vector + keyword) | Horizontal |
| **Qdrant** | Open source / managed | High performance, filtering | Horizontal |
| **pgvector** | PostgreSQL extension | Existing Postgres, small-medium scale | Vertical |
| **Chroma** | Open source | Prototyping, small datasets | Limited |

**Selection Decision**:
```
< 100K vectors AND already using Postgres → pgvector
< 1M vectors AND need hybrid search → Weaviate or Qdrant
Any scale AND want zero ops → Pinecone
Need maximum control AND have ops capacity → Qdrant self-hosted
Prototyping → Chroma
```

**Limitations**: Embedding quality degrades for out-of-domain content. If your domain has specialized vocabulary (legal, medical, scientific), evaluate embedding quality on your actual data before selecting a model. General-purpose models may require domain fine-tuning.

---

### Model Evaluation Frameworks

**When to use**: Before launching any AI feature, and continuously after launch.

**Evaluation Dimensions**:

| Dimension | What It Measures | Metrics |
|-----------|-----------------|---------|
| **Accuracy** | Correctness of output | Precision, recall, F1, exact match |
| **Relevance** | How well output addresses the query | NDCG, MRR (retrieval); human relevance rating |
| **Faithfulness** | Whether output is grounded in provided context | Hallucination rate, citation accuracy |
| **Helpfulness** | Whether output actually helps the user | Task completion rate, user satisfaction |
| **Safety** | Whether output avoids harmful content | Toxicity rate, PII leakage rate, refusal accuracy |
| **Latency** | Response time | P50, P95, P99 response times |
| **Cost** | Cost per query | Average tokens per query, cost per 1K queries |

**Evaluation Pipeline Template**:
```
1. GOLDEN DATASET
   - 100-500 curated question/answer pairs
   - Covers common, edge, and adversarial cases
   - Updated quarterly with new patterns

2. AUTOMATED EVALUATION (runs on every deployment)
   - Retrieval quality: relevance of retrieved chunks
   - Generation quality: LLM-as-judge scoring
   - Safety: adversarial prompt test suite
   - Performance: latency and token usage

3. HUMAN EVALUATION (runs weekly/monthly)
   - Sample of production queries reviewed by domain experts
   - Scoring: accuracy (1-5), helpfulness (1-5), safety (pass/fail)
   - Feedback loop to improve golden dataset

4. PRODUCTION MONITORING (continuous)
   - User feedback signals (thumbs up/down, regenerate clicks)
   - Error rate and fallback trigger rate
   - Cost per query trends
   - Drift detection (quality degradation over time)
```

**Limitations**: LLM-as-judge evaluation has known biases (preference for longer, more verbose responses). Use it as a signal, not a ground truth. Human evaluation is expensive but necessary for high-stakes applications.

---

### Prompt Engineering Patterns

**When to use**: For every LLM integration. Prompt design is the primary lever for output quality.

**Pattern Library**:

| Pattern | Description | Template |
|---------|-------------|----------|
| **System-User-Assistant** | Standard role-based prompting | System: role + rules; User: query; Assistant: response |
| **Few-Shot** | Provide examples of desired output | System + 2-5 example pairs + user query |
| **Chain of Thought** | Instruct step-by-step reasoning | "Think through this step by step: 1. ... 2. ..." |
| **Output Formatting** | Constrain output shape | "Respond in JSON with these fields: ..." |
| **Guardrail Instructions** | Prevent unwanted behavior | "If unsure, say 'I don't know.' Never make up facts." |
| **Persona** | Assign expertise | "You are a senior [domain] expert with 15 years experience." |

**Prompt Template Structure**:
```
SYSTEM PROMPT:
  [Role/Persona] You are a [specific expert].
  [Context] You have access to [specific knowledge].
  [Instructions] When answering:
    1. [Specific rule]
    2. [Specific rule]
    3. [Specific rule]
  [Format] Respond in [specific format].
  [Guardrails] If you cannot answer, say "[specific fallback]".
  [Examples] (optional few-shot examples)

USER PROMPT:
  [Context from RAG or user data]
  [User's actual question]
```

**Limitations**: Prompt engineering has diminishing returns. After optimizing the prompt, the next quality improvement usually comes from better retrieval (RAG), fine-tuning, or a more capable model — not from more prompt tweaking.

---

### Fine-Tuning vs. RAG vs. Prompt Engineering Decision Tree

**When to use**: When deciding how to give an LLM access to specific knowledge or behavior.

**Decision Framework**:

```
Do you need the LLM to use specific knowledge?
  ├── YES → Is the knowledge static or slowly changing?
  │     ├── STATIC (changes quarterly or less) → Consider fine-tuning
  │     └── DYNAMIC (changes daily/weekly) → Use RAG
  └── NO → Do you need specific output format or behavior?
        ├── YES → Prompt engineering (try first)
        │     └── Not sufficient? → Fine-tuning for behavior
        └── NO → Use the model as-is

For knowledge integration:
  1. TRY: Prompt engineering with context injection
  2. THEN: RAG (if context is too large for prompt or changes frequently)
  3. THEN: Fine-tuning (if RAG quality is insufficient for narrow domain)
  4. LAST: Custom training (only if no existing model handles the task)
```

**Comparison**:

| Approach | Knowledge Freshness | Cost to Build | Cost to Run | Quality Ceiling |
|----------|--------------------|--------------|----|----------------|
| Prompt Engineering | Real-time (in context) | Very Low | Per-token | Limited by context window |
| RAG | Minutes to hours | Medium | Per-query (embed + retrieve + generate) | High for factual Q&A |
| Fine-Tuning | Frozen at training time | High | Per-token (may use smaller model) | High for specific tasks |
| Pre-Training | Frozen at training time | Very High | Per-token | Highest (but rarely justified) |

**Limitations**: These approaches are not mutually exclusive. The best production systems often combine them: fine-tuned model + RAG + careful prompt engineering. Start with the simplest approach and add complexity only when measurement shows it is needed.

---

### AI Cost Optimization

**When to use**: As a design constraint from the start, and continuously as usage grows.

**Cost Levers**:

| Lever | Savings Potential | Implementation Effort |
|-------|-------------------|-----------------------|
| **Model right-sizing** | 50-90% | Low — use smaller models for simpler tasks |
| **Prompt optimization** | 10-30% | Low — reduce prompt length, remove redundancy |
| **Caching** | 30-80% | Medium — cache responses for repeated queries |
| **Batching** | 20-40% | Medium — batch similar requests |
| **Tiered routing** | 40-70% | Medium — route simple queries to cheaper models |
| **Fine-tuned small models** | 60-90% | High — train for specific tasks, deploy smaller |

**Cost Modeling Template**:
```markdown
## AI Cost Model: [Feature Name]

### Per-Query Cost Breakdown
| Component | Tokens/Units | Unit Cost | Cost/Query |
|-----------|-------------|-----------|-----------|
| Embedding (query) | [tokens] | $[X]/1M tokens | $[X] |
| Vector search | [queries] | $[X]/query | $[X] |
| LLM input (prompt + context) | [tokens] | $[X]/1M tokens | $[X] |
| LLM output | [tokens] | $[X]/1M tokens | $[X] |
| **Total per query** | | | **$[X]** |

### Projected Monthly Cost
| Scale | Queries/Month | Monthly Cost |
|-------|---------------|-------------|
| Current | [X] | $[X] |
| 3-month projection | [X] | $[X] |
| 12-month projection | [X] | $[X] |

### Optimization Opportunities
- [ ] [Lever]: Estimated savings $[X]/month
```

**Limitations**: AI costs scale linearly with usage in the absence of caching or batching. Model costs are also subject to vendor pricing changes. Build in margin and monitor cost per query as a key metric.

---

### Responsible AI Frameworks

**When to use**: For every user-facing AI feature. Non-negotiable.

**Five Pillars**:

| Pillar | What It Means | How to Implement |
|--------|--------------|------------------|
| **Fairness** | AI does not discriminate based on protected attributes | Bias testing across demographic groups; balanced training data |
| **Transparency** | Users understand when and how AI is used | Clear AI disclosure; explainable outputs; confidence indicators |
| **Safety** | AI does not produce harmful outputs | Input filtering, output guardrails, human escalation paths |
| **Privacy** | AI respects data rights and minimizes data use | Data minimization; no PII in training without consent; right to deletion |
| **Accountability** | Clear ownership for AI behavior and outcomes | Incident response plan; AI decision audit trail; designated AI owner |

**Safety Guardrail Template**:
```
INPUT GUARDRAILS:
  - Prompt injection detection (pattern matching + classifier)
  - PII detection and redaction before processing
  - Content classification (reject prohibited categories)
  - Rate limiting per user to prevent abuse

OUTPUT GUARDRAILS:
  - Content safety classifier (toxicity, harmful content)
  - PII detection in generated output
  - Factual grounding check (for RAG systems)
  - Confidence threshold (low confidence → fallback response)
  - Citation verification (claimed sources exist in context)

FALLBACK BEHAVIOR:
  - Guardrail triggered → Return safe default response
  - Model failure → Return cached/static response
  - Repeated failures → Escalate to human support
  - All fallbacks logged for analysis
```

**Limitations**: No guardrail system is perfect. The goal is defense in depth: multiple layers of protection, with monitoring to catch what slips through. Plan for guardrail failures in your incident response process.

---

## AI Architecture Checklist

Quick reference for any AI feature architecture:

- [ ] **Problem statement**: Clear articulation of what AI solves better than alternatives
- [ ] **Model selection**: Justified choice with alternatives considered
- [ ] **Evaluation framework**: Automated + human eval, golden dataset
- [ ] **Guardrails**: Input validation, output filtering, fallback paths
- [ ] **Cost model**: Per-query cost, projected monthly cost, optimization plan
- [ ] **Monitoring**: Quality metrics, cost tracking, drift detection
- [ ] **Responsible AI**: Bias testing, transparency, safety controls
- [ ] **Fallback**: What happens when AI fails or produces low-quality output
- [ ] **Data pipeline**: Source data quality, freshness, privacy compliance
- [ ] **Latency budget**: End-to-end response time target with all steps

---

## Operating Principle

> "AI in production is not a model — it is a system. The model is one component surrounded by evaluation, guardrails, monitoring, and fallbacks. If you cannot measure quality, control costs, and handle failures gracefully, you are running a demo, not a product."


## Common Pitfalls

- LLM token costs and rate limits change frequently — verify current pricing before recommending
- RAG quality depends heavily on chunking strategy and embedding model — there's no universal best approach
- AI system evaluations must use consistent test sets — ad hoc testing gives misleading confidence
- Prompt engineering is model-specific — what works on one model may fail on another

---

<!-- Source: Anthropic best practices, Claude documentation, emerging production LLM patterns from AI engineering community -->

## LLM Integration Patterns (Advanced)

This section covers production-grade patterns for integrating large language models into systems at scale. These patterns go beyond basic API calls to address the real engineering challenges: managing context, orchestrating agents, evaluating quality, and running reliably in production.

The patterns here reflect current best practice as of 2025-2026. LLM tooling evolves rapidly — validate implementation details against current library versions.

---

### RAG Architecture — Advanced Patterns

**Modular RAG** (beyond naive and advanced tiers):

Modular RAG decomposes retrieval into composable components that can be independently swapped, evaluated, and improved.

```
MODULES:

  Query Understanding:
    → Query classification (factual / reasoning / conversational)
    → Intent detection (lookup / summarization / comparison)
    → Entity extraction for targeted retrieval

  Query Transformation:
    → Query expansion: rewrite query into multiple perspectives
    → HyDE (Hypothetical Document Embeddings): generate a hypothetical answer,
      embed it, use it to find similar real documents
    → Step-back prompting: abstract specific query to general principle first

  Retrieval:
    → Dense retrieval (embedding similarity)
    → Sparse retrieval (BM25 keyword)
    → Hybrid (weighted combination of dense + sparse)
    → Knowledge graph traversal (for structured relationships)

  Post-Retrieval:
    → Cross-encoder reranking (more accurate, higher cost)
    → Contextual compression (remove irrelevant sentences from chunks)
    → Deduplication (remove near-duplicate chunks)
    → Self-reflection: ask LLM to evaluate retrieved relevance before generating

  Generation:
    → Citation-aware prompting
    → Multi-hop synthesis for questions requiring multiple sources
    → Uncertainty expression ("Based on the provided context..." / "I cannot find...")
```

**Chunking Strategy Decision (Detailed)**:

| Strategy | Description | Best For | Typical Config |
|----------|-------------|---------|---------------|
| Fixed-size | Split every N tokens with overlap | Uniform prose documents | 512-1024 tokens, 10-20% overlap |
| Semantic | Split at natural paragraph or section boundaries | Technical docs, manuals | Variable size by section |
| Recursive | Try headers → paragraphs → sentences → characters | Mixed content types | Hierarchical fallback |
| Document-structure-aware | Use actual document structure (headings, tables, code blocks) | PDFs, HTML, markdown | Parse structure first |
| Sentence-window | Index sentences, retrieve surrounding window | High-precision Q&A | 1 sentence indexed, 3-5 retrieved |
| Parent-document | Index small chunks, retrieve full parent document | Dense documents needing full context | Small index, large retrieval |

**Embedding Model Selection Criteria**:
```
Evaluate on YOUR data, not benchmarks:
  1. Download MTEB evaluation data in your domain
  2. Run candidate models, measure NDCG@10 on a 500-query sample
  3. Measure cost per embedding and query latency
  4. Check context window (some models cap at 512 tokens)

Decision signals:
  Short queries / documents (< 256 tokens)  → all-MiniLM-L6-v2 (fast, cheap)
  General enterprise content                → text-embedding-3-small
  High-stakes accuracy requirement          → text-embedding-3-large or BGE-large
  Multilingual content                      → multilingual-e5-large
  Domain-specific (legal, medical, code)    → fine-tuned model on domain data
```

**Vector Database Comparison (Production Criteria)**:

| Database | Deployment | Hybrid Search | Filtering | Best Fit |
|----------|-----------|---------------|-----------|---------|
| **Pinecone** | Managed only | Yes (serverless) | Yes | Fast start, no ops budget |
| **Weaviate** | Self-hosted or cloud | Yes (native) | Yes | Hybrid search priority |
| **Qdrant** | Self-hosted or cloud | Yes | Yes (rich payload filtering) | Performance + control |
| **pgvector** | Postgres extension | Partial (with pg_search) | Yes (SQL) | Already on Postgres, < 5M vectors |
| **Chroma** | Local or managed | No | Yes | Prototyping and development |

```
Production selection flow:
  Already on Postgres AND < 5M vectors  → pgvector (zero new infra)
  Need hybrid (semantic + keyword)       → Weaviate or Qdrant
  No ops team / fast start               → Pinecone serverless
  High write throughput (> 10K inserts/s) → Qdrant
  Development / local testing             → Chroma
```

---

### Agent Orchestration Patterns

**ReAct (Reasoning + Acting)**:

The most common agent pattern. The LLM interleaves reasoning traces with tool calls in a loop.

```
Pattern:
  Thought: [LLM reasons about what to do next]
  Action:  [Tool call with parameters]
  Observation: [Tool result]
  Thought: [Reason about the result, decide next step]
  ... repeat until ...
  Final Answer: [LLM provides final response]

Prompt structure:
  "You have access to the following tools: [tool list]
   Use this format:
     Thought: [your reasoning]
     Action: [tool_name]
     Action Input: [input]
     Observation: [tool output - filled by system]
     ... (repeat N times)
   Final Answer: [your final answer]"

When to use:
  - Tasks requiring multiple tool calls with dependencies
  - Research and synthesis tasks
  - Any task where the next step depends on prior results
```

**Plan-and-Execute**:

Separates planning from execution. A planner LLM creates a step-by-step plan; an executor LLM executes each step.

```
Phase 1 — Plan:
  Planner LLM receives the task
  Outputs: ordered list of subtasks with dependencies
  Each subtask: description, tool(s) needed, expected output

Phase 2 — Execute:
  For each subtask in order:
    Executor LLM runs the subtask
    Results stored and passed to dependent subtasks
    Planner may re-plan if a subtask fails or produces unexpected output

Phase 3 — Synthesize:
  Combine all subtask outputs
  Generate final response

When to use:
  - Complex multi-step tasks with clear subtask decomposition
  - When you want to review or modify the plan before execution
  - Human-in-the-loop workflows (approve plan before executing)
```

**Multi-Agent Collaboration Patterns**:

| Pattern | Structure | When to Use |
|---------|-----------|------------|
| **Supervisor** | One orchestrator delegates to specialist agents | Clear subtask boundaries; one agent owns synthesis |
| **Consensus** | Multiple agents answer independently; voting or synthesis | High-stakes decisions; reduce single-model bias |
| **Debate** | Agents argue opposing positions; third agent synthesizes | Genuine tradeoffs; adversarial evaluation of ideas |
| **Assembly Line** | Sequential agent pipeline; each refines prior output | Document generation; multi-stage transformation |
| **Parallel Fan-Out** | Orchestrator spawns agents in parallel; collects results | Independent subtasks; speed-critical workflows |

**Supervisor Pattern Template**:
```
Orchestrator prompt:
  "You are coordinating agents to complete: [task]
   Available agents: [list with capabilities]
   Decompose the task, assign to agents, synthesize results.
   You speak last after reviewing all agent outputs."

Sub-agent prompt:
  "You are [Agent Name] specializing in [domain].
   Your task: [specific subtask]
   Input from prior agents: [context]
   Produce: [specific deliverable format]"

Orchestrator synthesis:
  "Agent outputs: [collected results]
   Synthesize into: [final output format]
   Resolve any conflicts by: [conflict resolution rule]"
```

**Tool Use Patterns (Function Calling)**:

```
Structured Output (no tool needed):
  Use when: You want the LLM to return structured data
  How: Specify JSON schema in the prompt or use response_format parameter
  Example: Classification labels, extracted fields, formatted analysis

Simple Tool Call:
  Use when: One tool call per response, no chaining needed
  How: Define tool with JSON schema; parse structured tool call from response

Parallel Tool Calls:
  Use when: Multiple independent tools can be called simultaneously
  How: Claude and GPT-4 support multiple tool calls in one response
  Example: Retrieve from 3 databases simultaneously

Sequential Tool Chains:
  Use when: Each tool call depends on prior results
  How: Agent loop; pass prior tool output into next prompt

Human-in-the-Loop:
  Use when: Tool action is irreversible or high-stakes
  How: Before executing the tool, present the planned action for approval
  Pattern: PLAN → CONFIRM → EXECUTE
```

---

### Prompt Engineering Patterns (Advanced)

**System Prompt Design Principles**:

```
Structure (order matters):
  1. Role/Persona    — Sets the model's identity and expertise
  2. Context         — What the model has access to
  3. Instructions    — How to behave, what to prioritize
  4. Constraints     — What NOT to do (guardrails)
  5. Format          — How to structure the output
  6. Examples        — 2-5 few-shot demonstrations (if needed)

Anti-patterns to avoid:
  - Contradictory instructions (say X, but do not do Y — where Y is required for X)
  - Vague personas ("be helpful") — be specific ("you are a senior tax attorney")
  - Overloaded prompts — if > 2000 tokens, split into multiple prompts
  - Instructions that fight the model's training (e.g., "never use bullets" then providing a bulleted list)
```

**Few-Shot Prompting**:
```
When to use:
  - Output has a specific format the model does not naturally produce
  - Domain has terminology or style the model needs calibration on
  - Task has edge cases the model gets wrong without examples

Number of examples:
  2 examples:   Usually sufficient for format calibration
  5 examples:   For complex tasks with meaningful variation
  10+ examples: Consider fine-tuning instead

Example quality over quantity:
  - Cover diverse cases (do not repeat same type 3x)
  - Include edge cases you know are problematic
  - Ensure examples reflect ground truth — wrong examples teach wrong behavior
```

**Chain-of-Thought (CoT) Variants**:

| Variant | Prompt Pattern | When |
|---------|---------------|------|
| **Zero-shot CoT** | "Think step by step." | Simple reasoning, quick to implement |
| **Few-shot CoT** | Show 3-5 worked examples with reasoning | Complex domain reasoning |
| **Self-consistency** | Generate N reasoning chains, take majority answer | High-stakes; reduce variance |
| **Tree of Thoughts** | Explore multiple reasoning branches, backtrack | Problems requiring search |
| **Step-back Prompting** | Ask the general principle before the specific question | Domain knowledge activation |

**Prompt Caching Strategies**:

```
Anthropic Prompt Caching:
  How it works: Cache a fixed prefix (system prompt + static context)
  Cost savings: Cached tokens cost ~90% less on subsequent calls
  Min cache size: 1024 tokens (Claude 3) to be eligible
  Cache TTL: ~5 minutes; refreshed on each use

When to cache:
  - Long system prompts (> 1000 tokens) used across many requests
  - Large document context that does not change per user
  - Few-shot examples included in every prompt
  - RAG context that is the same across a session

Structure for maximum caching:
  [System prompt]          ← Always cache this
  [Static document context] ← Cache if > 1024 tokens
  [Dynamic user context]   ← Do NOT include in cache prefix
  [User message]           ← Always after cached prefix

Prefix Caching (general):
  - All major model providers support some form of KV cache
  - Keep static content at the front of the prompt
  - Put variable content (user query, session context) at the end
  - Avoid inserting variable tokens in the middle of cached content
```

---

### Context Window Management

**When to use**: When your application has conversations, documents, or sessions that approach or exceed the model's context window limit.

**Sliding Window with Summarization**:
```
Strategy:
  Keep last N messages verbatim (recent context)
  Summarize older messages into a compressed representation
  Include summary + recent messages in every prompt

Implementation:
  max_messages = 20  (keep verbatim)
  When conversation exceeds max_messages:
    older = messages[:-max_messages]
    summary = summarize(older)  → LLM call: "Summarize this conversation"
    context = [system_prompt, summary_message, *messages[-max_messages:]]

Summary message format:
  "Earlier in this conversation: [summary text]
   The user's original goal was: [initial goal]
   Key decisions made: [bullet list]"
```

**Hierarchical Context**:
```
Layers (from stable to dynamic):
  1. System context:   Role, capabilities, constraints  (never changes)
  2. Session context:  User profile, goals, preferences (changes per session)
  3. Working context:  Current task, recent tool outputs (changes per message)
  4. Message context:  Current user turn                (changes every message)

Token allocation:
  System context:  10-20% of context window (static, cache this)
  Session context: 10-20% (load once per session)
  Working context: 40-60% (most important — where RAG content goes)
  Message:         5-10% (the actual user input)
```

**Context Compression Techniques**:

| Technique | How | Compression Ratio | Quality Loss |
|-----------|-----|-------------------|-------------|
| **Summarization** | LLM compresses older turns | 5-10x | Low for facts; high for nuance |
| **Selective retention** | Keep only messages flagged as important | Variable | Depends on flagging quality |
| **Entity extraction** | Extract key entities/facts; discard conversation | 10-20x | Loses conversational flow |
| **Hybrid** | Summarize + keep last N turns verbatim | 3-5x | Best quality/compression balance |
| **Embedding-based retrieval** | Convert old messages to embeddings, retrieve relevant ones | Variable | Misses implicit context |

---

### LLM Evaluation Frameworks

**RAGAS (Retrieval-Augmented Generation Assessment)**:
```
Metrics (all scored 0-1):
  Faithfulness:         Does the answer contain only info from the context?
  Answer Relevance:     Is the answer responsive to the question?
  Context Precision:    What fraction of retrieved context is relevant?
  Context Recall:       Was all necessary context retrieved?
  Answer Correctness:   Is the answer factually correct? (requires ground truth)

Threshold recommendations:
  Production minimum:   Faithfulness > 0.85, Answer Relevance > 0.80
  High-stakes minimum:  Faithfulness > 0.92, Context Recall > 0.85
  Alert threshold:      Any metric drops > 10% week-over-week
```

**DeepEval Framework**:
```
Metrics available:
  G-Eval:          LLM-as-judge with custom criteria
  Hallucination:   Factual consistency check
  Toxicity:        Harmful content detection
  Bias:            Demographic bias detection
  Summarization:   Compression quality for summarization tasks
  Answer Relevancy: Direct answer-to-question relevance

Integration pattern:
  from deepeval.metrics import HallucinationMetric, AnswerRelevancyMetric
  from deepeval.test_case import LLMTestCase
  test_case = LLMTestCase(input=query, actual_output=response, context=chunks)
  metric = HallucinationMetric(threshold=0.5)
  metric.measure(test_case)
```

**Hallucination Detection**:
```
Detection approaches:
  1. NLI (Natural Language Inference): Check if claims are entailed by context
  2. Citation check: Verify every cited source actually supports the claim
  3. Consistency sampling: Generate N responses; check if claims are consistent
  4. Self-evaluation: Ask the LLM to check its own answer against context

Practical implementation:
  After generation, run this prompt on every response:
    "Given this context: [chunks]
     Review this answer: [response]
     List any claims in the answer that are NOT supported by the context above.
     If all claims are supported, say 'GROUNDED'."

  Flag responses where unsupported claims are detected
  Log for human review; do not silently pass to user
```

**Factual Grounding Metrics**:
```
Precision (attribution quality):
  = (correctly attributed claims) / (total claims in response)
  Target: > 0.90 for customer-facing applications

Recall (coverage quality):
  = (claims with valid sources) / (total facts user needed)
  Target: > 0.80 for knowledge retrieval use cases

Citation accuracy:
  = (citations that actually support the claim) / (total citations)
  Test: Have evaluator verify each citation supports the adjacent claim
```

---

### Production LLM Patterns

**Guardrails (Input and Output)**:

```
INPUT VALIDATION:
  Prompt injection detection:
    - Pattern matching for "ignore previous instructions", "you are now", "jailbreak"
    - Classifier (fine-tuned or LLM-based) for adversarial prompts
    - Input length limits (reject > N tokens to prevent context stuffing)

  PII Detection (before sending to LLM):
    - Regex patterns for emails, phone numbers, SSNs, credit card numbers
    - NER model for names, addresses, medical identifiers
    - Redact or reject based on policy ("replace PII with [REDACTED]" or "reject")

  Content Classification:
    - Route to appropriate system prompt based on detected intent
    - Reject queries outside the system's defined scope
    - Rate limit per user to prevent abuse

OUTPUT VALIDATION:
  Content safety:
    - Toxicity classifier (Perspective API, OpenAI Moderation, custom)
    - Harmful category detection (violence, self-harm, illegal activity)
    - Brand safety check (do not mention competitors, pricing, legal claims)

  Factual grounding (for RAG):
    - Check output cites only information present in retrieved context
    - Flag responses that introduce facts not in the retrieval context

  Format validation:
    - If output must be JSON: parse and validate schema before returning
    - If output has required fields: verify all are present
    - If structured: validate against Pydantic model or JSON Schema
```

**Observability (Logging, Tracing, Cost Tracking)**:

```
What to log for every LLM call:
  Request:   model, timestamp, user_id, session_id, input tokens, prompt hash
  Response:  output tokens, latency_ms, finish_reason, cost_usd
  Quality:   guardrail_triggered (bool), evaluation_scores (if available)
  Business:  feature, use_case, experiment_id (for A/B tests)

Tracing:
  Use distributed tracing (OpenTelemetry, Langsmith, Helicone)
  Trace ID propagated across all LLM calls in a single user interaction
  Include retrieval steps in traces: query → embed → search → rerank → generate
  Trace each tool call in agent workflows

Cost tracking:
  Per-call cost:    (input_tokens × input_price) + (output_tokens × output_price)
  Daily budget:     Alert if > [threshold] per day
  Per-user cost:    Identify outliers (users with unusually high token usage)
  Cost per feature: Roll up cost by feature for product-level ROI tracking

Dashboards to build:
  - Average cost per query by feature and user tier
  - P50/P95/P99 latency by model and endpoint
  - Guardrail trigger rate by category
  - Quality metric trends (faithfulness, relevance week-over-week)
  - Cache hit rate and savings (if using prompt caching)
```

**Model Routing**:

Reduce costs and latency by routing requests to the cheapest model that can handle the task quality.

```
Routing Strategies:

  Complexity-based:
    Simple (classification, lookup, short Q&A)  → small/fast model (e.g., Claude Haiku)
    Medium (summarization, extraction, draft)   → mid-tier model (e.g., Claude Sonnet)
    Complex (reasoning, long-form, synthesis)   → large model (e.g., Claude Opus)

    Classify complexity using:
      - Input token count (proxy for complexity)
      - Intent classifier (fine-tuned or rule-based)
      - Domain-specific heuristics

  Cost-based routing:
    Try cheap model first → if quality score < threshold → retry with expensive model
    Quality gate: run LLM-as-judge on cheap model output before returning to user
    Cost savings target: route > 70% of requests to cheaper models

  Latency-based routing:
    If user requires < 1s response → fast model regardless of quality tier
    If user tolerates 3-5s → quality-optimized model
    Flag latency requirements per feature, not globally

Router Configuration Template:
  {
    "routes": [
      { "intent": "faq_lookup",    "model": "claude-haiku-3",   "max_tokens": 500  },
      { "intent": "summarization", "model": "claude-sonnet-3-5", "max_tokens": 1000 },
      { "intent": "analysis",      "model": "claude-opus-4",    "max_tokens": 4000 },
      { "intent": "default",       "model": "claude-sonnet-3-5", "max_tokens": 2000 }
    ]
  }
```

**Streaming and SSE Patterns**:

```
When to use streaming:
  - Response is > 200 tokens (user perceives faster responses)
  - Conversational interfaces (chat, assistants)
  - Long-form generation (documents, code)

When NOT to stream:
  - Response requires post-processing before display (structured JSON, guardrail check)
  - Response feeds into another automated step (agent tool input)
  - Batch processing (stream has no benefit if user is not watching)

SSE Implementation Pattern:
  Server:
    for chunk in llm_stream:
      yield f"data: {json.dumps({'delta': chunk.text})}\n\n"
    yield "data: [DONE]\n\n"

  Client:
    const es = new EventSource('/api/stream')
    es.onmessage = (e) => {
      if (e.data === '[DONE]') { es.close(); return; }
      const { delta } = JSON.parse(e.data)
      appendToUI(delta)
    }

Streaming with guardrails:
  Problem: You cannot check output safety until the stream is complete
  Solution 1: Buffer the full output, check, then stream to client (adds latency)
  Solution 2: Stream to client but add "interrupt" signal if safety violation detected
  Solution 3: Run cheap classifier on partial output every N tokens

  For high-stakes applications: always buffer and check before streaming to user
```

**Structured Output Reliability**:
```
Challenge: LLMs do not always produce valid JSON or follow schemas reliably

Approaches (in order of preference):
  1. Native structured output (most reliable):
     - Anthropic: response_format parameter (where supported)
     - OpenAI: json_mode or json_schema parameter
     - Constraint enforces valid JSON at generation time

  2. Constrained decoding (very reliable):
     - Libraries: outlines, guidance, lm-format-enforcer
     - Forces output tokens to follow a grammar
     - Works with local models; not always available with hosted APIs

  3. Retry with correction (reliable with overhead):
     - Parse output; if invalid, ask LLM to fix it
     - "Your response was not valid JSON. The error was: [error]. Return valid JSON."
     - Max 2 correction attempts before fallback

  4. Prompt-only (least reliable):
     - Include schema in prompt: "Return ONLY valid JSON matching this schema: ..."
     - Add few-shot examples of correct JSON output
     - Validate output; retry if invalid
```
