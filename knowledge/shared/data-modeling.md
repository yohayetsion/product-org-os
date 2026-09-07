# Data Modeling Patterns — Frameworks & Methods

## Overview

Data modeling is the discipline of defining how data is structured, stored, and related within a system. Good data models encode business rules, enable query patterns, and evolve gracefully over time. Poor data models create compounding technical debt: every application layer built on a bad model inherits its contradictions.

This reference covers relational and NoSQL modeling, event-driven patterns, partitioning, and migration strategies. The guidance is ordered from foundational to specialized — start with relational patterns unless you have evidence that another paradigm better fits your read/write access patterns.

**Version**: 1.0.0
**Type**: Knowledge Pack
**Primary Users**: 🗄️ Data Architect, 🏗️ Chief Architect, 🔧 Backend Developer

---
<!-- Attribution:
  Frameworks and patterns in this knowledge pack were informed by:
  - Internal ER modeling, NoSQL, and event sourcing best practices
  - Martin Fowler's "Patterns of Enterprise Application Architecture"
  - Joe Celko's SQL for Smarties (hierarchy patterns)
  - Martin Kleppmann's "Designing Data-Intensive Applications"
  2026-06 delta sources:
  - dbt Core v1.12 Semantic Layer spec — docs.getdbt.com/blog/modernizing-the-semantic-layer-spec, docs.getdbt.com/docs/build/latest-metrics-spec (per dbt docs / license)
  - Databricks "Unity Catalog and the next era of Apache Iceberg" — databricks.com/blog/unity-catalog-and-next-era-apache-icebergtm
  - Snowflake Summit 2026: Open Semantic Interchange (Apache-2.0) — snowflake.com/en/blog/open-semantic-interchanges-specs-finalized/; Atlan Summit 2026 recap — atlan.com/know/snowflake/summit-2026-announcements/
  Adapted and expanded for Product Org OS agents.
-->

---

## Entity-Relationship Modeling

### Three Levels of Abstraction

**When to use**: All relational data modeling starts here. Work top-down: conceptual → logical → physical.

| Level | Purpose | Audience | Contains |
|-------|---------|----------|----------|
| **Conceptual** | Business understanding; what entities exist | Business stakeholders | Entities and high-level relationships only |
| **Logical** | Technology-independent data structure | Architects, senior devs | Entities, attributes, keys, cardinality, normalization |
| **Physical** | Database-specific implementation | DBAs, backend devs | Tables, columns, data types, indexes, constraints, partitions |

**Process**:
```
1. Identify entities (nouns in the business domain)
2. Identify relationships (verbs between entities)
3. Define cardinality (one-to-one, one-to-many, many-to-many)
4. Assign attributes to entities (not relationships, unless associative)
5. Identify candidate keys, choose primary keys
6. Normalize to remove redundancy (see Normalization section)
7. Denormalize selectively for performance (see Anti-Patterns)
```

---

### ER Diagram Notation

**Three major notations — choose one and stay consistent within a project.**

#### Chen Notation
```
[ENTITY]───◇───[RELATIONSHIP]───◇───[ENTITY]
  │                                    │
(attribute)                        (attribute)

Cardinality: 1, N, M placed on the line near the entity
```

#### Crow's Foot Notation (preferred for physical models)
```
ENTITY_A ──|o────<── ENTITY_B

Symbols (read at the entity end of the line):
  |    exactly one
  O    zero
  <    many (crow's foot)

Examples:
  ──|──|──   exactly one to exactly one
  ──|──O──   exactly one to zero or one
  ──|──<──   exactly one to one or many (mandatory one-to-many)
  ──O──<──   zero or one to one or many (optional one-to-many)
  ──O──<<─   zero or many to zero or many (many-to-many)
```

#### UML Class Diagram Notation
```
+----------------+       1..*       +----------------+
|    Order       |─────────────────>|   OrderLine    |
+----------------+                  +----------------+
| orderId: UUID  |                  | lineId: UUID   |
| customerId: FK |                  | orderId: FK    |
| createdAt: TS  |                  | productId: FK  |
+----------------+                  | quantity: INT  |
                                    +----------------+

Multiplicity: 1 (exactly one), * (many), 0..1 (optional), 1..* (one or more)
```

---

## Normalization

### Normal Forms Reference

**When to use**: Apply during logical modeling. Aim for 3NF by default; consider BCNF for complex key structures; 4NF/5NF only when multi-valued dependencies create real anomalies.

#### First Normal Form (1NF)
**Rule**: Every column contains atomic (indivisible) values. No repeating groups.

```
VIOLATION — multi-valued column:
Orders: | orderId | items              | total |
        | 1       | "pen, notebook"    | 15.00 |

FIX — extract to separate table:
Orders:    | orderId | total |
OrderItems:| orderId | item  |
```

**Key question**: Can a column value be split further and still be meaningful?

#### Second Normal Form (2NF)
**Rule**: Must be in 1NF. Every non-key attribute must depend on the WHOLE primary key (no partial dependencies). Only applies when the primary key is composite.

```
VIOLATION — partial dependency on composite key:
OrderItems: | orderId | productId | productName | quantity |
            ProductName depends only on productId, not on (orderId, productId)

FIX:
OrderItems: | orderId | productId | quantity |
Products:   | productId | productName |
```

#### Third Normal Form (3NF)
**Rule**: Must be in 2NF. No transitive dependencies — non-key attributes must not depend on other non-key attributes.

```
VIOLATION — transitive dependency:
Employees: | empId | deptId | deptName | salary |
           deptName depends on deptId, not directly on empId

FIX:
Employees:   | empId | deptId | salary |
Departments: | deptId | deptName |
```

**3NF is the practical default for OLTP systems.**

#### Boyce-Codd Normal Form (BCNF)
**Rule**: For every functional dependency X → Y, X must be a superkey. Stricter than 3NF; relevant when a table has multiple overlapping candidate keys.

#### Fourth Normal Form (4NF)
**Rule**: No multi-valued dependencies other than those implied by a superkey.

```
VIOLATION — independent multi-valued facts in one table:
Skills: | empId | language | certification |
        Languages and certifications are independent; each creates a Cartesian product

FIX:
EmpLanguages:      | empId | language |
EmpCertifications: | empId | certification |
```

#### Fifth Normal Form (5NF)
**Rule**: No join dependencies that are not implied by candidate keys. Decompose tables that can only be reconstructed by joining three or more tables. Rarely needed in practice.

---

### When to Denormalize

**Deliberate denormalization is valid when**:
- Read performance is critical and joins across hot tables are expensive
- Data is read-heavy and write-light (reporting, analytics, dashboards)
- The denormalized value is derived and recalculated on write (computed columns)
- Separate OLAP/reporting layer from OLTP source (ETL → data warehouse)

**Denormalization patterns**:
- Duplicate a column to avoid a join (e.g., store `customerName` on `Orders`)
- Pre-aggregate totals on a parent row (e.g., `orderLineCount` on `Order`)
- Materialized views for complex read queries
- Separate OLAP schema (star/snowflake) from normalized OLTP source

**Warning**: Denormalized data must be kept consistent. Every write path must update all copies. Missing an update path creates data inconsistency bugs that are hard to detect.

---

## Relational Schema Design Patterns

### Polymorphic Associations

**Problem**: A single table needs to relate to multiple parent tables (e.g., `Comments` on both `Posts` and `Videos`).

**Pattern A — Exclusive Arc** (simple, constrained):
```sql
Comments (
  commentId     UUID PRIMARY KEY,
  postId        UUID REFERENCES Posts(postId),    -- nullable
  videoId       UUID REFERENCES Videos(videoId),  -- nullable
  -- CONSTRAINT: exactly one of postId, videoId must be non-null
  CONSTRAINT chk_one_parent CHECK (
    (postId IS NOT NULL)::int + (videoId IS NOT NULL)::int = 1
  )
)
```
Pro: Referential integrity. Con: Adding a new parent type requires a schema change.

**Pattern B — Generic FK + Type Discriminator** (flexible, no FK constraint):
```sql
Comments (
  commentId     UUID PRIMARY KEY,
  parentType    VARCHAR(50) NOT NULL,  -- 'post', 'video'
  parentId      UUID NOT NULL,
  -- No FK constraint — enforced at application layer
  INDEX idx_parent (parentType, parentId)
)
```
Pro: Easy to extend. Con: No database-level referential integrity; orphaned records possible.

**Pattern C — Separate Junction Tables** (cleanest, most normalized):
```sql
PostComments  (commentId UUID, postId UUID)
VideoComments (commentId UUID, videoId UUID)
```
Pro: Full referential integrity, clear ownership. Con: Queries across types require UNIONs.

**Recommendation**: Pattern A for 2-3 fixed parent types. Pattern C for clean relational design. Pattern B when flexibility outweighs integrity concerns.

---

### Entity-Attribute-Value (EAV)

**Problem**: Entities have highly variable, schema-less attributes (e.g., product catalog with hundreds of optional specs per category).

**Pattern**:
```sql
Products    (productId, name, categoryId)
Attributes  (attributeId, name, dataType)
ProductAttr (productId, attributeId, value VARCHAR)
```

**When EAV is justified**:
- Truly dynamic attributes that cannot be known at schema design time
- Number of attribute types is unbounded
- Most attributes sparse (most products have only a few)

**EAV limitations** (see Anti-Patterns section):
- No data type enforcement on `value` column
- Querying specific attributes requires pivot or self-joins — poor performance
- Foreign key constraints on attribute values impossible
- Reporting across attributes is complex

**Alternative**: Use JSONB column in PostgreSQL for semi-structured attributes with indexing support.

---

### Hierarchy Patterns

**Problem**: Represent tree structures (categories, org charts, threaded comments, folder hierarchies).

#### Adjacency List
```sql
Categories (categoryId, name, parentId REFERENCES Categories(categoryId))
```
- Simple to insert and move nodes
- Retrieving the full subtree requires recursive CTEs (WITH RECURSIVE)
- Good for shallow hierarchies or when full-tree queries are rare

#### Nested Sets
```sql
Categories (categoryId, name, lft INT, rgt INT)
-- All descendants: WHERE lft BETWEEN parent.lft AND parent.rgt
-- Parent count (depth): SELECT COUNT(*) WHERE lft < node.lft AND rgt > node.rgt
```
- Fast subtree reads (single range query)
- Expensive inserts/moves (rewrite lft/rgt for large portions of tree)
- Good for read-heavy, rarely changing hierarchies

#### Closure Table (recommended for most cases)
```sql
Categories     (categoryId, name)
CategoryPaths  (ancestorId, descendantId, depth)
-- Ancestors: SELECT * FROM CategoryPaths WHERE descendantId = ?
-- Descendants: SELECT * FROM CategoryPaths WHERE ancestorId = ?
-- Direct children: WHERE ancestorId = ? AND depth = 1
```
- Fast reads for any ancestor/descendant query
- Clean inserts: add one row per ancestor + self
- Move = delete old paths, insert new paths
- Slightly larger storage footprint
- Best balance of read performance and write simplicity

---

## NoSQL Data Modeling

### Choosing the Right NoSQL Store

**Decision Matrix**:

| Use Case | Recommended Store | Why |
|----------|------------------|-----|
| Flexible documents, rich queries | Document (MongoDB, Firestore) | Schema flexibility, nested data |
| Simple fast lookups by key | Key-Value (Redis, DynamoDB) | O(1) access, high throughput |
| Write-heavy time series, wide rows | Wide-Column (Cassandra, HBase) | Optimized for partition + sort key access |
| Highly connected data, traversal queries | Graph (Neo4j, Amazon Neptune) | Native relationship traversal |
| Full-text search | Search (Elasticsearch) | Inverted index, relevance scoring |

**Rule**: Model for your read patterns, not your write patterns. In NoSQL, the query drives the schema design.

---

### Document Store Patterns (MongoDB)

#### Embedding vs. Referencing

**Embed when**:
- Data is accessed together (parent always fetched with child)
- Child data is exclusively owned by parent (no other relationships)
- Child set is bounded and small (under ~100 items)
- Data is rarely updated independently

```javascript
// Embedded — order with lines (always fetched together, bounded set)
{
  _id: "ord_123",
  customerId: "cust_456",
  status: "confirmed",
  lines: [
    { productId: "prod_789", qty: 2, unitPrice: 19.99 },
    { productId: "prod_101", qty: 1, unitPrice: 49.99 }
  ],
  total: 89.97
}
```

**Reference when**:
- Child data is shared across multiple parents
- Child set is unbounded (can grow without limit)
- Child data is updated independently and frequently
- You need to query children directly without fetching parent

```javascript
// Referenced — posts with author (author shared, queried independently)
{ _id: "post_123", title: "...", authorId: "user_456", tags: ["mongodb"] }
{ _id: "user_456", name: "Alice", email: "alice@example.com" }
```

#### Schema Versioning
```javascript
// Always include a schema version field
{
  _id: "doc_123",
  _schemaVersion: 2,    // increment when schema changes
  // ... fields for version 2
}

// Migration strategy: lazy migration on read
function readDocument(doc) {
  if (doc._schemaVersion === 1) return migrateV1toV2(doc);
  return doc;
}
```

---

### Key-Value Store Patterns (Redis)

#### Cache-Aside (Lazy Loading)
```
Read path:
  1. Check cache: GET product:{id}
  2. Cache hit → return cached value
  3. Cache miss → query database → SET product:{id} value EX 3600 → return value

Write path:
  1. Write to database
  2. DEL product:{id}  (invalidate, don't update — avoids race conditions)
```
Best for: Read-heavy data with acceptable staleness window. Default caching pattern.

#### Write-Through
```
Write path:
  1. SET product:{id} value EX 3600
  2. Write to database
  (both writes succeed or neither — use transactions or queue)
```
Best for: Data where cache staleness is unacceptable (inventory counts, prices).

#### Sorted Sets for Leaderboards/Rankings
```
ZADD leaderboard 1500 "user:alice"
ZADD leaderboard 2300 "user:bob"
ZREVRANGE leaderboard 0 9 WITHSCORES   -- top 10
ZRANK leaderboard "user:alice"         -- rank of specific member
```

#### Key Naming Convention
```
{entity}:{id}               product:123
{entity}:{id}:{subtype}    user:456:session
{prefix}:{context}:{id}    cache:product:789
```
Always include a TTL. Never store unbounded sets in a single key.

---

### Wide-Column Patterns (Cassandra)

**Core principle**: Design tables around query patterns, not data relationships.

#### Partition Key Design
```
-- Good: partition key distributes load evenly
CREATE TABLE events (
  userId    UUID,
  eventDate DATE,
  eventTime TIMESTAMP,
  eventType TEXT,
  payload   TEXT,
  PRIMARY KEY ((userId, eventDate), eventTime)
) WITH CLUSTERING ORDER BY (eventTime DESC);
-- Partition: (userId, eventDate) — bounded per user per day
-- Clustering: eventTime — sorted for range queries within partition

-- Bad: hot partition — all data for one date goes to one node
PRIMARY KEY (eventDate, userId, eventTime)
-- eventDate partition will receive ALL writes for that day
```

**Partition key guidelines**:
- Should distribute writes evenly across nodes (high cardinality)
- Should be included in every query (no full scans)
- Keep partition size bounded (target under 100MB, under 100k rows)
- Combine fields if single field creates hot partitions

#### Denormalization for Read Paths
```
-- Write the same data in multiple tables shaped for each query
-- "One table per query pattern" is the Cassandra way

-- Table 1: Look up order by orderId
orders_by_id (orderId, customerId, status, total, createdAt)
PRIMARY KEY (orderId)

-- Table 2: Look up orders by customer
orders_by_customer (customerId, createdAt, orderId, status, total)
PRIMARY KEY (customerId, createdAt)
WITH CLUSTERING ORDER BY (createdAt DESC)
```

---

### Graph Database Patterns (Neo4j)

#### Property Graph Model
```
Nodes:   Represent entities       (User), (Product), (Order)
Edges:   Represent relationships  (User)-[:PLACED]->(Order)
Both:    Can have properties       {name: "Alice"}, {quantity: 2}
```

#### Traversal Optimization
```cypher
-- Index node properties used in WHERE clauses
CREATE INDEX ON :User(email)
CREATE INDEX ON :Product(sku)

-- Use relationship types to limit traversal scope
MATCH (u:User)-[:PURCHASED]->(p:Product)  -- fast, typed
MATCH (u:User)-->(p:Product)              -- slow, untyped, scans all relationship types

-- Avoid variable-length paths without bounds
MATCH path = (a)-[*]->(b)          -- dangerous: unbounded
MATCH path = (a)-[*1..4]->(b)      -- safe: bounded depth
```

#### Common Graph Patterns
- **Friend-of-Friend**: `MATCH (u)-[:FOLLOWS*2]->(rec)` — social recommendations
- **Shortest Path**: `SHORTESTPATH((a)-[*]->(b))` — routing, dependency resolution
- **Community Detection**: Nodes with dense internal connections — fraud rings, topic clusters
- **Permission Inheritance**: `(user)-[:MEMBER_OF*]->(group)-[:HAS_PERMISSION]->(resource)`

---

## Event Sourcing

### Core Pattern

**When to use**: Audit requirements, temporal queries ("what was the state on date X?"), complex domain logic, CQRS read model rebuilding.

```
Traditional:   Store current state → mutate on write → history lost
Event Sourced: Append events → replay to get current state → history preserved

Event Store:
  { eventId, aggregateId, eventType, payload, occurredAt, version }

Rehydration:
  events = loadEvents(aggregateId)
  state  = events.reduce(applyEvent, initialState)
```

### Event Store Design
```sql
events (
  eventId       UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  aggregateId   UUID NOT NULL,
  aggregateType VARCHAR(100) NOT NULL,
  eventType     VARCHAR(100) NOT NULL,
  payload       JSONB NOT NULL,
  metadata      JSONB,           -- correlation_id, causation_id, user_id
  version       INT NOT NULL,    -- aggregate version at time of event
  occurredAt    TIMESTAMPTZ NOT NULL DEFAULT NOW(),

  UNIQUE (aggregateId, version),  -- optimistic concurrency control
  INDEX idx_aggregate (aggregateId, version)
)
```

**Optimistic concurrency**: When writing, include the expected version. If another writer incremented it first, the UNIQUE constraint rejects the write → client retries.

### Projections
```
Projection = a read model built by replaying events

// Example: OrderSummary projection
function applyEvent(state, event) {
  switch (event.eventType) {
    case 'OrderPlaced':
      return { ...state, status: 'placed', total: event.payload.total };
    case 'OrderConfirmed':
      return { ...state, status: 'confirmed' };
    case 'OrderShipped':
      return { ...state, status: 'shipped', trackingId: event.payload.trackingId };
  }
}
```

Projections are disposable and rebuildable. When you add a new query need, write a new projection and replay all events.

### Snapshots
```
Problem: Replaying 10,000 events on every read is slow.
Solution: Periodically save a snapshot of aggregate state.

Snapshot table:
  snapshots (aggregateId, version, state JSONB, createdAt)

Load strategy:
  1. Load latest snapshot for aggregateId
  2. Load events WHERE version > snapshot.version
  3. Apply events on top of snapshot state
```

**Snapshot frequency**: Every N events (e.g., every 100), or when aggregate reaches a known checkpoint state.

### Temporal Queries
```
// State at a point in time
events = loadEventsUpTo(aggregateId, pointInTime)
historicalState = events.reduce(applyEvent, initialState)

// What changed between two dates
eventsInRange = loadEventsBetween(aggregateId, startDate, endDate)
```

---

## CQRS (Command Query Responsibility Segregation)

### Pattern Overview

```
Command Side (Write):                Query Side (Read):
  ┌─────────────┐                     ┌─────────────┐
  │   Command   │ → validate →        │    Query    │
  │   Handler   │   apply →           │   Handler   │
  │             │   emit events       │             │
  └──────┬──────┘                     └──────┬──────┘
         │                                   │
    Event Store                        Read Models
    (normalized,                      (denormalized,
     append-only)                      query-optimized)
         │                                   ↑
         └────────── Event Bus ──────────────┘
                   (async projection)
```

### Separate Read/Write Models

**Write model**: Enforces business rules, validates invariants, emits domain events. Optimized for consistency.

**Read model**: Denormalized, optimized for specific query patterns. Eventually consistent with write model.

```sql
-- Write model: normalized, enforces constraints
orders      (orderId, customerId, status, version)
order_lines (lineId, orderId, productId, quantity, unitPrice)

-- Read model: denormalized for order dashboard query
order_dashboard_view (
  orderId, customerName, customerEmail,
  status, lineCount, total, createdAt, lastUpdated
)
-- Rebuilt from events; no joins needed at query time
```

### Eventual Consistency Handling
- **Optimistic UI**: Assume command succeeds, revert if event doesn't arrive within timeout
- **Polling**: Client polls until read model reflects expected state
- **WebSocket push**: Emit event to client when projection updates
- **Correlation ID**: Client tracks commandId → waits for acknowledgement event with same correlationId

---

## Data Partitioning

### Horizontal Sharding (Range-Based)

```
Shard 1: customerId 1–1,000,000
Shard 2: customerId 1,000,001–2,000,000
Shard 3: customerId 2,000,001–3,000,000

Pros:  Simple routing logic; efficient range scans within a shard
Cons:  Hot shards if data isn't uniformly distributed (e.g., new signups all hit Shard 3)
```

Use when: Data has a natural, evenly distributed range key (timestamps for time-series sharding).

### Consistent Hashing

```
Ring with 2^32 positions.
Nodes placed at hash(nodeId) positions on ring.
Data key routed to first node clockwise from hash(key).

Adding a node: only keys between new node and its predecessor migrate.
Removing a node: only that node's keys migrate to the next node clockwise.

Virtual nodes (vnodes): each physical node owns multiple ring segments
→ more uniform distribution, easier rebalancing.
```

Use when: You need elastic scale with minimal data movement on topology changes.

### Vertical Sharding (Functional Decomposition)

```
Monolithic DB           After vertical sharding:
┌─────────────┐         ┌──────────────┐  ┌──────────────┐  ┌──────────────┐
│  Users      │         │  User DB     │  │  Order DB    │  │  Product DB  │
│  Orders     │  ──→    │  (users,     │  │  (orders,    │  │  (products,  │
│  Products   │         │   sessions)  │  │   payments)  │  │   inventory) │
│  Payments   │         └──────────────┘  └──────────────┘  └──────────────┘
└─────────────┘
```

Use when: Different domains have very different scaling, availability, or compliance requirements.

### Partition Pruning

Always include the partition key in WHERE clauses. Without it, queries fan out to all shards.

```sql
-- Good: includes shard key (customerId) — routes to one shard
SELECT * FROM orders WHERE customerId = 456 AND status = 'shipped';

-- Bad: no shard key — queries all shards, aggregates results
SELECT * FROM orders WHERE status = 'shipped';
```

---

## Time-Series Data Modeling

### Principles

1. **Append-only**: Never update historical data points. Corrections are new data points.
2. **Time-bucketed partitions**: Partition by time period so old data can be archived/dropped efficiently.
3. **Schema on write for metrics**: Know your tags (dimensions) and fields (measures) upfront.

### Relational Time-Series Pattern
```sql
-- Partition by month for efficient range scans and archival
CREATE TABLE sensor_readings (
  sensorId     UUID NOT NULL,
  recordedAt   TIMESTAMPTZ NOT NULL,
  temperature  DECIMAL(5,2),
  humidity     DECIMAL(5,2),
  PRIMARY KEY (sensorId, recordedAt)
) PARTITION BY RANGE (recordedAt);

CREATE TABLE sensor_readings_2026_03
  PARTITION OF sensor_readings
  FOR VALUES FROM ('2026-03-01') TO ('2026-04-01');
```

### Downsampling for Long-Term Storage
```
Raw data:      1-second resolution → keep for 7 days
1-min rollup:  AVG/MAX/MIN per minute → keep for 90 days
1-hour rollup: AVG/MAX/MIN per hour → keep for 2 years
1-day rollup:  AVG/MAX/MIN per day → keep forever
```

### InfluxDB/TimescaleDB Line Protocol Pattern
```
measurement,tag1=val1,tag2=val2 field1=v1,field2=v2 timestamp

cpu,host=server01,region=us-east usage_idle=97.5,usage_user=2.1 1711700000000000000
```
Tags: indexed dimensions used in GROUP BY/WHERE. Fields: measured values. Keep tag cardinality bounded.

---

## Schema Evolution and Migration

### Migration Strategies

**Expand/Contract (Blue-Green Schema)**:
```
Phase 1 — Expand:
  Add new column/table. Write to both old and new. Read from old.
  Deploy: safe, backward compatible.

Phase 2 — Migrate:
  Backfill new column from old column data.
  Validate data is correct in new location.

Phase 3 — Contract:
  Switch reads to new column.
  Remove writes to old column.
  Drop old column in next deploy cycle.
```

This pattern supports zero-downtime migrations with instant rollback at each phase.

### Backward Compatibility Rules

| Change | Compatible? | Notes |
|--------|------------|-------|
| Add nullable column | Yes | Existing queries unaffected |
| Add NOT NULL column with default | Yes | Default covers existing rows |
| Add NOT NULL column without default | No | Existing rows fail constraint |
| Rename column | No | All queries using old name break |
| Remove column | No | Queries referencing it break |
| Add table | Yes | No existing queries affected |
| Add index | Yes | Performance-only change |
| Change column type (widening) | Usually yes | INT → BIGINT, VARCHAR(50) → VARCHAR(100) |
| Change column type (narrowing) | No | Potential data loss |

### Schema Versioning Table
```sql
schema_migrations (
  version      VARCHAR(20) PRIMARY KEY,   -- '20260301120000'
  description  TEXT,
  appliedAt    TIMESTAMPTZ DEFAULT NOW(),
  appliedBy    TEXT
)
```

Run migrations in transactions where possible. Separate DDL migrations (schema changes) from DML migrations (data backfills) — backfills run offline against large tables.

---

## 2026-06 Delta Update (as of 2026-06-06)

Three in-window developments reinforce the semantic-layer / governed-substrate thesis for analytics. This pack historically focused on transactional (OLTP/NoSQL/event-sourced) modeling and did not carry semantic-layer or open-table-format authorship guidance; the items below add that coverage. Where a future version of this pack describes dbt MetricFlow or "Iceberg + Unity Catalog OSS," treat the descriptions below as the current authority.

### 1. dbt Core v1.12 rewrote the Semantic Layer YAML spec (shipped May 2026)

The dbt Semantic Layer authorship model changed materially:

- **Semantic definitions are now authored inline inside model schema YAML** — there are no longer separate semantic-model files. Semantics live next to the model they describe.
- **`measures` are removed from the authorship spec.** "Simple metrics" become the primary building block; a simple metric can now carry aggregations and expressions directly, absorbing the role measures used to play.
- **Migration path**: `dbt-autofix deprecations --semantic-layer` rewrites legacy semantic-model + measure definitions into the new inline / simple-metric form.
- dbt also shipped a **Developer / Copilot agent in preview** that generates models, SQL, tests, docs, and semantic models from natural-language prompts.

Practical implication: any guidance that describes MetricFlow authorship via standalone `semantic_models:` files with a `measures:` block is now stale. Author semantics inline; define metrics as simple metrics with aggregation + expression.

Sources: https://docs.getdbt.com/blog/modernizing-the-semantic-layer-spec ; https://docs.getdbt.com/docs/build/latest-metrics-spec ; https://docs.getdbt.com/docs/dbt-versions/dbt-cloud-release-notes

### 2. Apache Iceberg v3 GA in Databricks Unity Catalog (2026-05-28)

Iceberg v3, Managed Iceberg, and Foreign Iceberg moved to GA in Databricks Unity Catalog. Iceberg v3 adds **Deletion Vectors, the Variant type, Row IDs, and geospatial types** — capabilities now shared with Delta Lake. Databricks signaled an **Iceberg v4 + Delta 5.0 convergence on unified metadata**, narrowing the open-table-format divide. Any "Iceberg + Unity Catalog (OSS preview)" framing is version-stale: Iceberg v3 on Unity Catalog is GA.

Source: https://www.databricks.com/blog/unity-catalog-and-next-era-apache-icebergtm

### 3. Snowflake Summit 2026 (2026-06-01 to 06-04) — governed semantic substrate for agents

Snowflake Summit confirmed the market direction that agentic analytics needs a governed semantic substrate, not ad-hoc SQL:

- **Cortex Sense** — auto-assembles data + business definitions + operational knowledge into a shared context layer for agents.
- **Horizon Context** — governance / truth layer.
- **Semantic Studio** — authoring surface for semantics.
- **Iceberg v3** support; rebrands: **CoWork** (was Snowflake Intelligence) and **CoCo** (was Cortex Code).
- **OSI (Open Semantic Interchange)** — vendor-neutral semantic spec, Apache-2.0, spec finalized 2026-01-27 — had its adoption moment at Summit.

Net read: the clearest market confirmation yet that conversational / agentic analytics depends on a governed, vendor-portable semantic layer (dbt Semantic Layer, OSI, Cortex Sense / Horizon Context) sitting above the warehouse.

Sources: https://www.snowflake.com/en/blog/open-semantic-interchanges-specs-finalized/ ; https://atlan.com/know/snowflake/summit-2026-announcements/

---

## Anti-Patterns to Avoid

### God Table
```
VIOLATION:
entities (id, type, name, field1, field2, ..., field50)
-- One table tries to model everything. 80% of columns NULL for any given row.

SYMPTOM: Table has 40+ columns; many nullable; type discriminator column present.
FIX: Decompose into separate tables per entity type. Use inheritance patterns if needed.
```

### EAV Overuse
```
VIOLATION: Using EAV for data that has known, bounded attributes.
-- EAV is justified only for truly dynamic, sparse, unbounded attribute sets.

SYMPTOM: Every product attribute stored as (productId, attributeName, attributeValue).
         Simple queries require 5+ self-joins.
FIX: Use proper columns for known attributes. Use JSONB for optional semi-structured data.
```

### Premature Denormalization
```
VIOLATION: Denormalizing before you have measured a performance problem.
-- "It'll be faster" is not justification. Measure first.

SYMPTOM: Duplicated data with no update triggers or application-layer sync logic.
FIX: Start normalized. Profile queries. Denormalize only specific hot paths with evidence.
```

### Magic Number Primary Keys
```
VIOLATION: Using sequential integers as business identifiers shared with external systems.
-- Sequential IDs expose record counts, enable enumeration attacks.
FIX: Use UUIDs for external-facing identifiers. Use surrogate integer PKs internally for join performance.
```

### Missing Indexes on Foreign Keys
```
VIOLATION: Defining FK constraints without corresponding indexes.
-- Child table scanned fully on every parent DELETE/UPDATE.
FIX: Every FK column should have an index unless the table is tiny (<1,000 rows).
```

### Storing Derived Data Without Invalidation Logic
```
VIOLATION: Caching a computed value (e.g., orderTotal) in a column without a trigger or
           application layer ensuring it updates when its inputs change.
FIX: Either recompute on every read (if cheap), use a database trigger, or document
     every write path that must update the derived value.
```

---

## Data Modeling Checklist

### Before You Start
- [ ] Have you identified all major query patterns (not just write patterns)?
- [ ] Have you listed the top 5 read queries by frequency and latency requirement?
- [ ] Have you identified data ownership boundaries (which service owns which entities)?
- [ ] Have you chosen the right storage paradigm (relational / document / key-value / wide-column / graph)?

### Relational Schema Review
- [ ] All tables have a primary key (prefer UUID for external-facing, integer for internal joins)
- [ ] All FK columns have indexes
- [ ] NOT NULL constraints applied wherever nulls are not a valid business state
- [ ] Schema is in 3NF or there is documented justification for denormalization
- [ ] No multi-valued columns (1NF satisfied)
- [ ] Hierarchy pattern chosen deliberately (adjacency list / closure table / nested sets)
- [ ] JSONB/flexible columns used for truly dynamic attributes, not as a shortcut for poor modeling
- [ ] Audit columns on mutable tables (createdAt, updatedAt, createdBy)

### NoSQL Schema Review
- [ ] Partition keys distribute load evenly (no hot partitions)
- [ ] One table (or collection) per query pattern for wide-column stores
- [ ] Embedding vs. referencing decision documented for document stores
- [ ] TTLs set on cache keys
- [ ] Schema version field included in document stores for evolution

### Event Sourcing / CQRS Review
- [ ] Event schema includes: aggregateId, version, eventType, payload, occurredAt
- [ ] Optimistic concurrency enforced on event store writes
- [ ] Projection rebuild process documented and tested
- [ ] Snapshot strategy defined if aggregate lifespan is long
- [ ] Read models are clearly separated from write models

### Migration Safety Review
- [ ] Migration is backward compatible (expand/contract pattern used for breaking changes)
- [ ] Large data backfills run as separate step, not in DDL transaction
- [ ] Rollback plan documented for each migration phase
- [ ] Schema version tracked in migrations table
- [ ] Migration tested on production-sized data volume (not just dev sample)

### Performance Review
- [ ] Index coverage verified for all WHERE / JOIN / ORDER BY columns in top queries
- [ ] Partition strategy includes partition key in hot query WHERE clauses
- [ ] No unbounded result sets (all queries have LIMIT or pagination)
- [ ] Explain plan reviewed for top 5 queries before production deploy
