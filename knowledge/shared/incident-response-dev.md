# Incident Response for Engineering Teams — SRE Runbooks & On-Call

## Overview

Engineering incident response covers how development teams detect, triage, resolve, and learn from production failures. Unlike the security incident playbook (NIST SP 800-61 / CSIRT), this pack focuses on SRE practice: on-call rotations, runbook-driven response, blameless postmortems, and error budget management.

When production breaks at 2 AM, the team's response quality is determined entirely by the preparation done in advance. Clear severity tiers, well-tested runbooks, and a practiced postmortem culture are the difference between a 15-minute fix and a 4-hour outage.

**Version**: 1.0.0
**Type**: Knowledge Pack
**Primary Users**: ⚙️ DevOps, 🛠️ Tech Lead, 🔧 Backend Dev

---
<!-- Attribution:
  Frameworks and patterns in this knowledge pack were informed by:
  - techlearn-center/incident-response-runbooks (SRE patterns, runbook templates)
  - Google Site Reliability Engineering (SRE Book, sre.google)
  - PagerDuty Incident Response Documentation (response.pagerduty.com)
  - Adapted and expanded for Product Org OS agents.
-->

---

## Incident Severity Classification

Severity tiers define response urgency, team escalation, and communication requirements. Every incident receives a severity level at triage — and the level should be re-evaluated as the situation develops.

### Severity Tiers

| Level | Name | Definition | Response Time | Escalation |
|-------|------|-----------|---------------|------------|
| **P0** | Critical | Complete service outage or data breach/loss. Zero users can complete core flows. Revenue impact immediate. | Acknowledge in **5 min**, bridge open in **15 min** | On-call engineer → on-call lead → engineering director → CTO |
| **P1** | Major | Core feature severely degraded. Majority of users affected or key enterprise customer down. | Acknowledge in **15 min**, begin remediation in **30 min** | On-call engineer → on-call lead → engineering director |
| **P2** | Minor | Non-critical feature degraded. Partial outage affecting a subset of users or a secondary workflow. | Acknowledge in **1 hour**, begin remediation same shift | On-call engineer → on-call lead (if not resolved in 2 hrs) |
| **P3** | Low | Cosmetic issue or non-urgent bug. No direct user impact on key workflows. | Acknowledge in **4 hours**, ticket by end of business day | On-call engineer (may defer to next sprint) |
| **P4** | Enhancement | Performance improvement, technical debt item, or proactive improvement identified during incident review. | Normal sprint planning | Standard product backlog |

### Severity Determination Guide

When an alert fires, answer these questions in order:

1. **Are users unable to complete the primary workflow?** → P0
2. **Is a core feature broken for more than 20% of users?** → P1
3. **Is there any confirmed or suspected data loss or breach?** → P0 immediately (escalate to security team in parallel)
4. **Is a secondary workflow degraded but primary is healthy?** → P2
5. **Is it cosmetic, slow, or intermittent with workaround available?** → P3

**Default to higher severity when uncertain.** It is easier to downgrade a P1 to a P2 than to explain why a P0 took 45 minutes because it was triaged as P2.

### Severity and Communication Matrix

| Severity | Status Page Update | Internal Notification | Customer Notification | Executive Brief |
|----------|-------------------|----------------------|----------------------|-----------------|
| P0 | Within 10 min | Immediate (Slack #incidents + phone) | Within 30 min | Within 1 hour |
| P1 | Within 20 min | Slack #incidents | Within 1 hour | If >2 hours |
| P2 | If customer-visible | Slack #incidents | If enterprise-affected | No |
| P3 | No | Ticket only | No | No |
| P4 | No | Ticket only | No | No |

---

## Incident Response Process

Every incident follows five phases. Do not skip phases — especially "Learn," which is where the investment of every other phase pays dividends.

### Phase 1: Detect

**Goal**: Identify that something is wrong, as fast as possible.

**Detection vectors**:
- Automated alerting (APM, uptime monitors, error rate thresholds)
- Synthetic monitoring (scripted user journeys running on a schedule)
- Customer reports via support (often the first signal for edge-case failures)
- On-call engineer observation during a routine check
- Anomaly detection in dashboards (traffic drop, latency spike)

**Detection best practices**:
- Alert on **symptoms** (error rate > 1%, p99 latency > 2s), not just causes (CPU > 80%)
- Set alert thresholds at levels that matter to users — not at arbitrary system limits
- Use multi-window alerting (short window to detect, longer window to confirm) to reduce false positives
- Every alert must have a corresponding runbook link in the alert body

**MTTD target**: P0/P1 detected within 5 minutes of first impact

---

### Phase 2: Triage

**Goal**: Confirm the incident is real, assign a severity, declare it, and mobilize the right people.

**Triage checklist**:
- [ ] Confirm the alert is a true positive (check dashboards, not just the alert)
- [ ] Identify affected surface area (which services, which users, which regions)
- [ ] Assign severity (P0–P4) using the guide above
- [ ] Declare the incident in the incident channel (create #incident-YYYY-MM-DD-[name])
- [ ] Assign Incident Commander (IC) — default is the on-call engineer; escalate for P0
- [ ] Assign Communications Lead if P0 or P1 (separate from IC — IC should not be typing status updates)
- [ ] Link to the runbook for the identified failure pattern

**Incident Commander responsibilities**:
- Own the response from declaration to resolution
- Drive the call/channel — keep it focused on resolution, not diagnosis rabbit holes
- Make the call on remediation actions when the team is stuck
- Authorize rollbacks, failovers, or emergency deploys
- Ensure the postmortem is scheduled before the call closes

---

### Phase 3: Respond

**Goal**: Stop the bleeding. Prioritize restoring service over finding root cause.

**Response principles**:
1. **Restore first, diagnose second.** A rollback that fixes the outage in 10 minutes beats a 2-hour root cause analysis that ends in the same rollback.
2. **One action at a time.** Making multiple changes simultaneously makes it impossible to know what fixed (or worsened) things.
3. **Communicate continuously.** Update the incident channel every 15-30 minutes even if there is nothing new to report — silence breeds panic.
4. **Preserve evidence.** Before rolling back or restarting, capture logs, thread dumps, and metrics snapshots. Evidence destroyed now means a shallower postmortem.
5. **Timebox investigations.** If a hypothesis has not been confirmed in 20 minutes, pivot to a different theory or escalate.

**Common response actions by failure type**:

| Failure Type | First Response | Second Response |
|-------------|---------------|-----------------|
| Bad deploy | Roll back immediately | Hotfix path if rollback is not safe |
| Infrastructure failure | Failover to standby | Scale out / restart unhealthy instances |
| Database performance | Kill long-running queries, check indexes | Connection pool restart, read replica failover |
| Dependency outage | Activate circuit breaker / fallback | Notify dependency team, set degraded mode |
| Traffic spike | Scale out, activate CDN caching | Rate limiting, shed non-critical load |
| Data corruption | Halt writes, assess scope | Point-in-time recovery, downstream notification |

---

### Phase 4: Resolve

**Goal**: Confirm the incident is over, restore full service, and close the loop.

**Resolution checklist**:
- [ ] Confirm all error rates have returned to baseline (not just trending down)
- [ ] Confirm all affected regions/services show green
- [ ] Verify no secondary failures were introduced during remediation
- [ ] Remove any temporary mitigations that should not remain in production (e.g., rate limits set during spike)
- [ ] Update status page to "Resolved" with a brief description
- [ ] Send customer-facing post-resolution notification (P0/P1)
- [ ] Schedule postmortem (within 48-72 hours while memory is fresh)
- [ ] Create follow-up tickets for all action items identified during the incident
- [ ] Close the incident channel with a summary post

**Resolution declaration**: The IC formally declares the incident resolved. Do not close until all checks above are complete. Premature resolution is a common cause of follow-on incidents.

---

### Phase 5: Learn

**Goal**: Extract the maximum learning from the incident to prevent recurrence and improve response.

This phase is not optional — it is the phase that makes the investment in the previous four worthwhile. A team that resolves 50 incidents without ever improving is running a treadmill. See the **Postmortem Template** and **Blameless Culture** sections below.

---

## On-Call Best Practices

### Rotation Design

A healthy on-call rotation protects engineer wellbeing while ensuring coverage. Burned-out on-call engineers miss alerts, make poor decisions, and leave the company.

**Core design principles**:
- **Primary + Secondary**: Always maintain a two-tier rotation. Primary responds; secondary escalates to if primary is unresponsive within 5 minutes. Never rely on a single person.
- **Rotation frequency**: Weekly rotations are the most common balance between context continuity and rest. Shorter = more switches (loss of context); longer = more burden.
- **Handoff procedure**: Outgoing on-call must complete a written handoff covering active incidents, degraded systems, recent deploys at risk, and known noisy alerts.
- **Team size**: A rotation with fewer than 4 engineers means each person is on-call more than once a month — a strong predictor of burnout.
- **Follow-the-sun for global teams**: Split rotations by timezone to avoid requiring engineers to respond at 3 AM. The goal is one team never covers more than 12 hours of their own nighttime.

**Handoff template**:
```
## On-Call Handoff — [Date] [Outgoing] → [Incoming]

### Active / Watchlist Items
- [Service/issue]: [Status, what to watch for, who to contact if it worsens]

### Recent Deploys (last 48 hours)
- [Service] [version] deployed [date] — [any known risks or rollback procedure]

### Known Noisy Alerts
- [Alert name]: [Why it fires, whether it requires action, ticket ref]

### Open Incidents
- [Incident ID]: [Status, current owner, expected resolution]

### Contacts
- Escalation: [Name, phone]
- Vendor on-call (if relevant): [Name, number]
```

---

### Alert Fatigue Prevention

Alert fatigue is the single biggest threat to on-call effectiveness. An engineer who sees 50 alerts a week starts treating all of them as noise — including the P0.

**Alert hygiene rules**:
- Every alert must be **actionable**. If the correct response is "monitor and wait," it is not an alert — it is a dashboard.
- Every alert must have a **runbook**. If there is no runbook, the alert is not ready to fire.
- **Review alert volume monthly**. Any alert that fires more than 5 times without resulting in a real action is a candidate for tuning or deletion.
- **Track alert-to-action rate**: What percentage of alerts require the on-call to actually do something? Below 50% indicates systemic alert fatigue risk.
- **No informational alerts at night**. Any alert that fires outside business hours must be P2 or higher.

**Noise reduction tactics**:
- Increase thresholds for alerts that fire frequently with no action
- Add minimum duration requirements (must be elevated for 5 minutes before alerting)
- Group related alerts into a single incident (avoid 20 alerts for one root cause)
- Use symptom-based alerting at the user-visible layer rather than resource-based alerting at the infrastructure layer

---

### Escalation Matrix Template

```
## Escalation Matrix — [Service/Team Name]

| Level | Condition | Who | Contact Method | Response SLA |
|-------|-----------|-----|----------------|--------------|
| L1 | Initial alert fires | On-call Engineer (Primary) | PagerDuty page | 5 min acknowledge |
| L1.5 | Primary unresponsive 5 min | On-call Engineer (Secondary) | PagerDuty escalation | 5 min acknowledge |
| L2 | P0/P1 unresolved after 30 min | Engineering Lead / Staff Engineer | PagerDuty + phone | 10 min respond |
| L3 | P0 unresolved after 1 hour | Engineering Director | Phone + Slack DM | Immediate |
| L4 | P0 with customer/data impact | CTO + Customer Success Lead | Phone | Immediate |
| External | Dependency-caused outage | [Vendor name] support | [Support line/portal] | Per SLA |
```

---

### On-Call Compensation Guidelines

On-call is a professional obligation that carries real personal cost. Compensation should reflect that.

**Common models**:
- **Flat stipend**: A fixed weekly amount for being on rotation (e.g., $200-500/week depending on market and frequency of pages)
- **Per-page compensation**: Payment for each after-hours page that requires active work
- **Time-in-lieu**: Compensatory time off following a disruptive on-call week (common in Europe and startup environments)
- **On-call equity**: Additional equity vesting credit for engineers who consistently carry on-call load

**Principles**:
- Compensation should increase when rotation is shorter (higher burden per engineer)
- After-hours pages that require more than 30 minutes of active work warrant compensation equivalent to overtime
- On-call burden should factor into performance reviews and promotion criteria, not just output
- Make on-call burden visible to management — track hours paged, hours of sleep disrupted, and incidents resolved per engineer

---

## Runbook Templates

Runbooks remove the guesswork from high-pressure situations. A runbook that requires deep system knowledge to follow has failed. Write runbooks for the sleepy, stressed engineer at 3 AM.

### Runbook Structure (for all runbooks)

```markdown
# [Service/Issue Name] Runbook

**Last Tested**: [YYYY-MM-DD]
**Owner**: [Team/person]
**Severity Range**: [P0/P1/P2]
**Escalation Contact**: [Name + contact]

## Symptoms
[What the alert or report looks like. Dashboard screenshots if available.]

## Impact
[What users experience when this happens. Business context.]

## Investigation
[Ordered steps to diagnose. Commands with exact syntax. Expected vs. abnormal output.]

## Resolution
[Ordered steps to fix. Exact commands. Flags and caveats.]

## Rollback
[How to undo the resolution if it makes things worse.]

## Escalation
[When and who to escalate to if the runbook does not resolve the issue.]

## Related Runbooks
[Links to runbooks for related failures.]
```

---

### High CPU Runbook

**Symptoms**: CPU utilization alert (>80% sustained), increased latency, possible request timeouts.

**Investigation**:
1. Identify which instance(s) are affected: check APM host map or cloud console
2. SSH into the affected host (or use `kubectl exec` for container)
3. Run `top` or `htop` — identify the PID consuming CPU
4. For the high-CPU process, run: `ps aux | grep [pid]` to identify service
5. Check for runaway queries: connect to DB, run `SHOW PROCESSLIST` (MySQL) or `SELECT pid, query, state FROM pg_stat_activity WHERE state = 'active'` (Postgres)
6. Check recent deploys — correlate spike start time with deploy history
7. Check for traffic spike: review request rate graph in APM for the same time window

**Resolution**:
- If caused by specific query: kill the query (`KILL [query_id]`), add missing index, or add query timeout
- If caused by bad deploy: roll back the deploy
- If caused by traffic spike: scale horizontally (add instances), enable CDN caching if applicable
- If process is unresponsive: `kill -9 [pid]` as last resort (service will restart via process manager)

**Escalation**: If CPU remains elevated 20 minutes after applying resolution, escalate to on-call lead.

---

### High Memory / OOM Runbook

**Symptoms**: Memory utilization alert (>85% sustained), OOMKilled pods, service restarts.

**Investigation**:
1. Check which pods/instances are restarting: `kubectl get pods` (look for RESTARTS count) or cloud console
2. Check OOM events: `kubectl describe pod [pod-name]` (look for OOMKilled in Last State)
3. Check memory growth trend — is it gradual (leak) or sudden (spike)?
4. For gradual growth: look for recent code changes that added in-memory caching, large dataset loading, or removed memory limits
5. For sudden spike: check for traffic anomaly, large file upload, or batch job starting

**Resolution**:
- Immediate: Restart affected pods/instances to clear memory: `kubectl rollout restart deployment/[name]`
- If memory leak in code: roll back to previous version, create ticket for fix
- If undersized: increase memory limits in deployment config (requires deploy)
- If caused by specific operation: implement pagination, streaming, or offload to queue

**Escalation**: If restarts are occurring faster than the service can recover, escalate immediately.

---

### Database Performance Runbook

**Symptoms**: Query latency alert, connection pool exhaustion, application timeout errors pointing to DB.

**Investigation**:
1. Check DB dashboard: CPU, active connections, query latency metrics
2. Identify slow queries: run slow query log analysis or `EXPLAIN ANALYZE` on suspects
3. Check active connections: compare current vs. max allowed (connection pool exhaustion is common)
4. Check for lock contention: `SELECT * FROM pg_locks` (Postgres) or `SHOW ENGINE INNODB STATUS` (MySQL)
5. Check index usage: are recent feature deploys using indexes or performing full table scans?

**Resolution**:
- Kill long-running blocking queries (get approval from IC first for production DBs)
- If connection exhaustion: restart application to release leaked connections, then address root cause
- If missing index: `CREATE INDEX CONCURRENTLY` (Postgres) for zero-downtime index creation
- If lock contention: identify and terminate the blocking transaction

**Escalation**: Any risk of data loss or corruption → escalate to engineering lead immediately before taking action.

---

### Service Unavailable Runbook

**Symptoms**: HTTP 503/502 errors, uptime monitor firing, load balancer health checks failing.

**Investigation**:
1. Check load balancer health check status — how many instances are healthy vs. failing?
2. Check application logs for the unhealthy instances: what error is causing the health check to fail?
3. Verify the application process is running: `systemctl status [service]` or `kubectl get pods`
4. Check disk space — full disk is a common silent killer: `df -h`
5. Check recent deploys — did a deploy introduce a startup failure or config error?
6. Check external dependencies: is the DB, cache, or third-party API causing startup failures?

**Resolution**:
- If bad deploy: roll back immediately
- If disk full: identify and clear log files, temp files, or old build artifacts
- If dependency failure causing startup crash: enable degraded mode (if available) or restart when dependency recovers
- If process crashed: restart the service and monitor closely

---

### Deployment Rollback Runbook

**Symptoms**: Error rate spike immediately following deploy, specific functionality broken post-deploy.

**Investigation**:
1. Confirm the deploy timestamp correlates with the issue start time
2. Identify what changed: review the diff/changelog for the deploy
3. Confirm the issue is deterministic (not intermittent) before deciding to roll back

**Resolution**:

For Kubernetes / container deployments:
```bash
# Check rollout history
kubectl rollout history deployment/[service-name]

# Roll back to previous version
kubectl rollout undo deployment/[service-name]

# Roll back to a specific revision
kubectl rollout undo deployment/[service-name] --to-revision=3

# Monitor rollback progress
kubectl rollout status deployment/[service-name]
```

For Vercel / PaaS deployments:
- Navigate to deployment history in the platform dashboard
- Click "Promote" or "Redeploy" on the last known-good deployment

For database migrations included in the deploy:
- Rollback is more complex if a schema migration ran — consult engineering lead
- If migration is backward-compatible, app rollback is safe without reverting the migration
- If migration is destructive (dropped columns), rollback requires a forward fix, not a rollback

**Post-rollback**: Confirm error rate returns to baseline. Create a hotfix branch. Do not re-deploy without understanding the root cause.

---

### SSL/TLS Certificate Expiry Runbook

**Symptoms**: Certificate expiry alert, users seeing browser security warnings, API clients receiving TLS errors.

**Investigation**:
1. Confirm expiry date: `openssl s_client -connect [domain]:443 2>/dev/null | openssl x509 -noout -dates`
2. Check whether auto-renewal is configured (Let's Encrypt / ACM) and why it failed
3. Identify all services using the expiring certificate

**Resolution**:

Let's Encrypt (Certbot):
```bash
# Check renewal status
certbot renew --dry-run

# Force renewal
certbot renew --force-renewal

# Reload web server to pick up new cert
systemctl reload nginx  # or apache2
```

AWS Certificate Manager (ACM):
- ACM auto-renews — check if DNS validation records are still present
- Navigate to ACM console, find the certificate, check "Renewal status" and "Domain validation"
- If DNS validation record is missing, re-add the CNAME record shown in ACM

**Prevention**: Alerts should fire 30 days before expiry (warning) and 7 days before expiry (critical). Never rely solely on auto-renewal — monitor expiry dates independently.

---

## Runbook Writing Guide

A runbook that exists but cannot be followed under pressure is not a runbook — it is documentation theater.

### Structure Requirements

Every runbook must have:
1. **Symptoms** — what the alert/report looks like, not what is happening internally
2. **Impact** — what users experience (grounds the responder in what matters)
3. **Investigation** — ordered steps with exact commands, not high-level directions
4. **Resolution** — ordered steps with exact commands and expected outcomes
5. **Rollback** — how to undo the fix if it makes things worse
6. **Escalation** — when and who to call if the runbook fails

### Writing Principles

- **Write for a new team member on their first on-call shift.** If the runbook requires deep context to follow, it will fail at 3 AM.
- **Use exact commands, not concepts.** "Restart the service" → `systemctl restart [service-name]` or `kubectl rollout restart deployment/[name]`
- **Show expected output.** After a command, show what the successful output looks like so the responder knows if it worked.
- **One action per step.** Do not combine diagnosis and action in the same step.
- **Include gotchas.** "NOTE: This command will briefly interrupt the websocket connections" is essential context.

### Testing and Maintenance

- **Test every runbook in staging before it is considered ready.** An untested runbook has unknown failure modes.
- **Review runbooks after every incident.** If the responder had to deviate from the runbook, update it.
- **Set a maximum staleness policy**: runbooks not reviewed in 90 days are flagged for review.
- **Include a "last tested" date** in the runbook header.

---

## Incident Communication Templates

### Internal Status Update (every 15-30 minutes during P0/P1)

```
**INCIDENT UPDATE — [HH:MM UTC]**
Severity: [P0/P1]
Status: [Investigating / Identified / Remediating / Monitoring]
Incident Commander: [Name]

**What we know**: [1-2 sentences on current state of the system]
**What we're doing**: [Current action being taken]
**Next update**: [HH:MM UTC] or when status changes

Impact: [Brief description of user impact]
```

### Customer-Facing Status Page Template

```
**[Service Name] — [Investigating / Identified / Update / Resolved]**

[Date, HH:MM UTC]

We are [investigating reports of / have identified / continue to monitor] an issue affecting [service/feature]. [% of users / which regions / which operations] may be [experiencing / have experienced] [symptoms].

Our team is actively working to resolve this. We will provide the next update by [HH:MM UTC].

We apologize for the inconvenience.
```

### Post-Resolution Customer Notification

```
Subject: Resolved — [Service] Incident on [Date]

We are writing to inform you that an incident affecting [service/feature] between [start time] and [end time] UTC has been resolved.

**What happened**: [1-2 sentences, plain language, no jargon]
**Impact**: [Who was affected and how]
**What we did**: [Brief remediation steps taken]
**What we're doing to prevent recurrence**: [1-2 action items]

We apologize for any disruption this caused. If you have questions, please contact [support channel].
```

---

## Postmortem Template

Postmortems are the primary mechanism for extracting learning from incidents. A postmortem that produces no action items has not been done — it has been performed.

```markdown
# Postmortem: [Incident Name / ID]

**Date**: [YYYY-MM-DD]
**Duration**: [HH:MM — HH:MM UTC] ([X hours Y minutes total])
**Severity**: [P0 / P1 / P2]
**Author**: [Primary author]
**Reviewers**: [Names]
**Status**: [Draft / In Review / Final]

---

## Summary

[2-4 sentences. What happened, what was the user impact, what was the root cause, and what has been done to prevent recurrence. Written to be readable by someone who was not in the incident.]

---

## Impact

| Dimension | Details |
|-----------|---------|
| Users affected | [Number or % of user base] |
| Duration | [X hours Y minutes] |
| Features affected | [List of affected features/endpoints] |
| Data impact | [Any data lost, corrupted, or exposed — "None" if none] |
| Revenue/SLA impact | [Estimated impact — "TBD" if not yet quantified] |

---

## Timeline

All times in UTC.

| Time | Event |
|------|-------|
| [HH:MM] | [Event — be specific: "Alert fired for error rate > 2% on /api/checkout"] |
| [HH:MM] | [On-call acknowledged] |
| [HH:MM] | [Incident declared, IC assigned] |
| [HH:MM] | [Key diagnostic step — "Identified deploy at 14:32 as likely cause"] |
| [HH:MM] | [Remediation action taken — "Rollback initiated"] |
| [HH:MM] | [Recovery — "Error rate returned to baseline"] |
| [HH:MM] | [Incident resolved, status page updated] |

---

## Root Cause

[Precise technical description of the root cause. Not "human error" — describe the system conditions that made the error possible. What was the proximate cause? What was the contributing cause?]

**Five Whys Analysis**:
1. Why did [symptom occur]? → Because [cause 1]
2. Why did [cause 1] occur? → Because [cause 2]
3. Why did [cause 2] occur? → Because [cause 3]
4. Why did [cause 3] occur? → Because [cause 4]
5. Why did [cause 4] occur? → [Root cause]

---

## Lessons Learned

### What went well
- [Specific thing — e.g., "Rollback procedure was completed in under 5 minutes due to clear runbook"]
- [Specific thing — e.g., "Customer communication was drafted and posted within 8 minutes of incident declaration"]

### What could have gone better
- [Specific gap — e.g., "Alert did not fire until 12 minutes after first errors appeared due to insufficient window duration"]
- [Specific gap — e.g., "No runbook existed for this failure mode — responders had to diagnose from scratch"]

---

## Action Items

| # | Action | Owner | Priority | Due Date | Status |
|---|--------|-------|----------|----------|--------|
| 1 | [Specific action — e.g., "Add alert for DB connection pool saturation"] | [Name] | P1 | [YYYY-MM-DD] | Open |
| 2 | [Specific action — e.g., "Write runbook for high memory / OOM scenario"] | [Name] | P2 | [YYYY-MM-DD] | Open |
| 3 | [Specific action — e.g., "Reduce alert window from 15 min to 5 min for checkout errors"] | [Name] | P1 | [YYYY-MM-DD] | Open |

**Action items must have owners and due dates.** An action item without an owner is a wish, not a commitment.
```

---

## Blameless Postmortem Culture

The purpose of a postmortem is learning, not punishment. Engineers make mistakes. Systems have failure modes. Organizations that respond to incidents with blame prevent people from reporting problems, taking risks, or being honest in postmortems — which guarantees more incidents.

**Blameless principles**:

1. **Assume good intent.** Engineers made the decisions that seemed best given the information, pressure, and tools available at the time. The postmortem asks "what conditions made this outcome possible?" not "who is responsible?"

2. **Investigate system failures, not personal failures.** If a human action caused an incident, ask: Why did the system allow that action? Why was there no safeguard? These are engineering problems.

3. **Separate learning from accountability.** Engineers can be held accountable for following procedures without their mistakes being weaponized. "We need to understand what happened" and "we need to make sure this doesn't happen again" are compatible with "this will not affect your performance review."

4. **Psychological safety is load-bearing.** If engineers fear that honest postmortems will harm them, they will write dishonest postmortems. Dishonest postmortems produce no learning. The culture choice is between blameless postmortems with real learning or blame-based postmortems with theater.

5. **Fix the system, not the person.** If the recommendation after an incident is "train the engineer more carefully," the postmortem has failed. The recommendation should be a system change: automation, better tooling, improved runbooks, additional safeguards.

---

## SLI / SLO / SLA Framework

### Definitions

| Term | Definition | Example |
|------|-----------|---------|
| **SLI** (Service Level Indicator) | A specific measurable metric that reflects service health from the user's perspective | "% of requests completed in < 200ms" |
| **SLO** (Service Level Objective) | An internal target for the SLI. The commitment the team makes to itself. | "99.5% of requests complete in < 200ms over a 30-day rolling window" |
| **SLA** (Service Level Agreement) | A contractual commitment to customers, typically with financial penalties for breach | "99% availability per calendar month or credit issued" |
| **Error Budget** | The allowable amount of SLO violation. If SLO is 99.9%, the error budget is 0.1% of the measurement window. | 0.1% of 30 days = 43.2 minutes of downtime per month |

### SLI Design Principles

Good SLIs measure what users experience, not what systems report:
- **Availability**: `successful_requests / total_requests` (not server uptime %)
- **Latency**: `requests_under_threshold / total_requests` (not average latency — averages hide tail latency)
- **Error rate**: `error_responses / total_responses`
- **Throughput**: `requests_completed_per_second`

Avoid SLIs that measure internal resource metrics (CPU, memory) — these are implementation details. Users do not care about CPU; they care whether their request succeeded.

### Error Budget Calculation

```
Error Budget = (1 - SLO target) × measurement window

Example:
SLO: 99.9% availability over 30 days
Measurement window: 30 days × 24 hours × 60 minutes = 43,200 minutes
Error Budget = (1 - 0.999) × 43,200 = 43.2 minutes

If the service has been down for 30 minutes this month:
Remaining budget = 43.2 - 30 = 13.2 minutes
Budget consumed = 30/43.2 = 69.4%
```

### Error Budget Policy

The error budget creates a mechanical link between reliability and feature velocity:

| Budget Consumed | Policy |
|----------------|--------|
| < 50% | Normal feature development velocity |
| 50-75% | Reliability work begins alongside feature work |
| 75-100% | Freeze new feature deploys; focus on reliability |
| > 100% (SLO breached) | All hands on reliability until budget is restored |

---

## Chaos Engineering Basics

Chaos engineering is the practice of intentionally introducing failures in controlled conditions to find weaknesses before they cause real incidents.

### Core Principles

1. **Build a hypothesis around steady state.** Define what "normal" looks like before injecting failure: response time, error rate, throughput.
2. **Vary real-world events.** Inject failures that mimic real incidents: instance termination, network partition, latency injection, dependency failure.
3. **Run in production.** Staging does not replicate production traffic patterns, dependencies, or scale. Controlled production experiments are more valuable than staging experiments.
4. **Minimize blast radius.** Start with a small percentage of traffic or a single instance. Expand scope as confidence grows.
5. **Stop when steady state is violated.** If the experiment causes real user impact, abort immediately.

### Common Chaos Experiments

| Experiment | What It Tests | Tool |
|-----------|---------------|------|
| Random instance termination | Auto-scaling, failover, session persistence | AWS FIS, Chaos Monkey |
| Network latency injection (100-500ms) | Timeout handling, retry logic, UI loading states | tc (Linux), Toxiproxy |
| Dependency unavailability | Circuit breakers, fallback behavior, error messages | Toxiproxy, WireMock |
| Resource exhaustion (CPU, memory) | Throttling, backpressure, queue behavior | stress-ng, cgroups |
| Database connection failure | Connection pooling, reconnect logic, queue buildup | iptables, Chaos Toolkit |
| Deploy failure mid-rollout | Canary detection, automatic rollback | Kubernetes rollout pause |

### Game Day Structure

A Game Day is a scheduled chaos experiment conducted as a team exercise.

1. **Announce** the Game Day 1-2 weeks in advance. Brief all on-call engineers.
2. **Define the experiment**: what failure will be injected, in which service, at what scale.
3. **Set success criteria**: what does "the system handled it well" look like?
4. **Run the experiment** during business hours with the team observing dashboards.
5. **Debrief**: what failed as expected? What failed unexpectedly? What improvements are needed?
6. **Document findings** as runbook updates and engineering tickets.

---

## Incident Metrics

Track these metrics to evaluate and improve incident response effectiveness over time.

| Metric | Definition | Formula | Target |
|--------|-----------|---------|--------|
| **MTTD** | Mean Time to Detect — from first user impact to alert firing | Avg(alert_time - impact_start_time) | < 5 min for P0/P1 |
| **MTTI** | Mean Time to Investigate — from detection to IC assigned and triage complete | Avg(triage_complete - alert_time) | < 15 min for P0 |
| **MTTR** | Mean Time to Resolve — from incident declaration to resolution | Avg(resolution_time - declaration_time) | < 60 min for P0; < 4 hrs for P1 |
| **Incident Frequency** | Number of incidents per week/month by severity | Count(incidents) / period | Trending down quarter-over-quarter |
| **Recurrence Rate** | % of incidents that are repeat occurrences of a previous root cause | Count(repeat_incidents) / Count(total_incidents) | < 20% |
| **Action Item Completion Rate** | % of postmortem action items completed on schedule | Count(completed_on_time) / Count(total) | > 80% within deadline |
| **Alert-to-Action Rate** | % of alerts that required actual engineering action | Count(actionable_alerts) / Count(total_alerts) | > 50% |

**Display these metrics in a shared dashboard.** Metrics that are not visible are not improved.

---

## AI On-Call / SRE Teammate

A new class of tooling sits alongside the on-call engineer: AI agents that watch telemetry, correlate signals, and draft root-cause hypotheses and runbook steps during an incident. Used well, they compress the Detect → Triage → Respond loop by surfacing the likely cause and the matching runbook before a sleepy human has finished reading the alert. Used badly, they auto-execute remediation no one reviewed and turn a P1 into a P0. The dividing line is a hard human-approval gate.

**The pattern: observe → propose → human-approve.**

1. **Observe** — the AI teammate ingests the same signals the on-call sees (APM, logs, error rates, recent deploy history, dependency status) plus the runbook corpus. It does NOT take privileged action to gather this; it reads what monitoring already exposes.
2. **Propose** — on an alert, it produces a *draft*: a ranked set of root-cause hypotheses with the evidence behind each, the matching runbook (linked, per our alert-has-a-runbook rule above), and the specific remediation steps it would suggest (rollback target, query to kill, pod to restart). This is the AI's whole job: a structured first pass, not an action.
3. **Human-approve** — a human (the Incident Commander or on-call engineer) reviews the proposal and decides. Nothing the AI proposes — rollback, failover, kill query, restart, scale — executes until a human approves it. The AI may *prepare* the exact command (so the human can paste-and-run), but the human pulls the trigger. This preserves the "one action at a time" and "restore first, with the IC authorizing" discipline from Phase 3 above.

**Where it fits our process:** AI-proposed RCA accelerates Phase 2 (Triage — faster, evidence-backed severity and surface-area calls) and Phase 3 (Respond — the matching runbook and a drafted remediation surface in seconds). It MUST NOT collapse the human-approval step. The severity tiers, escalation matrix, and IC authority defined above are unchanged: the AI is an input to the IC's judgment, never a substitute for it. Treat AI-proposed remediation exactly like a junior engineer's suggestion in the incident channel — useful, reviewed, approved or rejected by the person accountable.

**Landscape (examples, not endorsements — evaluate against this gate):** Datadog Bits AI SRE (autonomous investigation + RCA drafting on Datadog telemetry), incident.io (AI-assisted incident management and on-call summarization), and K8sGPT / HolmesGPT-style RCA agents (Kubernetes-cluster diagnosis and root-cause suggestion). *(Added 2026-06-24, DD-6:)* **Vercel Agent — Investigation (Beta)** is the platform-native instance for a Vercel shop: on an anomaly alert it auto-queries logs/metrics and proposes root causes (requires Observability Plus) — a platform-native example that fits the observe→propose loop without requiring a new incident-response architecture. Each can observe and propose; the human-approve gate is ours to enforce regardless of how much autonomy a given tool offers. Before adopting any of them, confirm: (a) it can run in propose-only mode, (b) its action surface is gated behind explicit human approval, and (c) its proposals link evidence so the IC can verify rather than trust.

**Adapted from**: Datadog Bits AI SRE (docs.datadoghq.com/bits_ai/), incident.io (incident.io), K8sGPT (k8sgpt.ai) / HolmesGPT (robusta.dev) — named as landscape examples of AI on-call / RCA tooling, not endorsements.
**Source licence**: per-source-terms (vendor products + OSS; K8sGPT Apache-2.0, HolmesGPT MIT; cited publicly, no structure lifted)
**V2V refinements**:
- Imposed the observe → propose → human-approve pattern with a hard human-approval gate as the non-negotiable adoption condition (AI proposes RCA/runbook steps; a human accountable for the incident approves before any action executes)
- Wired the pattern to this pack's existing severity tiers, escalation matrix, and Incident Commander authority (AI is an input to IC judgment, never a substitute)
- Added the three-point adoption checklist (propose-only mode, action gated behind human approval, evidence-linked proposals) for evaluating any tool against the gate

---

## AI On-Call Governance Scaffold — permission gate + closed-loop (as of 2026-06-24)

*Added 2026-06-24 (DD-12).* **Adapted from**: Azure SRE Agent (learn.microsoft.com/azure/sre-agent, GA 2026-06) + Datadog Bits AI SRE (DASH 2026) + AWS DevOps Agent (GA 2026-03-31). **Source licence**: vendor docs, publicly cited as landscape patterns. **V2V refinements**: extracted the *governance scaffold* (permission gate + agent hooks + audit) as the reusable shape every AI-on-call tool must satisfy regardless of vendor; bound it to the observe→propose→human-approve gate above.

**Pattern reference — this public pack adopts the governance shape, not the named products.** Two 2026 developments sharpen the AI-on-call gate above:

- **Permission-gate + agent-hooks scaffold (Azure SRE Agent GA model).** The reusable governance shape, vendor-neutral: an AI-on-call agent exposes a fixed set of primitives (skills, sub-agents for logs/metrics/RCA/scanning, tools, MCP connectors, pre-/post-action hooks) behind a **permission gate that evaluates every proposed tool call before it runs**, with human-approval-required on any state-changing action and an audit trail of what was proposed / approved / executed. "No change deploys without human sign-off" is the invariant — the observe→propose→human-approve gate above, made structural. When evaluating any AI-on-call tool, require: (a) a permission gate on the action surface, (b) pre/post hooks you control, (c) an audit log you own.
- **Closed-loop detect→remediate→validate (Datadog Bits AI SRE, DASH 2026).** The market is moving from investigate-only to a full **detect → investigate → remediate → validate** autonomy loop. This does NOT relax our gate: a closed-loop tool may *propose* a remediation and *validate* it post-approval, but the **remediate step still requires the human-approve gate** — autonomy on detect/investigate/validate is fine; autonomy on the state-changing remediate is not. Read "closed-loop" vendor claims as "closed-loop *around* a human approval," never "human removed from the loop."

**Net:** the permission gate + audit is the structural form of this section's human-approve rule; closed-loop autonomy is acceptable everywhere except the state-changing action, which stays gated.

---

## Agent-Config Isolation — `--safe-mode` (dev troubleshooting primitive)

*Added 2026-06-24 (DD-7).* When a Claude Code agent misbehaves and you suspect *config* rather than code — a bad the host instruction file rule, a broken skill/plugin/hook, or a misfiring MCP server poisoning every spawn — **`--safe-mode`** (or `CLAUDE_CODE_SAFE_MODE=1`, Claude Code v2.1.172) boots with the host instruction file / skills / plugins / hooks / MCP all disabled, isolating the broken layer. It's the agent-environment analog of `git bisect`: reproduce the failure in safe-mode to confirm it's config (not the task), then re-enable layers until the culprit surfaces. Pair with **`fallbackModel` chains** (up to 3 models on overload) for resilience when a model tier is unavailable mid-incident. [Claude Code v2.1.172 changelog]

---

## Operating Principle

> "Every incident is a gift — an opportunity to find and fix a weakness before it causes a worse incident. The teams that treat incidents as learning opportunities build more reliable systems than teams that treat them as failures to be blamed."
