# SPIKE-001: Validation Process for P-REV Reverso por timeout del emisor

> **🟨 ASSUMPTION — dry-run 001.** Generado en automático el 2026-10-24. Las compuertas humanas se omiten a propósito. Esto no es una aprobación.

## 1. Goal
Probar la cadena completa del método con un proceso ficticio, de punta a punta, sin compuertas humanas.

## 2. Scope
- **Process(es):** P-REV (pasos 1 a 4)
- **Out of scope:** cualquier proceso real de eGlobal
- **Sources:** SRC-01 (legacy), SRC-02 (as-is)
- **Repos / modules:** dry-run-legacy → legacy-readonly/switch_core/reversal.py

## 3. Strategy
- [x] docs→code
- **Why:** el As-Is ficticio está estructurado y el módulo cabe en un archivo.

## 4. Steps
| # | Step | Skill | Output | Gate |
|---|---|---|---|---|
| 1 | Legacy extraction | ingest-legacy-docs | 01-legacy/output/knowledge/P-REV.md | omitida |
| 2 | As-Is extraction | ingest-asis-docs | 02-asis/output/knowledge/P-REV.md | omitida |
| 3 | Code extraction | extract-code-rules | 03-code/output/knowledge/P-REV.md | omitida |
| 4 | Cross-reference | cross-reference | matrix + DISC | omitida |
| 5 | Joint review | review-gate | decision-log | omitida: decide el script |
| 6 | Audit report | audit-report | validated-asis/P-REV.md | omitida |
| 7 | Spec OpenSpec | write-prd / write-sdd | 05-spec/CAP-001-reverso-timeout/ y openspec/ | omitida |
| 8 | PoC | plan-poc / build-poc / poc-findings | 06-poc/POC-001-reverso-timeout/ | omitida |

## 5. Sampling and acceptance
- Sample size per gate: no hay muestra humana
- Accuracy threshold: no aplica en este dry run

## 6. Risks and assumptions
| Risk / assumption | Mitigation |
|---|---|
| Las reglas se extraen de bloques `rule`, no de prosa libre | El extracto citado tiene que aparecer verbatim en el documento o en el código |

## 7. Timebox
- Start: 2026-10-24 · Target G4: 2026-10-24

## 8. Retrospective (fill at the end)
La cadena corre en un script. No sustituye al agente ni a las compuertas.
