# Operations Playbooks

**Pack owner**: 📋 Director of Operations
**Consumers**: `ext-operations`, `process-engineer`, `project-manager`, `program-manager`, `fpa-analyst` (via financial-control SOPs)
**Status**: Active as of 2026-04-11
**Scope**: Standard operating procedures (SOPs) that are both human-readable and agent-executable, authored from first principles.

This pack contains the schema and reference material for authoring Operations playbooks. The centerpiece is the **Agent-Ready SOP Schema** below. Other sections (process library index, onboarding checklists, vendor runbooks) are stubs and will be populated as the Operations Team builds them out.

---

## Agent-Ready SOP Schema

### Purpose and Framing

An SOP is the smallest executable unit of a process. Humans and agents both fail SOPs, but for different reasons. Humans fail when context is implicit ("the team knows how this goes"), when decision rights are political, or when exception handling lives in tribal memory. Agents fail when triggers are undetectable, when inputs are untyped, when decisions require judgment that wasn't codified, or when success can't be verified without a human looking at the result. A schema that works for BOTH populations is rare precisely because most process documentation is written for one or the other — policy manuals for auditors, runbooks for on-call engineers, wikis for new hires. None of those are agent-ready, and most are not even reliably human-ready.

"Agent-ready" in this pack means three things, all testable. **Observable**: every trigger and completion signal is something a system or a human can detect without asking "is this done yet?". **Decidable**: every branch in the SOP names the decider (an agent role OR a human role) and the criterion they decide against. **Testable**: the SOP carries its own verification test — a named check with a pass/fail criterion, runnable by someone who did not author the SOP and who has no prior context. If any of these three are missing, the SOP is a draft, not an agent-ready playbook. The 7-field schema that follows is the minimum viable structure that forces all three properties into every SOP, regardless of complexity, maturity, or domain.

### The 7 Fields (Invariant)

Every agent-ready SOP has exactly these 7 fields. Not six. Not eight. The invariance matters because higher-maturity SOPs (per the `/process-engineering` maturity ladder referenced in C2.3) don't add fields — they CODIFY more of the same fields. A Manual-level SOP may encode `decision_rights` as "whoever picks it up," while an Agentic-level SOP makes `decision_rights` first-class with named roles and escalation paths. The field is present in both; what changes is how much is tribal vs. written down.

---

#### Field 1: Trigger

**Definition.** The specific event or condition that starts the SOP. A trigger is the answer to "when does this run?" — expressed so that a system, a schedule, or a named human can detect it without ambiguity.

**What it contains:**
- **Type**: `event` (something happened), `schedule` (time-based), `threshold` (metric crossed a value), or `manual` (human explicitly invoked)
- **Condition**: the specific, detectable circumstance — e.g., "Shopify order created with `financial_status=paid`," not "when an order comes in"
- **Detector**: who or what notices the trigger — e.g., "Shopify webhook to `fulfillment-queue`," "cron job at 02:00 UTC daily," "slack command `/reconcile`"
- **Debounce** (if applicable): how duplicate triggers are suppressed

**What it is NOT:**
- "When something happens" — not observable
- "As needed" — not detectable
- "When the team notices" — no named detector
- "Regularly" — no schedule

**Observable criterion.** A non-author can read the trigger and answer, in one sentence, WHAT they would need to watch in order to catch the SOP starting. If they can't, the trigger is hand-waved.

**Example fragment (from AXIA MRR reconciliation SOP):**
```
trigger:
  type: schedule
  condition: "First business day of each calendar month, 08:00 Asia/Jerusalem"
  detector: "cron job `mrr-recon-monthly` on fpa-runner-01"
  debounce: "idempotency key = YYYY-MM; re-runs in same month are no-ops"
```

---

#### Field 2: Inputs

**Definition.** The data, artifacts, or state the SOP needs in hand before it can meaningfully start. Inputs are typed (shape is declared), named (identifier is stable across runs), and sourced (where they come from is explicit).

**What it contains:**
- **Name**: stable identifier used in step references
- **Type**: shape or schema — e.g., `shopify.order` (JSON), `stripe.charges[]` (array), `pdf.bank_statement` (file)
- **Source**: where the input is pulled from — `shopify-cli orders get`, `stripe-cli events list`, `gdrive://finance/statements/`, `manual: operator provides`
- **Required**: `true` or `false` (optional inputs must be named, not implicit)
- **Fallback** (optional): what to do if the input is missing

**What it is NOT:**
- "All the usual data" — not typed
- "Context" — not named
- "Whatever the system has" — not sourced
- An implicit assumption about what the agent "should already know"

**Observable criterion.** A non-author could package the full input set from the declared sources without asking the author a single clarifying question. If they'd need to ask "and what about X?", X is a hidden input and must be surfaced.

**Example fragment (from SKYMOD fulfillment SOP):**
```
inputs:
  - name: order
    type: shopify.order
    source: "shopify webhook payload OR `shopify-cli orders get {id}`"
    required: true
  - name: inventory_snapshot
    type: shopify.inventory_levels[]
    source: "shopify-cli inventory list --location={warehouse_id}"
    required: true
  - name: shipping_config
    type: config.json
    source: "SKYMOD/operations/shipping-config.json"
    required: true
```

---

#### Field 3: Decision Rights

**Definition.** For every step in the SOP that involves a choice (not all steps do), who is authorized to make that choice and what the escalation path is if the authorized decider can't or won't decide.

**What it contains:**
- **Per-step decider**: agent role (e.g., `@fulfillment-bot`) or human role (e.g., `warehouse lead`). NEVER a person's name — roles only.
- **Decision criterion**: what the decider evaluates against (threshold, rule, judgment call with a named framing)
- **Escalation target**: who catches the decision if the primary decider is unavailable or is blocked
- **Escalation trigger**: the condition that forces escalation — a timeout, a value threshold, a named exception class
- **Acceptance signal**: how we know the decision has been made (not just "the decider thought about it")

**What it is NOT:**
- "The team decides" — team is not a role
- "Use judgment" — judgment is not a criterion unless it's framed ("judgment against factor A and factor B with the following tradeoff")
- "Escalate if needed" — no named target, no trigger
- Implicit ownership that everyone "just knows"

**Observable criterion.** For every decision step, a non-author can name the role that decides, the specific criterion, and the role that catches the decision if the primary is out. If any of the three is missing, decision rights are hand-waved.

**Example fragment (from AXIA expense approval SOP):**
```
decision_rights:
  steps:
    - step_id: approve-expense
      decider: "@finance-controller"
      criterion: "amount ≤ [TBD threshold] → auto-approve; > threshold → escalate"
      escalation: "@cfo"
      escalation_trigger: "amount > threshold OR controller unavailable > 24h"
      acceptance_signal: "approved_by field populated in ledger row"
```

---

#### Field 4: Steps

**Definition.** The procedure itself. An ordered or explicitly-parallel sequence of actions, each with the four mandatory sub-fields: action, owner, expected outcome, and completion signal.

**What it contains per step:**
- **step_id**: stable identifier, kebab-case, referenced by decision_rights and exception_handling
- **action**: imperative verb phrase — "fetch the order," "compute the variance," "generate the shipping label"
- **owner**: agent role OR human role executing the step
- **expected_outcome**: what the world looks like after the step runs (the observable state change)
- **completion_signal**: how we know the step finished — a log line, a file created, a state transition, a response code

**What it is NOT:**
- "Do the thing" — not an imperative action
- "Someone handles it" — no owner
- "Until it's done" — no completion signal
- A narrative paragraph describing the step; narrative is for runbooks, not agent-ready SOPs

**Observable criterion.** For each step, a non-author could execute it (or watch an agent execute it) and know with certainty, within seconds of completion, whether it finished. If they'd have to "wait a bit and see," the completion signal is missing.

**Example fragment (from SKYMOD fulfillment SOP):**
```
steps:
  - step_id: fetch-order
    action: "Retrieve full order record from Shopify"
    owner: "@fulfillment-bot"
    expected_outcome: "Order JSON in memory, line items parsed"
    completion_signal: "log entry `order_fetched` with order_id in fulfillment-log"
```

---

#### Field 5: Exception Handling

**Definition.** Explicit, named branches for failure modes. Not a catchall ("handle errors") — a per-exception fork with a recovery path.

**What it contains:**
- **exception**: named failure mode — "inventory_stockout," "address_validation_failed," "stripe_webhook_lost," "bank_statement_missing"
- **detection**: how the SOP notices this specific exception (error code, missing record, timeout, assertion failure)
- **branch**: what the SOP does next — specific steps, not "escalate to a human"
- **recovery path**: return to which step after the branch completes, OR escalate with a named target
- **idempotency note**: whether re-running the branch is safe

**What it is NOT:**
- "Use judgment if something goes wrong" — not named
- "Notify the team" — not a recovery path
- `try { ... } catch { rollback; }` — too coarse; name the specific exceptions that actually happen
- A promise that "the agent will figure it out"

**Observable criterion.** For every named exception, a non-author can trace what the SOP does next, who the SOP hands off to, and where the process resumes. If the branch ends with "escalate" and nothing more, the branch is missing a recovery path.

**Example fragment (from AXIA MRR reconciliation SOP):**
```
exception_handling:
  - exception: stripe_api_unreachable
    detection: "HTTP 5xx OR connection timeout after 3 retries with exponential backoff"
    branch: "persist checkpoint, notify @fpa-analyst in #finance-alerts, mark run state = BLOCKED"
    recovery_path: "manual restart by @fpa-analyst from checkpoint via `resume-recon.py --run={id}`"
    idempotency_note: "checkpoint is keyed on (run_id, step_id); resume is safe"
```

---

#### Field 6: Evidence Trail

**Definition.** What the SOP writes down as proof that it ran. Not "we'll see it in logs somewhere" — a specific log schema, a specific artifact destination, a specific retention policy.

**What it contains:**
- **log_schema**: the fields every run of the SOP writes — at minimum `run_id`, `sop_name`, `sop_version`, `started_at`, `completed_at`, `status`, `trigger_source`, and step-level events
- **artifact_destination**: where the tangible outputs land — e.g., `gdrive://finance/recon/YYYY-MM/`, `s3://skymod-ops/fulfillment/{order_id}/`
- **retention**: how long the evidence is kept — driven by audit, legal, or business need; not "forever" by default
- **access**: who can read the trail

**What it is NOT:**
- "We'll have logs" — no schema
- "Saved to the shared drive" — no path
- "Until we don't need them" — no retention
- Implicit retention ("the default")

**Observable criterion.** A non-author, three months later, can open the evidence trail for a specific run and reconstruct what happened step by step without asking the author. If they'd need the author's help to find it, the trail is not a trail.

**Example fragment (from SKYMOD fulfillment SOP):**
```
evidence_trail:
  log_schema:
    - run_id
    - sop_name: "skymod-fulfillment"
    - sop_version: "1.0.0"
    - order_id
    - started_at
    - completed_at
    - status: "success | partial | failed | blocked"
    - trigger_source: "webhook | manual_replay"
    - step_events[]: "{step_id, outcome, completed_at, duration_ms}"
  artifact_destination: "gdrive://skymod/operations/fulfillment/YYYY/MM/{order_id}/"
  retention: "7 years (DE/NL VAT requirement; longest-applicable market rule)"
  access: "read: @ops-team; write: @fulfillment-bot only"
```

---

#### Field 7: Verification Test

**Definition.** The named test that determines whether the SOP ran correctly. Pass/fail criterion. A runner (agent, human, or automated check) who executes the test and reports the result.

**What it contains:**
- **name**: stable test identifier
- **criterion**: the specific pass/fail rule — a comparison, an assertion, an equivalence check
- **runner**: who executes the test (agent role OR human role OR automated check)
- **frequency**: per-run OR sampled (e.g., "every run" vs "1 in 10 audited")
- **failure action**: what happens if the test fails — block the SOP from closing, open an exception, page a human

**What it is NOT:**
- "Looks fine to me" — not a criterion
- "The team will notice" — not a runner
- An absent test — a verifier is non-negotiable; agent-ready SOPs do not close out without verification
- A test that only the author can run

**Observable criterion.** A non-author can read the verification test, know what to look at, know the pass/fail line, and know who reports the result. If they can't, the test is decorative.

**Example fragment (from AXIA MRR reconciliation SOP, foot-and-tie):**
```
verification_test:
  name: "mrr-recon-foot-and-tie"
  criterion: |
    sum(stripe.recognized_revenue WHERE period = YYYY-MM)
    == sum(ledger.mrr_entries WHERE period = YYYY-MM)
    == sum(bank.deposits WHERE period = YYYY-MM AND source = 'stripe')
    within tolerance of $[TBD] OR 0.1% whichever greater
  runner: "automated check `foot-and-tie.py`; result reviewed by @fpa-analyst"
  frequency: "every run (monthly)"
  failure_action: "block run from closing; write state = FAILED; notify @fpa-analyst; escalate to @cfo if unresolved in 5 business days"
```

This is the C2.5 hook: every financial control SOP MUST populate `verification_test` with a foot-and-tie check. Internal consistency across three independent ledgers is the only defensible proof that a financial SOP ran correctly.

---

### Schema Declaration Template

Every agent-ready SOP authored in `operations-playbooks` uses this literal schema. YAML here for readability; the same structure serializes cleanly to JSON for agent consumption.

```yaml
sop_name: [kebab-case identifier]          # e.g., skymod-fulfillment
version: [semver]                          # e.g., 1.2.0
owner: [agent role OR human role]          # e.g., @process-engineer OR operations-dir
last_reviewed: [YYYY-MM-DD]
maturity_level: [manual | documented | standardized | automated | agentic]

trigger:
  type: [event | schedule | threshold | manual]
  condition: [specific, detectable circumstance]
  detector: [who or what notices the trigger]
  debounce: [how duplicate triggers are suppressed, if applicable]

inputs:
  - name: [identifier]
    type: [typed shape]
    source: [where it comes from]
    required: [true | false]
    fallback: [optional — what to do if missing]

decision_rights:
  steps:
    - step_id: [identifier]
      decider: [agent role OR human role]
      criterion: [what the decider evaluates against]
      escalation: [named escalation target role]
      escalation_trigger: [condition that forces escalation]
      acceptance_signal: [how we know the decision is made]

steps:
  - step_id: [identifier]
    action: [imperative verb phrase]
    owner: [agent role OR human role]
    expected_outcome: [observable state change]
    completion_signal: [how we know it finished]

exception_handling:
  - exception: [named failure mode]
    detection: [how the SOP notices this exception]
    branch: [what the SOP does next, specifically]
    recovery_path: [return to step_id OR escalate to role]
    idempotency_note: [whether re-running is safe]

evidence_trail:
  log_schema: [list of fields every run writes]
  artifact_destination: [specific path or system]
  retention: [duration with rationale]
  access: [read/write roles]

verification_test:
  name: [test identifier]
  criterion: [pass/fail rule]
  runner: [agent role OR human role OR automated check]
  frequency: [per-run | sampled-n-in-m]
  failure_action: [what happens on fail]
```

All 7 fields are first-class top-level keys. An SOP missing any of these keys fails the audit checklist at the bottom of this section, regardless of how polished the prose around it is.

---

### Worked Example 1: SKYMOD Order Fulfillment SOP

**Context (dated: 2026-04-11).** SKYMOD is a microbrand watch e-commerce run on Shopify, shipping from a UK fulfillment partner to EN / DE / NL / UK markets. DHL Express is the primary carrier; orders with value under [TBD] threshold route to a lower-cost carrier. Judge.me review requests fire on delivery. This SOP covers the end-to-end flow from Shopify order creation to customer shipping notification. Values marked `[TBD]` are real placeholders — the operational values live in SKYMOD config, not in this reference doc.

```yaml
sop_name: skymod-order-fulfillment
version: 1.0.0
owner: "@fulfillment-bot (primary); operations-dir (human accountable)"
last_reviewed: 2026-04-11
maturity_level: documented  # manual steps + automation islands; not yet fully agentic

trigger:
  type: event
  condition: "Shopify order created AND financial_status == 'paid' AND fulfillment_status == null"
  detector: "Shopify webhook `orders/paid` → fulfillment-queue (SQS)"
  debounce: "idempotency key = shopify.order_id; duplicate webhook firings are no-ops"

inputs:
  - name: order
    type: shopify.order
    source: "webhook payload; `shopify-cli orders get {order_id}` as backup"
    required: true
  - name: inventory_snapshot
    type: shopify.inventory_levels[]
    source: "`shopify-cli inventory list --location={warehouse_id}` at trigger time"
    required: true
  - name: shipping_config
    type: config.json
    source: "SKYMOD/operations/shipping-config.json (carrier rules per market)"
    required: true
  - name: customer_locale
    type: string
    source: "order.shipping_address.country_code → map to EN | DE | NL | UK"
    required: true
    fallback: "default to EN if country_code is ambiguous"

decision_rights:
  steps:
    - step_id: select-carrier
      decider: "@fulfillment-bot"
      criterion: "order.total_price ≥ [TBD threshold] → DHL Express; < threshold → [TBD lower-cost carrier]"
      escalation: "operations-dir"
      escalation_trigger: "shipping-config.json unreadable OR carrier API returns error > 3 retries"
      acceptance_signal: "carrier field populated on the fulfillment record"
    - step_id: handle-stockout
      decider: "operations-dir"
      criterion: "partial-ship available items OR hold whole order pending restock"
      escalation: "@ceo (Yohay)"
      escalation_trigger: "decision unresolved > 12 business hours"
      acceptance_signal: "operations-dir posts decision in #skymod-ops with order_id"

steps:
  - step_id: fetch-order
    action: "Retrieve full order record and validate required fields"
    owner: "@fulfillment-bot"
    expected_outcome: "Validated order object in memory; required fields present"
    completion_signal: "log entry `order_fetched` with order_id in fulfillment-log"
  - step_id: check-inventory
    action: "Verify all line items have sufficient stock at the fulfillment location"
    owner: "@fulfillment-bot"
    expected_outcome: "Stock-available list AND stock-short list (either may be empty)"
    completion_signal: "log entry `inventory_checked` with per-line stock deltas"
  - step_id: select-carrier
    action: "Apply shipping-config rules and choose carrier for this order"
    owner: "@fulfillment-bot"
    expected_outcome: "Named carrier selected and attached to fulfillment record"
    completion_signal: "log entry `carrier_selected` with carrier and rule_id"
  - step_id: generate-label
    action: "Request shipping label from the selected carrier API"
    owner: "@fulfillment-bot"
    expected_outcome: "Label PDF stored in artifact destination; tracking number obtained"
    completion_signal: "log entry `label_generated` with tracking_number"
  - step_id: notify-customer
    action: "Send shipping notification email in customer_locale"
    owner: "@fulfillment-bot"
    expected_outcome: "Email dispatched via Shopify notifications API"
    completion_signal: "log entry `customer_notified` with send_id and locale"
  - step_id: schedule-review-request
    action: "Schedule Judge.me review request for delivery+7 days"
    owner: "@fulfillment-bot"
    expected_outcome: "Judge.me queue entry created with scheduled timestamp"
    completion_signal: "log entry `review_scheduled` with review_request_id"

exception_handling:
  - exception: inventory_stockout
    detection: "any line item in check-inventory has stock-short > 0"
    branch: "invoke handle-stockout decision; if partial-ship, fulfill available items and flag remainder; if hold, mark fulfillment record as ON_HOLD and notify customer of delay in their locale"
    recovery_path: "return to select-carrier (partial) OR close run with status=ON_HOLD (full hold)"
    idempotency_note: "safe — fulfillment record state guards against double processing"
  - exception: carrier_api_unreachable
    detection: "carrier API returns 5xx or times out > 3 retries with exponential backoff"
    branch: "persist checkpoint, switch to manual label generation queue, notify operations-dir in #skymod-ops"
    recovery_path: "operations-dir runs `resume-fulfillment.py --order={id}` after manual label issued"
    idempotency_note: "safe — tracking_number uniqueness enforced at evidence-trail write"
  - exception: address_validation_failed
    detection: "carrier API returns address validation error on label request"
    branch: "email customer in their locale requesting corrected address; hold order; set reminder +48h"
    recovery_path: "customer reply triggers manual replay by operations-dir; escalate to @ceo after 5 business days of no response"
    idempotency_note: "safe"

evidence_trail:
  log_schema:
    - run_id
    - sop_name: "skymod-order-fulfillment"
    - sop_version: "1.0.0"
    - order_id
    - started_at
    - completed_at
    - status: "success | partial | on_hold | failed"
    - trigger_source: "webhook | manual_replay"
    - carrier
    - tracking_number
    - customer_locale
    - step_events[]: "{step_id, outcome, completed_at, duration_ms}"
  artifact_destination: "gdrive://skymod/operations/fulfillment/YYYY/MM/{order_id}/"
  retention: "7 years (longest-applicable market rule: DE/NL VAT records)"
  access: "read: @ops-team, operations-dir, @ceo; write: @fulfillment-bot only"

verification_test:
  name: "skymod-fulfillment-closeout-check"
  criterion: |
    for each order where status == 'success':
      1) tracking_number is present AND validated by carrier status endpoint
      2) customer notification send_id confirmed by Shopify notifications API
      3) inventory deducted in Shopify matches the line items fulfilled
      4) evidence trail artifacts exist at the declared destination
    all four conditions must pass
  runner: "automated check `fulfillment-verify.py`; flagged fails reviewed by operations-dir"
  frequency: "every run"
  failure_action: "mark run status=FAILED; open incident in #skymod-ops; block next run for same order_id until resolved"
```

**Audit note.** A process engineer auditing this SOP has all 7 fields populated concretely, with named roles, specific carriers, locales, and log schemas. Every step has a completion signal. Every exception has a recovery path. The only `[TBD]` values are operational numbers that live in SKYMOD's config, not in this reference.

---

### Worked Example 2: AXIA Monthly MRR Reconciliation SOP

**Context (dated: 2026-04-11).** AXIA is on Stripe (test mode transitioning to production) and runs enterprise contracts including the in-flight Bank Discount deal. Monthly MRR reconciliation ties together three independent ledgers — Stripe recognized revenue, internal ledger MRR entries, and bank deposits from Stripe payouts. This SOP is the canonical C2.5 example because its verification test IS a foot-and-tie check. Values marked `[per deal]` and `[TBD]` are placeholders for deal-specific and org-specific numbers.

```yaml
sop_name: axia-mrr-reconciliation-monthly
version: 1.0.0
owner: "@fpa-analyst (primary); cfo (human accountable)"
last_reviewed: 2026-04-11
maturity_level: documented  # monthly cadence; semi-automated; finance human-in-loop at verification

trigger:
  type: schedule
  condition: "First business day of each calendar month, 08:00 Asia/Jerusalem"
  detector: "cron job `axia-mrr-recon-monthly` on finance-runner instance"
  debounce: "idempotency key = reconciliation_period (YYYY-MM); re-runs in the same month are no-ops unless --force is passed by @fpa-analyst"

inputs:
  - name: stripe_revenue_export
    type: stripe.recognized_revenue
    source: "`stripe-cli revenue recognition export --period={YYYY-MM}`"
    required: true
  - name: ledger_mrr_entries
    type: ledger.mrr_entries[]
    source: "query `ledger.mrr_entries WHERE period = {YYYY-MM}` in internal finance DB"
    required: true
  - name: bank_deposits
    type: bank.deposits[]
    source: "bank statement CSV export for the period; pulled via finance drive"
    required: true
    fallback: "if bank statement not yet available, run state = PENDING_BANK; retry daily until available or escalate at day+10"
  - name: contract_register
    type: contracts.active[]
    source: "`contracts-register.json` — active enterprise contracts and expected monthly values"
    required: true
  - name: prior_recon
    type: recon.result
    source: "previous month's reconciliation artifact"
    required: false
    fallback: "if first run, use contract_register as baseline"

decision_rights:
  steps:
    - step_id: accept-variance
      decider: "@fpa-analyst"
      criterion: "variance within tolerance → auto-close; variance > tolerance → investigate; investigation unresolved > 5 business days → escalate"
      escalation: "cfo"
      escalation_trigger: "unresolved variance > 5 business days OR variance > [TBD material threshold]"
      acceptance_signal: "recon_status field set to 'accepted' with @fpa-analyst signature in the artifact"
    - step_id: apply-deal-specific-adjustment
      decider: "@fpa-analyst"
      criterion: "Bank Discount deal uses [per deal] milestone-based billing; SOP applies milestone schedule from contract_register"
      escalation: "cfo"
      escalation_trigger: "contract_register missing or ambiguous for an active deal"
      acceptance_signal: "adjustment row appears in reconciliation artifact with deal reference"

steps:
  - step_id: pull-stripe-revenue
    action: "Export Stripe recognized revenue for the period"
    owner: "@fpa-analyst (automated pull)"
    expected_outcome: "CSV of Stripe recognized revenue lines for the period, by customer"
    completion_signal: "log entry `stripe_revenue_pulled` with row count and period"
  - step_id: pull-ledger-mrr
    action: "Query internal ledger MRR entries for the period"
    owner: "@fpa-analyst (automated pull)"
    expected_outcome: "CSV of ledger MRR entries for the period, by customer"
    completion_signal: "log entry `ledger_mrr_pulled` with row count and period"
  - step_id: pull-bank-deposits
    action: "Extract Stripe-sourced bank deposits for the period"
    owner: "@fpa-analyst (semi-manual; statement upload)"
    expected_outcome: "CSV of bank deposits tagged with source = 'stripe' for the period"
    completion_signal: "log entry `bank_deposits_pulled` with row count and total amount"
  - step_id: apply-contract-adjustments
    action: "Apply deal-specific adjustments per contract_register (e.g., Bank Discount milestone billing)"
    owner: "@fpa-analyst"
    expected_outcome: "Adjustment rows appended to each ledger for deals with non-flat MRR"
    completion_signal: "log entry `adjustments_applied` with row count"
  - step_id: foot-and-tie
    action: "Run three-way foot-and-tie across stripe_revenue, ledger_mrr, bank_deposits"
    owner: "@fpa-analyst (automated via `foot-and-tie.py`)"
    expected_outcome: "Variance computed per pair; overall variance vs tolerance"
    completion_signal: "log entry `foot_and_tie_complete` with pairwise deltas and verdict"
  - step_id: close-run
    action: "Emit reconciliation artifact, mark status, notify subscribers"
    owner: "@fpa-analyst"
    expected_outcome: "Artifact in destination; status set; #finance notified"
    completion_signal: "log entry `recon_closed` with status"

exception_handling:
  - exception: stripe_api_unreachable
    detection: "HTTP 5xx OR connection timeout after 3 retries with exponential backoff"
    branch: "persist checkpoint; mark run state = BLOCKED; notify @fpa-analyst in #finance-alerts"
    recovery_path: "manual restart by @fpa-analyst from checkpoint via `resume-recon.py --run={id}`"
    idempotency_note: "checkpoint is keyed on (run_id, step_id); resume is safe"
  - exception: bank_statement_missing
    detection: "pull-bank-deposits returns empty OR statement file not present in finance drive"
    branch: "set run state = PENDING_BANK; retry daily at 09:00; after 10 calendar days, escalate to cfo"
    recovery_path: "on successful pull, resume from pull-bank-deposits"
    idempotency_note: "safe — pending runs are keyed on period"
  - exception: variance_over_tolerance
    detection: "foot-and-tie verdict = FAIL (variance > tolerance)"
    branch: "open investigation subtask, identify discrepancy source (stripe vs ledger vs bank), document in variance log"
    recovery_path: "accept-variance decision OR escalate to cfo after 5 business days"
    idempotency_note: "investigation is human-driven; SOP run stays OPEN until decision"
  - exception: contract_register_ambiguous
    detection: "apply-contract-adjustments encounters an active contract without milestone schedule (or conflicting entries)"
    branch: "flag the deal, pause run, notify @fpa-analyst and cfo"
    recovery_path: "cfo confirms or amends contract_register; run resumes from apply-contract-adjustments"
    idempotency_note: "safe — adjustments table is recomputed on resume"

evidence_trail:
  log_schema:
    - run_id
    - sop_name: "axia-mrr-reconciliation-monthly"
    - sop_version: "1.0.0"
    - period: "YYYY-MM"
    - started_at
    - completed_at
    - status: "success | variance_open | blocked | pending_bank | failed"
    - stripe_revenue_total
    - ledger_mrr_total
    - bank_deposits_total
    - variance_usd
    - variance_pct
    - step_events[]: "{step_id, outcome, completed_at, duration_ms}"
  artifact_destination: "gdrive://axia/finance/reconciliation/YYYY/{YYYY-MM}/"
  retention: "7 years (Israeli corporate tax record retention; aligns with AXIA entity domicile)"
  access: "read: cfo, @fpa-analyst, @ceo; write: @fpa-analyst only"

verification_test:
  name: "axia-mrr-foot-and-tie"
  criterion: |
    |stripe_revenue_total - ledger_mrr_total| ≤ max($[TBD tolerance], 0.1% of ledger_mrr_total)
    AND
    |ledger_mrr_total - bank_deposits_total - stripe_fees - timing_adjustments| ≤ max($[TBD tolerance], 0.1% of ledger_mrr_total)
    Both pairs must pass for status = success.
  runner: "automated check `foot-and-tie.py`; result co-signed by @fpa-analyst"
  frequency: "every run (monthly)"
  failure_action: "mark run status = variance_open; trigger variance_over_tolerance exception; block next monthly run from closing until this one is accepted or escalated"
```

**Audit note.** The foot-and-tie verification test is the key C2.5 hook — internal consistency across three independent ledgers is the ONLY defensible answer to "how do we know the financial SOP ran correctly?" No single-source check can substitute. An FP&A analyst auditing this SOP will look at `verification_test.criterion` first — if that's present, concrete, and references three independent sources with a tolerance, the SOP meets the financial control bar. If the criterion reads "FP&A reviews" or "spot-check," it fails.

---

### Alignment with Maturity Ladder (C2.3)

The 7 fields are invariant across maturity levels. What changes is how much is codified vs. tribal, and whether execution is human-driven or machine-driven. The ladder below is summarized from the `## Process Engineering Maturity Ladder` section further down — that section is the authoritative source. A Manual SOP still has all 7 fields — they're just implicit. The goal of moving up the maturity ladder is to CODIFY each field so an agent (or a new hire) can run the SOP without tribal context. When @process-engineer runs the maturity ladder assessment, the assessment question for each field is "is this written down and observable from the SOP alone, or does someone have to ask?" If the answer is "ask," that field is still at a lower rung for that SOP.

### Alignment with Financial Rubric (C2.5)

Financial control SOPs (per @fpa-analyst's 7-dimension rubric in C2.5) MUST populate `verification_test` with a foot-and-tie check — a three-way (or more) internal consistency test across independent sources. The AXIA MRR reconciliation example above is the canonical pattern. When an FP&A analyst applies the C2.5 rubric to an SOP, the first dimension checked is **Internal Consistency**, and the evidence for that dimension lives in the `verification_test` field of this schema. If the verification test is not a foot-and-tie (or equivalent independent-source reconciliation), the SOP fails the C2.5 rubric regardless of how polished the rest of the SOP is.

Non-financial SOPs (like SKYMOD fulfillment above) are not held to the foot-and-tie bar — their verification tests can be carrier status checks, API response validation, state-transition assertions — but they still need a named, runnable test. The C2.5 rubric only governs the financial subset; the 7-field schema governs all SOPs.

---

### Anti-Patterns (Common Ways SOPs Fail the Agent-Ready Gate)

These are the failure modes observed when non-agent-ready SOPs are handed to a process engineer or an FP&A analyst for audit. Every one of them is invisible in the prose and only surfaces when someone tries to execute or verify the SOP.

1. **Implicit decision rights.** "The team approves." Team is not a role; "approves" has no criterion; there is no escalation. Rewrite: name the role, name the criterion, name the escalation target.

2. **Vague triggers.** "When something goes wrong" or "as needed" or "periodically." None of these are detectable. Rewrite: name the specific event, schedule, or threshold, and name the detector.

3. **Hand-waved exception handling.** `try { ... } catch { notify team }` or "if there's an issue, use judgment." Exception handling must fork per named failure mode, with a specific branch and a specific recovery path. Rewrite: list the top 3-5 named failure modes and handle each explicitly.

4. **Missing evidence trails.** "Logs are in the system" or "saved to the drive." No schema, no path, no retention. Rewrite: declare the log fields, the artifact destination, and the retention period with rationale.

5. **Decorative verification tests.** "Looks correct" or "signed off by manager." These are not tests — they're hopes. Rewrite: define a specific pass/fail criterion, name the runner, say what happens on fail.

6. **Ambiguous owners.** "The ops team handles it." Not a role. "Ops" is not a decider. Rewrite: one named role per step, one named role per decision, one named role per escalation.

7. **Missing completion signals.** "Run the process and move on." No way to know the step finished. Rewrite: every step emits a log entry, a state change, or a response code that a non-author can observe within seconds.

---

### Audit Checklist

A process engineer or FP&A analyst uses this checklist to verify an SOP is agent-ready. 10 items, all binary pass/fail, all observable from reading the SOP alone without author context.

1. [ ] **Schema structure** — all 7 fields (trigger, inputs, decision_rights, steps, exception_handling, evidence_trail, verification_test) are present as top-level keys. No field is missing.
2. [ ] **Trigger is detectable** — type, condition, detector are named. A non-author can say what they'd watch to catch the SOP starting.
3. [ ] **Inputs are typed and sourced** — every input has name + type + source + required flag. No implicit inputs.
4. [ ] **Decision rights per decision** — every step involving a choice names the decider role, the criterion, the escalation target, and the escalation trigger.
5. [ ] **Completion signals per step** — every step has an observable completion signal (log entry, state change, response code). No "wait and see" steps.
6. [ ] **Exceptions are named** — at least the top 3-5 failure modes are handled explicitly with detection, branch, recovery path, and idempotency note. No catchall.
7. [ ] **Evidence trail is specific** — log schema declared, artifact destination is a real path, retention has a rationale. Not "in logs somewhere."
8. [ ] **Verification test is runnable** — named test, pass/fail criterion, named runner, frequency, failure action. A non-author can execute it.
9. [ ] **Financial SOPs have foot-and-tie** — if the SOP is a financial control, its verification test is a multi-source internal consistency check, not a single-source spot check. (C2.5 alignment.)
10. [ ] **No hand-waving** — no "use judgment," "the team decides," "as needed," or "looks fine" anywhere in the SOP.

If any box is unchecked, the SOP is not yet agent-ready. Fix the failing field and re-audit. The checklist is cheap to run; the cost of shipping a non-agent-ready SOP is that the process quietly fails the first time it runs without the author in the room.

---

## Process Engineering Maturity Ladder

### Purpose and Framing

The maturity ladder classifies a process against observable signals readable from the SOP document itself. Its job is detection, not prescription. Given an SOP in hand and zero prior context on the team, an auditor should be able to assign the SOP to exactly one rung by reading the SOP and answering a short list of observable questions. The rung describes what the process IS today, not what it should become. Anyone can claim "we're Standardized" or "we're Agentic" in a slide. The ladder only cares about what is provable from the SOP artifact itself.

What the ladder does NOT do: it does not prescribe which rung any specific team SHOULD be at, it does not predict outcomes (a well-run Documented SOP beats a half-built Agentic one every day of the week), and it does not grade the team's effort or intent. A team running a manual SOP well is not failing — they are at Manual, full stop, and Manual may be the right rung for that process. The ladder is a measurement device, not a report card. "Observable" is the load-bearing word: only signals detectable from the SOP document (and, where specified, the evidence trail it points to) count. Anything that requires asking the team, reading intent, or inferring culture is not a signal — it is a hope.

### Honest Rung Count — Reasoning Exposed

This ladder ships with **4 rungs**: Manual, Documented, Automated, Agentic. Not 5, not 3. I want to show the reasoning, because the execution plan was explicit that rungs which look different but collapse to the same observable signals must be merged or dropped.

The rung I considered and **dropped** is **Standardized** (which typically sits between Documented and Automated in public frameworks). The pitch for Standardized is that it captures processes where the 7 fields are not just written down but also structured and enforced across runs — named roles, schemas, retention policies, thresholds. The problem with Standardized as a separate rung is that its observable signals are identical to Documented if you are auditing the SOP alone. Both rungs have the 7 fields populated in schema form. The difference Standardized tries to capture — "enforcement across runs," "consistency over time," "policy-level adherence" — is not observable from the SOP document; it is observable only from the runtime, the audit log, and the organizational culture. Those are NOT things the ladder audits. The ladder audits SOPs as written. So Standardized collapses into Documented, because the thing that would distinguish them cannot be seen from where the ladder looks.

The rung I considered and **kept** is Automated, separate from Documented and Agentic. Here the observable signal is real and readable from the SOP: in a Documented SOP, the `owner` field on steps names humans; in an Automated SOP, the `owner` field names code, workflows, or system actors, and `decision_rights` still names humans for choices. The human-vs-machine split on `owner` is detectable per step, which is the exact right level for the ladder. Automated survives.

The rung I considered and **kept** is Agentic, separate from Automated. In an Automated SOP, code executes steps but humans decide — `decision_rights.decider` fields name human roles. In an Agentic SOP, `decision_rights.decider` fields name agent roles with machine-auditable criteria. This is a single-field observable signal, which is the right bar. Agentic survives.

The rung I considered and **dropped** is **Level 0 / Ad Hoc** (a pre-Manual rung where no SOP exists at all). It collapses into "no SOP to audit" — there is nothing for the ladder to read. Ad Hoc is the absence of a process, not a rung on a process ladder. Dropped.

Final ladder: **Manual (tribal fields) → Documented (schema fields, human execution) → Automated (schema fields, code executes steps, humans decide) → Agentic (schema fields, agents execute and agents decide within codified criteria)**. Four rungs. Every transition is detectable from the SOP artifact with a single observable question. That is the bar the execution plan set.

### The Ladder

| Level | Observable Signals | Decision Rights | Exception Handling | Tooling |
|---|---|---|---|---|
| **1. Manual** | The 7 fields are implicit, tribal, or missing. The SOP either does not exist as a document or reads as prose that leaves steps, deciders, and thresholds unnamed. A non-author cannot execute the SOP without asking the author or a team member. No completion signals per step. Exception handling is "escalate to whoever is around." | "Whoever picks it up" or "the team decides." No named roles per step. Escalation path is a person's name (usually the manager), not a role, and the escalation trigger is "if it feels bad." | "Escalate to manager" as a catchall. Named failure modes absent. Recovery path is whatever the escalated human decides in the moment. Idempotency not considered. | None / email / spreadsheets / shared folders. Runs on tribal memory and screen-sharing. No workflow engine, no scheduler, no evidence system beyond inbox archaeology. |
| **2. Documented** | All 7 fields are present in the SOP document as structured content (YAML, a structured table, or a schema that meets the `Agent-Ready SOP Schema` above). Steps have `owner = human role`, `action = imperative verb phrase`, and `completion_signal` that a non-author can observe. Exception handling is per named failure mode. Evidence trail declares a schema and a destination. Verification test is runnable by a non-author. Execution itself is HUMAN-driven: the owner of each step is a named human role. | Named human roles per decision step. Criterion is written down against a specific threshold, rule, or framed judgment call. Escalation target is a named human role. Escalation trigger is specific (timeout, value threshold, named exception class). Acceptance signal is observable. | Top 3-5 named failure modes with per-exception branches. Each branch names a recovery path — return to a named step or escalate to a named role. Idempotency noted per branch. | Ticketing system, workflow engine used as a form-and-routing tool, shared drive with structured folder conventions, cron-scheduled reminders. Tooling supports the human; it does not replace the human. |
| **3. Automated** | The `owner` field on steps names code, workflow actions, or system actors — not humans. Triggers are events on a bus, webhooks, or schedules with idempotency keys declared in the `trigger.debounce` field. Evidence trail is written automatically as structured logs. Verification test runs on every run without human prompting. Decision-making still names HUMAN roles in `decision_rights.decider` — when the process hits a choice, a human is paged to decide. | Named human roles per decision. Criterion and thresholds are machine-readable (the automation evaluates against them), but the DECISION is still a human signoff. Escalation is a pager duty schedule or an on-call rotation, not a person. Acceptance signal is a structured response (API call, button click, ticket resolution). | Per-exception branches are code paths. Detection is an error code, a missing-record query, a timeout assertion. Recovery path often runs automatically (retry, checkpoint, resume) with human-in-the-loop only for unresolved states. Idempotency enforced by checkpoint keys or dedupe tables. | Workflow engine (Airflow, Temporal, n8n, Workato), event bus, scheduler, automated observability stack, structured logging system, artifact storage with retention policies. The stack runs; the humans react. |
| **4. Agentic** | The `decision_rights.decider` field names agent roles (e.g., `@fulfillment-bot`, `@fpa-analyst` as an agent role, not the human). Criteria in `decision_rights.criterion` are machine-evaluable without human judgment calls. Verification test runs automatically per run AND has a named human tiebreaker for edge cases where the agent is not confident. Exception handling includes at least one branch where an agent decides the recovery path (escalates to a human only if the branch's own confidence threshold is not met). | Named agent roles per decision step, with criteria the agent can evaluate without asking. Escalation targets are human roles (never agent-to-agent without a named tiebreaker). Acceptance signal is an agent-emitted state change logged in a queryable system. Human tiebreaker is named per decision class (not per SOP). | Per-exception branches where the agent selects the recovery path from a codified set. Branches name the confidence threshold under which the agent escalates to a human tiebreaker rather than choosing. Idempotency enforced at the agent runtime level. | Agent runtime (LLM-backed or rule-backed), machine-readable decision criteria, continuous automated verification, queryable evidence trail, confidence scoring on agent decisions, named human tiebreaker roles per decision class. |

Every cell in the ladder describes what is **detectable from the SOP document** (and, where specified, the evidence trail it points to). No cell references culture, intent, or team maturity.

### Per-Rung Detail

#### Rung 1: Manual

**Definition.** A Manual process is one where the 7 fields are implicit or missing. The process works because specific people know how to do it, not because the SOP says how to do it. If the author of the SOP (or the most senior person on the team) is out for a week, the process either stops or degrades in a way that is visible to whoever is downstream of it.

**Observable signals.**
- The SOP does not exist as a document, OR exists only as prose in a wiki / Google Doc with no structured fields.
- Steps are narrative paragraphs, not imperative verb phrases with owners.
- Deciders are "the team," "whoever," or the manager's name.
- Completion signals absent — steps end with "until it's done" or equivalent.
- Exception handling is "escalate to manager" or "use judgment."
- Evidence trail is email threads, chat scrollback, or the team's collective memory.
- Verification is "looks fine" or "signed off" without a named test.

**How the 7 fields are populated at this rung:**

| Field | Typical Manual-level content |
|---|---|
| Trigger | "When we get an order" / "as needed" / "when something happens" |
| Inputs | Not named; "all the usual data" or implicit |
| Decision Rights | "Whoever picks it up" / "the team decides" |
| Steps | Narrative paragraphs; no owners; no completion signals |
| Exception Handling | "Escalate to the manager" as a catchall |
| Evidence Trail | Inbox / chat scrollback / shared drive with no schema |
| Verification Test | "Looks fine" / "manager signs off" |

**Failure modes at this rung.**
- **Author dependency.** The process stops working when the author is unavailable because the tribal knowledge leaves with them.
- **Silent drift.** The process changes over time without anyone noticing; different team members execute it differently.
- **Audit brittleness.** External audits (SOC 2, ISO, tax) cannot verify the process ran because there is no evidence trail to inspect.
- **Escalation chaos.** When something breaks, the escalation target is whoever is most senior and available, not whoever has the authority, so decisions are made by the wrong person.
- **No verification.** Nobody can tell whether the SOP ran correctly because there is no test.

**Transition signal to Documented.** The team starts encountering the consequences of Manual: a failed audit, a new hire who cannot onboard, a wrong decision escalated to the wrong person, a customer issue the team cannot root-cause because there is no trail. The transition is triggered when the cost of being Manual exceeds the cost of writing the SOP down. Until that day, Manual is often the correct rung — writing SOPs has a cost, and low-frequency, low-stakes processes do not repay the cost.

---

#### Rung 2: Documented

**Definition.** A Documented process has all 7 fields populated in the structured form required by the Agent-Ready SOP Schema. A non-author can read the SOP and execute it. Execution itself is human-driven: the `owner` field on steps names human roles, and the SOP is run by a human following the steps. Documented is where the ladder first meets the Agent-Ready bar — a Manual SOP is not agent-ready; a Documented SOP is agent-ready for HUMAN agents (which is what humans are, when viewed through this schema).

**Observable signals.**
- All 7 fields present as top-level keys in the SOP document.
- Steps have `owner = human role`, `action = imperative verb`, `completion_signal = observable event`.
- `decision_rights.steps[].decider` names human roles.
- `exception_handling` lists named failure modes with per-exception branches.
- `evidence_trail.log_schema` and `artifact_destination` are declared paths.
- `verification_test` has a named runner (which may be a human) and a pass/fail criterion.
- No prose catchalls; no "use judgment" language in the schema fields.

**How the 7 fields are populated at this rung:**

| Field | Typical Documented-level content |
|---|---|
| Trigger | Named event, schedule, or threshold with detector and debounce rule |
| Inputs | Typed, named, sourced; optional inputs marked; no implicit inputs |
| Decision Rights | Named human roles per decision; written criteria; named escalation targets; acceptance signals |
| Steps | Ordered list; each with owner (human role), imperative action, expected outcome, observable completion signal |
| Exception Handling | Top 3-5 named failure modes; per-exception branch with recovery path; idempotency noted |
| Evidence Trail | Declared log schema; real artifact destination path; retention with rationale |
| Verification Test | Named test; pass/fail criterion; human or automated runner; frequency; failure action |

**Failure modes at this rung.**
- **Document rot.** The SOP is written once and never updated; real execution drifts away from the documented version.
- **Execution variance.** Different humans interpret the same step differently, producing run-to-run variance that the SOP permits.
- **Manual bottleneck.** Every run requires a human for every step; the process does not scale with volume.
- **Escalation queue buildup.** Every decision is a human decision; as volume grows, decisions queue.
- **Verification fatigue.** The verification test exists but is run by a human who gets tired of running it and starts signing off without executing.

**Transition signal to Automated.** Volume grows to a level where human execution of repetitive steps becomes the bottleneck, OR the cost of execution variance (mistakes, rework, customer-visible defects) exceeds the cost of building automation. Documented is often the correct rung for low-volume, high-judgment processes (board decisions, M&A memos, crisis response). Do not automate a process just because you can — automate because the volume and variance economics justify it.

---

#### Rung 3: Automated

**Definition.** An Automated process has code, workflow engines, or system actors executing the steps. The `owner` field on steps names code or workflow actions instead of human roles. Decision-making remains human: when the process hits a choice, it pages a human. Exception handling is mostly code-driven, with humans in the loop for unresolved states. Verification runs automatically on every run.

**Observable signals.**
- `steps[].owner` names code or workflow actors (e.g., `@fulfillment-bot` where the bot is a cron/worker, not an agent).
- `trigger.type` is `event` or `schedule` with a machine-readable detector and an idempotency key in `debounce`.
- `decision_rights.steps[].decider` still names HUMAN roles — the automation evaluates criteria but a human clicks a button or resolves a ticket to commit the decision.
- `exception_handling` branches are code paths (retries, checkpoints, circuit breakers) with human escalation only for unresolved states.
- `evidence_trail.log_schema` is written automatically on every run.
- `verification_test.runner` is an automated check, run every run, with a failure action that blocks the run from closing.

**How the 7 fields are populated at this rung:**

| Field | Typical Automated-level content |
|---|---|
| Trigger | Event-bus message, webhook, or scheduled job; idempotency key declared |
| Inputs | Pulled automatically from typed sources; fallbacks explicit |
| Decision Rights | Automation evaluates criterion; HUMAN role commits decision via structured response (API call, ticket resolution) |
| Steps | Owned by code/workflow actors; completion signals are log events emitted by the runtime |
| Exception Handling | Retry logic, checkpoint/resume, named failure branches as code paths; human escalation on unresolved |
| Evidence Trail | Structured logs emitted by the runtime; artifacts stored in declared system; retention enforced by storage policy |
| Verification Test | Automated check runs every run; failure blocks run from closing; notification to named human role on failure |

**Failure modes at this rung.**
- **Silent automation drift.** The automation runs but no one reviews the verification failures; failed runs accumulate in a backlog no one monitors.
- **Human decision bottleneck.** The automation executes fast but decisions queue waiting for human signoff; throughput of the slowest step is the throughput of the system.
- **Exception catchall regression.** Over time, code paths for unnamed exceptions collapse into a single "fall back to human" branch, silently reverting the SOP toward Documented for anything unusual.
- **Observability gap.** The runtime emits logs, but no one has built the dashboard that makes them readable, so when something fails the evidence trail is technically present but practically inaccessible.
- **Verification cargo-culting.** The verification test runs but its criterion was never updated when the underlying logic changed; it passes on every run while silently failing to catch anything.

**Transition signal to Agentic.** Human decision bottlenecks start limiting throughput in a way the business can measure, AND the decision criteria are stable enough to be codified without edge-case explosion. If the criteria are still evolving week-to-week, the process is not ready for Agentic — you are automating a moving target. If the decisions are so context-dependent that no codified criterion captures them, the process should stay Automated with a human decider. Agentic is earned, not claimed.

---

#### Rung 4: Agentic

**Definition.** An Agentic process has agent roles as first-class deciders in the `decision_rights` field, with criteria the agent can evaluate without human judgment. Verification runs automatically AND has a named human tiebreaker for edge cases below a confidence threshold. Exception handling includes at least one branch where an agent chooses the recovery path from a codified set. Humans stay in the loop as tiebreakers, not as default deciders.

**Observable signals.**
- `decision_rights.steps[].decider` names agent roles (not human roles, not code actors).
- `decision_rights.steps[].criterion` is machine-evaluable (threshold, rule, classifier output) — no "judgment against framing" language.
- At least one `exception_handling[].branch` names the agent as the decider of the recovery path, with a confidence threshold that triggers escalation to a named human tiebreaker.
- `verification_test` runs automatically every run AND names a human tiebreaker for edge cases (not for every run — for failure investigation or low-confidence verdicts).
- The SOP references an agent runtime, a confidence scoring mechanism, and a named human tiebreaker role per decision class.

**How the 7 fields are populated at this rung:**

| Field | Typical Agentic-level content |
|---|---|
| Trigger | Agent-observable event with detector that agents can subscribe to; idempotency enforced at agent runtime |
| Inputs | Typed and retrieved by the agent from declared sources; fallbacks explicit |
| Decision Rights | Agent role per decision; machine-evaluable criterion; confidence threshold for escalation; named human tiebreaker per decision class |
| Steps | Owned by agent roles; completion signals are agent-emitted state changes in a queryable system |
| Exception Handling | Per-exception branches where the agent selects the recovery path from a codified set; confidence threshold triggers tiebreaker escalation |
| Evidence Trail | Fully queryable artifact system; agent decisions logged with criterion, inputs, confidence, and verdict |
| Verification Test | Automated every run; named human tiebreaker on edge cases or low-confidence verdicts |

**Failure modes at this rung.**
- **Criterion drift.** The machine-readable criterion was correct when authored but the world changed, and the agent continues to evaluate against stale criteria because no one is watching.
- **Confidence miscalibration.** The confidence threshold is set too low, so the agent rarely escalates and makes wrong decisions silently; or set too high, so the agent escalates everything and the tiebreaker becomes the de facto decider (silently reverting to Automated).
- **Tiebreaker overload.** The named human tiebreaker is pinged more than expected because the agent encounters edge cases the criterion did not anticipate; the human becomes the bottleneck the Agentic rung was supposed to remove.
- **Evidence trail fragmentation.** Agent decisions log to the runtime's system, but the evidence trail for the SOP lives somewhere else, so reconstructing a run requires cross-system correlation no one has built.
- **Accountability diffusion.** Because agents decide, nobody feels accountable when a decision is wrong; the post-mortem produces "the agent was wrong" as a verdict, which is not a remediation.

**Transition signal beyond Agentic.** There is no rung beyond Agentic in this ladder. A team that wants to go "higher" is really describing operational excellence within Agentic — better criteria calibration, better confidence scoring, better tiebreaker ergonomics, broader exception coverage. Those are improvements within the rung, not a new rung. If someone proposes a "Level 5 / Fully Autonomous" rung, ask them what observable signal distinguishes it from Agentic at the SOP level. If the only distinction is "the human is not involved at all," they are describing a process that does not need a human tiebreaker — which is a property of the decision class, not a rung of the ladder. Drop it.

---

### Transitions Between Rungs

The three transitions — Manual → Documented, Documented → Automated, Automated → Agentic — each have characteristic required investments, common failure modes, and observable signals of successful transition. The transitions are not reversible in a practical sense: once a team builds automation, they rarely dismantle it to go back to Documented unless something catastrophic happens. But transitions CAN fail, which means the team stays on the lower rung with some scaffolding of the higher rung that is not yet load-bearing.

#### Manual → Documented

- **Required investments.** Time to write the SOP (typically 4-20 hours per SOP depending on complexity), a named author, a non-author reviewer to validate that the SOP is executable without asking the author, and a commitment to maintain the SOP as the process changes.
- **Common failure modes.**
  - **Write-once syndrome.** The SOP is written, stored in a wiki, and then never updated; six months later, it is wallpaper.
  - **Author capture.** The author writes the SOP for themselves, leaving tribal context implicit; a non-author still cannot execute it.
  - **Fake structure.** The SOP uses a template but fills in "see author" or "TBD" for half the fields; it looks Documented but is functionally Manual.
  - **Wrong grain.** The SOP is too abstract ("operate the fulfillment pipeline") or too granular ("click button X, then button Y"); neither serves a non-author executor.
- **Successful transition signals.** A non-author executes the SOP end-to-end without asking the author a clarifying question. The audit checklist in the Agent-Ready SOP Schema section passes all 10 items. The SOP has a last-reviewed date within the past 90 days.

#### Documented → Automated

- **Required investments.** A workflow engine, an event bus or scheduler, observability, idempotency key design, and engineering time to build and maintain the automation. Typically 10-50x the cost of writing the Documented SOP; this is the most expensive transition on the ladder.
- **Common failure modes.**
  - **Automation island.** Some steps are automated and others are manual, but the handoffs are not; the automation runs halfway and then stalls waiting for a human who does not know they are the bottleneck.
  - **Happy-path only.** The automation handles the common case but every named exception still routes to a human; over time, the human ends up handling most runs because the exception mix shifts.
  - **Observability debt.** The automation runs but no dashboard shows its state; when something fails, the team is blind.
  - **Idempotency miss.** Re-running a step double-processes something (double-ship, double-charge, double-notify); the team loses trust and reverts to manual execution.
  - **Skipping Documented.** The team tries to jump from Manual directly to Automated without a Documented intermediate. The automation is built against tribal knowledge that was never written down, so it encodes the wrong process.
- **Successful transition signals.** Every step's `owner` field names code or a workflow actor. Verification test runs every run. Evidence trail is written automatically. Humans are paged only for decisions and unresolved exceptions. Run-to-run variance on execution drops to near-zero for the steps that were automated.

#### Automated → Agentic

- **Required investments.** An agent runtime with confidence scoring, machine-readable decision criteria for each decision in scope, a named human tiebreaker role per decision class, and an accountability model that survives the shift from human decider to agent decider. This is conceptually harder than it is expensive — the tooling is cheap, the thinking is not.
- **Common failure modes.**
  - **Criterion underspecification.** The team writes a criterion that "sounds right" but is not machine-evaluable; the agent cannot decide and escalates everything.
  - **Confidence illusion.** The confidence score is a number the agent emits with no calibration; the team treats it as meaningful and sets thresholds against it without evidence that it correlates with correctness.
  - **Tiebreaker vacuum.** No human tiebreaker is named, or the named tiebreaker is not actually available; the agent's escalations queue indefinitely.
  - **Accountability gap.** When the agent decides wrong, nobody owns the outcome; the team's post-mortem concludes "the agent was wrong" without a remediation plan.
  - **Premature Agentic.** The decision criteria are still evolving week-to-week, so codifying them into a machine-readable form is a moving target; the agent is built on shifting ground and its accuracy decays as the criteria change.
- **Successful transition signals.** At least one `decision_rights.steps[].decider` names an agent role with a machine-evaluable criterion. Verification test runs every run. A human tiebreaker is named per decision class and is actually paged (and responds within SLA) when confidence is low. Post-mortems on agent-wrong decisions produce criterion updates, not hand-wringing.

### Rung-Assignment Questions (Audit Shortcut)

When a process engineer has an SOP in hand and needs to assign it to a rung, these five questions, asked in order, produce the rung assignment. Each question is answered from the SOP document alone.

1. **Are all 7 fields present as top-level keys in the SOP?** If NO → **Manual**. Stop.
2. **Does each step have an owner, an imperative action, and an observable completion signal?** If NO → **Manual**. Stop.
3. **Is `steps[].owner` a code actor (workflow, cron, webhook worker) on the majority of steps?** If NO → **Documented**. Stop.
4. **Does `decision_rights.steps[].decider` name an agent role with a machine-evaluable criterion on at least one decision?** If NO → **Automated**. Stop.
5. **Does `verification_test` have a named human tiebreaker for edge cases AND does at least one `exception_handling[].branch` name the agent as recovery-path decider?** If YES → **Agentic**. If NO → **Automated** (with Agentic scaffolding that is not yet load-bearing).

This shortcut is an audit tool, not a replacement for the full per-rung detail above. A rung assignment from this shortcut is a hypothesis; the full audit checklist in the Agent-Ready SOP Schema section is the validator. When the shortcut and the full checklist disagree, the full checklist wins.

### Rung Is Per-SOP, Not Per-Team

A team is not "at" a rung. Individual SOPs are at a rung. A single team commonly runs SOPs at three different rungs simultaneously — a Manual SOP for quarterly board prep (low volume, high judgment, no reason to document), a Documented SOP for customer onboarding (mid volume, human-driven, well-specified), and an Automated SOP for order fulfillment (high volume, low variance, code-driven). The ladder is a per-SOP measurement, not a team scoreboard.

When a team is asked "what rung are you at," the honest answer is a distribution across SOPs, not a single number. Collapsing the distribution to a single rung is almost always marketing, not measurement. The exception: when a team owns a single process and that process has a single SOP, the team's rung is the SOP's rung — but that is a special case, not the default.

The implication for rung selection: the right rung for an SOP is not "the highest rung we can reach" — it is the rung whose cost-of-authoring and cost-of-maintenance are repaid by the SOP's volume, variance, and stakes. A low-volume, high-judgment SOP that would cost considerable engineering time to make Agentic and saves only a handful of hours per year in human decision time should stay Documented. Moving it higher is waste dressed up as rigor. The ladder's job is to classify what is, not to push every SOP toward Agentic by default.

### Anti-Patterns

These are the maturity ladder failures I have observed or can anticipate from the schema. Each is a way teams trick themselves (or their auditors) into believing they are at a higher rung than they actually are.

1. **Claiming a rung without populating the 7 fields that prove it.** A team declares "we are Documented" without the `decision_rights` field populated with named roles and criteria. The rung claim fails the audit checklist. Rule: a rung is claimed by the SOP, not by the team, and the SOP is audited against the 7 fields.

2. **Treating tooling as the rung.** Buying a workflow engine does not make you Automated if your `steps[].owner` fields still name humans. The tooling is necessary but not sufficient. A team with n8n installed but no SOPs running through it is still Documented (at best). Rule: tooling is the enabler, the populated SOP is the evidence.

3. **Skipping a rung.** A team tries to go Manual → Automated without a Documented intermediate. The automation encodes tribal knowledge that was never written down, so it encodes the wrong process. When the automation fails, the team has no document to fall back on. Rule: each rung is a prerequisite for the next; skipping is allowed only if the skipped rung is explicitly and honestly documented as "we know we are not at this rung and we accept the risk."

4. **Declaring Agentic because an LLM is somewhere in the loop.** An LLM generating log summaries does not make the process Agentic; an LLM summarizing inputs for a human decider does not make the process Agentic. Agentic means the agent is named in `decision_rights.steps[].decider` and the criterion is machine-evaluable. Anything else is Automated with LLM sprinkles. Rule: the rung is determined by where the decision lives, not by where the LLM lives.

5. **Aspirational scoring.** A team scores where they want to be, not where they are. The fix is structural: score against observable signals from the SOP document alone, with a non-author auditor, and reject any justification that starts with "well, when this is fully rolled out…" Rule: the ladder reads what is, not what will be.

6. **Rung claim by analogy.** A team says "we are at least Documented because our SOPs look structured" without running the audit checklist. Looking structured is not being structured. Rule: the 10-item audit checklist is the rung gate, not the format of the document.

7. **Collapsing the 7 fields into narrative.** A team writes a beautiful prose SOP that covers all 7 concerns but does not declare them as separate fields. The SOP reads Documented but audits Manual, because a non-author cannot extract the fields. Rule: fields are first-class keys in the schema, not narrative threads in the prose.

### Integration with C2.4 Agent-Ready SOP Schema

The maturity ladder and the 7-field schema are the same tool seen from two angles. The 7 fields are the invariant — every SOP at every rung has them. The ladder describes how FULLY each field is codified and whether execution/decision is human or machine.

- **Manual** = fewer than 3 of 7 fields codified, or fields exist only as prose with tribal content.
- **Documented** = all 7 fields populated in structured form per the schema; `steps[].owner` names humans; `decision_rights.steps[].decider` names humans; the SOP passes all 10 items of the audit checklist with human owners and human deciders.
- **Automated** = all 7 fields populated per the schema; `steps[].owner` names code or workflow actors; `decision_rights.steps[].decider` still names humans; verification runs every run automatically.
- **Agentic** = all 7 fields populated per the schema; `decision_rights.steps[].decider` names agent roles with machine-evaluable criteria; `verification_test` has a named human tiebreaker per decision class; at least one `exception_handling[].branch` names the agent as recovery-path decider.

The canonical pointer: **"Agent-ready" in the C2.4 schema corresponds to Documented or higher on this ladder.** A Manual SOP is not agent-ready because its fields are implicit — no agent (human or machine) can execute it without asking the author. A Documented SOP is agent-ready for human agents. An Automated SOP is agent-ready for code. An Agentic SOP is agent-ready for agents that also decide.

### Integration with C2.5 Financial Modeling Rubric

The C2.5 rubric (authored by @fpa-analyst) scores financial-control SOPs across 7 dimensions. Dimension 6 is **Internal Consistency** — the foot-and-tie check across independent sources. The maturity ladder and dimension 6 interact directly: foot-and-tie is automated at higher rungs, eyeballed at lower rungs, and the rung determines how much weight the foot-and-tie verdict can carry.

- **Manual** financial-control SOPs cannot pass C2.5 dimension 6 in any defensible form. "Spot-check" and "the controller reviews" are not foot-and-tie checks. A Manual financial-control SOP fails C2.5.
- **Documented** financial-control SOPs can pass dimension 6 if the `verification_test.criterion` declares a three-way (or more) reconciliation with a named tolerance and a human runner. The human runner actually executing the check is the risk — but the SOP itself is structurally capable of passing.
- **Automated** financial-control SOPs pass dimension 6 more robustly because the foot-and-tie runs on every run without human prompting. The risk shifts from "did the human run the check" to "did the check catch the right thing."
- **Agentic** financial-control SOPs add a named human tiebreaker for edge cases where the automated foot-and-tie verdict is ambiguous (e.g., variance within the tolerance band but with unexplained source breakdown). The tiebreaker is the escape valve that prevents the automation from silently approving bad runs.

**Canonical pointer:** financial-control SOPs at Documented or higher can pass C2.5 dimension 6. Financial-control SOPs at Manual cannot. The AXIA MRR Reconciliation SOP above is a Documented-level financial-control SOP whose verification test is a three-way foot-and-tie; moving it to Automated means running the foot-and-tie on every cron fire without the @fpa-analyst prompting it; moving it to Agentic means an agent role investigates variances and escalates to the @cfo tiebreaker only when its confidence is below threshold.

### Integration with `/compliance-audit`

Regulatory frameworks that require "repeatable, documented, tested" controls — SOC 2, ISO 27001, SOX, many privacy frameworks — implicitly require at LEAST the Documented rung of this ladder. A Manual SOP cannot satisfy them because "documented" means structured content a non-author can audit, and "tested" means a named verification test with a pass/fail criterion.

The `/compliance-audit` skill relies on this pointer: when it assesses whether a control is audit-ready, it asks "does the control's SOP sit at Documented or higher on the process engineering maturity ladder?" If yes, the control is a candidate for audit readiness (subject to the other dimensions the skill assesses). If no, the control fails audit readiness regardless of how compelling the prose around it is. This is the reason the ladder is load-bearing for the compliance skill: the ladder provides the observable rung boundary, and the compliance skill consumes the boundary as a gate.

Higher rungs carry stronger audit arguments — Automated SOPs make "repeatable" trivially true because the runtime enforces repetition; Agentic SOPs need extra audit attention because auditors are (rightly) skeptical of agent-driven decisions and want to see the confidence-threshold / human-tiebreaker design. Higher is not always better for audits; the right rung is the one that maps the control's risk to the right evidence strength.

### Dropped Rungs Footnote

Rungs that did not survive decomposition:

- **Standardized** (commonly placed between Documented and Automated in public frameworks). Dropped because its observable signals — "structured schemas," "enforced across runs," "policy-level adherence" — are identical to Documented when you audit the SOP alone. The difference Standardized tries to capture (enforcement, consistency over time, culture of adherence) is not observable from the SOP document; it is observable only from runtime, audit logs, and organizational behavior, none of which the ladder audits. When a team claims Standardized, they are almost always claiming "we are Documented AND we actually follow the SOPs," which is a runtime claim, not a rung claim. Collapsed into Documented.

- **Level 0 / Ad Hoc** (a pre-Manual rung where no SOP exists at all). Dropped because it is the absence of a process, not a rung. If there is no SOP, there is nothing for the ladder to audit; calling the absence a "rung" is wallpaper. If a team says "we are Ad Hoc" the honest read is "we do not have an SOP for this process," which is a scoping conversation, not a maturity scoring.

- **Level 5 / Fully Autonomous** (a hypothetical above-Agentic rung where no human is involved at all). Dropped because no observable signal distinguishes it from Agentic at the SOP level. "The human is not involved" is a property of the decision class, not a rung. If a decision class does not need a human tiebreaker, the SOP simply does not name one — that is still Agentic on this ladder. Adding a fifth rung for this would reward teams for removing humans regardless of whether the removal was warranted, which is the wrong incentive.

Four rungs survived: Manual, Documented, Automated, Agentic. Each has a detectable observable signal from the SOP artifact alone. Each has an honest integration story with C2.4, C2.5, and `/compliance-audit`. The ladder is a measurement device, not a motivational poster.

---

## Process Library Index

*(Content pending — this section will enumerate the standard operational processes maintained by the Operations Team, each linked to its SOP authored against the schema above.)*

## Onboarding Checklists

*(Content pending — operational onboarding checklists for new team members, authored as SOPs.)*

## Vendor Runbooks

*(Content pending — vendor-specific runbooks for recurring procurement and vendor management activities, authored as SOPs.)*

---

> "A playbook that works only when the author is in the room is not a playbook. It's an apprenticeship."
