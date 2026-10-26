# Templates

> **🟩 METHOD — NeuForce standard.** Review optional; propose changes via PR. **Owner:** NeuForce

Skills copy these templates. Agents must never invent a different format. Every template starts with a header comment that says what it is for, who owns it, and who consumes it.

| Template | Used by skill | Produces |
|---|---|---|
| `validation-process.md` | design-validation-process | `04-audit/spikes/SPIKE-###/validation-process.md` |
| `inventory.md` | ingest-legacy-docs, ingest-asis-docs | `0[12]-*/output/inventory.md` |
| `knowledge-unit.md` | ingest-*, extract-code-rules | `*/output/knowledge/<P-PROC>.md` |
| `legacy-delta.md` | ingest-asis-docs | `02-asis/output/legacy-delta.md` |
| `code-map.md` | extract-code-rules | `03-code/output/code-map.md` |
| `discrepancy.md` | cross-reference | `04-audit/output/discrepancies/DISC-*.md` |
| `review-log-entry.md` | review-gate | `*/review/*-log.md` |
| `validated-asis.md` | audit-report | `04-audit/output/validated-asis/<P-PROC>.md` |
| `audit-report.md` | audit-report | `04-audit/output/audit-report.md` |
| `prd.md` | write-prd | `05-spec/CAP-*/prd.md` |
| `sdd.md` | write-sdd | `05-spec/CAP-*/sdd.md` |
| `subprocess-AGENTS.md` | write-sdd | `05-spec/CAP-*/AGENTS.md` |
| `poc-plan.md` | plan-poc | `06-poc/POC-*/poc-plan.md` |
| `poc-findings.md` | poc-findings | `06-poc/POC-*/findings.md` |
| ADR | solution-architect | `00-context/architecture/adr/ADR-000-template.md` |
