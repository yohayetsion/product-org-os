# Cloud & Infrastructure — Frameworks & Methods

## Overview

Cloud infrastructure architecture is the discipline of designing, deploying, and operating the compute, storage, and networking resources that underpin a product. The decisions made here determine availability, performance, cost, and operational burden for the lifetime of the system.

This reference covers the foundational patterns and decision frameworks for cloud-native systems. The emphasis is on practical guidance: what to choose, when, and why. Cloud infrastructure is not about using the most features — it is about using the right features to build a reliable, cost-effective platform.

---

## Frameworks

### 12-Factor App Methodology

**When to use**: As a baseline checklist for any cloud-native application design. These factors ensure the application is portable, scalable, and operationally sound.

**The 12 Factors**:

| # | Factor | Rule | Architecture Impact |
|---|--------|------|---------------------|
| 1 | **Codebase** | One codebase tracked in VCS, many deploys | Mono-repo or per-service repo; branch strategy defined |
| 2 | **Dependencies** | Explicitly declare and isolate dependencies | Lockfiles (package-lock, requirements.txt); containerized builds |
| 3 | **Config** | Store config in the environment | No config files in code; use env vars, config maps, or vault |
| 4 | **Backing Services** | Treat backing services as attached resources | Database URLs, cache endpoints as config; swappable without code change |
| 5 | **Build, Release, Run** | Strictly separate build and run stages | Immutable artifacts (Docker images); never patch production directly |
| 6 | **Processes** | Execute the app as stateless processes | No sticky sessions; state in external stores (Redis, DB) |
| 7 | **Port Binding** | Export services via port binding | Self-contained web server; no external app server dependency |
| 8 | **Concurrency** | Scale out via the process model | Horizontal scaling; each process type scales independently |
| 9 | **Disposability** | Maximize robustness with fast startup and graceful shutdown | Sub-second startup; handle SIGTERM gracefully; drain connections |
| 10 | **Dev/Prod Parity** | Keep dev, staging, and production as similar as possible | Same Docker images across environments; differ only in config |
| 11 | **Logs** | Treat logs as event streams | Write to stdout; external log aggregation (not local files) |
| 12 | **Admin Processes** | Run admin tasks as one-off processes | Migrations, data fixes as jobs; same codebase and config |

**Limitations**: 12-Factor was designed for web applications. Data-intensive workloads, ML pipelines, and event-driven systems may require adjustments to factors 6 (stateless) and 8 (concurrency).

---

### Infrastructure-as-Code Patterns

**When to use**: For all infrastructure provisioning and management. There is no acceptable alternative for production environments.

**Tool Selection**:

| Tool | Best For | State Management | Language |
|------|---------|------------------|----------|
| **Terraform** | Multi-cloud, general purpose | Remote state (S3, GCS) | HCL |
| **Pulumi** | Teams preferring general-purpose languages | Remote state | Python, TypeScript, Go |
| **CloudFormation** | AWS-only environments | AWS-managed | YAML/JSON |
| **CDK** | AWS with programming language preference | AWS-managed via CFN | TypeScript, Python |

**Module Structure Template**:
```
infrastructure/
  modules/
    networking/       ← VPC, subnets, security groups
    compute/          ← EC2, ECS, Lambda
    database/         ← RDS, DynamoDB
    monitoring/       ← CloudWatch, Datadog
    security/         ← IAM, KMS, WAF
  environments/
    dev/
      main.tf         ← Module composition + dev-specific params
      variables.tf
      terraform.tfvars
    staging/
      main.tf
    production/
      main.tf
  global/
    state.tf          ← Remote state configuration
    providers.tf      ← Provider versions pinned
```

**IaC Quality Checklist**:
- [ ] All resources defined in code (zero ClickOps)
- [ ] Remote state with locking (prevent concurrent modifications)
- [ ] Modules are parameterized and reusable
- [ ] Drift detection runs on schedule
- [ ] Plan output reviewed before apply
- [ ] Sensitive values stored in vault, never in tfvars

**Limitations**: IaC introduces a learning curve and requires discipline to maintain. State management is the most common source of issues — always use remote state with locking, and never manually edit state files.

---

### Container Orchestration Decisions

**When to use**: When deciding how to run containerized workloads in production.

**Decision Framework**:

| Factor | Kubernetes | Managed Container Service (ECS, Cloud Run) | Serverless (Lambda, Cloud Functions) |
|--------|-----------|---------------------------------------------|--------------------------------------|
| Team expertise | K8s experience on team | Container experience, not K8s | Any |
| Workload type | Long-running, stateful, complex | Long-running, stateless | Event-driven, short-lived |
| Scaling needs | Fine-grained control | Automated, simpler config | Fully automated |
| Operational burden | High (even managed K8s) | Medium | Low |
| Cost at scale | Efficient with right-sizing | Moderate | Can be expensive at high volume |
| Vendor lock-in | Low (portable) | Medium | High |

**Kubernetes Decision**:
```
Do you NEED Kubernetes?
  ├── Complex service mesh with 10+ services? → Consider K8s
  ├── Stateful workloads requiring custom operators? → Consider K8s
  ├── Multi-cloud portability is a hard requirement? → Consider K8s
  └── Otherwise → Managed container service is simpler and cheaper
```

**Limitations**: Kubernetes is powerful but operationally expensive. Even managed Kubernetes (EKS, GKE, AKS) requires significant expertise. Do not adopt K8s for fewer than 5-10 services unless you have a specific requirement it uniquely solves.

---

### Serverless Patterns and Tradeoffs

**When to use**: For event-driven workloads, APIs with variable traffic, or background processing jobs.

**Pattern Catalog**:

| Pattern | Description | Best For |
|---------|-------------|----------|
| **API Gateway + Lambda** | HTTP requests trigger serverless functions | APIs with variable/spiky traffic |
| **Event Processing** | Queue/stream events trigger functions | Async processing, ETL, notifications |
| **Scheduled Jobs** | Cron-triggered functions | Periodic tasks, cleanup, reports |
| **Fan-Out/Fan-In** | One event triggers multiple parallel functions | Parallel processing, batch operations |

**Tradeoff Analysis**:

| Benefit | Tradeoff |
|---------|----------|
| No infrastructure management | Cold start latency (100ms-5s depending on runtime) |
| Pay per invocation | Expensive at sustained high throughput |
| Auto-scaling to zero | Limited execution duration (15 min Lambda, 60 min Cloud Functions) |
| Rapid deployment | Vendor lock-in to function runtime and triggers |
| Built-in HA | Debugging and observability more complex |

**When NOT to Use Serverless**:
- Sustained high throughput (>100 req/sec consistently) — containers are cheaper
- Workloads requiring >15 minutes execution
- Applications needing persistent connections (WebSockets, long-polling)
- Latency-sensitive operations where cold starts are unacceptable

**Limitations**: Serverless is not a universal solution. The "no servers to manage" benefit comes with trade-offs in debugging, testing, and operational visibility. Always model costs at projected scale before committing.

---

### Multi-Region Architecture

**When to use**: When availability requirements exceed what a single region provides (typically 99.99%+ SLA), or when latency requirements demand geographic proximity to users.

**Architecture Tiers**:

| Tier | Description | Availability | Complexity | Cost |
|------|-------------|-------------|------------|------|
| **Single AZ** | One availability zone | ~99.9% | Low | Baseline |
| **Multi-AZ** | Multiple AZs in one region | ~99.99% | Medium | +30-50% |
| **Active-Passive Multi-Region** | Primary region + standby | ~99.99% with manual failover | High | +100% |
| **Active-Active Multi-Region** | Both regions serve traffic | ~99.999% | Very High | +150-200% |

**Multi-AZ Template** (recommended default for production):
```
Region: us-east-1
  AZ-a: Application instances + DB primary
  AZ-b: Application instances + DB replica
  AZ-c: Application instances (optional)

Load Balancer: Cross-AZ with health checks
Database: Multi-AZ RDS (automatic failover)
Cache: ElastiCache Multi-AZ with automatic failover
Storage: S3 (automatically cross-AZ)
```

**Limitations**: Multi-region adds complexity in data synchronization, conflict resolution, and routing. Active-active multi-region with strong consistency is extremely difficult. Consider eventual consistency models and design for conflict resolution if pursuing active-active.

---

### Cost Optimization Framework

**When to use**: Continuously, as part of every infrastructure decision and on a monthly review cadence.

**Cost Optimization Levers**:

| Lever | Savings Potential | Effort | Risk |
|-------|-------------------|--------|------|
| **Right-sizing** | 20-40% | Low | Low |
| **Reserved/Committed Use** | 30-60% | Low | Medium (commitment) |
| **Spot/Preemptible** | 60-90% | Medium | High (interruption) |
| **Auto-scaling** | 15-30% | Medium | Low |
| **Storage tiering** | 20-50% | Low | Low |
| **Architecture optimization** | Variable | High | Medium |

**Monthly Review Template**:
```markdown
## Cloud Cost Review: [Month]

**Total Spend**: $[X] (vs. budget: $[Y])
**Delta**: [+/-]% vs. last month

### Top Cost Drivers
| Service | Cost | % of Total | Trend | Action |
|---------|------|-----------|-------|--------|
| EC2 | $X | Y% | [up/down/flat] | [Right-size / Reserve / Optimize] |
| RDS | $X | Y% | | |
| S3 | $X | Y% | | |

### Optimization Actions
- [ ] [Action]: Estimated savings $X/month
- [ ] [Action]: Estimated savings $X/month

### Reserved Instance Recommendations
- [Instance type]: [Count] at [term] = $X savings/year
```

**Limitations**: Cost optimization must be balanced against performance and reliability. Do not sacrifice availability to save money. The cheapest infrastructure is the one that goes down.

---

### CI/CD Pipeline Patterns

**When to use**: For every project. There is no acceptable alternative to automated build, test, and deploy pipelines.

**Pipeline Stages**:

```
Source → Build → Test → Security → Deploy Staging → Test Staging → Deploy Prod → Verify
```

**Stage Details**:

| Stage | Activities | Gate |
|-------|-----------|------|
| **Source** | Code push, PR created | Code review approved |
| **Build** | Compile, Docker build, artifact creation | Build succeeds |
| **Unit Test** | Unit tests, coverage check | Coverage >= threshold |
| **Security** | SAST, dependency scan, secret scan | No critical/high findings |
| **Deploy Staging** | Deploy to staging environment | Health checks pass |
| **Integration Test** | E2E tests, contract tests | All tests pass |
| **Deploy Production** | Rolling deploy or blue-green | Health checks + canary metrics |
| **Verify** | Smoke tests, synthetic monitoring | Key flows operational |

**Deployment Strategy Selection**:

| Strategy | Downtime | Rollback Speed | Resource Cost | Best For |
|----------|----------|----------------|---------------|----------|
| **Rolling** | Zero | Minutes | 1x + buffer | Most applications |
| **Blue-Green** | Zero | Seconds (switch) | 2x during deploy | Critical applications |
| **Canary** | Zero | Seconds (route) | 1x + small canary | High-traffic, risk-averse |
| **Recreate** | Brief | Minutes | 1x | Dev/staging environments |

**Limitations**: Pipeline complexity should match team maturity. Start with a simple build-test-deploy pipeline and add stages as the team grows and the product matures.

---

### Observability (Logs, Metrics, Traces)

**When to use**: From day one. Observability is not a feature to add later — it is infrastructure that must exist from the first deployment.

**Three Pillars**:

| Pillar | Purpose | Tool Examples | Key Practices |
|--------|---------|---------------|---------------|
| **Logs** | Record discrete events | ELK, CloudWatch Logs, Datadog | Structured JSON, correlation IDs, log levels |
| **Metrics** | Track numerical measurements over time | Prometheus, CloudWatch Metrics, Datadog | RED method (Rate, Errors, Duration), USE method |
| **Traces** | Follow requests across services | Jaeger, AWS X-Ray, Datadog APM | Distributed tracing with propagated context |

**Alerting Rules**:
```
Alert on SYMPTOMS, not causes:
  - Alert: Error rate > 1% for 5 minutes → Page
  - Alert: P99 latency > 2s for 10 minutes → Page
  - Alert: Available disk < 20% → Ticket

Do NOT alert on:
  - CPU > 80% (symptom alerts will catch the impact)
  - Individual request failures (log and aggregate)
```

**SLA/SLO/SLI Framework**:

| Term | Definition | Example |
|------|-----------|---------|
| **SLI** (Service Level Indicator) | Measured metric | Request success rate, latency P99 |
| **SLO** (Service Level Objective) | Target for the SLI | 99.9% success rate, P99 < 500ms |
| **SLA** (Service Level Agreement) | Contractual commitment with consequences | 99.9% uptime or service credits |

**Template**:
```markdown
## SLO Definition: [Service Name]

| SLI | Measurement | SLO Target | Error Budget (30d) |
|-----|-------------|------------|-------------------|
| Availability | Successful requests / total requests | 99.9% | 43.2 minutes |
| Latency (P99) | 99th percentile response time | < 500ms | N/A |
| Error Rate | 5xx responses / total responses | < 0.1% | 43.2 minutes |

**Burn Rate Alert**: If error budget consumption exceeds 2% in 1 hour → page on-call
```

**Limitations**: Observability generates significant data volume and cost. Define retention policies early: high-resolution data for 7-30 days, aggregated data for longer. Alert fatigue is a real risk — fewer, more meaningful alerts are better than comprehensive noisy alerts.

---

## Quick Reference: Cloud Architecture Decisions

| Decision | Default | Escalate When |
|----------|---------|---------------|
| Deployment target | Managed containers (ECS, Cloud Run) | Need K8s-specific features (operators, service mesh) |
| Database | Managed relational (RDS, Cloud SQL) | Need NoSQL patterns, >10TB, or sub-ms latency |
| Caching | Managed Redis (ElastiCache, Memorystore) | Need complex data structures or pub/sub |
| Object storage | S3/GCS | Never — managed object storage is always correct |
| CDN | CloudFront/Cloud CDN for static assets | Dynamic content caching requires careful cache invalidation |
| IaC | Terraform | AWS-only → CDK is acceptable; multi-cloud → Terraform |
| CI/CD | GitHub Actions | Complex pipelines → Jenkins/CircleCI; GitLab ecosystem → GitLab CI |
| Monitoring | Cloud-native (CloudWatch, GCP Monitoring) | Multi-cloud → Datadog; complex tracing → Jaeger |

---

## Operating Principle

> "Infrastructure should be invisible when it works and immediately diagnosable when it does not. Invest in automation, observability, and cost transparency from day one — they compound in value as the system grows."


## Common Pitfalls

- Cloud cost estimates change frequently — always verify current pricing
- Auto-scaling configurations need upper bounds — unbounded scaling causes bill shock
- Multi-region deployment adds complexity — only recommend when requirements justify it
