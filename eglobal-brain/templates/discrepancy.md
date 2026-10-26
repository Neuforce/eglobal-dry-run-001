<!--
PURPOSE:     One record per non-✅ match. Gives humans everything they need to decide.
OWNER:       Agent drafts · Alejandra + Tech Lead decide
CONSUMED BY: audit-report, validated-asis, write-prd
FILE:        04-audit/output/discrepancies/DISC-<PROC>-###.md
-->
# DISC-<PROC>-###: <short title>

- **Category:** ⚠️ Drift | 🕳️ Undocumented | 👻 Orphan | ❓ Ambiguous
- **Process / step:** P-XXX / <step>
- **Impact:** H | M | L. <!-- why it matters: money, compliance, customer, ops -->

## Evidence
| Source | KU | Says | Citation |
|---|---|---|---|
| Legacy | KU-LEG-… | | |
| As-Is | KU-ASIS-… | | |
| Code | KU-CODE-… | | |

## Analysis (agent)
<!-- What differs, possible explanations (runtime config, other system, obsolete doc…) -->

## Recommendation (agent, non-binding)
<!-- e.g. "Code looks authoritative; update the As-Is doc" -->

## Decision (humans)
- **Decision:** docs are right | code is right | both wrong (truth = …) | out of scope | needs investigation
- **Truth statement:** <the rule as it should appear in the validated As-Is>
- **Follow-up:** update doc / backlog item for To-Be / investigate
- **Decided by:** <names> · **Date:** · **Ref:** decision-log#<entry>
