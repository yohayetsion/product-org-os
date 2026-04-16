# System Architecture Patterns — Frameworks & Methods

<!-- Attribution:
  Resilience patterns section informed by:
  - Google SRE Book ("Site Reliability Engineering", Google) — resilience patterns and reliability engineering
  - Resilience patterns community — circuit breaker, bulkhead, retry/backoff patterns
  Adapted and expanded for Product Org OS agents.
-->

## Overview

System architecture patterns are proven structural approaches to organizing software systems. Choosing the right pattern is one of the highest-leverage decisions an architect makes — it constrains every downstream decision about data flow, team structure, deployment, and scaling.

This reference covers the major patterns you will encounter and provides decision frameworks for choosing between them. No pattern is universally correct. The right choice depends on your team size, domain complexity, scaling requirements, and organizational structure.

The patterns here are ordered from simplest to most complex. Start at the top and move down only when you have evidence that simpler patterns do not meet your needs.

---

## Frameworks

### Monolith vs. Microservices Decision Framework

**When to use**: At the start of any new system or when considering decomposition of an existing one.

**How it works**: The decision is not "monolith or microservices" — it is "where on the spectrum does my context place me?" Most systems should start as monoliths and decompose only when specific pain points emerge.

**Decision Matrix**:

| Factor | Favors Monolith | Favors Microservices |
|--------|-----------------|---------------------|
| Team size | < 20 engineers | > 50 engineers |
| Domain clarity | Unclear boundaries | Well-understood bounded contexts |
| Deployment frequency | Weekly or less | Multiple teams deploying independently daily |
| Scaling needs | Uniform load across features | Highly variable load per feature |
| Data sharing | Frequent joins across domains | Minimal cross-domain queries |
| Org structure | Single team | Multiple autonomous teams |

**Template for Decision Record**:
```markdown
## Architecture Decision: System Structure

**Context**: [What triggered this decision]
**Team Size**: [Current and projected 12-month]
**Domain Boundaries**: [Clear / Emerging / Unclear]
**Scaling Profile**: [Uniform / Variable by feature]

**Decision**: [Monolith / Modular Monolith / Microservices / Hybrid]

**Rationale**: [Why this choice for this context]

**Re-evaluate when**:
- Team grows beyond [X] engineers
- Deployment frequency exceeds [X] per week
- [Specific scaling bottleneck] is observed
```

**Limitations**: This framework does not account for regulatory requirements that may mandate service isolation (e.g., PCI compliance for payment processing). Add compliance as an explicit factor when applicable.

---

### Modular Monolith

**When to use**: You need clear domain boundaries and independent module development, but your team is not large enough to justify the operational overhead of distributed services.

**How it works**: A single deployable unit internally organized into modules with explicit boundaries. Modules communicate through defined interfaces (not direct database access). Modules share a deployment pipeline but maintain separate codebases or packages.

**Key Design Rules**:
1. Each module owns its database tables — no cross-module direct table access
2. Modules communicate through a defined interface layer (function calls, internal events)
3. Module boundaries align with business domains (bounded contexts)
4. Modules can be extracted into services later without changing their interface

**Template**:
```
src/
  modules/
    orders/
      api/          ← Public interface (what other modules can call)
      internal/     ← Private implementation
      storage/      ← Module-owned tables and queries
    inventory/
      api/
      internal/
      storage/
    payments/
      api/
      internal/
      storage/
  shared/
    events/         ← Internal event bus for async module communication
    auth/           ← Cross-cutting concerns
```

**Limitations**: Enforcing module boundaries requires discipline — the compiler will not prevent a developer from importing another module's internals. Use linting rules, architecture fitness functions, or code review policies to enforce boundaries.

---

### Event-Driven Architecture

**When to use**: When you need to decouple producers from consumers, support asynchronous processing, or build systems that react to state changes across service boundaries.

**How it works**: Components communicate by producing and consuming events rather than making direct synchronous calls. Events represent facts about what happened (past tense: "OrderPlaced", "PaymentProcessed"). Consumers decide independently how to react.

**Three Patterns Within EDA**:

| Pattern | Description | Use When |
|---------|-------------|----------|
| **Event Notification** | Thin events trigger consumers to fetch details | Loose coupling, consumers need different data |
| **Event-Carried State Transfer** | Events contain all necessary data | Consumers need autonomy, can tolerate eventual consistency |
| **Event Sourcing** | Events are the system of record | Need complete audit trail, temporal queries, replay capability |

**Template for Event Design**:
```json
{
  "eventId": "uuid",
  "eventType": "OrderPlaced",
  "timestamp": "ISO 8601",
  "source": "order-service",
  "version": "1.0",
  "data": {
    "orderId": "uuid",
    "customerId": "uuid",
    "items": [],
    "totalAmount": 0.00
  },
  "metadata": {
    "correlationId": "uuid",
    "causationId": "uuid"
  }
}
```

**Limitations**: Event-driven systems are harder to debug than request-response. Invest in correlation IDs, distributed tracing, and dead-letter queues from the start. Eventual consistency requires explicit handling in the UI and API layers.

---

### CQRS (Command Query Responsibility Segregation)

**When to use**: When read and write patterns differ significantly in shape, scale, or performance requirements. Common in systems with complex querying needs but simpler write paths.

**How it works**: Separate the model for writing data (commands) from the model for reading data (queries). The write model is optimized for consistency and business rules. The read model is optimized for query performance and can be denormalized, cached, or served from a different store entirely.

**Decision Criteria**:

| Factor | Standard CRUD Sufficient | CQRS Warranted |
|--------|--------------------------|----------------|
| Read/write ratio | Roughly balanced | > 10:1 or < 1:10 |
| Read shape | Similar to write shape | Aggregated, joined, or reshaped |
| Scale | Uniform | Reads and writes scale independently |
| Complexity | Simple domain | Complex domain logic on writes |

**Template**:
```
Write Side (Commands):
  Command → Validation → Domain Logic → Persist → Publish Event

Read Side (Queries):
  Event → Projection → Read Store → Query → Response

Synchronization:
  Write events flow to read projections
  Eventual consistency (specify max acceptable lag)
  Rebuild projections from event log if needed
```

**Limitations**: CQRS adds infrastructure complexity. You now maintain two models and a synchronization mechanism. Do not apply CQRS across the entire system — apply it only to bounded contexts where the read/write asymmetry justifies the cost.

---

### Domain-Driven Design — Strategic Patterns

**When to use**: When system complexity comes primarily from the business domain rather than from technical challenges. When multiple teams work on different parts of a complex business.

**How it works**: DDD strategic patterns help define system boundaries based on business domain concepts rather than technical layers.

**Key Concepts**:

| Concept | Definition | Practical Impact |
|---------|-----------|------------------|
| **Bounded Context** | A boundary within which a domain model is consistent | Maps to a service, module, or team |
| **Ubiquitous Language** | Shared vocabulary within a bounded context | Same word means the same thing in code, docs, and conversation |
| **Context Map** | How bounded contexts relate to each other | Defines integration patterns between teams/services |
| **Aggregate** | Cluster of entities treated as a unit for consistency | Defines the transaction boundary |

**Context Mapping Patterns**:

| Pattern | Relationship | When to Use |
|---------|-------------|-------------|
| **Shared Kernel** | Two contexts share a small common model | Tightly coupled teams that co-evolve |
| **Customer-Supplier** | Upstream context serves downstream | Clear provider/consumer relationship |
| **Conformist** | Downstream conforms to upstream model | No leverage to change upstream |
| **Anti-Corruption Layer** | Translate between different models | Integrating with legacy or external systems |
| **Open Host Service** | Published interface for multiple consumers | Public API, integration platform |

**Limitations**: DDD requires significant investment in domain modeling workshops and close collaboration with domain experts. It is overkill for simple CRUD applications. The value of DDD increases with domain complexity.

---

### Hexagonal Architecture (Ports and Adapters)

**When to use**: When you need to isolate business logic from infrastructure concerns (databases, APIs, messaging) to enable testing, technology migration, or multi-channel delivery.

**How it works**: Business logic sits at the center, surrounded by ports (interfaces) and adapters (implementations). The core domain has no dependencies on infrastructure — infrastructure depends on the domain.

**Structure**:
```
Adapters (Infrastructure):
  ├── REST API Adapter       ← Driving (input)
  ├── CLI Adapter            ← Driving (input)
  ├── Message Queue Adapter  ← Driving (input)
  ├── PostgreSQL Adapter     ← Driven (output)
  ├── Email Service Adapter  ← Driven (output)
  └── S3 Storage Adapter     ← Driven (output)

Ports (Interfaces):
  ├── OrderService (driving port)
  ├── OrderRepository (driven port)
  └── NotificationSender (driven port)

Core Domain:
  ├── Order (aggregate)
  ├── OrderItem (entity)
  └── PricingPolicy (domain service)
```

**Template for Port Definition**:
```
Port: OrderRepository
Direction: Driven (output)
Operations:
  - save(order: Order): void
  - findById(id: OrderId): Order | null
  - findByCustomer(customerId: CustomerId): Order[]

Adapters:
  - PostgresOrderRepository (production)
  - InMemoryOrderRepository (testing)
```

**Limitations**: Hexagonal architecture introduces indirection that can feel heavy for simple services. Apply it to domains with complex business logic. For simple data-in-data-out services, standard layered architecture may be sufficient.

---

### Strangler Fig Migration Pattern

**When to use**: When migrating from a legacy system to a new architecture incrementally, without a risky big-bang cutover.

**How it works**: Named after the strangler fig tree that grows around its host. New functionality is built in the new system. Existing functionality is gradually migrated. A routing layer (facade) directs traffic to either the old or new system based on the feature. Eventually, the old system is fully replaced.

**Migration Template**:
```
Phase 1: Facade
  - Deploy routing layer in front of legacy system
  - All traffic flows through facade to legacy (no behavior change)
  - Validate facade introduces no regressions

Phase 2: First Feature Migration
  - Build feature X in new system
  - Route feature X traffic to new system via facade
  - Legacy handles everything else
  - Validate feature X works correctly in new system

Phase 3: Incremental Migration
  - Migrate features one at a time
  - Each migration: build → route → validate → decommission legacy code
  - Maintain rollback capability at each step

Phase 4: Decommission
  - All traffic routes to new system
  - Legacy system enters read-only mode
  - After validation period, decommission legacy
```

**Risk Mitigation Checklist**:
- [ ] Facade can route per-feature, not just all-or-nothing
- [ ] Each migrated feature can be rolled back independently
- [ ] Data synchronization between old and new systems is handled
- [ ] Monitoring covers both systems during migration
- [ ] Migration progress is visible to stakeholders

**Limitations**: The facade layer adds latency and a point of failure. Data synchronization between old and new systems during migration is the hardest problem — plan it carefully. Migrations that stall midway leave you maintaining two systems indefinitely, which is the worst outcome.

---

### Saga Pattern (Distributed Transactions)

**When to use**: When a business operation spans multiple services and you need to maintain data consistency without distributed transactions (which do not work reliably across services).

**How it works**: A saga is a sequence of local transactions. Each service completes its local transaction and publishes an event. If a step fails, compensating transactions undo the prior steps.

**Two Approaches**:

| Approach | How | Best For |
|----------|-----|----------|
| **Choreography** | Each service listens for events and reacts | Simple sagas (2-4 steps), loosely coupled teams |
| **Orchestration** | Central coordinator directs the saga flow | Complex sagas (5+ steps), clear visibility needed |

**Template for Saga Design**:
```
Saga: PlaceOrder

Steps:
  1. OrderService.createOrder() → OrderCreated
  2. PaymentService.processPayment() → PaymentProcessed
  3. InventoryService.reserveStock() → StockReserved
  4. ShippingService.scheduleShipment() → ShipmentScheduled

Compensations (reverse order):
  4c. ShippingService.cancelShipment()
  3c. InventoryService.releaseStock()
  2c. PaymentService.refundPayment()
  1c. OrderService.cancelOrder()

Failure Handling:
  - If step 3 fails: execute 2c, then 1c
  - If compensation fails: alert + manual intervention queue
  - Idempotency required for all steps and compensations
```

**Limitations**: Compensating transactions cannot always perfectly undo a step (e.g., an email already sent). Design compensations pragmatically. Sagas introduce eventual consistency — the UI must handle intermediate states gracefully.

---

## Pattern Selection Guide

When faced with an architecture decision, use this quick reference:

| Situation | Start With | Escalate To |
|-----------|-----------|-------------|
| New product, small team | Monolith | Modular Monolith when boundaries clarify |
| Growing product, 3+ teams | Modular Monolith | Microservices when deployment coupling hurts |
| Read-heavy analytics + write-heavy operations | Standard + caching | CQRS for the specific bounded context |
| Cross-service business operations | Direct calls + retries | Saga pattern when consistency matters |
| Legacy system replacement | In-place refactoring | Strangler Fig when risk tolerance is low |
| Complex business domain | Layered architecture | DDD + Hexagonal when domain logic dominates |
| Async processing, event reactions | Request-response + queues | Event-Driven Architecture when decoupling is primary |

---

## Operating Principle

> "The best architecture is the simplest that meets current needs while remaining adaptable to future change. Complexity is not a feature — it is a cost that must be justified by specific, demonstrated requirements."


## Common Pitfalls

- Architecture patterns are context-dependent — microservices aren't always better than monoliths
- Scalability estimates without load testing data are speculation — flag as assumptions
- Database technology choice depends on access patterns, not popularity

---

<!-- Source: SRE runbooks, Netflix Tech Blog, AWS Well-Architected Framework resilience pillar, Google SRE Book -->

## Resilience Patterns

Resilience patterns are structural approaches to building systems that fail gracefully, recover automatically, and protect themselves from cascading failures. These patterns originate from SRE practice at Netflix, Amazon, and Google and are now standard for any production system at meaningful scale.

The core idea is that failures are inevitable — resilience engineering designs for failure rather than trying to prevent it.

---

### Circuit Breaker Pattern

**When to use**: When a service calls a dependency that may be slow or unavailable. Prevents your service from being dragged down by a failing dependency.

**How it works**: A state machine wraps every outbound call. When failures exceed a threshold, the circuit "opens" and calls fail immediately (fast-fail) without reaching the dependency. After a recovery window, the circuit moves to "half-open" and probes the dependency before restoring full traffic.

**States**:

| State | Behavior | Transition |
|-------|----------|-----------|
| **Closed** | All calls pass through | Opens when failure rate exceeds threshold |
| **Open** | All calls fail immediately (no network call) | Moves to half-open after timeout window |
| **Half-Open** | Limited probe calls allowed | Closes on success; re-opens on failure |

**Configuration Parameters**:
```
Failure Threshold:     50% failure rate over 10-second window
Minimum Calls:         20 (don't open on 1 failure out of 2)
Open Duration:         30 seconds before half-open probe
Half-Open Probe Calls: 5 calls to test recovery
Success Threshold:     80% success rate to re-close
```

**Implementation Libraries**:
- **.NET / Polly**: `Policy.Handle<Exception>().CircuitBreakerAsync(exceptionsAllowed, durationOfBreak)`
- **Java / Resilience4j**: `CircuitBreakerConfig.custom().failureRateThreshold(50).build()`
- **Node.js / opossum**: `new CircuitBreaker(asyncFn, { timeout: 3000, errorThresholdPercentage: 50 })`

**Fallback Strategies**:
```
1. Return cached/stale data (with age indicator in response)
2. Return degraded response (partial data, feature disabled)
3. Return static default (empty list, placeholder content)
4. Fail fast with clear error (upstream caller handles it)
5. Queue the request for retry when circuit closes
```

**Limitations**: Circuit breakers protect callers but do not fix the underlying dependency. Pair with retry logic for transient errors, but do not retry when the circuit is open.

---

### Bulkhead Pattern

**When to use**: When one slow or failed operation should not consume all available resources and starve other operations.

**How it works**: Named after ship compartments that isolate flooding. Partition your thread pools, connection pools, or semaphores by operation type or tenant so that exhaustion in one partition does not affect others.

**Two Approaches**:

| Approach | How | When |
|----------|-----|------|
| **Thread Pool Isolation** | Each operation type gets a fixed thread pool | High-throughput services; CPU-bound operations |
| **Semaphore Isolation** | Each operation type gets a concurrent call limit | I/O-bound operations; lower overhead |

**Partition by Criticality Template**:
```
Critical Path:      10 threads (checkout, payment, auth)
Standard Path:      20 threads (product search, catalog)
Background Path:    5 threads (analytics, recommendations)
Third-Party:        5 threads (per external service)

Rule: Critical path resources are never shared with background
Rule: Each third-party integration has its own pool
```

**Tenant Isolation Example**:
```
Enterprise tenants:  Dedicated thread pool (never throttled)
Standard tenants:    Shared pool with semaphore per tenant
Free tenants:        Lower semaphore limit; graceful queueing
```

**Limitations**: Bulkheads add memory and thread overhead. Right-sizing pools requires load testing — too small and you artificially throttle; too large and you waste resources.

---

### Retry with Exponential Backoff

**When to use**: For transient failures (network blip, temporary throttle, brief service restart) where the same request will likely succeed if retried after a short wait.

**How it works**: After a failure, wait before retrying. Each subsequent retry waits exponentially longer. Add random jitter to prevent retry storms when many callers fail simultaneously.

**Formula**:
```
Wait time = min(base * 2^attempt + jitter, max_wait)

Example:
  Attempt 1: 1s + jitter(0-500ms)
  Attempt 2: 2s + jitter(0-500ms)
  Attempt 3: 4s + jitter(0-500ms)
  Attempt 4: 8s + jitter(0-500ms)
  Max wait:  30s cap
  Max attempts: 5
```

**Jitter Strategies**:

| Strategy | Formula | When |
|----------|---------|------|
| **Full Jitter** | `random(0, base * 2^n)` | Highest thundering herd prevention |
| **Equal Jitter** | `base * 2^n / 2 + random(0, base * 2^n / 2)` | Balance between spread and predictability |
| **Decorrelated Jitter** | `random(base, prev_wait * 3)` | AWS recommended pattern |
| **No Jitter** | `base * 2^n` | Only acceptable for single-caller scenarios |

**Idempotency Requirements**:
```
SAFE to retry:    GET, reads, idempotent writes (same result if called N times)
UNSAFE to retry:  POST creating resources, payments, emails — add idempotency keys
  - Include client-generated idempotency key in request
  - Server returns same result for duplicate keys within TTL
  - Key format: [operation-type]-[client-id]-[timestamp]
```

**What to Retry vs. Not Retry**:
```
RETRY:      429 Too Many Requests, 503, 504, network timeouts, connection reset
DO NOT:     400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found, 409 Conflict
```

**Limitations**: Retry logic can make a degraded downstream worse by amplifying load. Always combine with circuit breakers. Never retry without a maximum retry limit.

---

### Timeout Pattern

**When to use**: Always. Every network call must have an explicit timeout. Default is "never" which is never acceptable in production.

**Two Types**:

| Type | What It Covers | Typical Values |
|------|---------------|---------------|
| **Connect Timeout** | Time to establish the TCP connection | 1-5 seconds |
| **Read Timeout** | Time to receive the first byte or complete response | 5-30 seconds depending on operation |

**Cascading Timeout Budgets**:
```
User request total budget: 3000ms
  └─ API Gateway:          200ms (auth, routing)
  └─ Service A:            2500ms total budget
        └─ DB query:       200ms
        └─ Service B call: 1000ms (service B has 800ms net budget)
              └─ DB query: 300ms
              └─ Cache:    100ms
        └─ Response build: 300ms
        └─ Margin:         1000ms
```

**Rule**: Each downstream timeout must be less than your own timeout minus your local processing time. Never set a downstream timeout equal to or greater than your own.

**Implementation Pattern**:
```
// Set timeout at every layer
httpClient.connectTimeout(2, TimeUnit.SECONDS)
httpClient.readTimeout(5, TimeUnit.SECONDS)

// Pass deadline context for distributed tracing
context.withDeadline(deadline.offset(-100ms))  // trim 100ms for network

// Differentiate timeout errors from other failures
catch TimeoutException → return DEGRADED response
catch NetworkException → retry with backoff
```

**Limitations**: Overly aggressive timeouts cause false failures for legitimately slow operations. Measure actual P99 response times before setting timeouts. Too-long timeouts waste threads waiting for responses that will never come.

---

### Rate Limiting

**When to use**: To protect services from overload, enforce fair use, and prevent abuse.

**Algorithms**:

| Algorithm | Description | Precision | Memory | Use When |
|-----------|-------------|-----------|--------|----------|
| **Token Bucket** | Tokens refill at fixed rate; burst allowed up to bucket size | High | Low | APIs with burst allowance |
| **Sliding Window Log** | Track exact timestamps of all requests | Exact | High (per user) | Strict rate enforcement |
| **Sliding Window Counter** | Interpolate between two fixed windows | Near-exact | Low | General use |
| **Fixed Window** | Counter resets at fixed intervals | Low | Lowest | Internal throttles |

**Token Bucket Configuration**:
```
Bucket capacity:    100 requests  (burst limit)
Refill rate:        10 requests/second  (sustained limit)
Initial tokens:     100  (full bucket on startup)

Result: User can burst 100 immediately, sustained at 10 rps
```

**Distributed Rate Limiting**:
```
Single-node:    In-memory counter (fast, not shared across instances)
Multi-node:     Redis INCR + EXPIRE (atomic, shared)
               Lua script for atomic check-and-increment

Redis pattern:
  key: rate_limit:{user_id}:{window}
  MULTI
    INCR key
    EXPIRE key {window_seconds}
  EXEC
  IF count > limit: reject with 429 + Retry-After header
```

**Response Headers** (standard):
```
X-RateLimit-Limit: 100
X-RateLimit-Remaining: 42
X-RateLimit-Reset: 1678886400  (Unix timestamp)
Retry-After: 30  (seconds, on 429 response)
```

**Limitations**: Per-node rate limiting in multi-instance deployments is approximate. For strict enforcement, use a shared store (Redis). Distributed rate limiting adds latency per request — measure whether this is acceptable for your SLA.

---

### Load Shedding

**When to use**: When a service is overloaded beyond its capacity and must protect itself by deliberately dropping work rather than processing it too slowly for all callers.

**Three Strategies**:

| Strategy | How | When |
|----------|-----|------|
| **Priority-Based** | Drop low-priority requests first; protect critical paths | Multi-tier user base; clear priority ordering |
| **Random** | Drop a random percentage of incoming requests | Stateless traffic; no priority information |
| **Adaptive** | Monitor queue depth or latency; shed automatically when threshold exceeded | Production services with SLO-based capacity |

**Priority Classification Template**:
```
P0 (never shed):    Authentication, payment processing, health checks
P1 (shed last):     User-initiated reads (product pages, search)
P2 (shed first):    Analytics events, background sync, batch jobs
P3 (drop freely):   Non-critical logging, optional telemetry
```

**Adaptive Shedding Pattern**:
```
Signal:           Queue depth > 80% capacity OR P99 latency > 2x baseline
Action:           Begin shedding P2/P3 traffic at 50% sample rate
Escalation:       If signal persists > 30s, shed all P2/P3 traffic
Recovery:         Signal clears for 60s → restore normal processing
Response:         503 Service Unavailable with Retry-After header
```

**Limitations**: Load shedding is a last-resort mechanism. If you shed frequently, you have a capacity problem that requires scaling or optimization. Monitor shed rates as a capacity signal.

---

### Graceful Degradation

**When to use**: When a non-critical dependency fails and you can still serve a useful (if reduced) response rather than failing completely.

**Strategies**:

| Strategy | Description | Implementation |
|----------|-------------|---------------|
| **Feature Flags** | Disable non-critical features at runtime | `if (featureFlag.enabled("recommendations")) { ... }` |
| **Fallback Responses** | Return cached, default, or partial data | Stale cache → empty list → static default |
| **Read-Only Mode** | Accept reads, queue or reject writes | Detect write failure, switch to read-only path |
| **Reduced Functionality** | Core features work; secondary features disabled | Layered feature dependency map |
| **Static Fallback** | Serve pre-rendered or cached version | CDN fallback to last-known-good static snapshot |

**Degradation Hierarchy Template**:
```
Level 0 (Normal):       Full functionality
Level 1 (Degraded):     Non-personalized responses (no recommendations)
Level 2 (Minimal):      Core reads only (catalog, search) — no checkout
Level 3 (Emergency):    Static maintenance page with status link
```

**Feature Dependency Map**:
```
ALWAYS available:   Auth, checkout, core catalog
DEGRADE gracefully: Recommendations (→ popular items), Personalization (→ generic)
DISABLE cleanly:    Real-time notifications, activity feed, social features
```

**Limitations**: Graceful degradation requires explicit design — it does not happen automatically. Each degradation path must be tested. Users must be informed when they are receiving a degraded experience.

---

### Health Check Patterns

**When to use**: For every service. Health checks enable load balancers, orchestrators, and operators to know service state.

**Two Types**:

| Type | Question It Answers | What to Check |
|------|---------------------|---------------|
| **Liveness** | Is the process alive? Should it be restarted? | Process running, no deadlock, basic responsiveness |
| **Readiness** | Is the service ready to receive traffic? | Dependencies available, data loaded, warm-up complete |

**Deep Health Check Template**:
```json
GET /health
{
  "status": "healthy | degraded | unhealthy",
  "version": "1.2.3",
  "uptime": 3600,
  "checks": {
    "database": { "status": "healthy", "latency_ms": 12 },
    "cache": { "status": "healthy", "latency_ms": 2 },
    "external_api": { "status": "degraded", "latency_ms": 850, "note": "slow but available" },
    "disk_space": { "status": "healthy", "free_gb": 42 }
  }
}
```

**Status Mapping**:
```
healthy:   All critical dependencies up; serving traffic normally
degraded:  Non-critical dependency down; serving with reduced functionality
unhealthy: Critical dependency down or self-check failed; remove from LB rotation
```

**Rules**:
- Liveness endpoint must respond in < 100ms (no database calls)
- Readiness may include dependency checks but must timeout quickly (< 2s)
- Never mark unhealthy due to downstream failures you can gracefully degrade
- Expose a /metrics endpoint separately for Prometheus scraping

**Limitations**: Overly strict health checks that check every dependency cause unnecessary restarts. Overly lenient checks mask real issues. Design each check threshold based on actual SLO impact.

---

### Chaos Engineering Principles

**When to use**: When your system needs to validate that resilience patterns work under real conditions, not just in theory.

**How it works**: Deliberately inject failures in controlled conditions to discover weaknesses before they manifest in production incidents.

**The Steady State Hypothesis**:
```
Before experiment:
  1. Define "normal" — measurable output indicating system is healthy
     Example: "Error rate < 0.1%, P99 latency < 500ms, checkout success > 99%"
  2. Confirm system is in steady state
  3. Define what you expect the system to do when the failure is injected

Experiment:
  1. Inject the failure in a controlled scope (blast radius)
  2. Observe whether system maintains steady state
  3. Stop experiment if steady state is violated unexpectedly

After experiment:
  1. Restore normal state
  2. If steady state held: confirm hypothesis, document resilience
  3. If steady state broke: file issue, fix, re-test
```

**Blast Radius Control**:
```
Start smallest: Single host, single canary group, 1% of traffic
Escalate when: Previous scope validated, confidence is high
Maximize isolation: Use feature flags to limit experiment scope
Kill switch: One button stops the experiment immediately
Never in: Peak traffic hours without explicit approval
```

**Experiment Catalog** (common scenarios):
```
Instance failure:      Kill a random service instance
Network latency:       Add 200ms-2000ms latency to specific calls
Packet loss:           Drop 10-50% of packets on a network interface
Dependency failure:    Return 500 or timeout from a downstream service
Disk full:             Fill disk to threshold on a single host
Memory pressure:       Consume memory to trigger GC or OOM
DNS failure:           Poison DNS resolution for a service
Region failure:        Simulate AZ or region unavailability
```

**Limitations**: Chaos engineering requires mature monitoring and observability before it is useful. If you cannot measure steady state, you cannot run experiments. Start with game days (manual failure injection) before automated chaos.

---

### Resilience Testing Checklist

Use before any service enters production or before significant traffic increases.

**Circuit Breaker**
- [ ] Verified circuit opens when failure rate exceeds threshold
- [ ] Verified fallback behavior returns appropriate degraded response
- [ ] Verified circuit recovers (closes) after downstream recovers
- [ ] Timeout configuration tested; confirmed no thread leaks on timeout

**Retry Logic**
- [ ] Verified retries use exponential backoff with jitter
- [ ] Verified non-retryable errors (4xx) do not retry
- [ ] Verified idempotency keys implemented for non-safe operations
- [ ] Max retry limit tested; confirmed failure returned after limit

**Bulkheads**
- [ ] Thread pools per operation type are properly isolated
- [ ] Exhausting one pool does not affect other pools (tested)
- [ ] Pool sizes validated against expected load profile

**Timeouts**
- [ ] Every outbound call has explicit connect + read timeout configured
- [ ] Timeout cascade budget verified (downstream < upstream)
- [ ] Behavior on timeout verified (circuit breaker increment, fallback, logging)

**Rate Limiting**
- [ ] Rate limits enforce correctly at configured thresholds
- [ ] 429 response includes Retry-After header
- [ ] Distributed rate limiting tested under multi-instance deployment

**Health Checks**
- [ ] Liveness endpoint responds in < 100ms without DB calls
- [ ] Readiness endpoint correctly gates traffic until dependencies available
- [ ] Load balancer drains instance when readiness fails

**Graceful Degradation**
- [ ] Each critical dependency has a defined degradation path
- [ ] Degraded responses are tested end-to-end
- [ ] Feature flags work at runtime without deployment

**Chaos**
- [ ] At least one game day conducted before production launch
- [ ] Kill-switch process tested and documented
- [ ] Incident response runbook includes chaos experiment observations
