# Security Patterns — Frameworks & Methods

## Overview

Security architecture is the practice of designing systems where confidentiality, integrity, and availability are structural properties rather than bolted-on controls. This reference provides actionable frameworks for the security decisions architects face most frequently.

The patterns here are organized from foundational (threat modeling, OWASP) to architectural (zero trust, auth design) to compliance (SOC2, GDPR). Use threat modeling first to identify what matters, then apply the appropriate patterns to address the real risks.

Security is not about eliminating all risk — it is about understanding which risks exist, which ones you accept, and which ones you mitigate with controls proportional to the threat.

---

## Frameworks

### STRIDE Threat Modeling

**When to use**: During the design phase of any new system, feature, or integration. Before implementation begins, not after.

**How it works**: STRIDE is a structured approach to identifying threats by examining each component of the system against six threat categories. It produces a prioritized list of threats with specific mitigations.

**The Six Categories**:

| Category | Threat | Typical Target | Example |
|----------|--------|---------------|---------|
| **S**poofing | Pretending to be someone else | Authentication | Stolen credentials, forged tokens |
| **T**ampering | Modifying data or code | Data integrity | SQL injection, modified API payloads |
| **R**epudiation | Denying an action occurred | Audit logging | Unlogged admin actions, missing audit trail |
| **I**nformation Disclosure | Exposing confidential data | Data confidentiality | Error messages leaking internals, unencrypted PII |
| **D**enial of Service | Making system unavailable | Availability | DDoS, resource exhaustion, algorithmic complexity attacks |
| **E**levation of Privilege | Gaining unauthorized access | Authorization | IDOR, privilege escalation, missing access checks |

**Process Template**:
```
1. DIAGRAM the system
   - Data flow diagram showing components, trust boundaries, data stores
   - Identify external entities, processes, and data flows

2. ENUMERATE threats per component
   For each component crossing a trust boundary:
   - S: Who can impersonate this component?
   - T: What data can be modified in transit or at rest?
   - R: What actions lack audit trails?
   - I: What data could be exposed?
   - D: How could this component be overwhelmed?
   - E: What access controls could be bypassed?

3. RATE each threat
   Severity = Impact (1-3) x Likelihood (1-3)
   - Critical (7-9): Address before launch
   - High (5-6): Address within first release cycle
   - Medium (3-4): Track and plan mitigation
   - Low (1-2): Accept with documentation

4. MITIGATE
   For each threat rated High or Critical:
   - Specific control to implement
   - Residual risk after mitigation
   - Owner responsible for implementation
```

**Limitations**: STRIDE is component-focused. It may miss business logic vulnerabilities (e.g., pricing manipulation, workflow bypasses). Supplement with abuse case analysis for business logic threats.

---

### OWASP Top 10 Mitigation Guide

**When to use**: As a baseline security checklist for any web application or API. This is the minimum, not the goal.

**Mitigations by Category**:

| # | Vulnerability | Architectural Mitigation |
|---|--------------|-------------------------|
| A01 | Broken Access Control | Deny-by-default access policy; validate authorization on every request at the server; enforce record-level ownership checks |
| A02 | Cryptographic Failures | Encrypt all data in transit (TLS 1.2+); encrypt PII at rest (AES-256); never store passwords in plaintext (use bcrypt/argon2) |
| A03 | Injection | Parameterized queries everywhere; input validation at API boundary; output encoding for rendered content |
| A04 | Insecure Design | Threat model during design phase; define abuse cases alongside use cases; enforce rate limits and business logic constraints |
| A05 | Security Misconfiguration | Hardened default configs; automated security scanning in CI; disable unnecessary features, ports, and accounts |
| A06 | Vulnerable Components | Automated dependency scanning (Dependabot, Snyk); defined patching SLA by severity; SBOM maintained |
| A07 | Auth Failures | MFA for sensitive operations; account lockout after failed attempts; secure session management with proper timeouts |
| A08 | Data Integrity Failures | Verify software integrity (signed packages, checksums); validate CI/CD pipeline integrity; code review for all changes |
| A09 | Logging & Monitoring Failures | Log all auth events, access control failures, and server-side validation failures; alert on anomalies; retain logs per compliance |
| A10 | SSRF | Validate and sanitize all URLs; deny-list internal network ranges; use allowlists for external service calls |

**Template for Security Review Against OWASP**:
```markdown
## OWASP Security Review: [System Name]

| # | Category | Status | Finding | Remediation |
|---|----------|--------|---------|-------------|
| A01 | Access Control | [Pass/Fail/Partial] | [Specific finding] | [Required action] |
| A02 | Crypto | ... | ... | ... |
[Continue for all 10]

**Critical Findings**: [Count]
**Remediation Owner**: [Name]
**Review Date**: [Date]
**Next Review**: [Date]
```

**Limitations**: OWASP Top 10 covers the most common web vulnerabilities but is not comprehensive. It does not cover API-specific threats (see OWASP API Security Top 10), mobile threats, or infrastructure security.

---

### Zero Trust Architecture

**When to use**: As the default network and access architecture for any new system. Especially critical for cloud-native, multi-service, and remote-access environments.

**How it works**: Zero Trust eliminates the concept of a trusted network. Every request is authenticated, authorized, and encrypted regardless of where it originates. The network location of a request (internal vs. external) does not grant any implicit trust.

**Core Principles**:

1. **Verify explicitly** — Authenticate and authorize every request based on all available data: identity, location, device health, service, data classification
2. **Use least-privilege access** — Limit access with just-in-time and just-enough-access; use risk-based adaptive policies
3. **Assume breach** — Segment access, verify end-to-end encryption, use analytics for threat detection

**Implementation Layers**:

| Layer | Controls |
|-------|----------|
| **Identity** | Strong authentication (MFA), SSO, service-to-service identity (mTLS, SPIFFE) |
| **Device** | Device health attestation, endpoint compliance checks |
| **Network** | Micro-segmentation, encrypted service mesh, no implicit trust zones |
| **Application** | Per-request authorization, input validation, output filtering |
| **Data** | Classification-based access, encryption at rest and in transit, DLP |

**Limitations**: Zero Trust is a goal, not a binary state. Full implementation requires significant infrastructure investment. Prioritize based on data sensitivity: apply strictest controls to your most sensitive data first, then expand.

---

### OAuth2 / OIDC Flow Selection Guide

**When to use**: When designing authentication and authorization for applications, APIs, or service-to-service communication.

**Flow Selection Decision Tree**:

| Client Type | User Involved? | Recommended Flow |
|-------------|---------------|-----------------|
| Web app (server-rendered) | Yes | Authorization Code |
| SPA (single-page app) | Yes | Authorization Code + PKCE |
| Mobile app | Yes | Authorization Code + PKCE |
| Server-to-server | No | Client Credentials |
| CLI tool | Yes | Device Code |
| Highly trusted first-party app | Yes | Authorization Code (never Resource Owner Password) |

**Token Lifecycle Template**:
```
Access Token:
  - Type: JWT (signed, not encrypted unless containing PII)
  - Lifetime: 15-60 minutes
  - Storage: Memory (SPA), HttpOnly cookie (web), Keychain (mobile)
  - Revocation: Check token introspection endpoint for sensitive operations

Refresh Token:
  - Lifetime: 7-30 days
  - Storage: HttpOnly Secure cookie (web), Keychain (mobile), NEVER localStorage
  - Rotation: Issue new refresh token on each use (detect reuse = compromise)
  - Revocation: Server-side revocation list

ID Token:
  - Purpose: Authentication only (never for authorization)
  - Lifetime: Same as access token
  - Validation: Verify signature, issuer, audience, expiration
```

**Limitations**: OAuth2 is an authorization framework, not an authentication protocol. OIDC adds authentication on top. Do not use access tokens for authentication. Do not implement custom flows — use a proven library or identity provider.

---

### JWT vs. Session Decision Framework

**When to use**: When choosing between stateless tokens (JWT) and server-side sessions for managing authenticated state.

**Decision Matrix**:

| Factor | Favors JWT | Favors Sessions |
|--------|-----------|-----------------|
| Architecture | Distributed, microservices | Monolith, single-server |
| Revocation needs | Rare, can tolerate delay | Immediate revocation required |
| Token size | Small claims, few attributes | Large user context needed |
| Scaling | Stateless scaling preferred | Session store acceptable |
| Security sensitivity | Standard | High (financial, healthcare) |

**Hybrid Approach** (recommended for most systems):
- Use JWTs for API authentication (stateless, verifiable)
- Keep JWTs short-lived (15 minutes)
- Use refresh tokens (server-side, revocable) for token renewal
- For high-security operations, verify against server-side session/revocation list

**Limitations**: JWTs cannot be revoked before expiration without a server-side revocation list, which partially negates their stateless benefit. If you need instant revocation, either use very short-lived JWTs or server-side sessions.

---

### RBAC vs. ABAC Comparison

**When to use**: When designing the authorization model for your application.

| Aspect | RBAC (Role-Based) | ABAC (Attribute-Based) |
|--------|-------------------|----------------------|
| **Model** | Users have roles; roles have permissions | Policies evaluate attributes of user, resource, action, and context |
| **Complexity** | Simple to implement and understand | Complex but flexible |
| **Best for** | Static permission structures, small-medium apps | Dynamic, context-dependent access, multi-tenant |
| **Example** | "Editors can edit articles" | "Users can edit articles they authored in their department during business hours" |
| **Scaling** | Role explosion in complex systems | Handles complex rules without role proliferation |

**RBAC Template**:
```
Roles:
  admin: [all permissions]
  editor: [create, read, update articles]
  viewer: [read articles]

Assignment:
  User → Role → Permissions

Enforcement:
  if (user.hasPermission("articles:update")) { allow }
```

**ABAC Template**:
```
Policy: Allow Article Edit
  Subject: user.department == resource.department
  Action: "edit"
  Resource: resource.type == "article"
  Context: time.hour >= 9 AND time.hour <= 17

Evaluation: AND(all conditions) → allow/deny
```

**Recommendation**: Start with RBAC. Migrate to ABAC when role explosion becomes unmanageable or when authorization requires contextual attributes.

**Limitations**: ABAC policies can become difficult to audit and debug. Maintain a policy registry with clear documentation and test cases for each policy.

---

### Encryption Patterns

**When to use**: Whenever data is stored (at rest) or transmitted (in transit).

**At Rest**:

| Approach | Use When | Implementation |
|----------|----------|---------------|
| Database-level (TDE) | Default for managed databases | Enable TDE on RDS/Cloud SQL; provider manages keys |
| Application-level | PII or regulated data requiring field-level encryption | Encrypt specific fields before storage; manage keys in vault |
| Filesystem-level | Storage volumes, backups | Encrypted EBS/persistent disks; provider manages keys |

**In Transit**:

| Approach | Use When | Implementation |
|----------|----------|---------------|
| TLS 1.2+ | All external communication | Enforce in load balancers, API gateways; HSTS headers |
| mTLS | Service-to-service within service mesh | Both sides present certificates; managed via service mesh (Istio, Linkerd) |
| End-to-end encryption | Sensitive data through intermediaries | Client encrypts, only intended recipient decrypts |

**Key Management Template**:
```
Key Hierarchy:
  Root Key (HSM-protected) → Data Encryption Key (DEK) → Encrypted Data

Rotation Policy:
  - Root keys: Annual rotation, HSM-backed
  - DEKs: Rotate with each key usage or on schedule (90 days)
  - API keys: Rotate on suspected compromise, minimum quarterly

Storage:
  - Never in source code
  - Use cloud KMS or HashiCorp Vault
  - Access logged and auditable
```

**Limitations**: Encryption protects data at rest and in transit but not data in use (while being processed in memory). For extremely sensitive workloads, consider confidential computing (TEEs).

---

### Compliance Framework Overview

**When to use**: When the product handles customer data, financial information, or operates in regulated industries.

| Framework | Focus | Key Requirements | Common Industries |
|-----------|-------|-----------------|-------------------|
| **SOC 2** | Trust service criteria (security, availability, confidentiality) | Access control, encryption, monitoring, incident response, vendor management | SaaS, B2B technology |
| **ISO 27001** | Information security management system (ISMS) | Risk assessment, security policy, asset management, access control, cryptography | Enterprise, global operations |
| **GDPR** | Personal data protection for EU residents | Lawful basis for processing, data minimization, right to erasure, breach notification (72 hrs), DPO | Any product with EU users |
| **SOC 2 Type II** | SOC 2 with operational effectiveness over time | All SOC 2 controls + evidence of consistent operation over 6-12 months | Enterprise SaaS |
| **HIPAA** | Protected health information (PHI) | Access controls, audit logs, encryption, BAAs with vendors, breach notification | Healthcare, health tech |
| **PCI DSS** | Payment card data | Network segmentation, encryption, access control, vulnerability scanning | E-commerce, payment processing |

**Compliance-to-Architecture Mapping Template**:
```markdown
## Compliance Control Mapping: [Framework]

| Control ID | Requirement | Architecture Control | Evidence |
|-----------|-------------|---------------------|----------|
| CC6.1 | Logical access controls | RBAC + MFA via [identity provider] | IAM policy configs, MFA enrollment reports |
| CC6.7 | Encryption in transit | TLS 1.2+ enforced at load balancer | TLS configuration, HSTS headers |
| CC7.2 | Monitoring and alerting | Centralized logging via [tool] | Alert configurations, incident response logs |
```

**Limitations**: Compliance frameworks define minimum requirements, not optimal security. A system can be compliant and still insecure. Use compliance as a baseline and layer additional security based on your threat model.

---

## Security Architecture Checklist

Quick reference for security review of any system design:

- [ ] **Authentication**: MFA for users, mTLS or JWT for services, no shared credentials
- [ ] **Authorization**: Deny-by-default, least privilege, per-request validation
- [ ] **Encryption**: TLS in transit, AES-256 at rest for sensitive data, key rotation policy
- [ ] **Input validation**: Server-side validation on all inputs, parameterized queries
- [ ] **Logging**: Auth events, access control failures, data access logged, tamper-resistant
- [ ] **Secrets**: Managed in vault/KMS, rotated, never in code
- [ ] **Dependencies**: Automated scanning, patching SLA defined
- [ ] **Incident response**: Detection mechanisms, containment plan, communication plan
- [ ] **Data classification**: All data classified, controls match classification level
- [ ] **Compliance**: Applicable frameworks identified, control mapping documented

---

## Operating Principle

> "Security is a property of the architecture, not a feature of the application. A secure system makes the right thing easy and the wrong thing hard. If your security controls require heroic effort to maintain, they will eventually be bypassed."


## Common Pitfalls

- Security recommendations should be conservative — when in doubt, add the control
- Authentication and authorization are different concerns — don't conflate them
- Never hardcode secrets, even in examples — use placeholder syntax
