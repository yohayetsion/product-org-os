# API Design Patterns — Frameworks & Methods

## Overview

API design is the discipline of defining how software components communicate. A well-designed API is a product in its own right — it has consumers, contracts, versioning, and a developer experience that determines adoption. Poor API design creates compounding costs: every consumer that integrates with a bad API inherits its problems.

This reference covers REST, GraphQL, gRPC, and event-driven patterns. It provides decision frameworks for choosing between them, and detailed guidance on cross-cutting concerns like authentication, pagination, error handling, and versioning. The guidance is ordered from most common to most specialized — start with REST unless you have evidence that another paradigm better fits your use case.

**Version**: 1.0.0
**Type**: Knowledge Pack
**Primary Users**: 🔌 API Architect, 🏗️ Chief Architect

---
<!-- Attribution:
  Frameworks and patterns in this knowledge pack were informed by:
  - Anthropic knowledge-work-plugins (engineering domain reference)
  - REST/GraphQL/gRPC community standards and best practices
  - OWASP API Security Top 10 (owasp.org) — API security patterns
  Adapted and expanded for Product Org OS agents.
-->

## API Style Selection Framework

**When to use**: At the start of any new API surface or when evaluating whether to add a second paradigm.

**Decision Matrix**:

| Factor | REST | GraphQL | gRPC |
|--------|------|---------|------|
| Primary consumers | Web/mobile apps, third parties | Frontend teams needing flexible queries | Internal microservices |
| Data shape | Predictable, resource-oriented | Deeply nested, variable per view | Strongly typed, high throughput |
| Real-time needs | Webhooks, SSE | Subscriptions (built-in) | Bidirectional streaming |
| Caching | HTTP caching (CDN, browser) | Complex (requires persisted queries) | No HTTP caching |
| Learning curve | Low (ubiquitous) | Medium (schema + query language) | High (protobuf, tooling) |
| Tooling maturity | Excellent | Good | Good (but language-dependent) |
| File upload | Multipart form data | Awkward (separate endpoint or multipart spec) | Streaming chunks |
| Browser support | Native | Via client library | Requires grpc-web proxy |

**Template for Decision Record**:
```markdown
## Architecture Decision: API Style

**Context**: [What triggered this decision — new product, new consumer type, performance issue]
**Consumer Types**: [Web app / Mobile / Third-party / Internal services]
**Data Access Patterns**: [CRUD / Flexible queries / High-throughput RPC / Streaming]
**Team Expertise**: [REST / GraphQL / gRPC experience levels]

**Decision**: [REST / GraphQL / gRPC / Hybrid]

**Rationale**: [Why this choice for this context]

**Re-evaluate when**:
- Consumer count exceeds [X] and over-fetching becomes measurable
- Internal service mesh grows beyond [X] services
- Real-time requirements emerge that current approach handles poorly
```

**Common hybrid patterns**:
- REST for public API + gRPC for internal service communication
- REST for CRUD + GraphQL for complex dashboard queries
- REST for writes + GraphQL for reads (CQRS alignment)

**Limitations**: This framework assumes greenfield. Migrating existing APIs requires additional factors: consumer migration cost, backward compatibility windows, and team retraining time.

---

## REST API Design

### Resource Design Principles

REST APIs model resources, not actions. Every design decision flows from this principle.

**Naming conventions**:

| Pattern | Example | Rule |
|---------|---------|------|
| Collection | `/users` | Plural nouns |
| Instance | `/users/{id}` | Singular resource by identifier |
| Sub-resource | `/users/{id}/orders` | Relationship expressed as nested path |
| Action (when unavoidable) | `/orders/{id}/cancel` | POST to verb endpoint — use sparingly |
| Filtering | `/users?status=active&role=admin` | Query parameters for filtering collections |
| Search | `/users/search?q=term` | Dedicated search endpoint for full-text |

**Rules that prevent inconsistency**:
1. Use lowercase with hyphens: `/user-profiles`, not `/userProfiles` or `/user_profiles`
2. Never expose internal IDs in URLs when public UUIDs serve the same purpose
3. Avoid deep nesting beyond two levels: `/users/{id}/orders` is fine; `/users/{id}/orders/{oid}/items/{iid}/variants` is not — flatten to `/order-items/{iid}`
4. Use plural nouns for collections, even when it sounds odd (`/metadata`, not `/metadatas` — keep it as `/metadata`)
5. Version prefix in URL: `/v1/users` (see Versioning section)

### HTTP Methods

| Method | Semantics | Idempotent | Safe | Request Body | Success Code |
|--------|-----------|------------|------|-------------|--------------|
| GET | Read resource(s) | Yes | Yes | No | 200 |
| POST | Create resource or trigger action | No | No | Yes | 201 (create), 200 (action) |
| PUT | Full replace of resource | Yes | No | Yes (complete) | 200 |
| PATCH | Partial update of resource | No* | No | Yes (partial) | 200 |
| DELETE | Remove resource | Yes | No | No | 204 |
| HEAD | GET without body (check existence) | Yes | Yes | No | 200 |
| OPTIONS | Discover allowed methods (CORS) | Yes | Yes | No | 204 |

*PATCH can be made idempotent with JSON Merge Patch (RFC 7396) or JSON Patch (RFC 6902) depending on the operation.

### HTTP Status Codes

Use the narrowest applicable code. Generic 200/400/500 responses lose information that consumers need.

| Range | Category | Key Codes |
|-------|----------|-----------|
| 2xx | Success | 200 OK, 201 Created, 202 Accepted (async), 204 No Content |
| 3xx | Redirection | 301 Moved Permanently, 304 Not Modified |
| 4xx | Client error | 400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found, 409 Conflict, 422 Unprocessable Entity, 429 Too Many Requests |
| 5xx | Server error | 500 Internal Server Error, 502 Bad Gateway, 503 Service Unavailable, 504 Gateway Timeout |

**Common mistakes**:
- Using 200 for everything with error details in the body — breaks HTTP semantics and client libraries
- Using 401 when you mean 403 — 401 means "not authenticated," 403 means "authenticated but not authorized"
- Using 404 to hide resource existence — use 403 when the resource exists but the user lacks access (unless information hiding is a security requirement)
- Using 500 for validation errors — 422 or 400 is correct
- Returning 200 on DELETE — use 204 (No Content) when the resource is removed

### HATEOAS (Hypermedia as the Engine of Application State)

HATEOAS makes APIs self-describing by embedding links to related resources and available actions.

**Practical adoption levels**:

| Level | What You Include | When |
|-------|-----------------|------|
| **Level 0** (minimum) | `self` link on every resource | Always — costs nothing, enables debugging |
| **Level 1** (recommended) | Related resource links + pagination links | Public APIs, APIs with multiple consumers |
| **Level 2** (full) | Available actions with methods and link relations | API marketplaces, highly discoverable APIs |

**Example (Level 1)**:
```json
{
  "id": "usr_abc123",
  "name": "Jane Smith",
  "email": "jane@example.com",
  "_links": {
    "self": { "href": "/v1/users/usr_abc123" },
    "orders": { "href": "/v1/users/usr_abc123/orders" },
    "organization": { "href": "/v1/orgs/org_xyz789" }
  }
}
```

**Example (Level 1 — collection with pagination)**:
```json
{
  "data": [ ... ],
  "_links": {
    "self": { "href": "/v1/users?page=2&limit=20" },
    "first": { "href": "/v1/users?page=1&limit=20" },
    "prev": { "href": "/v1/users?page=1&limit=20" },
    "next": { "href": "/v1/users?page=3&limit=20" },
    "last": { "href": "/v1/users?page=12&limit=20" }
  },
  "_meta": {
    "total": 234,
    "page": 2,
    "limit": 20
  }
}
```

---

## GraphQL Design Patterns

### Schema Design

**Type design principles**:
1. **Start with the query, not the database** — design types from what the client needs, not what the tables look like
2. **Use interfaces for shared fields** — `Node` interface with `id` field for refetchable objects
3. **Connections over arrays** — use Relay-style connections for any list that could paginate
4. **Input types for mutations** — always wrap mutation arguments in a dedicated `input` type
5. **Enums over strings** — use enums for any field with a fixed set of values

**Schema structure template**:
```graphql
# Node interface for globally unique IDs
interface Node {
  id: ID!
}

# Relay-style connection pattern
type UserConnection {
  edges: [UserEdge!]!
  pageInfo: PageInfo!
  totalCount: Int!
}

type UserEdge {
  node: User!
  cursor: String!
}

type PageInfo {
  hasNextPage: Boolean!
  hasPreviousPage: Boolean!
  startCursor: String
  endCursor: String
}

# Mutation input pattern
input CreateUserInput {
  name: String!
  email: String!
  role: UserRole!
}

type CreateUserPayload {
  user: User
  errors: [UserError!]!
}

type UserError {
  field: String!
  message: String!
  code: ErrorCode!
}
```

### Resolver Design

| Pattern | When | How |
|---------|------|-----|
| **DataLoader** | N+1 query prevention (always) | Batch and cache database lookups per request |
| **Field-level auth** | Different fields have different access | Check permissions in resolver, return null or error |
| **Computed fields** | Derived data that should not be stored | Resolve from other fields; mark with `@deprecated` if migrating |
| **Pagination** | Any list that could exceed 20 items | Cursor-based with `first`/`after` and `last`/`before` |

### Subscriptions

Use subscriptions for real-time updates. Prefer WebSocket transport (graphql-ws protocol).

**Design rules**:
1. Subscribe to events, not polling — `onOrderStatusChanged`, not `getOrderStatus`
2. Filter at the server — accept filter arguments so clients do not receive irrelevant events
3. Keep payloads small — send the changed entity or a reference, not the entire object graph
4. Authenticate on connection init, not per message

### GraphQL Security

| Threat | Mitigation |
|--------|------------|
| Deep query attacks | Query depth limiting (max 10-15 levels) |
| Wide query attacks | Query complexity analysis with cost limits |
| Introspection leaks | Disable introspection in production |
| Batch attacks | Limit array sizes in queries and mutations |
| Persisted queries | Whitelist known queries in production (APQ) |

---

## gRPC Patterns

### Service Definition

```protobuf
syntax = "proto3";

package orders.v1;

service OrderService {
  // Unary - simple request/response
  rpc GetOrder(GetOrderRequest) returns (GetOrderResponse);

  // Server streaming - server pushes multiple responses
  rpc WatchOrderStatus(WatchOrderStatusRequest) returns (stream OrderStatusUpdate);

  // Client streaming - client sends multiple messages
  rpc UploadOrderItems(stream OrderItem) returns (UploadSummary);

  // Bidirectional streaming
  rpc OrderChat(stream ChatMessage) returns (stream ChatMessage);
}
```

### Streaming Patterns

| Pattern | Use Case | Example |
|---------|----------|---------|
| **Unary** | Simple CRUD | Get order, create user |
| **Server streaming** | Real-time feeds, large result sets | Price ticker, log tailing |
| **Client streaming** | Bulk uploads, telemetry | File upload, metric ingestion |
| **Bidirectional** | Chat, collaborative editing | Real-time collaboration |

### gRPC Error Handling

gRPC uses status codes (not HTTP codes). Map them correctly:

| gRPC Code | HTTP Equivalent | When to Use |
|-----------|-----------------|-------------|
| OK | 200 | Success |
| INVALID_ARGUMENT | 400 | Client sent bad data |
| UNAUTHENTICATED | 401 | Missing or invalid credentials |
| PERMISSION_DENIED | 403 | Authenticated but not authorized |
| NOT_FOUND | 404 | Resource does not exist |
| ALREADY_EXISTS | 409 | Duplicate creation attempt |
| RESOURCE_EXHAUSTED | 429 | Rate limit exceeded |
| INTERNAL | 500 | Server bug |
| UNAVAILABLE | 503 | Transient failure — client should retry |
| DEADLINE_EXCEEDED | 504 | Timeout |

**Rich error details**: Use `google.rpc.Status` with `details` field for structured error metadata (error info, retry info, debug info).

### gRPC Best Practices

1. **Set deadlines on every call** — no call should wait forever
2. **Use interceptors** for cross-cutting concerns (auth, logging, metrics)
3. **Design for backward compatibility** — never reuse field numbers, add new fields instead
4. **Keep messages small** — stream large payloads rather than sending single large messages
5. **Use reflection** in development but disable in production

---

## API Versioning Strategies

### Decision Framework

| Strategy | Mechanism | Pros | Cons | Best For |
|----------|-----------|------|------|----------|
| **URL path** | `/v1/users` | Simple, visible, cacheable | URL changes, client updates needed | Public APIs, most common |
| **Header** | `Accept: application/vnd.api.v2+json` | Clean URLs, content negotiation | Hidden, harder to test | Internal APIs, sophisticated consumers |
| **Query parameter** | `/users?version=2` | Easy to test, no URL change | Breaks caching, feels hacky | Transitional, rarely recommended |
| **No versioning** | Additive changes only | No version management | Limits evolution | Small, controlled consumer base |

**Recommended default**: URL path versioning. It is explicit, discoverable, and works with all HTTP tooling.

### Versioning Rules

1. **Semantic versioning for APIs**: Major (breaking) = new URL version. Minor/patch = backward-compatible additions.
2. **What constitutes a breaking change**:
   - Removing or renaming a field
   - Changing a field's type
   - Adding a required field to a request
   - Changing the meaning of a status code
   - Removing an endpoint
   - Changing authentication requirements
3. **What is NOT a breaking change**:
   - Adding an optional field to a response
   - Adding a new endpoint
   - Adding an optional query parameter
   - Adding a new enum value (if clients handle unknown values)
4. **Deprecation timeline template**:
   ```
   v1 released: 2025-01-01
   v2 released: 2025-07-01 (v1 deprecated notice)
   v1 sunset warning: 2025-10-01 (Sunset header + documentation)
   v1 shutdown: 2026-01-01 (minimum 6 months after v2 GA)
   ```
5. **Sunset header** (RFC 8594): `Sunset: Sat, 01 Jan 2026 00:00:00 GMT`
6. **Deprecation header**: `Deprecation: true`

---

## Authentication & Authorization

### Method Selection

| Method | Use Case | Security Level | Complexity |
|--------|----------|---------------|------------|
| **API Keys** | Server-to-server, low sensitivity | Low | Low |
| **OAuth 2.0 + PKCE** | User-facing apps, delegated access | High | High |
| **JWT (Bearer)** | Stateless auth, microservices | Medium-High | Medium |
| **Mutual TLS** | Service mesh, zero-trust | Very High | Very High |
| **API Keys + HMAC** | Webhook verification, signed requests | High | Medium |

### OAuth 2.0 Flows

| Flow | Client Type | Use Case |
|------|-------------|----------|
| **Authorization Code + PKCE** | SPA, mobile, server-side | User login — the default for most apps |
| **Client Credentials** | Machine-to-machine | Service accounts, cron jobs, backend integrations |
| **Device Code** | TV, CLI, IoT | Input-constrained devices |
| **Refresh Token** | Any long-lived session | Maintain access without re-authentication |

**Deprecated flows** (do not use): Implicit flow, Resource Owner Password Credentials (ROPC).

### JWT Best Practices

| Concern | Guidance |
|---------|----------|
| Signing algorithm | RS256 (asymmetric) for distributed systems, HS256 (symmetric) only for single-service |
| Token lifetime | Access token: 15-60 minutes. Refresh token: 7-30 days |
| Claims | Include `sub`, `iss`, `exp`, `iat`, `aud`. Keep custom claims minimal |
| Storage (browser) | HttpOnly, Secure, SameSite=Strict cookie. Never localStorage |
| Revocation | Short-lived tokens + refresh token rotation. Blocklist for immediate revocation |
| Size | Keep under 1KB. JWTs go in every request header |

### Scopes and Permissions

Design scopes as `resource:action` pairs:
```
users:read        — Read user profiles
users:write       — Create and update users
orders:read       — Read orders
orders:write      — Create orders
orders:admin      — Cancel, refund, modify any order
```

**Rules**:
1. Default to least privilege — new clients get minimal scopes
2. Separate read and write scopes for every resource
3. Admin scopes require explicit approval flow
4. Document every scope in the API reference

---

## Rate Limiting and Throttling

### Strategy Selection

| Strategy | How It Works | Best For |
|----------|-------------|----------|
| **Fixed window** | Count requests per time window (e.g., 100/minute) | Simple, but allows bursts at window boundaries |
| **Sliding window** | Weighted average of current and previous window | Smoother than fixed window, moderate complexity |
| **Token bucket** | Tokens replenish at fixed rate, each request costs one | Allows controlled bursts, most flexible |
| **Leaky bucket** | Requests queue and process at fixed rate | Strict rate enforcement, smooths traffic |

### Response Headers (IETF draft-polli-ratelimit)

Always return rate limit information in response headers:

```
RateLimit-Limit: 100
RateLimit-Remaining: 45
RateLimit-Reset: 30
Retry-After: 30          (on 429 responses)
```

### Rate Limit Design

| Dimension | Example |
|-----------|---------|
| Per API key | 1000 requests/hour |
| Per user | 100 requests/minute |
| Per endpoint | 10 requests/second for expensive operations |
| Per IP | 50 requests/minute for unauthenticated |
| Per plan/tier | Free: 100/hr, Pro: 10,000/hr, Enterprise: custom |

**Response on limit exceeded**:
```json
HTTP/1.1 429 Too Many Requests
Retry-After: 30
Content-Type: application/problem+json

{
  "type": "https://api.example.com/errors/rate-limit-exceeded",
  "title": "Rate Limit Exceeded",
  "status": 429,
  "detail": "You have exceeded 100 requests per minute. Retry after 30 seconds.",
  "instance": "/v1/users"
}
```

---

## API Gateway Patterns

### Core Gateway Responsibilities

| Capability | Description |
|------------|-------------|
| **Routing** | Route requests to appropriate backend services |
| **Authentication** | Validate tokens, API keys before reaching backends |
| **Rate limiting** | Enforce per-consumer rate limits centrally |
| **Request transformation** | Modify headers, paths, payloads between client and service |
| **Response aggregation** | Combine responses from multiple services (BFF pattern) |
| **Caching** | Cache GET responses at the edge |
| **Circuit breaking** | Stop routing to failing backends |
| **Observability** | Centralized logging, metrics, tracing |
| **TLS termination** | Handle SSL/TLS at the gateway, not each service |

### Gateway Architecture Patterns

| Pattern | Description | When |
|---------|-------------|------|
| **Single gateway** | One gateway for all consumers | Small API surface, single team |
| **BFF (Backend for Frontend)** | Separate gateway per consumer type (web, mobile, partner) | Different clients need different API shapes |
| **Federated gateway** | Each team manages their own gateway config | Large org, many teams, many services |
| **Sidecar proxy** | Gateway logic runs as sidecar (e.g., Envoy) per service | Service mesh, fine-grained control |

**Anti-patterns**:
- Putting business logic in the gateway — gateways handle cross-cutting concerns only
- Single gateway bottleneck — scale horizontally, use circuit breakers
- Gateway as ESB — do not build an Enterprise Service Bus disguised as a gateway

---

## Pagination Approaches

### Selection Framework

| Approach | Mechanism | Pros | Cons | Best For |
|----------|-----------|------|------|----------|
| **Offset** | `?offset=20&limit=10` | Simple, random access | Skips/duplicates on insert, slow on large offsets | Admin UIs, small datasets |
| **Cursor** | `?after=abc123&limit=10` | Consistent on insert/delete, fast | No random access, opaque cursors | Feeds, timelines, real-time data |
| **Keyset** | `?created_after=2025-01-01&limit=10` | Fast (index-based), transparent | Requires sortable unique column | Time-series, log data |
| **Page number** | `?page=3&per_page=20` | Familiar UX | Same issues as offset | Simple CRUD, traditional UIs |

### Standard Pagination Response

```json
{
  "data": [ ... ],
  "pagination": {
    "total": 1234,
    "limit": 20,
    "has_more": true,
    "next_cursor": "eyJpZCI6MTAwfQ=="
  },
  "_links": {
    "next": { "href": "/v1/orders?after=eyJpZCI6MTAwfQ==&limit=20" },
    "prev": { "href": "/v1/orders?before=eyJpZCI6ODF9&limit=20" }
  }
}
```

**Rules**:
1. Default `limit` should be reasonable (20-50). Maximum should be enforced (100-200).
2. Always return `has_more` or equivalent so clients know when to stop.
3. For cursor-based pagination, cursors should be opaque (base64-encoded) — do not expose internal IDs.
4. Include `total` count only if cheap to compute. Omit or make it optional for large datasets.
5. Use consistent pagination across all endpoints — do not mix approaches.

---

## Error Handling — RFC 7807 Problem Details

### Standard Error Response Format

All errors should use `application/problem+json` (RFC 7807, updated by RFC 9457):

```json
{
  "type": "https://api.example.com/errors/insufficient-funds",
  "title": "Insufficient Funds",
  "status": 422,
  "detail": "Account acc_123 has a balance of $5.00, but the transfer requires $10.00.",
  "instance": "/v1/transfers/txn_456",
  "balance": 5.00,
  "required": 10.00
}
```

### Field Definitions

| Field | Required | Description |
|-------|----------|-------------|
| `type` | Yes | URI reference identifying the error type. Use `about:blank` for generic HTTP errors |
| `title` | Yes | Human-readable summary. Should be consistent for the same `type` |
| `status` | Yes | HTTP status code (redundant with header, but useful for logging) |
| `detail` | Yes | Human-readable explanation specific to this occurrence |
| `instance` | No | URI reference identifying the specific occurrence |
| Extension fields | No | Additional machine-readable data specific to the error type |

### Validation Error Pattern

```json
{
  "type": "https://api.example.com/errors/validation-error",
  "title": "Validation Error",
  "status": 422,
  "detail": "The request body contains 2 validation errors.",
  "errors": [
    {
      "field": "email",
      "code": "INVALID_FORMAT",
      "message": "Must be a valid email address"
    },
    {
      "field": "age",
      "code": "OUT_OF_RANGE",
      "message": "Must be between 18 and 120"
    }
  ]
}
```

### Error Design Rules

1. **Never expose stack traces** in production — log them server-side, return a correlation ID
2. **Use error codes, not just messages** — `INVALID_FORMAT` is parseable; "Must be a valid email" is not
3. **Include a correlation ID** — `"trace_id": "abc-123-def"` for support and debugging
4. **Be specific but safe** — "User not found" is fine; "SQL query failed: SELECT * FROM users WHERE..." is not
5. **Localize messages** — use `Accept-Language` header to return localized `detail` text
6. **Document every error type** — each `type` URI should resolve to documentation explaining the error and resolution

---

## API Documentation — OpenAPI / Swagger

### OpenAPI 3.1 Structure

```yaml
openapi: 3.1.0
info:
  title: Order API
  version: 1.0.0
  description: Manage customer orders
  contact:
    name: API Support
    email: api-support@example.com
  license:
    name: MIT

servers:
  - url: https://api.example.com/v1
    description: Production
  - url: https://api.staging.example.com/v1
    description: Staging

paths:
  /orders:
    get:
      summary: List orders
      operationId: listOrders
      tags: [Orders]
      parameters:
        - $ref: '#/components/parameters/PageLimit'
        - $ref: '#/components/parameters/PageCursor'
      responses:
        '200':
          description: List of orders
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/OrderList'
              examples:
                default:
                  $ref: '#/components/examples/OrderListExample'
```

### Documentation Quality Checklist

| Requirement | Details |
|-------------|---------|
| Every endpoint has examples | Request body + response for every status code |
| Authentication documented | Security schemes defined, scopes listed per endpoint |
| Error responses documented | Every possible error code with example body |
| Pagination documented | Query parameters, response format, cursor usage |
| Rate limits documented | Headers, limits per tier, retry behavior |
| Changelog maintained | Every change with date, version, and migration notes |
| SDKs generated | OpenAPI spec used to auto-generate client libraries |

### Documentation Anti-Patterns

- Auto-generated docs with no examples — useless for onboarding
- Documenting only success cases — error handling is what developers need most
- Stale documentation — CI pipeline should validate spec against implementation
- No sandbox/playground — developers cannot try before they integrate

---

## Webhook Design Patterns

### Webhook Architecture

| Component | Responsibility |
|-----------|----------------|
| **Event producer** | Detects state changes, creates event payloads |
| **Delivery system** | Queues, retries, delivers HTTP POST to subscriber URLs |
| **Subscriber** | Registers URL, receives events, returns 2xx to acknowledge |

### Webhook Design Rules

1. **POST to subscriber URL** with event payload in the body
2. **Sign every payload** with HMAC-SHA256 using a per-subscriber secret
   ```
   X-Webhook-Signature: sha256=5d7ab3...
   X-Webhook-Timestamp: 1679012345
   ```
3. **Include event metadata** — event type, timestamp, idempotency key
4. **Retry with exponential backoff** — 1s, 5s, 30s, 5m, 30m, 2h, 8h (then disable)
5. **Provide a replay endpoint** — let subscribers re-request missed events
6. **Send thin payloads** — include the event type and resource ID; let consumers fetch full details if needed (prevents stale data in retries)
7. **Support event type filtering** — subscribers should select which events they receive

### Webhook Event Payload Template

```json
{
  "id": "evt_abc123",
  "type": "order.completed",
  "created_at": "2025-06-15T10:30:00Z",
  "api_version": "2025-06-01",
  "data": {
    "object": {
      "id": "ord_xyz789",
      "status": "completed",
      "total": 99.99
    },
    "previous_attributes": {
      "status": "processing"
    }
  }
}
```

### Webhook Security

| Concern | Mitigation |
|---------|------------|
| Replay attacks | Include timestamp; reject events older than 5 minutes |
| Payload tampering | HMAC signature verification |
| Subscriber URL spoofing | Verification handshake on registration (challenge-response) |
| Denial of service | Rate limit outgoing webhooks; circuit break on repeated failures |

---

## Idempotency Patterns

### Why Idempotency Matters

Network failures cause retries. Without idempotency, retries create duplicate resources, double charges, and inconsistent state.

### Implementation

**Client-generated idempotency key**:
```
POST /v1/payments
Idempotency-Key: idem_abc123xyz

{ "amount": 100, "currency": "USD" }
```

**Server behavior**:

| Scenario | Action |
|----------|--------|
| First request with this key | Process normally, store key + response |
| Retry with same key + same body | Return stored response (do not reprocess) |
| Retry with same key + different body | Return 422 with error explaining the conflict |
| Key not provided on non-idempotent endpoint | Return 400 requiring the key |

### Design Rules

1. **Require idempotency keys on all non-idempotent operations** — POST, PATCH that creates side effects
2. **Keys should be client-generated UUIDs** — server should not generate them
3. **Key scope**: per API key or per user (not global)
4. **Key TTL**: 24-48 hours. After expiry, the same key creates a new operation
5. **Store the full response** — replay the exact response on retry, including status code and headers
6. **GET, PUT, DELETE are naturally idempotent** — no key needed (but PUT and DELETE must be implemented correctly)

---

## CQRS and Event-Driven API Patterns

### CQRS (Command Query Responsibility Segregation)

Separate the write model (commands) from the read model (queries).

| Aspect | Command Side | Query Side |
|--------|-------------|------------|
| Purpose | Validate and execute state changes | Serve optimized read views |
| Model | Domain model with business rules | Denormalized projections |
| Store | Event store or write-optimized DB | Read-optimized DB, cache, search index |
| API style | POST/PUT/PATCH/DELETE | GET (or GraphQL queries) |
| Consistency | Strongly consistent writes | Eventually consistent reads |

### Event-Driven API Patterns

| Pattern | Description | Use When |
|---------|-------------|----------|
| **Event notification** | Thin event ("order created") triggers consumer to fetch details | Consumers need current state, not historical |
| **Event-carried state** | Full entity in event payload | Consumers need to avoid callback API calls |
| **Event sourcing** | Events ARE the source of truth; state is derived | Audit trail required, complex domain logic |
| **Domain events** | Internal events within a bounded context | Decoupling modules within a monolith |

### Event Design Template

```json
{
  "event_id": "evt_unique_id",
  "event_type": "com.example.order.completed.v1",
  "source": "order-service",
  "time": "2025-06-15T10:30:00Z",
  "data_content_type": "application/json",
  "data": { ... },
  "metadata": {
    "correlation_id": "corr_abc",
    "causation_id": "evt_previous",
    "user_id": "usr_initiator"
  }
}
```

**CloudEvents specification** (CNCF standard) provides a standardized envelope. Prefer it for interoperability.

---

## Backward Compatibility Rules

### The Robustness Principle (Postel's Law)

> "Be conservative in what you send, be liberal in what you accept."

### Compatibility Checklist

| Change Type | Backward Compatible? | Action Required |
|-------------|---------------------|-----------------|
| Add optional response field | Yes | None — clients should ignore unknown fields |
| Add optional request parameter | Yes | None — defaults apply |
| Add new endpoint | Yes | Document and announce |
| Add new enum value | Depends | Only if clients handle unknown values gracefully |
| Remove response field | **No** | New API version |
| Remove endpoint | **No** | New API version with deprecation period |
| Rename field | **No** | New API version (or support both temporarily) |
| Change field type | **No** | New API version |
| Make optional field required | **No** | New API version |
| Change error format | **No** | New API version |
| Change authentication | **No** | New API version with migration period |

### Evolution Strategy

1. **Additive changes only** within a version — add fields, endpoints, optional parameters
2. **Use feature flags** for gradual rollout of new behavior
3. **Support old and new simultaneously** during transition periods
4. **Consumer-driven contract testing** — verify that changes do not break existing consumers
5. **Deprecation warnings** — `Deprecation: true` header + sunset date + migration guide

---

## API Security — OWASP API Security Top 10 (2023)

| # | Vulnerability | Mitigation |
|---|--------------|------------|
| **API1** | Broken Object Level Authorization (BOLA) | Verify user owns the resource on every request. Never trust client-supplied IDs alone |
| **API2** | Broken Authentication | Use standard OAuth 2.0 / OIDC. Enforce rate limiting on auth endpoints. Require MFA for sensitive operations |
| **API3** | Broken Object Property Level Authorization | Return only fields the user is authorized to see. Validate writable fields on input |
| **API4** | Unrestricted Resource Consumption | Rate limiting, payload size limits, pagination limits, query complexity limits |
| **API5** | Broken Function Level Authorization | Role-based access checks on every endpoint. Admin functions on separate paths |
| **API6** | Unrestricted Access to Sensitive Business Flows | Detect and throttle automated abuse (credential stuffing, scraping, checkout bots) |
| **API7** | Server Side Request Forgery (SSRF) | Validate and sanitize all URLs. Allowlist outbound destinations. Block internal IPs |
| **API8** | Security Misconfiguration | Disable debug mode, restrict CORS, enforce HTTPS, remove default credentials, disable unnecessary HTTP methods |
| **API9** | Improper Inventory Management | Maintain an API inventory. Deprecate and remove old versions. Monitor shadow/zombie APIs |
| **API10** | Unsafe Consumption of APIs | Validate all data from third-party APIs. Apply timeouts, rate limits, circuit breakers to outbound calls |

### Security Headers Checklist

```
Strict-Transport-Security: max-age=63072000; includeSubDomains; preload
Content-Security-Policy: default-src 'none'; frame-ancestors 'none'
X-Content-Type-Options: nosniff
X-Frame-Options: DENY
Cache-Control: no-store (for sensitive responses)
```

### Input Validation Rules

1. **Validate content type** — reject requests with wrong `Content-Type`
2. **Validate content length** — enforce maximum payload sizes
3. **Validate all input** — type, range, format, length for every field
4. **Sanitize output** — encode responses to prevent XSS in API consumers that render HTML
5. **Reject unknown fields** — strict mode parsing (optional, but recommended for security-sensitive APIs)

---

## API Testing Strategies

### Testing Pyramid for APIs

| Layer | What You Test | Tools / Approach |
|-------|--------------|-----------------|
| **Contract tests** | API spec matches implementation | OpenAPI validator, Spectral, consumer-driven contracts (Pact) |
| **Unit tests** | Individual handler/resolver logic | Standard unit test frameworks |
| **Integration tests** | Endpoint behavior with real dependencies | Test against running service with test DB |
| **Load tests** | Performance under expected and peak load | k6, Gatling, Locust |
| **Security tests** | Vulnerabilities, auth bypass, injection | OWASP ZAP, Burp Suite, custom fuzzing |
| **Chaos tests** | Behavior under failure conditions | Simulated latency, dropped connections, partial failures |

### Contract Testing Approach

```
1. API spec (OpenAPI) is the source of truth
2. CI pipeline validates implementation against spec on every commit
3. Consumer teams write consumer-driven contracts (Pact)
4. Provider CI runs consumer contracts before deploying
5. Breaking changes are caught before they reach production
```

### Test Checklist Per Endpoint

| Category | Tests |
|----------|-------|
| **Happy path** | Valid request returns expected response and status code |
| **Validation** | Invalid input returns 400/422 with clear error details |
| **Authentication** | Missing token returns 401; invalid token returns 401; expired token returns 401 |
| **Authorization** | Valid token but wrong scope returns 403; accessing another user's resource returns 403 |
| **Pagination** | First page, middle page, last page, empty results, invalid cursor |
| **Rate limiting** | Exceeding limit returns 429 with Retry-After header |
| **Idempotency** | Retry with same key returns same response; different body returns 422 |
| **Concurrency** | Simultaneous updates handled (optimistic locking, ETags) |
| **Edge cases** | Empty body, missing content-type, extra fields, unicode in strings, large payloads |

---

## Common Pitfalls

| Pitfall | Why It Happens | How to Avoid |
|---------|---------------|--------------|
| **Designing the API after implementation** | "We will just expose the database" | Contract-first: OpenAPI spec reviewed and approved before code begins |
| **Inconsistent naming** | Multiple teams, no standards doc | Publish an API style guide and lint against it in CI |
| **No pagination on collections** | "We only have 50 records" | Every collection endpoint gets pagination from day one |
| **Breaking changes without versioning** | "Nobody uses that field" | Consumer-driven contract tests catch what you miss |
| **Leaking internal structure** | Database column names in API responses | Design API types from consumer needs, not table schemas |
| **Auth as afterthought** | "We will add auth later" | Define auth requirements in the OpenAPI spec before implementation |
| **No rate limiting** | "Our users are trusted" | One misbehaving client can take down the service for everyone |
| **Ignoring error design** | "Just return 500 with a message" | RFC 7807 Problem Details from the start. Document every error type |
| **Overloading GET with body** | "We need complex filters" | Use POST for complex queries with a body; keep GET for simple queries with URL params |
| **Chatty APIs** | One resource per endpoint, forcing multiple round trips | Design for common access patterns; offer `include`/`expand` for related resources |
| **No idempotency on writes** | "Retries are the client's problem" | Require idempotency keys on POST endpoints that create resources or trigger side effects |
| **Webhook without signature** | "It is an internal webhook" | Always sign. Internal today, external tomorrow. Security is not optional |
| **Testing only happy paths** | Time pressure | The error path test checklist above is the minimum bar |

---

## Quick Reference: API Design Checklist

Use this checklist before publishing any new API or endpoint:

```markdown
## API Design Review Checklist

### Naming & Structure
- [ ] Resources use plural nouns (`/users`, not `/user`)
- [ ] URLs use lowercase with hyphens
- [ ] Nesting is at most 2 levels deep
- [ ] HTTP methods match semantics (GET reads, POST creates, etc.)

### Contract
- [ ] OpenAPI spec written and reviewed before implementation
- [ ] Every endpoint has request/response examples
- [ ] Every error response is documented with Problem Details format

### Pagination & Filtering
- [ ] Collection endpoints are paginated
- [ ] Default and maximum page sizes are defined
- [ ] Filter parameters use consistent naming

### Authentication & Authorization
- [ ] Auth requirements defined per endpoint
- [ ] Scopes follow `resource:action` pattern
- [ ] BOLA protection: ownership verified on every request

### Error Handling
- [ ] RFC 7807 Problem Details format
- [ ] Validation errors include field-level detail
- [ ] No stack traces or internal details in production errors
- [ ] Correlation ID included for debugging

### Versioning & Compatibility
- [ ] Version in URL path (`/v1/...`)
- [ ] No breaking changes within a version
- [ ] Deprecation timeline documented

### Security
- [ ] Rate limiting configured
- [ ] Input validation on all fields
- [ ] Security headers set
- [ ] CORS configured restrictively

### Operations
- [ ] Idempotency keys required on non-idempotent operations
- [ ] Webhook signatures implemented (if applicable)
- [ ] Health check endpoint exists
- [ ] Metrics and logging in place
```
