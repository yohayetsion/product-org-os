# Decision Class Registry (Sidecar for `/decision-quality-audit`)

**Owner**: `/decision-quality-audit` skill (Path (b) sidecar registry, per V5.1-37 schema audit 2026-05-02).
**Purpose**: Map `/decision-record` IDs (DR-YYYY-NNN) to a `decision_class` value used by the Decision Improvability dimension. The registry is read at audit time and updated by the auditor; the v5.0 `/decision-record` schema is not amended.
**Why a sidecar (not a schema extension)**: The pre-execution schema audit (`H.5-V5.1-37-decision-record-schema-audit-2026-05-02.md`) confirmed `decision_class` is absent from the v5.0 `/decision-record` schema and from `context/index.json`. Path (b) preserves R-018 (zero v5.0 surface amendment) and absorbs the data dependency entirely inside `/decision-quality-audit`'s own scope.

---

## Registry shape

The registry is a single JSON object keyed by Decision ID. Each entry carries a `decision_class` value, the actor who classified the record, the classification date, and an optional rationale.

```json
{
  "registry_version": "1.0",
  "owner_skill": "decision-quality-audit",
  "schema_extension_avoided": true,
  "last_updated": "YYYY-MM-DD",
  "entries": {
    "DR-YYYY-NNN": {
      "decision_class": "strategic-bet | portfolio-tradeoff | execution-call | hire | vendor | pricing | partnership | other",
      "classified_by": "auditor | author",
      "classified_date": "YYYY-MM-DD",
      "rationale": "Optional one-line reason for the class assignment"
    }
  }
}
```

## Recommended class taxonomy

The auditor classifies each decision into one of the following classes. The taxonomy is deliberately narrow (eight values) to keep the trajectory analysis statistically meaningful — too many classes and each class has too few records to detect a trend.

| Class | What it covers | Typical decision examples |
|---|---|---|
| `strategic-bet` | A decision committing the organization to a multi-quarter direction with explicit assumptions and a re-decision trigger. Output of `/strategic-bet`. | "Build vs. buy CRM"; "Enter EU market in Q3"; "Replatform to event-driven architecture" |
| `portfolio-tradeoff` | A decision allocating finite resources across competing investments. Output of `/portfolio-tradeoff`. | "Fund Initiative A at the cost of Initiative B"; "Sunset Product X to free engineering for Product Y" |
| `execution-call` | A delivery-time decision inside an already-committed initiative. Scope, timing, or sequencing. | "Cut feature Z from the next release"; "Delay the migration by two weeks"; "Launch in market A first, then B" |
| `hire` | A hiring decision at a level that requires explicit deliberation (typically Director and above, or a critical IC role). | "Hire Director of Data"; "Hire VP Engineering external vs. internal promotion" |
| `vendor` | A decision selecting or replacing a strategic vendor or service provider above a meaningful spend threshold. | "Select cloud provider"; "Replace customer support platform"; "Sign with security-monitoring vendor" |
| `pricing` | A decision changing list price, discounting policy, packaging, or commercial terms. | "Move from per-seat to consumption-based pricing"; "Discontinue the free tier"; "Set the enterprise floor at $50k" |
| `partnership` | A decision entering, restructuring, or exiting a strategic partnership or channel relationship. | "Sign reseller agreement with Partner Z"; "Exit OEM partnership"; "Move from co-sell to resell motion" |
| `other` | Decisions that do not cleanly map to the seven classes above. Useful for one-off or unique decisions. | One-off restructures, governance changes, brand decisions, etc. |

If the registry's `other` bucket grows above ~20% of audited decisions, the taxonomy itself should be revisited (in a v6.0 RFC) — that's the signal that the eight-class shape is too narrow for this organization.

## Auditor classification flow (used by `/decision-quality-audit`)

1. `/decision-quality-audit` walks `context/decisions/` and enumerates all DR-YYYY-NNN records in scope.
2. For each record, the skill reads this registry and looks up the entry under `entries.DR-YYYY-NNN`.
3. If the entry exists → use its `decision_class` value for the Decision Improvability dimension.
4. If the entry does not exist → during the audit run, the skill presents the auditor with a short summary of the record (the Decision section + the Decision Drivers section) and the recommended taxonomy above. Auditor picks a class. Skill writes the entry back to the registry with `classified_by: "auditor"`, `classified_date` = today, and any rationale the auditor provides.
5. The registry persists across audits. The next audit reads classifications from previous audits without re-prompting.
6. Auditors may override a previous classification by editing the registry directly. The change carries a new `classified_date`. Best practice: leave a one-line rationale for the change.

## Why the registry is in this folder

The registry is owned by `/decision-quality-audit` and lives entirely inside its skill folder, which means:
- Other skills cannot accidentally read or write the registry (no cross-skill coupling).
- The R-018 attestation holds: v5.0 surface (the `/decision-record` schema, `context/index.json`) is not amended.
- A future v6.0 RFC could promote the sidecar into a `decision_class` field on `/decision-record` if usage proves the taxonomy stable. That is a v6.0 architectural conversation, not a v5.1 one.

## Empty-registry initial state

When the skill ships, the registry is empty:

```json
{
  "registry_version": "1.0",
  "owner_skill": "decision-quality-audit",
  "schema_extension_avoided": true,
  "last_updated": "2026-05-02",
  "entries": {}
}
```

The first audit run populates entries as the auditor classifies decisions inline. Subsequent audits read what's there and only prompt for newly added DR-YYYY-NNN records.
