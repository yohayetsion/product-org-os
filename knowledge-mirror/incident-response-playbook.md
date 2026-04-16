# Incident Response Playbook Knowledge Pack

**Version**: 1.0
**Primary Users**: @it-security-policy, @cio, @security-architect, @risk-manager, @compliance-officer
**Domain**: Incident Response & Crisis Management

---
<!-- Attribution:
  Frameworks and patterns in this knowledge pack were informed by:
  - securitytemplates/sectemplates (github.com/securitytemplates/sectemplates) — incident response templates
  - NIST SP 800-61 (Computer Security Incident Handling Guide) — incident response lifecycle and procedures
  Adapted and expanded for Product Org OS agents.
-->

## NIST SP 800-61 Incident Response Lifecycle

### Phase Overview

| Phase | Purpose | Key Activities | Exit Criteria |
|-------|---------|----------------|---------------|
| **1. Preparation** | Build IR capability before incidents occur | Policy, team, tools, training, playbooks | IR plan approved, team trained, tools deployed |
| **2. Detection & Analysis** | Identify and validate security events | Monitoring, triage, classification, scoping | Incident confirmed, severity assigned, commander designated |
| **3. Containment** | Limit blast radius and prevent spread | Short-term containment, evidence preservation, long-term containment | Threat isolated, no further spread confirmed |
| **4. Eradication** | Remove threat from environment | Root cause removal, vulnerability patching, hardening | All threat artifacts removed, vulnerabilities remediated |
| **5. Recovery** | Restore systems to normal operations | System restoration, validation, monitoring | Systems operational, no reinfection, monitoring heightened |
| **6. Post-Incident** | Learn and improve from the incident | Blameless postmortem, process updates, metrics | Lessons documented, action items assigned, playbooks updated |

### Phase 1: Preparation

**Objective**: Establish and maintain IR capability so the organization can respond effectively.

**Preparation Checklist**:
- [ ] IR policy and plan approved by executive leadership
- [ ] CSIRT team formed with defined roles and contact information
- [ ] Incident classification and severity matrix documented
- [ ] Communication templates prepared (internal, customer, regulator, media)
- [ ] Forensic toolkit deployed (disk imaging, memory capture, network capture)
- [ ] Incident tracking system configured (ticketing, evidence repository)
- [ ] Escalation paths documented and tested
- [ ] Tabletop exercises conducted (quarterly minimum)
- [ ] Mutual aid agreements with external IR firms established
- [ ] Cyber insurance policy reviewed and current
- [ ] Legal counsel briefed on notification obligations
- [ ] War room (physical and virtual) identified and equipped
- [ ] Out-of-band communication channels established (non-corporate email, phone bridge)
- [ ] Asset inventory and network diagrams current
- [ ] Log aggregation and SIEM configured with alerting rules

### Phase 2: Detection & Analysis

**Detection Sources**:

| Source | Examples | Typical Alert Types |
|--------|----------|---------------------|
| SIEM/Log Analysis | Splunk, Elastic, Sentinel | Correlation rules, anomaly detection |
| EDR/XDR | CrowdStrike, SentinelOne, Defender | Malware, suspicious process, lateral movement |
| Network Monitoring | IDS/IPS, NDR, NetFlow | C2 traffic, exfiltration, scanning |
| Email Security | Proofpoint, Mimecast | Phishing, BEC, malicious attachments |
| Cloud Security | CSPM, CASB | Misconfigurations, anomalous API calls |
| User Reports | Helpdesk, phishing button | Suspicious emails, unusual system behavior |
| Threat Intelligence | ISAC feeds, vendor advisories | IOCs matching environment |
| Vulnerability Scanners | Qualys, Tenable | Exploited CVEs, critical exposures |

**Analysis Framework**:
1. **Validate**: Confirm the alert is a true positive (not a false alarm or test)
2. **Scope**: Determine affected systems, accounts, data, and business processes
3. **Attribute**: Identify threat actor type (external, insider, automated, targeted)
4. **Classify**: Assign incident type and severity level
5. **Document**: Begin incident timeline and evidence log
6. **Notify**: Engage incident commander and required stakeholders

### Phase 3: Containment

**Short-Term Containment** (minutes to hours):
- Isolate affected systems from the network (do NOT power off if forensics needed)
- Disable compromised accounts
- Block known malicious IPs, domains, and hashes
- Redirect DNS for compromised domains
- Enable enhanced logging on adjacent systems

**Evidence Preservation** (concurrent with containment):
- Capture volatile data (memory, running processes, network connections) before any changes
- Create forensic disk images of affected systems
- Preserve relevant logs (firewall, proxy, authentication, application)
- Document all containment actions with timestamps

**Long-Term Containment** (hours to days):
- Rebuild compromised systems from known-good images
- Apply emergency patches to exploited vulnerabilities
- Implement additional network segmentation
- Deploy enhanced monitoring on related systems
- Rotate credentials for affected and potentially affected accounts

### Phase 4: Eradication

**Eradication Checklist**:
- [ ] Root cause identified and documented
- [ ] All malware, backdoors, and persistence mechanisms removed
- [ ] Exploited vulnerabilities patched or mitigated
- [ ] Compromised credentials rotated across all systems
- [ ] Attacker-created accounts and access removed
- [ ] Affected systems reimaged or rebuilt (preferred over cleaning)
- [ ] IOCs shared with detection systems (SIEM rules, EDR policies)
- [ ] Threat hunting conducted for related activity across the environment

### Phase 5: Recovery

**Recovery Sequence**:
1. Restore systems from clean backups or rebuild from known-good images
2. Validate system integrity before reconnecting to the network
3. Implement additional security controls identified during analysis
4. Monitor restored systems closely for signs of reinfection (30-day heightened monitoring)
5. Gradually restore services in order of business criticality
6. Confirm business process functionality with system owners
7. Communicate restoration status to stakeholders

**Recovery Validation**:
- [ ] Systems pass integrity checks (file hashes, configuration baselines)
- [ ] No indicators of compromise detected on restored systems
- [ ] Security controls functioning as expected
- [ ] Business processes operating normally
- [ ] Enhanced monitoring in place for minimum 30 days

### Phase 6: Post-Incident Activity

See **Blameless Postmortem Template** section below.

---

## Incident Classification & Severity Levels

### Incident Type Taxonomy

| Type | Description | Examples |
|------|-------------|----------|
| **Malware** | Malicious software infection | Ransomware, trojan, worm, cryptominer |
| **Unauthorized Access** | Illegitimate system or data access | Compromised credentials, privilege escalation |
| **Data Breach** | Confirmed unauthorized data exposure | Exfiltration, accidental disclosure, lost device |
| **Denial of Service** | Availability disruption | DDoS, application-layer attack, resource exhaustion |
| **Insider Threat** | Threat from authorized users | Data theft, sabotage, policy violation |
| **Phishing/Social Engineering** | Human manipulation attack | Spear phishing, BEC, vishing, pretexting |
| **Supply Chain** | Compromise via third-party | Vendor breach, compromised software update, dependency attack |
| **Web Application** | Attack on web-facing systems | SQLi, XSS, API abuse, account takeover |
| **Physical** | Physical security incident | Unauthorized facility access, device theft, tailgating |

### Severity Matrix

| Severity | Definition | Response Time | Update Frequency | Escalation | Examples |
|----------|------------|---------------|------------------|------------|----------|
| **P0 - Critical** | Active, widespread impact on critical systems or confirmed large-scale data breach; existential business risk | **15 minutes** to assemble IR team | Every **30 minutes** to executive leadership | Immediate to CISO, CEO, General Counsel, Board (if public company) | Active ransomware spreading across network; confirmed breach of regulated customer data; critical infrastructure compromised |
| **P1 - High** | Confirmed incident with significant impact on business operations or sensitive data at risk; contained but not resolved | **30 minutes** to begin response | Every **2 hours** to CISO and affected business units | Within 1 hour to CISO; within 4 hours to executive team | Single system compromised with lateral movement potential; targeted attack on executive accounts; sensitive data exposure (limited scope) |
| **P2 - Medium** | Confirmed incident with limited impact; no sensitive data confirmed exposed; contained to isolated systems | **4 hours** to begin response | **Daily** to security management | Within 24 hours to security management | Malware on isolated endpoint (no spread); successful phishing with credential compromise (single user, no sensitive access); minor policy violation |
| **P3 - Low** | Potential incident requiring investigation; no confirmed compromise or impact | **Next business day** to begin investigation | **Weekly** or upon status change | As needed to security team lead | Suspicious but unconfirmed activity; failed attack attempts; minor vulnerability requiring monitoring |
| **P4 - Informational** | Security event for awareness; no action required beyond logging | **No active response** required | Included in monthly security report | None | Blocked attack attempts; security tool alerts (false positives); general threat intelligence |

### Severity Escalation Triggers

An incident severity MUST be escalated when any of the following occur:

| Current | Escalate To | Trigger |
|---------|-------------|---------|
| P3 | P2 | Investigation confirms actual compromise |
| P2 | P1 | Evidence of lateral movement, sensitive data access, or additional systems affected |
| P1 | P0 | Widespread propagation, confirmed data exfiltration, public exposure, or regulatory notification required |
| Any | P0 | Media inquiry about a security incident, law enforcement contact, or regulatory inquiry |

---

## Incident Commander Role & Responsibilities

### Incident Commander (IC) Definition

The Incident Commander is the single point of authority during an active incident. The IC owns the response, delegates tasks, makes containment decisions, and controls communications. There is always exactly ONE Incident Commander at any time.

### IC Responsibilities

| Area | Responsibilities |
|------|------------------|
| **Authority** | Final decision-maker for all response actions during the incident |
| **Coordination** | Direct and coordinate all IR team activities; assign tasks with clear ownership and deadlines |
| **Communication** | Own all external communications (approve messages to customers, regulators, media); provide regular internal status updates |
| **Escalation** | Decide when to escalate severity, engage external resources (IR firm, law enforcement, legal counsel) |
| **Documentation** | Ensure incident timeline is maintained; all decisions and actions are logged with rationale |
| **Scope Control** | Define incident scope; prevent scope creep; manage parallel workstreams |
| **Transition** | Execute formal handoff when transferring IC role (shift changes); never leave IC role vacant |
| **Post-Incident** | Initiate and lead the blameless postmortem process |

### IC Selection Matrix

| Severity | Default IC | Backup IC |
|----------|-----------|-----------|
| P0 | CISO or VP Security | Director of Security Operations |
| P1 | Director of Security Operations | Senior Security Engineer (on-call) |
| P2 | Security Operations Manager | Senior Security Analyst (on-call) |
| P3 | Security Analyst (on-call) | SOC Team Lead |

### IC Handoff Protocol

1. Outgoing IC briefs incoming IC on: current status, active workstreams, pending decisions, open questions
2. Incoming IC confirms understanding and formally accepts command
3. Announcement sent to all IR channels: "IC transition: [Outgoing] -> [Incoming] effective [timestamp]"
4. Outgoing IC remains available for 30 minutes for follow-up questions

---

## Communication Templates

### Template 1: Internal Executive Notification (P0/P1)

```
SUBJECT: [SEVERITY] Security Incident - [SHORT DESCRIPTION] - [INCIDENT ID]

STATUS: [Active / Contained / Resolved]
SEVERITY: [P0 / P1]
INCIDENT COMMANDER: [Name, Contact]
TIME DETECTED: [YYYY-MM-DD HH:MM UTC]

SITUATION:
[2-3 sentence description of what happened, what is affected, and current status]

IMPACT:
- Systems affected: [list]
- Data at risk: [type and estimated scope]
- Business processes impacted: [list]
- Customer impact: [none / potential / confirmed]

CURRENT ACTIONS:
1. [Action being taken]
2. [Action being taken]

NEXT UPDATE: [Time]
WAR ROOM: [Location / Bridge link]

PLEASE DO NOT share this information outside the executive team until
communications are coordinated through the Incident Commander.
```

### Template 2: Customer Notification (Data Breach)

```
SUBJECT: Important Security Notice from [Company Name]

Dear [Customer Name],

We are writing to inform you of a security incident that may have
affected your information.

WHAT HAPPENED:
[Clear, factual description of the incident without technical jargon.
Include dates of the incident and date of discovery.]

WHAT INFORMATION WAS INVOLVED:
[Specific data types affected. Be precise: names, emails, payment info, etc.
State clearly what was NOT affected.]

WHAT WE ARE DOING:
[Actions taken to contain and remediate. Steps to prevent recurrence.
Any free services being offered (credit monitoring, etc.).]

WHAT YOU CAN DO:
[Specific, actionable steps the customer can take. Password changes,
monitoring recommendations, etc.]

FOR MORE INFORMATION:
[Dedicated support channel: phone number, email, FAQ page URL.
Hours of availability.]

We take the security of your information seriously and sincerely
apologize for this incident.

[Signature]
```

### Template 3: Regulatory Notification (GDPR Article 33)

```
SUBJECT: Data Breach Notification - [Company Name] - [Incident ID]

To: [Supervisory Authority]

1. NATURE OF THE BREACH
   - Description: [What happened]
   - Categories of data subjects: [e.g., customers, employees]
   - Approximate number of data subjects: [count or estimate]
   - Categories of personal data: [e.g., names, emails, financial]
   - Approximate number of records: [count or estimate]

2. DATA PROTECTION OFFICER CONTACT
   - Name: [DPO Name]
   - Email: [DPO Email]
   - Phone: [DPO Phone]

3. LIKELY CONSEQUENCES
   [Assessment of potential impact on data subjects]

4. MEASURES TAKEN OR PROPOSED
   - Containment measures: [list]
   - Remediation measures: [list]
   - Measures to mitigate adverse effects on data subjects: [list]

5. TIMELINE
   - Date/time of breach: [if known]
   - Date/time of discovery: [date]
   - Date/time of this notification: [date]
   - Reason for delay (if >72 hours): [explanation]

6. ADDITIONAL INFORMATION
   [Any supplementary details]
```

### Template 4: Media Holding Statement

```
[Company Name] is aware of a security incident affecting [general scope].

We take the security of [customer/user/employee] data extremely seriously.
Upon discovery, we immediately activated our incident response procedures
and engaged [external cybersecurity firm] to assist with our investigation.

[If applicable: We have notified relevant law enforcement authorities and
are cooperating fully with their investigation.]

We are in the process of notifying affected [customers/users/individuals]
directly and providing them with [resources/support].

We will provide updates as our investigation progresses. For questions,
please contact [dedicated contact].
```

### Template 5: All-Hands Employee Communication

```
SUBJECT: Security Incident Update - Action Required

Team,

We want to make you aware of a security incident and share what we
know, what we are doing, and what we need from you.

WHAT WE KNOW:
[Brief, honest description appropriate for all employees]

WHAT WE ARE DOING:
[Response actions in plain language]

WHAT WE NEED FROM YOU:
1. [Specific action items for employees, e.g., password reset]
2. Do NOT discuss this incident on social media or with external parties
3. Direct all media inquiries to [communications team contact]
4. Report anything suspicious to [security team contact]

If you have questions, please reach out to [contact]. We will provide
another update by [time/date].

[Leadership signature]
```

---

## Runbook Templates

### Runbook: Data Breach

**Trigger**: Confirmed unauthorized access to or exfiltration of sensitive/regulated data.

**Immediate Actions (0-1 hour)**:
1. Activate P0/P1 incident response; designate Incident Commander
2. Identify the data types exposed (PII, PHI, financial, credentials, IP)
3. Determine scope: number of records, number of affected individuals, geographies
4. Preserve evidence: capture logs, memory dumps, network captures
5. Engage legal counsel immediately (attorney-client privilege for investigation)

**Containment (1-24 hours)**:
6. Revoke access for compromised accounts/systems
7. Block exfiltration channels identified in analysis
8. Isolate affected databases and storage systems
9. Deploy enhanced monitoring on data egress points
10. Determine if breach is ongoing or historical

**Investigation (24-72 hours)**:
11. Identify attack vector and timeline of unauthorized access
12. Determine exactly what data was accessed vs. exfiltrated
13. Identify all affected individuals by jurisdiction
14. Assess whether data was encrypted at rest/in transit
15. Engage external forensics firm if scope warrants

**Notification (per regulatory requirements)**:
16. Notify supervisory authority within 72 hours (GDPR Article 33)
17. Notify affected individuals "without unreasonable delay" (GDPR Article 34)
18. File state breach notifications per applicable laws (see Legal Requirements section)
19. Notify credit bureaus if >5,000 individuals affected (some US states)
20. Consider voluntary law enforcement notification

**Recovery**:
21. Remediate the vulnerability or access path exploited
22. Rotate all credentials that may have been exposed
23. Implement additional data loss prevention controls
24. Offer identity protection/credit monitoring to affected individuals
25. Update data handling procedures based on lessons learned

---

### Runbook: Ransomware

**Trigger**: Ransomware detected on one or more systems; files encrypted or ransom note displayed.

**Immediate Actions (0-30 minutes)**:
1. **DO NOT** pay the ransom without executive and legal approval
2. **DO NOT** power off encrypted systems (preserve memory for decryption keys)
3. Activate P0 incident response; designate Incident Commander
4. Disconnect affected systems from the network (pull cable, disable Wi-Fi)
5. Identify the ransomware variant (ransom note, file extensions, IOCs)
6. Check No More Ransom (nomoreransom.org) for available decryptors

**Containment (30 minutes - 4 hours)**:
7. Isolate network segments with confirmed infections
8. Disable shared drives and network shares
9. Block C2 domains/IPs at firewall and DNS
10. Disable Remote Desktop Protocol (RDP) if externally exposed
11. Preserve a sample of encrypted files and the ransomware binary
12. Identify patient zero and initial infection vector

**Assessment (4-24 hours)**:
13. Map the full blast radius: all encrypted systems and shares
14. Determine if data was exfiltrated before encryption (double extortion)
15. Assess backup integrity: are backups available, unencrypted, and recent?
16. Evaluate business impact: which critical processes are disrupted?
17. Engage cyber insurance carrier and external IR firm

**Recovery Decision Tree**:
- Backups available and clean? -> Restore from backups
- Decryptor available? -> Test on non-critical system first, then decrypt
- Neither available? -> Evaluate ransom payment (legal, ethical, practical considerations with counsel)

**Recovery (days to weeks)**:
18. Rebuild affected systems from clean images
19. Restore data from verified-clean backups
20. Patch the vulnerability used for initial access
21. Implement network segmentation to limit future spread
22. Deploy EDR on all endpoints if not already present
23. Conduct organization-wide credential reset
24. Enhance email security and user awareness training

---

### Runbook: DDoS Attack

**Trigger**: Service degradation or outage caused by volumetric, protocol, or application-layer attack.

**Immediate Actions (0-15 minutes)**:
1. Activate P1/P2 incident response (P0 if revenue-critical services affected)
2. Confirm DDoS vs. legitimate traffic spike or infrastructure failure
3. Engage DDoS mitigation provider (Cloudflare, Akamai, AWS Shield)
4. Activate rate limiting and geo-blocking for attack traffic sources
5. Notify NOC/infrastructure team and affected service owners

**Mitigation (15 minutes - 2 hours)**:
6. Enable DDoS scrubbing service and reroute traffic through scrubbing center
7. Implement application-layer protections (WAF rules, CAPTCHA challenges)
8. Scale infrastructure horizontally if cloud-based
9. Block attacking IP ranges at network edge (temporary; attackers rotate)
10. Enable traffic analysis to identify attack patterns and vectors

**Monitoring & Communication**:
11. Monitor mitigation effectiveness continuously
12. Update status page for affected services
13. Communicate with customers if SLA impact expected
14. Coordinate with ISP if attack exceeds mitigation capacity

**Recovery**:
15. Gradually relax emergency traffic restrictions
16. Analyze attack patterns for permanent defense improvements
17. Update DDoS response plan with lessons learned
18. Review and optimize auto-scaling and rate limiting configurations
19. Consider always-on DDoS protection for critical services

---

### Runbook: Insider Threat

**Trigger**: Suspected or confirmed malicious or negligent actions by an authorized user (employee, contractor, partner).

**Immediate Actions (0-2 hours)**:
1. Activate incident response with need-to-know restriction (limited team)
2. **DO NOT** alert the suspected individual
3. Engage HR and legal counsel immediately
4. Preserve all evidence of the individual's activities (access logs, email, file access, badge access)
5. Determine if threat is malicious (intentional) or negligent (accidental)

**Investigation (privileged and confidential)**:
6. Review DLP alerts, UEBA anomalies, and access logs for the individual
7. Analyze data access patterns: what data was accessed, downloaded, or transferred?
8. Review email and messaging for data exfiltration channels (personal email, cloud storage, USB)
9. Check for privilege escalation or unauthorized access attempts
10. Review HR records for potential motivation (resignation notice, performance issues, grievances)
11. Document findings with timestamps and evidence chain of custody

**Containment (coordinated with HR and Legal)**:
12. If active threat: disable access immediately with HR/Legal approval
13. If monitoring warranted: implement enhanced surveillance with legal authorization
14. Revoke access to sensitive systems and data
15. Change shared credentials the individual had access to
16. Preserve the individual's devices for forensic analysis

**Resolution**:
17. Follow HR termination or disciplinary procedures if warranted
18. Conduct exit interview (if applicable) with legal counsel present
19. File law enforcement report if criminal activity confirmed
20. Review and tighten access controls based on the exploitation path
21. Update insider threat indicators in monitoring systems

---

### Runbook: Phishing Compromise

**Trigger**: User has clicked a phishing link, submitted credentials, or opened a malicious attachment.

**Immediate Actions (0-30 minutes)**:
1. Activate P2/P3 incident response (escalate to P1 if executive or privileged account)
2. Reset the compromised user's password immediately
3. Revoke all active sessions and OAuth tokens for the account
4. Enable MFA if not already in place
5. Quarantine the phishing email across all mailboxes (clawback)

**Assessment (30 minutes - 4 hours)**:
6. Determine what the user interacted with (link click, credential submission, attachment execution)
7. Check for email forwarding rules or delegated access added to the account
8. Review the user's sent items for BEC/lateral phishing to other employees or contacts
9. Check if the user has access to sensitive systems or data
10. Scan the user's endpoint for malware if attachment was opened
11. Search for the phishing campaign across all users (subject line, sender, URLs, attachment hashes)

**Containment**:
12. Block the phishing sender, domain, and URLs at email gateway and proxy
13. Submit phishing indicators to threat intelligence feeds
14. If credentials were harvested: check for reuse on other systems
15. If malware was deployed: follow the Malware runbook
16. If BEC emails were sent: notify recipients immediately

**Recovery**:
17. Restore any modified mailbox configurations (rules, forwarding, delegates)
18. Re-credential the user with verified secure methods
19. Provide targeted security awareness reinforcement to the affected user
20. Send phishing alert to organization with indicators (sanitized)
21. Update email security rules based on the attack pattern

---

### Runbook: Service Outage (Non-Attack)

**Trigger**: Critical service or system unavailable due to infrastructure failure, misconfiguration, or software defect.

**Immediate Actions (0-15 minutes)**:
1. Activate P1/P2 incident response based on business impact
2. Confirm outage scope: which services, which users, which regions
3. Check for known maintenance windows or recent changes (change management log)
4. Engage on-call engineering for the affected service
5. Update internal status page

**Diagnosis (15 minutes - 2 hours)**:
6. Review recent deployments and configuration changes (most common root cause)
7. Check infrastructure health: compute, storage, network, DNS, CDN
8. Review application logs and error rates
9. Check third-party dependency status (cloud provider status pages, SaaS dependencies)
10. If recent deployment: evaluate rollback vs. forward-fix

**Resolution**:
11. Implement fix or rollback
12. Validate service restoration with synthetic monitoring and user confirmation
13. Clear any queued or failed transactions
14. Update external status page and notify affected customers
15. Schedule postmortem within 48 hours

---

### Runbook: Supply Chain Compromise

**Trigger**: Confirmed or suspected compromise of a vendor, supplier, open-source dependency, or third-party integration.

**Immediate Actions (0-2 hours)**:
1. Activate P0/P1 incident response (supply chain attacks are high-severity by default)
2. Identify the compromised component: vendor, library, service, or update
3. Determine exposure: which systems use the compromised component?
4. Check advisory sources: vendor security notices, CVE databases, CISA alerts, ISAC feeds

**Containment (2-24 hours)**:
5. Disable or isolate the compromised integration/service
6. Block network communication to compromised vendor infrastructure
7. Pin software dependencies to known-good versions; do not auto-update
8. Revoke API keys, tokens, and credentials shared with the compromised vendor
9. Assess whether the compromise provided access to your environment or data

**Investigation (24-72 hours)**:
10. Conduct threat hunting for IOCs associated with the supply chain attack
11. Review logs for anomalous activity from the compromised component
12. Determine if any data was exposed to or through the compromised vendor
13. Assess downstream impact: did you inadvertently pass the compromise to YOUR customers?
14. Engage the vendor's security team for information sharing

**Recovery**:
15. Apply vendor-provided patches or migrate to an alternative
16. Rebuild affected systems if compromise is confirmed in your environment
17. Update vendor risk assessment and third-party risk management program
18. Review and tighten software supply chain controls (SBOMs, dependency scanning, code signing)
19. Reassess vendor relationship and contractual security requirements

---

## Evidence Collection & Chain of Custody

### Order of Volatility

Collect evidence in order of volatility (most volatile first):

| Priority | Evidence Type | Volatility | Collection Method |
|----------|--------------|------------|-------------------|
| 1 | CPU registers, cache | Seconds | Live forensics tools |
| 2 | Memory (RAM) | Seconds-minutes | Memory dump (WinPmem, LiME, FTK Imager) |
| 3 | Network connections | Seconds-minutes | `netstat`, packet capture |
| 4 | Running processes | Minutes | `tasklist`, `ps`, process memory dumps |
| 5 | Disk (temporary files, swap) | Minutes-hours | Forensic imaging (dd, FTK Imager) |
| 6 | Disk (file system) | Hours-days | Forensic imaging |
| 7 | Remote logs (SIEM, cloud) | Days-months | Export/archive from logging platform |
| 8 | Physical media, backups | Months-years | Secure physical collection |

### Chain of Custody Record

Every piece of evidence MUST have a chain of custody record:

```
EVIDENCE CHAIN OF CUSTODY RECORD

Evidence ID: [EVD-YYYY-NNNN]
Incident ID: [INC-YYYY-NNNN]
Description: [What the evidence is]

COLLECTION:
  Collected by: [Name, Title]
  Date/Time: [YYYY-MM-DD HH:MM UTC]
  Location: [Physical/logical location]
  Method: [Tool and procedure used]
  Hash (SHA-256): [hash value at time of collection]

TRANSFER LOG:
| Date/Time | Released By | Received By | Purpose | Location |
|-----------|------------|-------------|---------|----------|
| | | | | |

STORAGE:
  Location: [Secure storage location]
  Access controls: [Who can access]
  Encryption: [Yes/No, method]

INTEGRITY VERIFICATION:
| Date | Verified By | Hash Match | Notes |
|------|------------|------------|-------|
| | | | |
```

### Evidence Collection Guidelines

- **Never** work on original evidence; always create forensic copies
- **Never** boot a compromised system from its own OS for analysis
- Use write-blockers when imaging storage media
- Document every action taken on or near evidence systems
- Photograph physical evidence (screens, connections, labels) before collection
- Store evidence in a locked, access-controlled location
- Maintain evidence for the legally required retention period (consult legal counsel)
- Two-person integrity: evidence handling should be witnessed when possible

---

## Forensic Analysis Procedures

### Memory Forensics

1. Capture memory dump using validated tool (WinPmem, LiME, Magnet RAM Capture)
2. Compute hash of memory dump file
3. Analyze with Volatility or Rekall:
   - Process list and process tree (hidden/injected processes)
   - Network connections (established, listening)
   - Loaded DLLs and kernel modules
   - Command history and clipboard contents
   - Registry hives (Windows)
   - Malware signatures and YARA rule scanning

### Disk Forensics

1. Create forensic image using dd, FTK Imager, or EnCase
2. Verify image integrity (hash comparison)
3. Mount image read-only for analysis
4. Key analysis areas:
   - File system timeline (creation, modification, access times)
   - Deleted file recovery
   - Browser history, downloads, and cache
   - Email artifacts
   - Registry analysis (Windows: autoruns, USB history, user activity)
   - Log file analysis (event logs, application logs)
   - Prefetch/Superfetch analysis (execution artifacts)
   - Alternate data streams (Windows NTFS)

### Network Forensics

1. Capture network traffic (tcpdump, Wireshark, network TAP)
2. Analyze packet captures for:
   - C2 communication patterns (beaconing intervals, DNS tunneling)
   - Data exfiltration (large outbound transfers, unusual protocols)
   - Lateral movement (SMB, RDP, WMI, PowerShell remoting)
   - Credential harvesting (cleartext protocols, pass-the-hash)
3. Correlate with firewall logs, proxy logs, and DNS query logs
4. Reconstruct sessions and extract transferred files

### Log Analysis

| Log Source | Key Indicators |
|------------|---------------|
| Windows Event Logs | 4624/4625 (logon), 4720 (account created), 4732 (group membership), 4688 (process creation), 1102 (log cleared) |
| Linux Auth Logs | SSH logins, sudo usage, account changes, cron modifications |
| Web Server Logs | Unusual request patterns, SQL injection attempts, path traversal, abnormal response sizes |
| Cloud Audit Logs | API calls, IAM changes, resource creation/deletion, data access |
| Application Logs | Authentication failures, privilege changes, data queries, error patterns |

---

## Blameless Postmortem Template

```
BLAMELESS POSTMORTEM

Incident ID: [INC-YYYY-NNNN]
Date of Incident: [YYYY-MM-DD]
Date of Postmortem: [YYYY-MM-DD]
Incident Commander: [Name]
Postmortem Lead: [Name]
Attendees: [List]

EXECUTIVE SUMMARY:
[2-3 sentence description of what happened and the business impact]

TIMELINE (UTC):
| Time | Event |
|------|-------|
| HH:MM | [First indicator / detection] |
| HH:MM | [Escalation / IC assigned] |
| HH:MM | [Key containment action] |
| HH:MM | [Resolution / recovery] |
| HH:MM | [Incident closed] |

IMPACT:
- Duration: [Total time from detection to resolution]
- Users/customers affected: [count or scope]
- Data impacted: [type and scope, or "none"]
- Revenue impact: [estimated or "not applicable"]
- SLA breaches: [list or "none"]

ROOT CAUSE:
[Description of the fundamental cause, not the proximate trigger.
Focus on systemic factors, not individual actions.]

CONTRIBUTING FACTORS:
1. [Factor that enabled or worsened the incident]
2. [Factor that delayed detection or response]
3. [Factor that complicated recovery]

WHAT WENT WELL:
- [Things that worked as designed]
- [Effective response actions]
- [Team collaboration highlights]

WHAT COULD BE IMPROVED:
- [Detection gaps]
- [Response process issues]
- [Communication challenges]
- [Tool or automation gaps]

ACTION ITEMS:
| ID | Action | Owner | Priority | Due Date | Status |
|----|--------|-------|----------|----------|--------|
| 1 | [Preventive action] | [Name] | P0/P1/P2 | [Date] | Open |
| 2 | [Detective improvement] | [Name] | P0/P1/P2 | [Date] | Open |
| 3 | [Process improvement] | [Name] | P0/P1/P2 | [Date] | Open |

LESSONS LEARNED:
1. [Key takeaway for the organization]
2. [Key takeaway for the organization]

BLAMELESS PRINCIPLE:
This postmortem focuses on systemic improvements, not individual blame.
People make the best decisions they can with the information available
at the time. Our goal is to improve the system.
```

---

## Incident Metrics

### Key Performance Indicators

| Metric | Definition | Target | Measurement |
|--------|-----------|--------|-------------|
| **MTTD** (Mean Time to Detect) | Time from incident occurrence to detection | P0: <1hr, P1: <4hrs, P2: <24hrs | Detection timestamp minus estimated start time |
| **MTTA** (Mean Time to Acknowledge) | Time from detection to IR team acknowledgment | P0: <15min, P1: <30min, P2: <4hrs | Acknowledgment timestamp minus detection timestamp |
| **MTTC** (Mean Time to Contain) | Time from acknowledgment to containment | P0: <4hrs, P1: <12hrs, P2: <48hrs | Containment timestamp minus acknowledgment timestamp |
| **MTTR** (Mean Time to Recover) | Time from detection to full recovery | P0: <24hrs, P1: <72hrs, P2: <1wk | Recovery timestamp minus detection timestamp |
| **Incident Frequency** | Number of incidents per time period by severity | Trending down quarter over quarter | Count per severity per month/quarter |
| **Escalation Rate** | Percentage of incidents escalated to higher severity | <20% of incidents | Escalated count / total incidents |
| **Postmortem Completion Rate** | Percentage of P0/P1 incidents with completed postmortems | 100% for P0/P1 | Postmortems completed / P0+P1 incidents |
| **Action Item Closure Rate** | Percentage of postmortem action items completed on time | >90% within 30 days | Closed on time / total action items |
| **False Positive Rate** | Percentage of alerts that are false positives | <30% | False positives / total alerts investigated |
| **Recurrence Rate** | Percentage of incidents with the same root cause recurring | <5% | Recurring root causes / total incidents |

### Metrics Dashboard Cadence

| Audience | Frequency | Metrics Included |
|----------|-----------|------------------|
| SOC/IR Team | Daily | Open incidents, MTTA, active alerts |
| Security Management | Weekly | MTTD, MTTR, incident count by type, false positive rate |
| CISO/Executive | Monthly | Trend analysis, recurrence rate, postmortem completion, action item closure |
| Board/Audit Committee | Quarterly | Year-over-year trends, material incidents, program maturity indicators |

---

## War Room Protocols

### War Room Activation

A war room is activated for all P0 incidents and P1 incidents lasting >4 hours.

### War Room Structure

| Role | Responsibility | Mandatory For |
|------|----------------|---------------|
| **Incident Commander** | Leads response, makes decisions, controls comms | P0, P1 |
| **Technical Lead** | Directs technical investigation and containment | P0, P1 |
| **Communications Lead** | Drafts and coordinates all stakeholder communications | P0 |
| **Scribe** | Maintains real-time incident timeline and decision log | P0, P1 |
| **Legal Representative** | Advises on notification obligations and privilege | P0 (data breach) |
| **Business Liaison** | Represents affected business units; communicates impact | P0 |
| **Executive Sponsor** | Authorizes extraordinary measures (system shutdowns, ransom decisions) | P0 |

### War Room Rules

1. **Single channel**: All incident communication flows through the designated war room channel (Slack/Teams + bridge line)
2. **Structured updates**: Every 30 minutes (P0) or 2 hours (P1), the IC provides a status update using the template: Status, Actions Taken, Actions Planned, Blockers, Next Update Time
3. **Decision log**: Every significant decision is logged with: timestamp, decision, rationale, decision-maker
4. **No side channels**: Do not discuss the incident in DMs, separate threads, or hallway conversations
5. **Need-to-know**: War room access is restricted to assigned roles; observers need IC approval
6. **Clear escalation**: If the IC needs executive authorization (shutdown, payment, disclosure), the request goes through the Executive Sponsor
7. **Shift management**: For incidents >8 hours, the IC must designate shifts and execute formal handoffs

### Out-of-Band Communication

If corporate systems are compromised, use pre-established out-of-band channels:

| Primary | Backup | Use Case |
|---------|--------|----------|
| Corporate Slack/Teams | Pre-configured Signal group | Real-time coordination |
| Corporate email | Personal email distribution list (pre-shared) | Notifications and documents |
| Corporate phone system | Personal mobile phone tree | Voice coordination |
| Corporate wiki | Pre-printed physical runbooks | Procedure reference |

---

## Legal & Regulatory Notification Requirements

### Notification Matrix

| Regulation | Scope | Notification Deadline | Notify To | Trigger |
|------------|-------|----------------------|-----------|---------|
| **GDPR (EU)** | EU data subjects | **72 hours** from awareness | Lead Supervisory Authority + data subjects (if high risk) | Personal data breach |
| **HIPAA (US)** | Protected health information | **60 days** from discovery (individuals); **60 days** after calendar year (HHS for <500); **immediately** for >500 | Affected individuals + HHS + media (if >500 in a state) | Breach of unsecured PHI |
| **CCPA/CPRA (California)** | California residents | "Most expedient time possible" without unreasonable delay | Affected individuals + CA Attorney General (if >500) | Breach of unencrypted personal information |
| **PCI DSS** | Payment card data | **Immediately** upon confirmation | Acquiring bank + card brands (Visa, Mastercard, etc.) | Compromise of cardholder data |
| **SOX** | Public company financial data | **Immediate** assessment of materiality | SEC (8-K filing within 4 business days if material), Board Audit Committee | Incident affecting financial reporting integrity |
| **NIS2 (EU)** | Essential/important entities | **24 hours** early warning; **72 hours** incident notification | National CSIRT/competent authority | Significant incident affecting service delivery |
| **DORA (EU)** | Financial entities | **4 hours** initial, **72 hours** intermediate | National competent authority | Major ICT-related incident |
| **US State Laws** | Varies by state (50 states + DC/territories) | Ranges from **30 days** to **90 days**; some "without unreasonable delay" | State AG and/or affected individuals | Breach of personal information (definitions vary) |
| **SEC Cyber Rules** | Public companies | **4 business days** (8-K) after determining materiality | SEC + investors (8-K filing) | Material cybersecurity incident |

### Notification Decision Tree

```
Incident confirmed as breach of personal/regulated data?
├── YES
│   ├── Determine jurisdictions (where do affected individuals reside?)
│   ├── Identify applicable regulations per jurisdiction
│   ├── Start shortest notification clock immediately
│   ├── Engage legal counsel for notification drafting
│   ├── Engage external forensics for scope determination
│   └── Begin notification preparation (even if scope not final)
└── NO
    ├── Document determination and rationale
    ├── Continue monitoring for scope expansion
    └── Reassess if new information emerges
```

### Key Legal Principles

- **Attorney-client privilege**: Engage outside counsel to direct the investigation; communications through counsel may be privileged
- **Litigation hold**: If breach may result in litigation, immediately preserve all relevant evidence and suspend routine data deletion
- **Insurance notification**: Notify cyber insurance carrier as early as possible; late notification can void coverage
- **Law enforcement**: Consider FBI/Secret Service notification for significant incidents; they can provide threat intelligence and sometimes assist with recovery
- **Regulatory cooperation**: Proactive, transparent engagement with regulators typically results in better outcomes than delayed or reluctant notification

---

## Tabletop Exercise Planning

### Exercise Types

| Type | Duration | Participants | Frequency | Complexity |
|------|----------|-------------|-----------|------------|
| **Walkthrough** | 1-2 hours | IR team only | Monthly | Low: review procedures step-by-step |
| **Tabletop** | 2-4 hours | IR team + business stakeholders | Quarterly | Medium: discuss scenario-based responses |
| **Functional** | 4-8 hours | Full IR team + executive | Semi-annually | High: simulate with tool usage (no real systems) |
| **Full Simulation** | 1-2 days | Entire organization | Annually | Very high: red team exercise with real attack simulation |

### Tabletop Exercise Template

```
TABLETOP EXERCISE PLAN

Exercise Name: [Name]
Date: [YYYY-MM-DD]
Duration: [X hours]
Facilitator: [Name]
Scenario Author: [Name]

OBJECTIVES:
1. [What capability are we testing?]
2. [What process are we validating?]
3. [What communication path are we exercising?]

PARTICIPANTS:
| Name | Role in Exercise | Real Role |
|------|-----------------|-----------|
| | | |

SCENARIO: [Scenario type - e.g., ransomware, data breach, insider threat]

INJECT TIMELINE:
| Time | Inject | Expected Response |
|------|--------|-------------------|
| T+0 | [Initial indicator presented to participants] | [What should they do?] |
| T+15 | [Escalation: situation worsens or new info] | [Expected escalation] |
| T+30 | [Complication: media inquiry, regulator call] | [Communications response] |
| T+45 | [Decision point: containment tradeoff] | [Decision framework] |
| T+60 | [Resolution path available] | [Recovery actions] |

DISCUSSION QUESTIONS:
1. At what point would you have escalated? Why?
2. What information did you need that you did not have?
3. Where did the process break down or feel unclear?
4. What would you do differently?

EVALUATION CRITERIA:
| Criterion | Met | Partially Met | Not Met | Notes |
|-----------|-----|---------------|---------|-------|
| Correct severity classification | | | | |
| Timely escalation to IC | | | | |
| Appropriate containment decision | | | | |
| Stakeholder communication initiated | | | | |
| Evidence preservation considered | | | | |
| Legal/regulatory notification identified | | | | |

FINDINGS AND RECOMMENDATIONS:
[Completed after exercise]

ACTION ITEMS:
| Action | Owner | Due Date |
|--------|-------|----------|
| | | |
```

### Recommended Scenario Rotation

| Quarter | Scenario | Focus Area |
|---------|----------|------------|
| Q1 | Ransomware attack on critical infrastructure | Technical response + executive decision-making |
| Q2 | Data breach with regulatory notification | Legal/compliance + customer communications |
| Q3 | Insider threat (privileged user) | HR coordination + evidence preservation |
| Q4 | Supply chain compromise | Third-party risk + cross-organizational coordination |

---

## CSIRT Team Structure

### Computer Security Incident Response Team (CSIRT)

```
                    ┌─────────────────┐
                    │   CISO / VP      │
                    │   Security       │
                    │  (Executive      │
                    │   Sponsor)       │
                    └────────┬────────┘
                             │
                    ┌────────┴────────┐
                    │   IR Manager     │
                    │  (Program Lead)  │
                    └────────┬────────┘
                             │
         ┌───────────┬───────┴───────┬───────────┐
         │           │               │           │
    ┌────┴────┐ ┌────┴────┐   ┌─────┴─────┐ ┌───┴────┐
    │  SOC /   │ │ Forensic │   │  Threat    │ │  IR     │
    │  Triage  │ │ Analysis │   │  Intel     │ │ Coord   │
    │  Team    │ │ Team     │   │  Team      │ │ Team    │
    └─────────┘ └─────────┘   └───────────┘ └────────┘
```

### CSIRT Roles and Responsibilities

| Role | Responsibilities | Skills Required | Staffing |
|------|------------------|-----------------|----------|
| **IR Manager** | Program leadership, process development, team management, exercise planning | Leadership, IR methodology, communication | 1 FTE |
| **SOC Analyst (Tier 1)** | Alert triage, initial classification, ticket creation, basic containment | SIEM, log analysis, alert investigation | 24x7 coverage (minimum 4 FTE) |
| **SOC Analyst (Tier 2)** | Deep investigation, malware triage, incident handling, containment execution | Advanced log analysis, network analysis, scripting | Business hours + on-call (minimum 2 FTE) |
| **Forensic Analyst** | Evidence collection, disk/memory/network forensics, root cause analysis | Forensic tools (EnCase, FTK, Volatility), chain of custody | On-call (minimum 1 FTE) |
| **Threat Intelligence Analyst** | IOC management, threat landscape monitoring, adversary profiling, hunt hypotheses | OSINT, threat frameworks (MITRE ATT&CK), intelligence analysis | Business hours (minimum 1 FTE) |
| **IR Coordinator** | Stakeholder communication, documentation, logistics, executive updates | Communication, project management, documentation | On-call (minimum 1 FTE) |
| **Malware Analyst** | Reverse engineering, sandbox analysis, YARA rule development | Reverse engineering, assembly, sandbox tools | On-call or outsourced |

### Extended CSIRT (Activated During Incidents)

| Function | Representative | Engaged For |
|----------|---------------|-------------|
| Legal / General Counsel | Legal team lead | P0, any data breach, regulatory considerations |
| Communications / PR | PR or comms lead | P0, any incident with potential public visibility |
| Human Resources | HR business partner | Insider threat, employee-related incidents |
| IT Operations | Infrastructure lead | System restoration, network changes, account management |
| Business Unit | Affected unit leader | Business impact assessment, process workarounds |
| Privacy / DPO | Data Protection Officer | Any incident involving personal data |
| Executive Leadership | CISO, CTO, or CEO | P0, incidents requiring executive authority |
| External Counsel | Retained law firm | P0 data breach, regulatory notification, litigation risk |
| External IR Firm | Retainer partner | P0, incidents exceeding internal capability |

### On-Call Rotation

| Tier | Coverage | Response Expectation | Compensation |
|------|----------|---------------------|--------------|
| Tier 1 (SOC) | 24x7x365 | Immediate (within SLA) | Shift-based |
| Tier 2 (Escalation) | Business hours + on-call | 30 minutes (P0/P1), 4 hours (P2) | On-call stipend |
| Tier 3 (Specialists) | On-call | 1 hour (P0), 4 hours (P1) | On-call stipend |
| IC (Management) | On-call | 15 minutes (P0), 30 minutes (P1) | On-call stipend |

### CSIRT Maturity Model

| Level | Name | Characteristics |
|-------|------|----------------|
| **1 - Ad Hoc** | No formal IR capability | IT staff handle incidents reactively; no dedicated team, plans, or tools |
| **2 - Defined** | IR plan exists, team designated | Documented plan, assigned roles, basic tools; inconsistent execution |
| **3 - Managed** | IR program operational | Dedicated staff, regular exercises, metrics tracked, lessons learned captured |
| **4 - Measured** | Metrics-driven improvement | KPIs tracked and benchmarked, continuous process improvement, threat hunting |
| **5 - Optimizing** | Proactive and intelligence-driven | Automated response, threat intelligence integration, adversary emulation, industry leadership |

---

## Quick Reference: Response Time Summary

| Severity | Assemble Team | First Update | Containment Target | Recovery Target |
|----------|--------------|-------------|---------------------|-----------------|
| **P0** | 15 min | 30 min | 4 hours | 24 hours |
| **P1** | 30 min | 2 hours | 12 hours | 72 hours |
| **P2** | 4 hours | Daily | 48 hours | 1 week |
| **P3** | Next business day | Weekly | Best effort | Best effort |
| **P4** | N/A | Monthly report | N/A | N/A |
