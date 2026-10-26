# Knowledge Schema

> **🟩 METHOD — NeuForce standard.** Review optional; propose changes via PR. **Owner:** NeuForce

## Knowledge Unit (KU)
The atomic unit. One business fact per KU. The format is the same for docs and code, which is what makes them comparable.

| Field | Required | Description |
|---|---|---|
| `id` | ✔ | `KU-<LEG\|ASIS\|CODE>-<PROC>-<###>` |
| `process` | ✔ | Process ID from `00-context/process-inventory.md` |
| `step` | ✔ | The step or sub-process it belongs to |
| `type` | ✔ | `validation` · `calculation` · `routing` · `authorization` · `state-transition` · `integration` · `data-entity` · `timing/SLA` · `exception-handling` |
| `statement` | ✔ | One sentence, in business language: "When X, the system Y" |
| `source` | ✔ | Citation (see `AGENTS.md` §6) |
| `excerpt` | ✔ | ≤ 3 lines, verbatim |
| `confidence` | ✔ | `H` (explicit), `M` (inferred from clear evidence), `L` (weak or partial) |
| `status` | ✔ | `proposed` · `approved` · `corrected` · `rejected` · `needs-source` |
| `glossary_terms` | | Domain terms used (help matching) |
| `related` | | Other KU IDs |
| `reviewer` | | Who reviewed it, and when |

## Discrepancy taxonomy (Phase 4)
| Icon | Category | Definition | Typical action |
|---|---|---|---|
| ✅ | Confirmed | The same rule appears in the docs and the code | None. It goes to the validated As-Is |
| ⚠️ | Drift | It appears in both but they differ | A human decides which one is true; the docs or the backlog get updated |
| 🕳️ | Undocumented | In the code, not in any doc | Document it; check whether it's intended |
| 👻 | Orphan | In the docs, not found in the code | Obsolete, not built, or lives in another system? |
| ❓ | Ambiguous | The evidence is unclear or incomplete | SME decision |

## Matching rules
1. Match on `process` + `step` + `type` first, then on statement meaning.
2. Use `00-context/domain-glossary.md` synonyms (e.g. business term ↔ code identifier).
3. One KU may match several on the other side; record all of them in the matrix.
4. Never mark ✅ on meaning alone when the numbers, thresholds, or conditions differ. That is ⚠️.
