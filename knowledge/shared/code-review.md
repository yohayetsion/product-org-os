# Code Review — Frameworks & Methods

## Overview

Code review is the structured practice of having one or more engineers examine code changes before they are merged. When done well, it prevents defects from reaching production, distributes knowledge across the team, and maintains the architectural integrity of the codebase over time. When done poorly, it becomes a bottleneck, a source of interpersonal friction, or a rubber-stamp ritual that catches nothing.

This knowledge pack covers the complete code review process — from how to structure a review session to language-specific checklists, severity classification, and the automated tooling layer that handles mechanical checks so reviewers can focus on judgment.

**Version**: 1.0.0
**Type**: Knowledge Pack
**Primary Users**: 🛠️ Tech Lead, 🔧 Backend Dev, 💻 Frontend Dev, 🔍 QA Engineer

---
<!-- Attribution:
  Frameworks and patterns in this knowledge pack were informed by:
  - Anthropic knowledge-work-plugins (engineering/code-review domain reference)
  - OWASP Top 10 Web Application Security Risks (owasp.org)
  - Google Engineering Practices: Code Review Guidelines
  - Adapted and expanded for Product Org OS agents.
-->

---

## Code Review Process

**When to use**: Every time a code change is submitted for merge. The process scales from a 5-minute review of a one-line fix to a multi-session review of a large architectural change.

### Phase 1: Understand Context

Before reading a single line of code, orient yourself:

1. **Read the PR description** — What problem does this solve? What approach was chosen and why?
2. **Check the linked ticket** — Does the code match the requirements? Are there acceptance criteria you can verify?
3. **Assess the scope** — How many files changed? What is the blast radius if this breaks?
4. **Identify the risk tier**:

| Risk Tier | Characteristics | Review Depth |
|-----------|----------------|--------------|
| **Low** | Tests only, docs only, trivial config change | Skim for obvious issues |
| **Medium** | Feature additions, refactors within a module | Standard review (all dimensions) |
| **High** | Authentication, payments, data migration, API contracts | Deep review + second reviewer |
| **Critical** | Security controls, infrastructure-as-code, schema changes | Mandatory pair review + staging validation |

### Phase 2: Review the Four Dimensions

Work through the four dimensions systematically. Do not review randomly — incomplete coverage creates false confidence.

1. **Security** — Can this be exploited? See Security Review Checklist.
2. **Performance** — Will this degrade under load? See Performance Review Checklist.
3. **Correctness** — Does this actually do what the author intended? Does it handle edge cases?
4. **Maintainability** — Can the next engineer understand and safely modify this in 6 months?

### Phase 3: Formulate Findings

Classify each finding by severity (see Severity Classification below) and write feedback that explains the problem, the risk, and — where possible — a suggested fix or direction.

### Phase 4: Deliver the Verdict

End every review with a clear verdict. Leaving a review without a verdict forces the author to guess whether they need to act.

---

## Review Dimensions

### Security

Security bugs are expensive: they affect users before they are found, they are difficult to fix safely under pressure, and they carry regulatory and reputational consequences. Security review is not optional.

**OWASP Top 10 Mapping**:

| OWASP Category | Code Patterns to Inspect |
|---------------|--------------------------|
| A01: Broken Access Control | Authorization checks on every route/endpoint; IDOR patterns where resource IDs are user-controlled; missing ownership validation |
| A02: Cryptographic Failures | Hardcoded secrets or API keys; weak algorithms (MD5, SHA1 for passwords); unencrypted PII in logs or database columns; insecure TLS config |
| A03: Injection | SQL string concatenation instead of parameterized queries; OS command construction from user input; LDAP injection; template injection |
| A04: Insecure Design | Missing rate limiting on auth endpoints; no CSRF protection on state-changing requests; predictable resource identifiers |
| A05: Security Misconfiguration | Debug mode enabled; verbose error messages exposing stack traces; unnecessary HTTP methods enabled; permissive CORS |
| A06: Vulnerable Components | New dependencies added without version pinning; known-vulnerable dependency versions; unused dependencies increasing attack surface |
| A07: Auth Failures | Passwords stored without bcrypt/argon2; weak session tokens; missing MFA enforcement for admin actions; JWT `alg: none` acceptance |
| A08: Data Integrity Failures | Deserialization of untrusted data; unsigned webhook payloads processed without validation; object prototype pollution (JS) |
| A09: Security Logging Failures | PII or secrets logged; authentication events not logged; no correlation ID for audit trail |
| A10: SSRF | URLs constructed from user input passed to HTTP clients; missing allowlists for outbound requests |

**High-priority patterns**:
```
# SQL Injection — never do this:
query = f"SELECT * FROM users WHERE email = '{email}'"

# Correct (parameterized):
query = "SELECT * FROM users WHERE email = %s"
cursor.execute(query, (email,))

# Path Traversal — never do this:
file_path = os.path.join(BASE_DIR, user_input)

# Correct:
file_path = os.path.realpath(os.path.join(BASE_DIR, user_input))
assert file_path.startswith(BASE_DIR)

# Hardcoded secret — flag immediately:
API_KEY = "sk-prod-abc123..."
```

---

### Performance

Performance bugs are often invisible in development and catastrophic in production. The most dangerous ones are not slow algorithms — they are database access patterns that look fine with 10 rows and fail with 10 million.

**Key patterns to catch**:

**N+1 Queries** — the most common production performance bug:
```python
# N+1: 1 query for all orders, then 1 query per order for user
orders = Order.objects.all()
for order in orders:
    print(order.user.name)  # triggers a new DB query per iteration

# Correct: single query with JOIN
orders = Order.objects.select_related('user').all()
```

**Missing Database Indexes**: Any column used in a `WHERE`, `JOIN`, `ORDER BY`, or `GROUP BY` clause that does not have an index is a query time bomb. Flag new query patterns that reference unindexed columns.

**Unbounded Queries**: Any query without a `LIMIT` clause on a table that can grow arbitrarily is a production incident waiting to happen.

**Memory Allocations**: Loading entire dataset into memory for operations that could be streamed or batched. Watch for `.all()`, `.to_list()`, or `.collect()` on large collections.

**Algorithmic Complexity**:

| Complexity | Acceptable For | Flag When |
|-----------|---------------|-----------|
| O(1) | Any data size | — |
| O(log n) | Any data size | — |
| O(n) | Up to millions of items | — |
| O(n log n) | Sorting/searching up to 100k items | Large datasets |
| O(n²) | Up to ~10k items | Any nested loop over user data |
| O(2^n) | Toy examples only | Anywhere in production |

**Resource Leaks**: Database connections, file handles, HTTP clients, and thread pool executors that are not closed/released in all code paths (including exception paths). Look for missing `finally` blocks, un-used `with` statements, and connections obtained but not returned to pools.

---

### Correctness

Correctness covers whether the code does what the author intended, handles cases the author did not consider, and fails safely when it cannot proceed.

**Edge cases to probe**:
- What happens when the input list is empty?
- What happens when a required external service is unavailable?
- What happens when a concurrent request modifies the same resource?
- What happens at integer boundaries (0, -1, MAX_INT)?
- What happens with null/None/undefined at every layer?

**Race Conditions**: Look for shared mutable state accessed from concurrent contexts without synchronization. Check for time-of-check-time-of-use (TOCTOU) patterns:
```python
# TOCTOU vulnerability:
if not user.has_spent_credit:
    # Another request can pass this check simultaneously
    charge_user_credit(user)
    user.has_spent_credit = True

# Correct: atomic operation
User.objects.filter(id=user.id, has_spent_credit=False).update(has_spent_credit=True)
```

**Error Handling**:
- Errors swallowed silently (`except: pass`, `catch (e) {}`) — always flag
- Errors that lose the original stack trace during re-throw
- HTTP status codes that don't match the error type (returning 200 with an error body)
- Missing rollback on partial transaction failure

**Type Safety**:
- Implicit type coercions that behave unexpectedly (`"2" + 2` in JavaScript)
- Missing type annotations on public function signatures
- `any` / `object` types that bypass the type system in critical paths

---

### Maintainability

Code is read far more often than it is written. Maintainability is about reducing the cognitive load on the next engineer to work in this area.

**Naming**: Variable names should explain what the value represents, not how it was computed. Function names should state what they do, not how.

**Single Responsibility Principle**: A function or class that does two distinct things should be two functions or classes. Long functions (>50 lines) with multiple branching paths are candidates for decomposition.

**Duplication**: Copy-pasted logic is a maintenance liability — when the logic changes, every copy must be found and updated. Flag duplicated blocks of 5+ lines.

**Test Coverage**: New features and bug fixes should include tests. Review tests for:
- Whether they actually test the production code path (not just the happy path)
- Whether they would catch a regression if the implementation changed
- Whether they are testing behavior (what the code does) vs. implementation (how it does it)

**Documentation**:
- Public API functions need docstrings that explain parameters, return values, and exceptions
- Complex algorithms need inline comments explaining the non-obvious step, not the obvious one
- `TODO` comments must include a ticket reference: `// TODO(PROJ-123): remove after migration`

---

## Review Output Template

Use this structure when delivering review findings in writing:

```markdown
## Code Review: [PR Title / PR Number]

**Reviewer**: [Name]
**Date**: [YYYY-MM-DD]
**Risk Tier**: [Low / Medium / High / Critical]
**Verdict**: [Approve / Approve with Minor Comments / Request Changes / Needs Major Rework]

---

### Summary

[2-4 sentences. What does this PR do? What is the overall quality? Any systemic patterns worth calling out?]

---

### Critical Issues (must fix before merge)

| # | File | Line | Issue | Severity | Suggested Fix |
|---|------|------|-------|----------|---------------|
| 1 | `auth/login.py` | 47 | SQL query constructed via string concatenation — SQL injection vulnerability | Critical | Use parameterized query |
| 2 | `api/orders.py` | 112 | No authorization check — any authenticated user can access any order | Critical | Add ownership check before returning order |

---

### Suggestions (should fix, non-blocking)

| # | File | Line | Suggestion | Severity |
|---|------|------|------------|----------|
| 1 | `models/user.py` | 23 | `get_user_data()` loads all fields — use `.only()` for the fields actually needed | Major |
| 2 | `utils/helpers.py` | 88 | Function is 80 lines with 4 branching paths — candidate for decomposition | Minor |

---

### Positive Observations

- Test coverage is thorough, including edge cases for empty input and concurrent modification
- Error handling is consistent with the project's established patterns
- The migration is backward-compatible with a clean rollback path

---

### Verdict: [Request Changes]

[1-2 sentences explaining what needs to happen before this can be approved.]
```

---

## Severity Classification

| Severity | Definition | Example | Action |
|----------|-----------|---------|--------|
| **Critical** | Security vulnerability, data corruption risk, or production-breaking defect | SQL injection, hardcoded production secret, missing auth check | Block merge. Must be fixed before any further review. |
| **Major** | Significant correctness issue, serious performance problem, or architectural violation | N+1 query on a hot path, unhandled exception that crashes the service, race condition | Block merge. Fix required, but author can address and request re-review. |
| **Minor** | Code quality issue that will cause future maintenance cost | Missing test coverage, function doing too much, unclear naming | Non-blocking. Author should address; reviewer may approve with comment. |
| **Nit** | Style preference or trivial improvement | Inconsistent spacing, variable name could be more descriptive, missing trailing newline | Non-blocking. Author's discretion. Prefix with "Nit:" in the comment. |

**Critical and Major findings always block merge. Minor and Nit findings do not.**

---

## Language-Specific Checklists

### JavaScript / TypeScript

**Async/Await Pitfalls**:
- [ ] `await` inside a loop where parallel execution (`Promise.all`) would be correct
- [ ] Unhandled promise rejections (missing `catch` or `try/catch` around `await`)
- [ ] `async` function that never actually awaits anything
- [ ] Race conditions between concurrent async operations on shared state

**Type Safety**:
- [ ] `any` type used in a security-sensitive or data-processing context
- [ ] Non-null assertions (`!`) used where the value could genuinely be null
- [ ] Missing `strict: true` TypeScript config on new modules
- [ ] Type casting that bypasses the type system without explanation

**Security**:
- [ ] `eval()`, `new Function()`, or `document.write()` with dynamic content — XSS vectors
- [ ] `dangerouslySetInnerHTML` in React without sanitization
- [ ] Object prototype pollution via `Object.assign({}, userInput)` or spread of untrusted objects
- [ ] `JSON.parse()` without try/catch and schema validation

**Dependencies**:
- [ ] New packages added — check license, download count, maintenance status, known CVEs
- [ ] Version pinned (exact version or `~minor` range, not `^major`)
- [ ] `devDependencies` correctly separated from `dependencies`

---

### Python

**GIL Considerations**:
- [ ] CPU-bound work using threads instead of multiprocessing (threads won't parallelize due to GIL)
- [ ] I/O-bound work using multiprocessing instead of `asyncio` or threads (wasteful)
- [ ] Shared mutable state between threads without locks

**Type System**:
- [ ] Public functions missing type annotations (PEP 484)
- [ ] `Optional[X]` used correctly — not just `X` when `None` is a valid return
- [ ] `Dict`, `List`, `Tuple` from `typing` vs. built-in generics (Python 3.9+ can use built-ins)

**Import Structure**:
- [ ] Circular imports (often a sign of poor module design)
- [ ] Star imports (`from module import *`) in production code
- [ ] Mutable default arguments: `def func(data=[])` — a classic Python gotcha

**Common Bugs**:
- [ ] `is` used to compare values instead of identity (`x is True` instead of `x == True`)
- [ ] Late binding closures in loops (`lambda: i` in a loop captures the final value of `i`)
- [ ] Exception handling catches `BaseException` or bare `except:` — catches `KeyboardInterrupt`

---

### Go

**Goroutine Leaks**:
- [ ] Goroutines launched without a way to signal termination (missing `ctx.Done()` check)
- [ ] Channels that can block forever if no receiver materializes
- [ ] `go func()` calls inside request handlers that outlive the request lifecycle

**Error Handling**:
- [ ] Errors discarded with `_` without documented justification
- [ ] `fmt.Errorf("failed: %v", err)` loses stack context — use `fmt.Errorf("...: %w", err)` for wrappable errors
- [ ] Sentinel errors compared with `==` instead of `errors.Is()`
- [ ] Custom error types compared with `==` instead of `errors.As()`

**Context Propagation**:
- [ ] `context.Background()` used inside a function that received a `ctx` parameter — breaks cancellation chain
- [ ] `context.WithTimeout` without a matching `defer cancel()` — goroutine/memory leak
- [ ] Context stored in a struct field — contexts should be passed as first function parameter

**Concurrency**:
- [ ] Struct fields accessed concurrently without mutex or `sync/atomic`
- [ ] Map read/writes from multiple goroutines without `sync.RWMutex` (Go maps are not safe for concurrent use)
- [ ] `sync.WaitGroup.Add()` called after the goroutine may have already completed

---

### React / Next.js

**Re-render Optimization**:
- [ ] New object or array literal created in render without `useMemo` passed to memoized child component
- [ ] New function created in render without `useCallback` passed as a prop to memoized child
- [ ] `React.memo()` used without checking whether props actually change (wrapping everything is noise)
- [ ] State updates inside `useEffect` without correct dependency array — infinite render loop

**SSR / CSR Boundaries**:
- [ ] `window`, `document`, or `localStorage` accessed outside a `useEffect` or `typeof window !== 'undefined'` guard (breaks SSR)
- [ ] `'use client'` directive missing on components using browser APIs or hooks
- [ ] Data fetching in a client component that could be a server component (increases bundle size)
- [ ] Secrets or server-only environment variables referenced in client components

**Hooks Rules**:
- [ ] Hook called conditionally (inside an `if` statement or after an early return)
- [ ] Hook called inside a loop
- [ ] Custom hook that does not start with `use`
- [ ] `useEffect` with a missing dependency that causes stale closure reads

**Next.js Specifics**:
- [ ] `getServerSideProps` used when `getStaticProps` + ISR would serve the use case (unnecessary server cost)
- [ ] Images served without `<Image>` component (missing optimization)
- [ ] Large page bundles without dynamic `import()` for components below the fold

---

## Security Review Checklist

Use this checklist for any PR touching authentication, authorization, data storage, external integrations, or user input handling.

**Authentication**:
- [ ] Passwords hashed with bcrypt, argon2, or scrypt (not SHA/MD5)
- [ ] Session tokens generated with cryptographically secure random source
- [ ] Tokens invalidated on logout and password change
- [ ] Brute force protection on login endpoint (rate limiting, lockout)
- [ ] JWT signature algorithm explicitly validated (reject `alg: none`)

**Authorization**:
- [ ] Every API endpoint checks authentication before processing
- [ ] Every resource access checks that the requesting user owns or has permission for that resource
- [ ] Admin/elevated operations have a second authorization layer
- [ ] Authorization logic is server-side, not client-side

**Input Handling**:
- [ ] All user-supplied data validated against a schema before use
- [ ] Database queries use parameterized statements or ORM (never string concatenation)
- [ ] File paths constructed from user input validated against an allowlist of base directories
- [ ] HTML output from user content sanitized (strip scripts, event handlers)
- [ ] Redirect URLs validated against an allowlist

**Secrets Management**:
- [ ] No credentials, API keys, or tokens in code or committed config files
- [ ] Secrets loaded from environment variables or secrets manager
- [ ] `.env` files in `.gitignore`

**Dependencies**:
- [ ] New dependencies have no known critical CVEs
- [ ] Dependency version is pinned
- [ ] Supply chain risk assessed for new packages (author reputation, ownership)

**Data Protection**:
- [ ] PII not logged in plaintext
- [ ] Sensitive data encrypted at rest where required
- [ ] HTTPS enforced for all external communications
- [ ] Error responses do not expose internal stack traces or system information

---

## Performance Review Checklist

**Database**:
- [ ] All query predicates reference indexed columns
- [ ] No N+1 query patterns — eager loading used where appropriate
- [ ] All queries have `LIMIT` clauses or pagination
- [ ] Bulk operations use batch inserts/updates instead of row-by-row
- [ ] Transactions are short (not spanning external API calls)
- [ ] Connection pool size appropriate for expected concurrency

**API & Network**:
- [ ] Response payloads include only fields the client needs (not full object dumps)
- [ ] Appropriate caching headers set (`Cache-Control`, `ETag`)
- [ ] Pagination implemented for list endpoints
- [ ] Compression enabled for large responses
- [ ] External API calls have timeouts and circuit breakers

**Frontend**:
- [ ] Images optimized and served in modern formats (WebP, AVIF)
- [ ] Large dependencies loaded lazily
- [ ] Critical CSS inlined; non-critical CSS deferred
- [ ] Web fonts loaded with `font-display: swap`
- [ ] Render-blocking scripts deferred or async

**Memory**:
- [ ] Large datasets streamed or paginated, not loaded entirely into memory
- [ ] Caches have eviction policies and size limits
- [ ] Objects with large memory footprints not stored in session or application state
- [ ] File handles, DB connections, and HTTP clients closed in all code paths

---

## PR Review Etiquette

Code review is a conversation between peers. The goal is better software, not proving the reviewer is smarter than the author.

**Tone principles**:
- Comment on the code, not the person. "This function does X and Y — consider separating those concerns" not "You made this too complicated."
- Explain the risk, not just the rule. "This pattern can cause a data race if two requests arrive simultaneously" is more useful than "This isn't thread-safe."
- Offer a direction, not just a critique. "Could this use `select_related` to avoid N+1?" is more helpful than "This has an N+1 problem."
- Distinguish opinion from requirement. Prefix stylistic preferences with "Nit:" or "Optional:" so the author knows what blocks merge.

**Constructive feedback template**:
```
[What you observed] + [Why it matters] + [One possible approach]

Example:
"This query runs inside the loop, so we'll hit the database once per order in the list.
On a large account this could be hundreds of queries. Could we move the query outside
the loop and use a dict for lookup, or use select_related here?"
```

**Recognize good work**: If an author handled an edge case elegantly, refactored a painful area, or added unusually thorough tests — say so. Positive feedback reinforces what good looks like and builds team culture.

**Response time expectations**:

| PR Size | Expected First Review | Expected Turnaround After Changes |
|---------|----------------------|----------------------------------|
| Small (<100 LOC) | Same business day | 4 hours |
| Medium (100-500 LOC) | 1 business day | Same day |
| Large (>500 LOC) | 2 business days | 1 business day |

**Large PRs**: If a PR is too large to review well in a single session, ask the author to split it. Reviewing a 2,000-line PR in one go produces worse results than two focused reviews of 1,000 lines each.

---

## Review Metrics

Track these to evaluate review effectiveness. Do not use them to evaluate individual reviewers — that incentivizes rubber-stamping.

| Metric | What It Measures | Healthy Range |
|--------|-----------------|---------------|
| **Review cycle time** | Time from PR open to merge | <24h for small, <48h for medium |
| **First review time** | Time from PR open to first reviewer comment | <8 hours (business hours) |
| **Defect escape rate** | Bugs found in production that passed code review | Trending down over quarters |
| **Review comment rate** | Average comments per PR | 3-8 (too few = rubber stamp; too many = noise) |
| **Blocking comment rate** | % of comments that block merge | Should match actual severity distribution |
| **Re-review count** | Number of review cycles per PR | 1-2 is healthy; >3 suggests unclear requirements or standards |

---

## Common Anti-Patterns by Language

| Language | Anti-Pattern | Risk | Better Approach |
|----------|-------------|------|----------------|
| JavaScript | `for...in` on arrays | Iterates prototype properties | Use `for...of` or `.forEach()` |
| JavaScript | Floating point equality: `0.1 + 0.2 === 0.3` | Always false | Use tolerance comparison or integer arithmetic |
| Python | Mutable default argument: `def f(x=[])` | Shared across all calls | Use `None` as default, initialize inside |
| Python | `except Exception as e: pass` | Silent failure | Log and re-raise or handle explicitly |
| Go | `defer` inside a loop | All defers run at function return, not loop iteration | Move loop body into a function |
| Go | `time.Sleep` in tests | Flaky tests | Use channels or `sync.WaitGroup` for coordination |
| React | Missing `key` prop in list renders | Incorrect reconciliation | Use stable, unique IDs as keys |
| React | Mutating state directly: `state.items.push(x)` | Bypasses React's change detection | Use `setState` with a new array |
| SQL | `SELECT *` in application code | Schema changes break silently | Select only needed columns explicitly |
| SQL | Boolean trap: `UPDATE users SET active = 1` | Unclear intent | Use named constants or enums |

---

## Automated Review Tools Reference

Automated tools handle the mechanical layer of code review (style, known vulnerability patterns, code smells). Use them to free up human reviewers for judgment-level work.

| Tool | Type | Languages | Best For |
|------|------|-----------|----------|
| **ESLint** | Linter | JavaScript, TypeScript | Style enforcement, common bug patterns, security rules (eslint-plugin-security) |
| **Pylint / Flake8 / Ruff** | Linter | Python | Style (PEP 8), unused imports, code smells. Ruff is 10-100x faster than Pylint |
| **golangci-lint** | Linter meta-runner | Go | Aggregates 50+ Go linters in one tool; runs staticcheck, errcheck, gosec |
| **SonarQube / SonarCloud** | SAST | Multi-language | Code quality gate, technical debt tracking, security hotspot detection |
| **Semgrep** | SAST | Multi-language | Custom rule patterns; very effective for organization-specific security policies |
| **Snyk / Dependabot** | Dependency scanning | Multi-language | Known CVEs in dependencies; auto-PRs for version upgrades |
| **CodeClimate** | Code quality | Multi-language | Maintainability metrics, cognitive complexity, duplication detection |
| **Trivy** | Container/IaC scanning | Docker, Terraform, K8s | Vulnerability scanning in container images and infrastructure code |
| **Checkov** | IaC scanning | Terraform, CloudFormation | Security misconfigurations in infrastructure definitions |

**Integration recommendation**: Run linters and dependency scanners in CI on every PR. Block merge on high-severity SAST findings. Human review focuses on logic, architecture, and anything automated tools cannot reason about.

---

## AI-Era Review Addendum (2026-06)

*Added 2026-06-12 (dev-team radar). Additive to v1.0.0 — everything above is unchanged and still applies. This section covers what changes when a meaningful share of PRs is agent-authored.*

<!-- Attribution (2026-06 addendum):
  Adapted from: Addy Osmani, "Code Review in the Age of AI" (addyo.substack.com); Sourcegraph "AI Code Review in 2026" (sourcegraph.com/blog/ai-code-review); CodeRabbit 470-PR analysis (via published 2026 state-of-AI-review coverage); GitClear AI Code Quality research 2025 (gitclear.com); DORA 2025 report (dora.dev/dora-report-2025).
  Source licence: no-license-but-publicly-cited (research findings + named public posts).
  V2V refinements: defect-profile-first review ordering; proof-of-work gate wired to the existing Review Output Template; severity rules extended to agent-authored PRs; queue-economics framing tied to the existing PR-size etiquette table.
-->

### The agent defect profile — probe this FIRST

Agent-written code fails differently. Before running the four dimensions, hunt the known profile:

| Defect class | Evidence base (as of 2026-06) |
|---|---|
| **Plausible-but-wrong logic** — clean, well-formatted, confidently wrong. Formatting quality is NOT a correctness signal | ~75% more logic errors and ~3× readability issues vs human PRs — CodeRabbit 470-PR analysis *(single-source)* |
| **Duplication instead of reuse** — valid new code where existing code should have been called | GitClear: duplicated blocks up 8×; refactoring fell 25% → <10% of changed lines (gitclear.com/ai_assistant_code_quality_2025_research) |
| **Hallucinated dependencies/APIs** — imports or methods that don't exist (also a supply-chain vector: squatted package names) | Widely reported across 2026 review-tool coverage; machine pass catches most |
| **Tests that assert nothing** — present, green, vacuous | Field consensus (Osmani, Sourcegraph); read the assertions, not the count |

For agent PRs, **missing tests are a Major finding by default** — tests are the agent's only self-verification scaffold (see `subagent-driven-development.md`).

### Same pipeline, no exemption

Agent-authored PRs enter the identical review gate and risk-tiering (Phase 1 above). Never tier down because "the AI reviewer already looked." Accountability is unchanged: **the human who merges owns the outcome regardless of authorship**.

### Proof-of-work gate

Every PR — human or agent — attaches to the Review Output Template's context: (1) **intent** in 1-2 sentences; (2) **evidence** — tests actually run, logs or screenshots; (3) for agent PRs, **the spec/plan/prompt that produced the code**. On non-trivial changes, **review the plan before the diff** — wrong-direction work is invisible in the diff and obvious in the plan. Treat AI output as a draft that must be verified, not a result that must be approved.

### The AI-reviewer layer (two-pass pipeline)

By mid-2026 an AI reviewer on every PR is standard plumbing (~60% of CI-using teams *(single-source)*). Field: **CodeRabbit** (install-base incumbent, 2M+ repos), **Greptile** (codebase-graph, cross-file ripple reasoning), **Claude Code `/code-review`**, **Qodo** (as of 2026-06; greptile.com/content-library/best-ai-code-review-tools).

- **Machine pass first**: linters + SAST (existing tools table) + AI reviewer clear ~70-80% of mechanical issues, including hallucinated dependencies.
- **Human pass spends its entire budget** on architectural fit, security implications, and "does this solve the original problem."
- AI-reviewer findings get the **same severity triage** as human findings: Critical/Major block, Minor/Nit don't.
- **Tune for low false positives** — a noisy AI reviewer trains the team to ignore it, which is worse than no reviewer.

### Review-queue economics

Agent throughput moves the constraint from authoring to **review capacity** — reviewers spend ~91% more time on AI PRs *(single-source, CodeRabbit)*; budget for it, don't pretend. The levers: enforce the small-PR discipline harder (**<400 LOC**) precisely because agents make large PRs cheap to produce and expensive to review; the etiquette table's response-time expectations hold only if PR size does. Reviewer time is the budget every other rule in this addendum protects.

### Tier routing under 2026 re-pricing (as of 2026-06-24)

*Added 2026-06-24 (DD-10).* **Adapted from**: securityboulevard.com "8 AI code review agents that critique diffs before commit" (2026-06-22) + GitHub Copilot billing change (community discussion, 2026-06-01) + vendor docs. **Source licence**: publicly cited; **all prices as-observed 2026-06, verify before relying**. **V2V refinements**: framed as cost-aware routing layered on the two-pass pipeline above; every price date-stamped + flagged "verify" (these rot fastest).

The AI-reviewer field re-priced in mid-2026 — route each diff to the cheapest gate that catches its risk class, and treat pricing as a moving target:
- **GitHub Copilot code review → metered (2026-06-01):** on private repos now consumes GitHub Actions minutes + AI credits (1 credit = $0.01, as-observed — verify). A previously-bundled feature now carries per-run cost.
- **Cursor Bugbot → usage-based** (~$1.00–1.50/PR, >$4 for ~5,000-line PRs, ~90% of runs <3 min, GitHub-only — as-observed). **Greptile → ~$30/seat for 50 reviews then ~$1/review** (as-observed).
- **Codacy AI Guardrails** — a free IDE extension scanning AI-generated code locally (a local-scan tier below the PR gate).
- **Copilot `/rubberduck`** (multi-model critique) + **`/security-review`** + reasoning-effort tiers; **Vercel Agent Code Review** (sandbox-validated patches — see `vercel-deployment` §Vercel Agent).
- **Routing rule (discipline unchanged):** trivial/local → IDE review agent or local scan (Codacy); routine shared-branch PRs → a PR-platform bot (CodeRabbit/Qodo/Greptile) for surface coverage; novel/security-sensitive/cross-cutting → in-Claude `/code-review` (the only gate that approves a merge). PR-bot output is signal, never the merge gate. **Cost-awareness:** metered tools (Copilot, Bugbot, Vercel Agent) bill per run — reserve them for the tier that needs them; don't fire a $0.30–$4 agent on a one-line diff.

---

## Operating Principle

> "Code review is how teams transfer knowledge and maintain quality without needing everyone to be everywhere at once. Review for the engineer who will maintain this code 18 months from now — that person might be you."
