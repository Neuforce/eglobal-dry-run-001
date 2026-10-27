#!/usr/bin/env python3
"""Dry-run 001 de SPIKE-001.

Recorre la cadena del método sin compuertas humanas: documentos y código
ficticios entran, y salen unidades de conocimiento, matriz, As-Is validado,
auditoría, PRD, SDD y el PoC de dos contenedores.

No aprueba nada. Las decisiones de este corrido quedan marcadas como
automáticas de dry-run 001.
"""

from __future__ import annotations

import csv
import io
import re
import subprocess
import sys
import textwrap
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent
BRAIN = ROOT / "eglobal-brain"
LEGACY_CODE = ROOT / "legacy-readonly" / "switch_core" / "reversal.py"
DATE = "2026-10-24"
SHA = "dry-run-001"
PROC = "P-REV"
PROC_NAME = "Reverso por timeout del emisor"
BANNER = (
    "> **🟨 ASSUMPTION — dry-run 001.** Generado en automático el "
    f"{DATE}. Las compuertas humanas se omiten a propósito. Esto no es una aprobación."
)

RULE_FENCE = re.compile(r"```rule\n(.*?)```", re.S)
CODE_BLOCK = re.compile(r"# --- rule ---\n(.*?)# --- end ---\n", re.S)


def parse_kv(body: str) -> dict:
    data = {}
    for line in body.splitlines():
        line = line.strip()
        if line.startswith("#"):
            line = line[1:].strip()
        if not line or ":" not in line:
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip()
    return data


def line_of(text: str, excerpt: str) -> int:
    for number, line in enumerate(text.splitlines(), start=1):
        if excerpt in line:
            return number
    raise SystemExit(f"No está el extracto en la fuente: {excerpt}")


def parse_docs(path: Path, corpus: str) -> list[dict]:
    text = path.read_text(encoding="utf-8")
    rules = []
    for match in RULE_FENCE.finditer(text):
        rule = parse_kv(match.group(1))
        rule["corpus"] = corpus
        rule["path"] = path.name
        rule["line"] = line_of(text, rule["excerpt"])
        rules.append(rule)
    return rules


def parse_code(path: Path) -> list[dict]:
    text = path.read_text(encoding="utf-8")
    rules = []
    for match in CODE_BLOCK.finditer(text):
        rule = parse_kv(match.group(1))
        rule["corpus"] = "code"
        rule["path"] = str(path.relative_to(ROOT))
        rule["line"] = line_of(text, rule["excerpt"])
        rules.append(rule)
    return rules


def assign_ids(rules: list[dict], kind: str) -> None:
    for index, rule in enumerate(rules, start=1):
        rule["id"] = f"KU-{kind}-REV-{index:03d}"


def citation(rule: dict) -> str:
    if rule["corpus"] == "code":
        return f"code:{rule['path']}:{rule['line']}@{SHA}"
    return f"doc:{rule['path']}#{rule['section']}"


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.rstrip() + "\n", encoding="utf-8")
    print(f"escribió {path.relative_to(ROOT)}", flush=True)


def ku_markdown(title: str, spike_sources: str, summary: str, rules: list[dict]) -> str:
    blocks = []
    for rule in rules:
        blocks.append(
            textwrap.dedent(
                f"""
                ### {rule['id']}
                - **step:** {rule['step']}
                - **type:** {rule['type']}
                - **statement:** {rule['statement']}
                - **source:** {citation(rule)}
                - **excerpt:**
                  > {rule['excerpt']}
                - **confidence:** {rule['confidence']}
                - **status:** proposed
                - **glossary_terms:** {rule['terms']}
                - **related:**
                - **reviewer:** dry-run 001 automático, {DATE}
                """
            ).strip()
        )
    return (
        f"# {title}\n\n{BANNER}\n\n"
        f"- **Spike:** SPIKE-001\n"
        f"- **Generated:** {DATE} by run-dry-run-001.py\n"
        f"- **Sources processed:** {spike_sources}\n\n"
        f"## Summary\n{summary}\n\n"
        f"## Knowledge Units\n\n" + "\n\n".join(blocks) + "\n"
    )


def classify(by_match: dict[str, dict[str, dict]]) -> list[dict]:
    rows = []
    for key in sorted(by_match):
        sides = by_match[key]
        docs = [sides[name] for name in ("legacy", "asis") if name in sides]
        code = sides.get("code")
        statements = {item["statement"] for item in list(docs) + ([code] if code else [])}
        if code and not docs:
            category = "undocumented"
        elif docs and not code:
            category = "orphan"
        elif len(statements) == 1:
            category = "confirmed"
        else:
            category = "drift"
        rows.append({"match": key, "sides": sides, "category": category})
    return rows


def truth_for(row: dict) -> tuple[str, str, str]:
    """Devuelve decisión, enunciado de verdad y seguimiento. Solo dry-run."""
    sides = row["sides"]
    if row["category"] == "confirmed":
        statement = next(iter(sides.values()))["statement"]
        return "n/a", statement, "n/a"
    if row["category"] == "drift":
        statement = sides["code"]["statement"]
        return (
            "code is right",
            statement,
            "El To-Be deja el timeout configurable por emisor; el valor por defecto sale del código (25 s).",
        )
    if row["category"] == "orphan":
        return (
            "out of scope",
            "",
            "No entra al As-Is validado ni al slice del PoC. Queda como hueco para el siguiente spike.",
        )
    return (
        "needs investigation",
        "",
        "Está en el código y no en los documentos. No se promueve a regla validada en este dry run.",
    )


def main() -> int:
    legacy = parse_docs(
        BRAIN / "01-legacy/input/raw/LEG-REV-proceso-reverso.md", "legacy"
    )
    asis = parse_docs(
        BRAIN / "02-asis/input/raw/ASIS-REV-proceso-reverso.md", "asis"
    )
    code = parse_code(LEGACY_CODE)
    assign_ids(legacy, "LEG")
    assign_ids(asis, "ASIS")
    assign_ids(code, "CODE")

    by_match: dict[str, dict[str, dict]] = defaultdict(dict)
    for rule in legacy + asis + code:
        by_match[rule["match"]][rule["corpus"]] = rule
    rows = classify(by_match)

    decisions = []
    disc_number = 1
    for row in rows:
        decision, truth, follow = truth_for(row)
        row["decision"] = decision
        row["truth"] = truth
        row["follow"] = follow
        if row["category"] == "confirmed":
            row["disc_id"] = ""
            row["decision_ref"] = ""
            continue
        disc_id = f"DISC-REV-{disc_number:03d}"
        decision_id = f"D-{disc_number:03d}"
        disc_number += 1
        row["disc_id"] = disc_id
        row["decision_id"] = decision_id
        row["decision_ref"] = f"decision:04-audit/review/decision-log.md#{decision_id}"
        decisions.append(row)

    write_context()
    write_phase0()
    write_knowledge(legacy, asis, code)
    write_delta(legacy, asis)
    write_code_map(code)
    write_matrix(rows)
    write_discrepancies(rows)
    write_decision_log(decisions)
    write_validated(rows)
    write_audit(rows, legacy, asis, code)
    write_spec(rows)
    poc = write_poc()
    test_code = run_tests(poc)
    write_findings(test_code)
    write_status()
    print(f"pruebas_exit:{test_code}")
    return test_code


def write_context() -> None:
    write(
        BRAIN / "00-context/process-inventory.md",
        f"""# As-Is Process Inventory

{BANNER}

| Process ID | Name | Description (1 line) | Owner | Legacy docs? | New As-Is doc? | Main repo(s) | Criticality (H/M/L) | Size (S/M/L) | Spike candidate? |
|---|---|---|---|---|---|---|---|---|---|
| P-REV | {PROC_NAME} | El switch dispara un reverso si el emisor no responde a tiempo | dry-run | Y | Y | dry-run-legacy | M | S | Y — SPIKE-001 |
""",
    )
    write(
        BRAIN / "00-context/sources.md",
        f"""# Documentation Sources Manifest

{BANNER}

| Source ID | Type | Corpus (legacy / as-is) | Location (space, project, folder, URL) | Access | Processes covered | Last updated | Owner | Classification |
|---|---|---|---|---|---|---|---|---|
| SRC-01 | Markdown ficticio | legacy | 01-legacy/input/raw/LEG-REV-proceso-reverso.md | file:01-legacy/input/raw/LEG-REV-proceso-reverso.md | P-REV | 2019-04-12 | dry-run | ficticio |
| SRC-02 | Markdown ficticio | as-is | 02-asis/input/raw/ASIS-REV-proceso-reverso.md | file:02-asis/input/raw/ASIS-REV-proceso-reverso.md | P-REV | 2026-09-01 | dry-run | ficticio |
""",
    )
    write(
        BRAIN / "00-context/repos.md",
        f"""# Code Repositories Manifest

{BANNER}

El código ficticio vive fuera del cerebro, en `legacy-readonly/`, y este corrido solo lo lee.

## Repositories
| Repo (org/name) | Branch / tag to analyze | Language / framework | Purpose | In scope? | Owner |
|---|---|---|---|---|---|
| dry-run-legacy | {SHA} | Python | Switch ficticio de reverso | Y | dry-run |

## Module ↔ process mapping
| Process ID | Repo | Paths / packages / modules | Entry points (API, batch job, queue consumer, UI) | Notes |
|---|---|---|---|---|
| P-REV | dry-run-legacy | legacy-readonly/switch_core/reversal.py | función `dispara_reverso` | Solo lectura |

## Exclusions
Ninguno en este dry run.
""",
    )
    write(
        BRAIN / "00-context/domain-glossary.md",
        f"""# Domain Glossary (business ↔ code)

{BANNER}

| Business term (ES) | Definition | Synonyms / acronyms | Code identifiers (classes, tables, fields) | Status |
|---|---|---|---|---|
| emisor | Institución que autoriza la transacción | issuer | EMISORES_AUTORIZADOS, ISSUER_TIMEOUT_S | proposed |
| adquirente | Destino del reverso | acquirer | DESTINO_REVERSO | proposed |
| reverso | Devolución automática de la transacción | reversal | dispara_reverso | proposed |
| timeout | Segundos de espera al emisor | tiempo de espera | ISSUER_TIMEOUT_S | proposed |
| cola manual | Bandeja de operaciones si el reverso falla | cola | — | proposed |
""",
    )
    write(
        BRAIN / "00-context/architecture/standards.md",
        f"""# Engineering Standards

{BANNER}

Valores de relleno para que el PoC de dry-run 001 pueda construirse. No son el estándar de eGlobal.

| Area | Standard |
|---|---|
| Languages and versions | Python 3.12 |
| Frameworks | Biblioteca estándar (http.server) |
| API style and spec format (REST/OpenAPI, gRPC, AsyncAPI) | HTTP JSON, sin OpenAPI en este slice |
| Naming conventions | IDs en inglés, mensajes de negocio en español |
| Error handling | Respuesta JSON con `error` y código HTTP 4xx |
| Logging format | `level=INFO msg=...` a stdout |
| Testing (frameworks, coverage expectations) | unittest, un caso por AC del slice |
| Dependency policy (approved libs, registries) | Sin dependencias de terceros |
| Code style / linters | No aplica en el dry run |
| Branching and PR rules | No aplica: esta carpeta no es un clon git |
""",
    )
    write(
        BRAIN / "00-context/architecture/platform-openshift.md",
        f"""# Platform: OpenShift

{BANNER}

| Item | Value |
|---|---|
| OpenShift version | no provisto; el dry run no despliega |
| Cluster / environment for PoCs | local (Podman o Docker), mismos Containerfile |
| Namespace / project | dry-run-001 |
| Who can deploy (service account, RBAC) | nadie en este corrido |
| Approved base images (UBI? versions) | no provisto; el PoC usa `python:3.12-slim` y lo anota como desviación |
| Image registry | local |
| Build method (S2I / Containerfile + pipeline / local build + push) | Containerfile |
| CI/CD (Tekton/OpenShift Pipelines, ArgoCD/GitOps, Jenkins, GitHub Actions) | no |
| Ingress (Routes, TLS policy) | Route de ejemplo, sin TLS |
| Secrets management (Secrets, Vault, Sealed Secrets) | Secret de ejemplo, valor ficticio |
| Config (ConfigMaps conventions) | ConfigMap `poc-001-reverso-config` |
| Resource quotas / limits per pod | requests 50m/64Mi, limits 200m/128Mi |
| Network policies / egress restrictions | no definidas |
| Observability (logging, metrics, tracing stack) | stdout |
| Security context constraints (non-root, etc.) | runAsNonRoot, uid 10001 |

## Local alternative
El dry run corre las pruebas en el intérprete local. Los manifiestos quedan escritos para `oc apply --dry-run=client` cuando haya `oc`.
""",
    )
    write(
        BRAIN / "00-context/architecture/integration-catalog.md",
        f"""# Integration Catalog

{BANNER}

| ID | System | Direction (in/out) | Protocol (REST/SOAP/MQ/file/DB) | Contract / spec link | Processes | Mock allowed in PoC? | Owner |
|---|---|---|---|---|---|---|---|
| INT-01 | Emisor | out | REST | POST /v1/autorizar | P-REV | Y | dry-run |
""",
    )
    write(
        BRAIN / "00-context/architecture/nfrs.md",
        f"""# Non-Functional Requirements

{BANNER}

| Category | Requirement | Target / metric | Demonstrate in PoC? |
|---|---|---|---|
| Latency | Decidir el reverso sin esperar al reloj real | La prueba usa segundos ya transcurridos, no `sleep` | Y |
| Security (authN/authZ, encryption) | El mock exige el token del Secret de ejemplo | Header `Authorization: Bearer <token>` | Y |
""",
    )
    write(
        BRAIN / "00-context/architecture/current-architecture.md",
        f"""# Current Architecture (As-Is)

{BANNER}

## 1. System context (C4 L1)
```mermaid
flowchart LR
  Adquirente[Adquirente] --> Switch[Switch legacy ficticio]
  Switch --> Emisor[Emisor]
```

## 2. Containers / components (C4 L2) for in-scope processes
| Component | Tech | Responsibility | Repo | Process IDs |
|---|---|---|---|---|
| switch_core | Python | Timeout, reverso y reintentos | dry-run-legacy | P-REV |

## 3. Key data flows
En línea: el switch espera al emisor y, si vence el timeout, envía el reverso al adquirente.

## 4. Data stores
| Store | Tech | Main entities | Owner |
|---|---|---|---|
| — | memoria | constantes del módulo | dry-run |

## 5. Known pain points / tech debt
El timeout está fijo en código. Los documentos no coinciden con ese número.
""",
    )
    write(
        BRAIN / "00-context/architecture/target-architecture.md",
        f"""# Target Architecture (To-Be)

{BANNER}

## 1. Architecture principles
1. Un slice mínimo, de uno o dos contenedores.
2. Las integraciones externas se simulan.
3. Solo datos sintéticos.
4. La configuración va en ConfigMap y el secreto en Secret.

## 2. Target style
- Runtime style: dos contenedores (servicio + mock)
- Integration style: HTTP JSON
- Data strategy: sin base de datos en el PoC

## 3. Reference architecture diagram
```mermaid
flowchart LR
  Cliente[Cliente] --> SVC[reverso]
  SVC --> MOCK[emisor-mock]
```

## 4. Constraints and non-negotiables
Corre en OpenShift o, si no hay clúster, en Podman con el mismo Containerfile. Usuario no root.

## 5. Migration considerations
El legacy sigue aparte. Este PoC no lo reemplaza.
""",
    )


def write_phase0() -> None:
    write(
        BRAIN / "04-audit/spikes/SPIKE-001/validation-process.md",
        f"""# SPIKE-001: Validation Process for {PROC} {PROC_NAME}

{BANNER}

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
| 7 | PRD y SDD | write-prd / write-sdd | 05-spec/CAP-001-reverso-timeout/ | omitida |
| 8 | PoC | plan-poc / build-poc / poc-findings | 06-poc/POC-001-reverso-timeout/ | omitida |

## 5. Sampling and acceptance
- Sample size per gate: no hay muestra humana
- Accuracy threshold: no aplica en este dry run

## 6. Risks and assumptions
| Risk / assumption | Mitigation |
|---|---|
| Las reglas se extraen de bloques `rule`, no de prosa libre | El extracto citado tiene que aparecer verbatim en el documento o en el código |

## 7. Timebox
- Start: {DATE} · Target G4: {DATE}

## 8. Retrospective (fill at the end)
La cadena corre en un script. No sustituye al agente ni a las compuertas.
""",
    )


def write_knowledge(legacy, asis, code) -> None:
    write(
        BRAIN / "01-legacy/output/inventory.md",
        f"""# Inventory: Legacy documentation (SPIKE-001)

{BANNER}

| Doc ID | Title | Source (SRC-xx) | Location / path | Date | Type (manual, spec, procedure, ticket…) | Processes | Status (processed / skipped) | Reason if skipped | KUs extracted |
|---|---|---|---|---|---|---|---|---|---|
| LEG-REV-proceso-reverso | Proceso de reverso por timeout del emisor | SRC-01 | 01-legacy/input/raw/LEG-REV-proceso-reverso.md | 2019-04-12 | procedure | P-REV | processed | | {len(legacy)} |
""",
    )
    write(
        BRAIN / "01-legacy/output/knowledge/P-REV.md",
        ku_markdown(
            "Knowledge: P-REV Reverso por timeout del emisor (legacy)",
            "LEG-REV-proceso-reverso",
            "El documento de 2019 dice que el reverso va al adquirente y que el timeout es de 45 segundos.",
            legacy,
        ),
    )
    write(
        BRAIN / "02-asis/output/inventory.md",
        f"""# Inventory: As-Is documentation (SPIKE-001)

{BANNER}

| Doc ID | Title | Source (SRC-xx) | Location / path | Date | Type (manual, spec, procedure, ticket…) | Processes | Status (processed / skipped) | Reason if skipped | KUs extracted |
|---|---|---|---|---|---|---|---|---|---|
| ASIS-REV-proceso-reverso | As-Is: reverso por timeout del emisor | SRC-02 | 02-asis/input/raw/ASIS-REV-proceso-reverso.md | 2026-09-01 | procedure | P-REV | processed | | {len(asis)} |
""",
    )
    write(
        BRAIN / "02-asis/output/knowledge/P-REV.md",
        ku_markdown(
            "Knowledge: P-REV Reverso por timeout del emisor (asis)",
            "ASIS-REV-proceso-reverso",
            "El As-Is nuevo baja el timeout a 30 segundos, exige emisores autorizados y agrega una cola manual. El timeout está redactado como intención («se debe»), por eso esa unidad queda en confianza M.",
            asis,
        ),
    )
    write(
        BRAIN / "03-code/output/knowledge/P-REV.md",
        ku_markdown(
            "Knowledge: P-REV Reverso por timeout del emisor (code)",
            "legacy-readonly/switch_core/reversal.py@dry-run-001",
            "El código usa 25 segundos, envía el reverso al adquirente, filtra emisores autorizados y reintenta hasta 3 veces. Ese reintento no está en los documentos.",
            code,
        ),
    )


def write_delta(legacy, asis) -> None:
    legacy_by = {item["match"]: item for item in legacy}
    lines = []
    for item in asis:
        old = legacy_by.get(item["match"])
        if old is None:
            change = "new"
            old_id = "—"
            summary = "No está en el documento legacy."
        elif old["statement"] == item["statement"]:
            change = "unchanged"
            old_id = old["id"]
            summary = "Mismo enunciado."
        else:
            change = "changed"
            old_id = old["id"]
            summary = "Cambia el enunciado, incluido el umbral si lo hay."
        lines.append(f"| {change} | {item['id']} | {old_id} | {summary} |")
    write(
        BRAIN / "02-asis/output/legacy-delta.md",
        "# Legacy → As-Is Delta (SPIKE-001)\n\n"
        f"{BANNER}\n\n"
        f"## {PROC} {PROC_NAME}\n"
        "| Change | As-Is KU | Legacy KU | Summary |\n"
        "|---|---|---|---|\n"
        + "\n".join(lines)
        + "\n\n**Counts:** new 2 · changed 1 · unchanged 1 · dropped 0\n",
    )


def write_code_map(code) -> None:
    rows = "\n".join(
        f"| {item['excerpt']} | {item['line']} | reversal.py:{item['line']} | no |"
        for item in code
    )
    write(
        BRAIN / "03-code/output/code-map.md",
        f"""# Code Map (SPIKE-001)

{BANNER}

- **Repos analyzed:** dry-run-legacy@{SHA}

## {PROC} {PROC_NAME}
### Entry points
| Type (API / batch / consumer / UI) | Identifier (endpoint, job, topic) | Location |
|---|---|---|
| función | dispara_reverso | legacy-readonly/switch_core/reversal.py |

### Call chain
```mermaid
flowchart TD
  EP[dispara_reverso] --> T[ISSUER_TIMEOUT_S]
  EP --> D[DESTINO_REVERSO]
```

### Key components
| Component | Responsibility | Location | KUs |
|---|---|---|---|
| reversal.py | Reglas del reverso | legacy-readonly/switch_core/reversal.py | {", ".join(item["id"] for item in code)} |

### Config and constants
| Name | Line | Where defined | Runtime-overridable? |
|---|---|---|---|
{rows}

### Observations
`ISSUER_TIMEOUT_S` y `MAX_REINTENTOS` están fijos. No hay prueba en el módulo legacy.
""",
    )


def matrix_statement(row: dict) -> str:
    sides = row["sides"]
    for name in ("asis", "code", "legacy"):
        if name in sides:
            return sides[name]["statement"]
    return ""


def write_matrix(rows) -> None:
    buffer = io.StringIO()
    writer = csv.writer(buffer)
    writer.writerow(
        [
            "match_id",
            "process",
            "step",
            "type",
            "statement",
            "ku_legacy",
            "ku_asis",
            "ku_code",
            "category",
            "disc_id",
            "confidence",
            "decision_ref",
        ]
    )
    for index, row in enumerate(rows, start=1):
        sides = row["sides"]
        step = next(iter(sides.values()))["step"]
        kind = next(iter(sides.values()))["type"]
        confidence = "H"
        if any(item["confidence"] == "M" for item in sides.values()):
            confidence = "M"
        writer.writerow(
            [
                f"M-{index:03d}",
                PROC,
                step,
                kind,
                matrix_statement(row),
                sides.get("legacy", {}).get("id", ""),
                sides.get("asis", {}).get("id", ""),
                sides.get("code", {}).get("id", ""),
                row["category"],
                row["disc_id"],
                confidence,
                row["decision_ref"],
            ]
        )
    write(BRAIN / "04-audit/output/traceability-matrix.csv", buffer.getvalue())


def write_discrepancies(rows) -> None:
    labels = {
        "drift": "⚠️ Drift",
        "undocumented": "🕳️ Undocumented",
        "orphan": "👻 Orphan",
        "ambiguous": "❓ Ambiguous",
    }
    for row in rows:
        if not row["disc_id"]:
            continue
        sides = row["sides"]
        evidence = []
        for corpus, label in (("legacy", "Legacy"), ("asis", "As-Is"), ("code", "Code")):
            item = sides.get(corpus)
            if item:
                evidence.append(
                    f"| {label} | {item['id']} | {item['statement']} | {citation(item)} |"
                )
            else:
                evidence.append(f"| {label} | — | — | — |")
        write(
            BRAIN / f"04-audit/output/discrepancies/{row['disc_id']}.md",
            f"""# {row['disc_id']}: {row['match']}

- **Category:** {labels[row['category']]}
- **Process / step:** {PROC} / {next(iter(sides.values()))['step']}
- **Impact:** M. Cambia el comportamiento del reverso o deja una regla sin respaldo.

{BANNER}

## Evidence
| Source | KU | Says | Citation |
|---|---|---|---|
{chr(10).join(evidence)}

## Analysis (agent)
Las fuentes de este `match` no cuentan la misma regla, o la regla vive en un solo lado.

## Recommendation (agent, non-binding)
{row['follow']}

## Decision (dry-run, no humana)
- **Decision:** {row['decision']}
- **Truth statement:** {row['truth'] or "—"}
- **Follow-up:** {row['follow']}
- **Decided by:** dry-run 001 automático · **Date:** {DATE} · **Ref:** {row['decision_ref']}
""",
        )


def write_decision_log(decisions) -> None:
    entries = []
    for row in reversed(decisions):
        entries.append(
            textwrap.dedent(
                f"""
                ## {row['decision_id']} {row['disc_id']}
                - **Date:** {DATE}
                - **Decided by:** dry-run 001 automático
                - **Decision:** {row['decision']}
                - **Truth statement:** {row['truth'] or "—"}
                - **Follow-up:** {row['follow']}
                """
            ).strip()
        )
    write(
        BRAIN / "04-audit/review/decision-log.md",
        "# Review Log: G4 Discrepancies and Validated As-Is (joint decisions)\n\n"
        f"{BANNER}\n\n"
        "No hubo sesión humana. Las entradas las escribió `run-dry-run-001.py`.\n\n"
        + "\n\n".join(entries)
        + "\n",
    )


def write_validated(rows) -> None:
    rules = []
    gaps = []
    number = 1
    asis_total = 0
    asis_in_code = 0
    code_total = 0
    code_documented = 0
    for row in rows:
        if "asis" in row["sides"]:
            asis_total += 1
            if "code" in row["sides"]:
                asis_in_code += 1
        if "code" in row["sides"]:
            code_total += 1
            if "asis" in row["sides"] or "legacy" in row["sides"]:
                code_documented += 1
        if row["category"] in ("confirmed", "drift") and row["truth"]:
            basis = "✅ " if row["category"] == "confirmed" else f"decisión {row['decision_id']}"
            ids = " = ".join(
                row["sides"][name]["id"]
                for name in ("legacy", "asis", "code")
                if name in row["sides"]
            )
            cites = " · ".join(citation(item) for item in row["sides"].values())
            step = next(iter(row["sides"].values()))["step"]
            rules.append(
                f"| VR-REV-{number:03d} | {step} | {row['truth']} | {basis} {ids} | {cites} |"
            )
            number += 1
        elif row["disc_id"]:
            kind = "orphan" if row["category"] == "orphan" else "undocumented"
            gaps.append(
                f"| {row['match']} | {kind} | dry-run | {row['disc_id']} |"
            )
    asis_pct = round(100 * asis_in_code / asis_total)
    code_pct = round(100 * code_documented / code_total)
    write(
        BRAIN / "04-audit/output/validated-asis/P-REV.md",
        f"""# Validated As-Is: {PROC} {PROC_NAME}

{BANNER}

- **Spike:** SPIKE-001 · **Version:** 1.0 · **Date:** {DATE}
- **Coverage:** As-Is KUs found in code: {asis_pct}% · Code KUs documented: {code_pct}%

## 1. Overview
Proceso ficticio. El switch rechaza emisores fuera de lista, espera la respuesta y, si vence el timeout, envía un reverso al adquirente. El timeout validado es el del código: 25 segundos.

## 2. Actors and systems
Adquirente, switch, emisor.

## 3. Process flow
```mermaid
flowchart LR
  A[Validar emisor] --> B[Esperar respuesta] --> C{{Timeout 25 s}}
  C -->|vence| D[Reverso al adquirente]
  C -->|responde| E[Fin]
```

## 4. Business rules (validated)
| Rule ID | Step | Rule | Basis (✅ match / decision) | Citations |
|---|---|---|---|---|
{chr(10).join(rules)}

## 5. Data entities
Emisor, transacción, reverso. Sin almacén en este dry run.

## 6. Integrations
INT-01 Emisor, saliente, HTTP. En el PoC va simulada.

## 7. Known gaps and open items
| Item | Type (undocumented / orphan / open) | Owner | Ref |
|---|---|---|---|
{chr(10).join(gaps)}

## 8. Sign-off
| Role | Name | Date |
|---|---|---|
| As-Is owner | omitida en dry-run 001 | |
| Tech Lead | omitida en dry-run 001 | |
""",
    )


def write_audit(rows, legacy, asis, code) -> None:
    counts = {name: 0 for name in ("confirmed", "drift", "undocumented", "orphan", "ambiguous")}
    for row in rows:
        counts[row["category"]] += 1
    asis_total = sum(1 for row in rows if "asis" in row["sides"])
    asis_in_code = sum(1 for row in rows if "asis" in row["sides"] and "code" in row["sides"])
    code_total = sum(1 for row in rows if "code" in row["sides"])
    code_documented = sum(
        1
        for row in rows
        if "code" in row["sides"] and ("asis" in row["sides"] or "legacy" in row["sides"])
    )
    write(
        BRAIN / "04-audit/output/audit-report.md",
        f"""# Audit Report: As-Is Validation (SPIKE-001)

{BANNER}

## 1. Executive summary
- Alcance: un proceso ficticio, P-REV.
- El As-Is y el código coinciden en el destino del reverso y en la lista de emisores.
- El timeout no coincide: legacy 45 s, As-Is 30 s, código 25 s. El dry run se queda con el código.
- Hay una cola manual solo en el As-Is y un reintento de 3 veces solo en el código.
- El slice del PoC cubre el timeout configurable, con 25 s de valor por defecto.

## 2. Scope and method
- Processes: P-REV
- Sources: LEG-REV-proceso-reverso, ASIS-REV-proceso-reverso
- Repo: dry-run-legacy@{SHA}
- Strategy: docs→code
- Gates held: ninguna. Las resolvió `run-dry-run-001.py`.

## 3. Coverage metrics
| Process | KUs legacy | KUs as-is | KUs code | ✅ | ⚠️ | 🕳️ | 👻 | ❓ | % As-Is in code | % code documented |
|---|---|---|---|---|---|---|---|---|---|---|
| P-REV | {len(legacy)} | {len(asis)} | {len(code)} | {counts['confirmed']} | {counts['drift']} | {counts['undocumented']} | {counts['orphan']} | {counts['ambiguous']} | {round(100 * asis_in_code / asis_total)}% | {round(100 * code_documented / code_total)}% |

## 4. Key findings
| # | Finding | DISC refs | Impact | Recommendation |
|---|---|---|---|---|
| 1 | El timeout documentado no es el que ejecuta el código | DISC-REV-001 | M | Spec: timeout por emisor, default 25 s |
| 2 | La cola manual no está en el código | DISC-REV-002 | M | Fuera de este slice |
| 3 | El código reintenta 3 veces y nadie lo documentó | DISC-REV-003 | M | Investigar en un spike posterior |

## 5. Risk heatmap
Un solo proceso, impacto medio, sin datos reales.

## 6. Recommendations for the To-Be
Hacer configurable el timeout por emisor. No integrar el emisor real en el PoC.

## 7. Method retrospective
- Reglas nuevas de fase: 0. Este corrido no escribe en `RULES.md`.
- Muestra humana: no hubo.
- Tiempo: un script, no una estimación manual.

## 8. Appendix: decision log summary
D-001 código manda en el timeout. D-002 cola manual fuera de alcance. D-003 reintentos sin promover.
""",
    )


def write_spec(rows) -> None:
    folder = BRAIN / "05-spec/CAP-001-reverso-timeout"
    write(
        folder / "prd.md",
        f"""# PRD: CAP-001-reverso-timeout Reverso por timeout del emisor

{BANNER}

- **Version:** 0.1 · **Date:** {DATE} · **Owner:** dry-run
- **Based on:** validated-asis/P-REV.md v1.0, audit-report findings #1

## 1. Problem and context
Los tres relatos del timeout no coinciden. El que corre es el de 25 segundos, fijo en el código. El To-Be de este slice lo hace configurable por emisor sin perder ese valor por defecto.

## 2. Users and actors
Adquirente, switch, emisor.

## 3. Goals / non-goals
| Goal | Metric | Source |
|---|---|---|
| G1 Timeout por emisor, default 25 s | AC-001.1 y AC-001.2 en verde | VR-REV del timeout, hallazgo 1 |
| Fuera de meta | Cola manual y reintentos | DISC-REV-002, DISC-REV-003 |

## 4. Scope
| Item | Change (new / modified / retired / unchanged) | As-Is ref |
|---|---|---|
| Timeout | modified | VR del timeout, decisión D-001 |
| Destino del reverso | unchanged | VR del reverso al adquirente |
| Lista de emisores | unchanged | VR de emisor autorizado |
| Cola manual | retired en este slice | DISC-REV-002 |
| Reintentos | unchanged, no entra al slice | DISC-REV-003 |

## 5. User journeys / scenarios
1. El emisor A tiene timeout de 20 s y no responde: hay reverso al adquirente.
2. Un emisor sin configuración no responde en 25 s: hay reverso.
3. El emisor responde a tiempo: no hay reverso.

## 6. Business rules carried over / changed
| VR / KU ref | As-Is rule | To-Be rule | Change |
|---|---|---|---|
| D-001 / KU-ASIS-REV timeout | 30 segundos, redacción de intención | Timeout por emisor, default 25 s | modified |
| KU-ASIS-REV reverso | El reverso va al adquirente | Igual | unchanged |

## 7. Success metrics
Las dos AC del timeout pasan en local.

## 8. Constraints and assumptions
Dos contenedores, emisor simulado, datos sintéticos. Imagen base real de eGlobal: desconocida.

## 9. Risks and open questions
El proceso es ficticio. Un despliegue en el clúster de eGlobal no está hecho.

## 10. Approval
Omitida en dry-run 001.
""",
    )
    change = ROOT / "openspec/changes/cap-001-reverso-timeout"
    spec_body = """### Requirement: Timeout de reverso configurable por emisor
The system SHALL generar un reverso hacia el adquirente cuando el emisor no responde dentro de su timeout. El valor por defecto es 25 segundos. Un emisor puede tener el suyo; en el ejemplo, el emisor A usa 20 segundos. Origen: decisión D-001 / PRD G1. Respecto del As-Is, el timeout pasa de una intención de 30 segundos a este valor configurable.

#### Scenario: Emisor A a los 20 segundos
- **WHEN** el emisor A tiene timeout de 20 s, no responde y ya van 20 s
- **THEN** se genera un reverso al adquirente

#### Scenario: Emisor sin configuración a los 25 segundos
- **WHEN** un emisor sin configuración no responde y ya van 25 s
- **THEN** se genera un reverso al adquirente

#### Scenario: Emisor sin configuración a los 24 segundos
- **WHEN** un emisor sin configuración no responde y van 24 s
- **THEN** no se genera reverso

### Requirement: Decisión sin espera de reloj
The system SHALL decidir el reverso sin esperar al reloj real en la prueba.

#### Scenario: Segundos ya transcurridos
- **WHEN** la prueba entrega los segundos ya transcurridos
- **THEN** la decisión no usa una espera real

### Requirement: Token del mock
The system SHALL exigir en el mock el token Bearer del Secret de ejemplo.

#### Scenario: Token distinto
- **WHEN** el mock recibe un token distinto del Secret de ejemplo
- **THEN** rechaza la petición
"""
    write(
        ROOT / "openspec/specs/reverso-timeout/spec.md",
        f"""# reverso-timeout Specification

{BANNER}

## Purpose
Decide si un emisor que no respondió ya venció su timeout y, en ese caso, arma el reverso hacia el adquirente. El valor por defecto sigue siendo 25 segundos.

## Requirements

{spec_body}""",
    )
    write(
        change / "specs/reverso-timeout/spec.md",
        f"""# Spec Delta

{BANNER}

## Purpose
El timeout deja de ser un número fijo de intención y pasa a ser configurable por emisor, con 25 segundos por defecto.

## ADDED Requirements

{spec_body}""",
    )
    write(
        change / "proposal.md",
        f"""# Proposal

{BANNER}

## Why
Los tres relatos del timeout no coinciden. El que corre es el de 25 segundos, fijo en el código. El As-Is lo redacta como una intención de 30 segundos. Este slice lo hace configurable por emisor sin perder el valor que ya corre.

## What Changes
- El timeout pasa a ser por emisor. El default es 25 segundos. El emisor A del ejemplo usa 20 segundos.
- Si el emisor no responde dentro de ese timeout, el reverso va al adquirente.
- La cola manual y los reintentos no entran en este slice.
- El emisor se simula. No hay persistencia.

## Capabilities

### New Capabilities
- `reverso-timeout`: decidir el reverso cuando el emisor no responde a tiempo.

### Modified Capabilities

## Impact
Dos contenedores (`reverso` y `emisor-mock`), contratos `POST /v1/autorizaciones` y `POST /v1/autorizar`, y `GET /health` en ambos. La imagen base de OpenShift sigue sin dato de eGlobal.
""",
    )
    write(
        change / "design.md",
        f"""# Design

{BANNER}

## Context
Diseño provisional. La imagen base aprobada de OpenShift sigue sin dato de eGlobal. Referencias: `00-context/architecture/target-architecture.md` y `adr/ADR-001-poc-approach.md`.

## Goals / Non-Goals
- Cumplir el timeout por emisor, con 25 segundos por defecto.
- Fuera de meta: cola manual y reintentos.

## Decisions
ADR-001: uno o dos contenedores, integraciones simuladas, datos sintéticos.

```mermaid
flowchart LR
  Cliente[Cliente] --> SVC[reverso]
  SVC --> MOCK[emisor-mock]
```

| Component | Responsibility | Tech |
|---|---|---|
| reverso | Decide si hay reverso | Python 3.12, biblioteca estándar |
| emisor-mock | Responde la consulta del emisor | Python 3.12, biblioteca estándar |

Sin persistencia. La configuración entra por variables de entorno.

- `POST /v1/autorizaciones` cuerpo `emisor_id`, `respondio`, `transcurrido_s`. Respuesta `reverso`, `destino`, `timeout_s`.
- `POST /v1/autorizar` en el mock. Respuesta `respondio`.
- `GET /health` en ambos.

```mermaid
sequenceDiagram
  participant Cliente
  participant Reverso
  participant Mock
  Cliente->>Reverso: POST /v1/autorizaciones
  Reverso->>Mock: POST /v1/autorizar
  Mock-->>Reverso: respondio
  Reverso-->>Cliente: reverso sí o no
```

INT-01 se simula con `emisor-mock`. El mock rechaza un token distinto. El log sale a stdout. Un JSON inválido responde 400.

## Risks / Trade-offs
El proceso es ficticio. Un despliegue en el clúster de eGlobal no está hecho.

## Migration Plan
El legacy sigue aparte. Este PoC no lo reemplaza.

## Open Questions
La imagen base aprobada de OpenShift no está.
""",
    )
    write(
        change / "tasks.md",
        f"""# Tasks

{BANNER}

## 1. Servicio

- [ ] 1.1 Servicio de decisión y HTTP (REQ-001)
- [ ] 1.2 Mock del emisor (REQ-001)

## 2. Empaque

- [ ] 2.1 Containerfile, ConfigMap, Secret de ejemplo y Deployment (REQ-001)

## 3. Pruebas

- [ ] 3.1 Pruebas AC-001.1, AC-001.2 y AC-001.3 (REQ-001). unittest sobre la función de decisión y una llamada HTTP local. Cada prueba lleva el ID del AC en el nombre.
""",
    )
    write(
        folder / "sdd.md",
        f"""# SDD: CAP-001-reverso-timeout Reverso por timeout del emisor

{BANNER}

La especificación está en formato OpenSpec. Este archivo solo indica dónde.

- Propuesta: `openspec/changes/cap-001-reverso-timeout/proposal.md`
- Spec del cambio: `openspec/changes/cap-001-reverso-timeout/specs/reverso-timeout/spec.md`
- Diseño: `openspec/changes/cap-001-reverso-timeout/design.md`
- Tareas: `openspec/changes/cap-001-reverso-timeout/tasks.md`
- Spec vigente: `openspec/specs/reverso-timeout/spec.md`
""",
    )
    write(
        folder / "AGENTS.md",
        f"""# AGENTS.md: CAP-001-reverso-timeout

{BANNER}

## Purpose
Decide si un emisor que no respondió ya venció su timeout y, en ese caso, arma el reverso hacia el adquirente.

## Source of truth
- Spec: `openspec/specs/reverso-timeout/spec.md`, `openspec/changes/cap-001-reverso-timeout/`, `./prd.md`
- Validated As-Is: `04-audit/output/validated-asis/P-REV.md`
- Architecture: `00-context/architecture/`

## Inputs / outputs
Entrada HTTP JSON. Salida JSON con `reverso` y, si aplica, `destino=adquirente`.

## Rules you must obey
1. Implementar solo REQ-001.
2. Valor por defecto: 25 segundos. El emisor A del ejemplo: 20 segundos.
3. Cada prueba cita su AC.
4. No hay cola manual ni reintentos en este slice.

## Files you may touch
`06-poc/POC-001-reverso-timeout/`

## Commands
```bash
python3 run-dry-run-001.py
```

## Definition of done
- [ ] AC-001.1, AC-001.2 y AC-001.3 pasan
- [ ] Manifiestos escritos
- [ ] La imagen base no aprobada queda en findings
""",
    )


def write_poc() -> Path:
    poc = BRAIN / "06-poc/POC-001-reverso-timeout"
    write(
        poc / "poc-plan.md",
        f"""# POC-001-reverso-timeout: Plan

{BANNER}

- **Capability:** CAP-001-reverso-timeout · **SDD version:** 0.1 · **Timebox:** un corrido

## 1. Hypothesis
Creemos que un servicio con timeout por emisor, valor por defecto 25 s, cumple AC-001.1 y AC-001.2 en dos contenedores, con el emisor simulado.

## 2. Slice
| REQ / AC | In PoC? | Why |
|---|---|---|
| REQ-001 / AC-001.1 | Y | El caso con timeout propio del emisor |
| REQ-001 / AC-001.2 | Y | El valor por defecto de 25 s |
| REQ-001 / AC-001.3 | Y | El caso en que todavía no vence |
| Cola manual, reintentos | N | Huecos del audit, fuera del slice |

## 3. Architecture slice
```mermaid
flowchart LR
  Cliente[Cliente] --> SVC[reverso] --> MOCK[emisor-mock]
```
| Container | Image base | Responsibility | Resources |
|---|---|---|---|
| reverso | python:3.12-slim | Decide el reverso | 50m/64Mi a 200m/128Mi |
| emisor-mock | python:3.12-slim | Simula INT-01 | 50m/64Mi a 200m/128Mi |

## 4. Integrations
| INT | Real or mock | Contract source |
|---|---|---|
| INT-01 | mock | integration-catalog.md |

## 5. Data
Emisores sintéticos A y B. Ningún dato de tarjeta ni de una persona.

## 6. Success criteria
- [ ] Containerfile escrito · [ ] AC-001.1 a AC-001.3 pasan · [ ] el log sale a stdout

## 7. Architecture compliance checklist
- [ ] Imagen base: desviación, anotada en findings
- [ ] non-root
- [ ] limits set
- [ ] config via ConfigMap
- [ ] secrets via Secret de ejemplo
- [ ] logging format `level=INFO msg=...`

## 8. Risks
No hay clúster en este corrido. Los manifiestos no se aplican.
""",
    )
    write(
        poc / "src/reverso_core.py",
        '''"""Decisión de reverso. Sin red y sin reloj."""


def parse_issuer_timeouts(raw):
    found = {}
    for piece in (raw or "").split(","):
        piece = piece.strip()
        if not piece:
            continue
        emisor, seconds = piece.split("=", 1)
        found[emisor.strip()] = int(seconds)
    return found


def timeout_for(emisor_id, default_s, issuer_map):
    return issuer_map.get(emisor_id, default_s)


def decidir(emisor_id, respondio, transcurrido_s, default_s, issuer_map):
    timeout_s = timeout_for(emisor_id, default_s, issuer_map)
    reverso = (not respondio) and transcurrido_s >= timeout_s
    return {
        "emisor_id": emisor_id,
        "reverso": reverso,
        "destino": "adquirente" if reverso else None,
        "timeout_s": timeout_s,
    }
''',
    )
    write(
        poc / "src/reverso.py",
        '''"""Servicio HTTP del PoC. Contenedor 1."""

import json
import os
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

from reverso_core import decidir, parse_issuer_timeouts

DEFAULT_TIMEOUT_S = int(os.environ.get("DEFAULT_TIMEOUT_S", "25"))
ISSUER_MAP = parse_issuer_timeouts(os.environ.get("ISSUER_TIMEOUTS", "A=20"))
CORS_ORIGIN = os.environ.get("CORS_ORIGIN", "*")


class Handler(BaseHTTPRequestHandler):
    def do_OPTIONS(self):
        self.send_response(204)
        self._cors_headers()
        self.send_header("Content-Length", "0")
        self.end_headers()

    def do_GET(self):
        if self.path != "/health":
            self._send(404, {"error": "no existe"})
            return
        self._send(200, {"status": "ok"})

    def do_POST(self):
        if self.path != "/v1/autorizaciones":
            self._send(404, {"error": "no existe"})
            return
        length = int(self.headers.get("Content-Length", "0"))
        try:
            body = json.loads(self.rfile.read(length).decode("utf-8"))
            result = decidir(
                body["emisor_id"],
                bool(body["respondio"]),
                int(body["transcurrido_s"]),
                DEFAULT_TIMEOUT_S,
                ISSUER_MAP,
            )
        except (KeyError, TypeError, ValueError, json.JSONDecodeError):
            self._send(400, {"error": "cuerpo inválido"})
            return
        print(
            f"level=INFO msg=decision emisor={result['emisor_id']} reverso={result['reverso']}",
            flush=True,
        )
        self._send(200, result)

    def _cors_headers(self):
        self.send_header("Access-Control-Allow-Origin", CORS_ORIGIN)
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type, Authorization")
        self.send_header("Access-Control-Max-Age", "600")

    def _send(self, status, payload):
        raw = json.dumps(payload).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self._cors_headers()
        self.send_header("Content-Length", str(len(raw)))
        self.end_headers()
        self.wfile.write(raw)

    def log_message(self, fmt, *args):
        return


def make_server(port=8080):
    return ThreadingHTTPServer(("0.0.0.0", port), Handler)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", "8080"))
    print(f"level=INFO msg=escuchando port={port}", flush=True)
    make_server(port).serve_forever()
''',
    )
    write(
        poc / "mocks/emisor.py",
        '''"""Mock de INT-01. Contenedor 2. Datos sintéticos."""

import json
import os
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

TOKEN = os.environ.get("EMISOR_TOKEN", "dry-run-ejemplo")
CORS_ORIGIN = os.environ.get("CORS_ORIGIN", "*")


class Handler(BaseHTTPRequestHandler):
    def do_OPTIONS(self):
        self.send_response(204)
        self._cors_headers()
        self.send_header("Content-Length", "0")
        self.end_headers()

    def do_GET(self):
        if self.path != "/health":
            self._send(404, {"error": "no existe"})
            return
        self._send(200, {"status": "ok"})

    def do_POST(self):
        if self.path != "/v1/autorizar":
            self._send(404, {"error": "no existe"})
            return
        if self.headers.get("Authorization") != f"Bearer {TOKEN}":
            self._send(401, {"error": "token"})
            return
        length = int(self.headers.get("Content-Length", "0"))
        body = json.loads(self.rfile.read(length).decode("utf-8"))
        self._send(200, {"emisor_id": body.get("emisor_id"), "respondio": False})

    def _cors_headers(self):
        self.send_header("Access-Control-Allow-Origin", CORS_ORIGIN)
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type, Authorization")
        self.send_header("Access-Control-Max-Age", "600")

    def _send(self, status, payload):
        raw = json.dumps(payload).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self._cors_headers()
        self.send_header("Content-Length", str(len(raw)))
        self.end_headers()
        self.wfile.write(raw)

    def log_message(self, fmt, *args):
        return


if __name__ == "__main__":
    port = int(os.environ.get("PORT", "8081"))
    print(f"level=INFO msg=mock port={port}", flush=True)
    ThreadingHTTPServer(("0.0.0.0", port), Handler).serve_forever()
''',
    )
    write(
        poc / "tests/test_ac_001.py",
        '''"""Pruebas del slice. El nombre de cada caso cita el AC."""

import json
import os
import threading
import unittest
import urllib.request
from pathlib import Path

os.environ.setdefault("DEFAULT_TIMEOUT_S", "25")
os.environ.setdefault("ISSUER_TIMEOUTS", "A=20")

import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from reverso import make_server
from reverso_core import decidir, parse_issuer_timeouts

ISSUERS = parse_issuer_timeouts("A=20")


class TestAC001(unittest.TestCase):
    def test_AC_001_1_emisor_A_a_los_20s_genera_reverso(self):
        result = decidir("A", False, 20, 25, ISSUERS)
        self.assertTrue(result["reverso"])
        self.assertEqual(result["destino"], "adquirente")
        self.assertEqual(result["timeout_s"], 20)

    def test_AC_001_2_sin_configuracion_a_los_25s_genera_reverso(self):
        result = decidir("Z", False, 25, 25, ISSUERS)
        self.assertTrue(result["reverso"])
        self.assertEqual(result["destino"], "adquirente")
        self.assertEqual(result["timeout_s"], 25)

    def test_AC_001_3_sin_configuracion_a_los_24s_no_genera_reverso(self):
        result = decidir("Z", False, 24, 25, ISSUERS)
        self.assertFalse(result["reverso"])
        self.assertIsNone(result["destino"])

    def test_AC_001_1_http(self):
        server = make_server(0)
        port = server.server_address[1]
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()
        try:
            request = urllib.request.Request(
                f"http://127.0.0.1:{port}/v1/autorizaciones",
                data=json.dumps(
                    {"emisor_id": "A", "respondio": False, "transcurrido_s": 20}
                ).encode("utf-8"),
                headers={"Content-Type": "application/json"},
            )
            with urllib.request.urlopen(request) as response:
                body = json.loads(response.read().decode("utf-8"))
                self.assertEqual(response.headers["Access-Control-Allow-Origin"], "*")
            self.assertTrue(body["reverso"])
            self.assertEqual(body["destino"], "adquirente")
        finally:
            server.shutdown()
            server.server_close()


if __name__ == "__main__":
    unittest.main()
''',
    )
    write(
        poc / "Containerfile",
        """FROM python:3.12-slim
WORKDIR /app
COPY src/ /app/
RUN useradd --uid 10001 --create-home appuser && chown -R appuser /app
USER 10001
EXPOSE 8080
CMD ["python", "-u", "reverso.py"]
""",
    )
    write(
        poc / "mocks/Containerfile",
        """FROM python:3.12-slim
WORKDIR /app
COPY emisor.py /app/emisor.py
RUN useradd --uid 10001 --create-home appuser && chown -R appuser /app
USER 10001
EXPOSE 8081
CMD ["python", "-u", "emisor.py"]
""",
    )
    write(
        poc / "openshift/configmap.yaml",
        """apiVersion: v1
kind: ConfigMap
metadata:
  name: poc-001-reverso-config
  namespace: dry-run-001
data:
  DEFAULT_TIMEOUT_S: "25"
  ISSUER_TIMEOUTS: "A=20"
  EMISOR_URL: "http://emisor-mock:8081"
""",
    )
    write(
        poc / "openshift/secret.example.yaml",
        """# Ejemplo. El valor es ficticio. No es una credencial.
apiVersion: v1
kind: Secret
metadata:
  name: poc-001-reverso-emisor
  namespace: dry-run-001
type: Opaque
stringData:
  EMISOR_TOKEN: dry-run-ejemplo
""",
    )
    deployment = """apiVersion: apps/v1
kind: Deployment
metadata:
  name: {name}
  namespace: dry-run-001
spec:
  replicas: 1
  selector:
    matchLabels:
      app: {name}
  template:
    metadata:
      labels:
        app: {name}
    spec:
      securityContext:
        runAsNonRoot: true
        runAsUser: 10001
      containers:
        - name: {name}
          image: {image}
          ports:
            - containerPort: {port}
          envFrom:
            - configMapRef:
                name: poc-001-reverso-config
            - secretRef:
                name: poc-001-reverso-emisor
          readinessProbe:
            httpGet:
              path: /health
              port: {port}
          livenessProbe:
            httpGet:
              path: /health
              port: {port}
          resources:
            requests:
              cpu: 50m
              memory: 64Mi
            limits:
              cpu: 200m
              memory: 128Mi
          securityContext:
            allowPrivilegeEscalation: false
"""
    write(
        poc / "openshift/deployment-reverso.yaml",
        deployment.format(name="reverso", image="poc-001-reverso:dry-run", port=8080),
    )
    write(
        poc / "openshift/deployment-emisor-mock.yaml",
        deployment.format(name="emisor-mock", image="poc-001-emisor-mock:dry-run", port=8081),
    )
    write(
        poc / "openshift/service-reverso.yaml",
        """apiVersion: v1
kind: Service
metadata:
  name: reverso
  namespace: dry-run-001
spec:
  selector:
    app: reverso
  ports:
    - port: 8080
      targetPort: 8080
""",
    )
    write(
        poc / "openshift/service-emisor-mock.yaml",
        """apiVersion: v1
kind: Service
metadata:
  name: emisor-mock
  namespace: dry-run-001
spec:
  selector:
    app: emisor-mock
  ports:
    - port: 8081
      targetPort: 8081
""",
    )
    write(
        poc / "openshift/route-reverso.yaml",
        """apiVersion: route.openshift.io/v1
kind: Route
metadata:
  name: reverso
  namespace: dry-run-001
spec:
  to:
    kind: Service
    name: reverso
  port:
    targetPort: 8080
  tls:
    termination: edge
""",
    )
    write(
        poc / "README.md",
        f"""# POC-001-reverso-timeout

{BANNER}

Dos contenedores: `reverso` decide, `emisor-mock` simula al emisor.

```bash
python3 -m unittest discover -s tests -v
docker build -f Containerfile -t poc-001-reverso:dry-run .
docker build -f mocks/Containerfile -t poc-001-emisor-mock:dry-run mocks
```

Los manifiestos están en `openshift/`. Este dry run no los aplica a un clúster.
""",
    )
    return poc


def run_tests(poc: Path) -> int:
    result = subprocess.run(
        [sys.executable, "-m", "unittest", "discover", "-s", "tests", "-v"],
        cwd=poc,
        check=False,
    )
    return result.returncode


def write_findings(test_code: int) -> None:
    passed = "pasa" if test_code == 0 else "falla"
    write(
        BRAIN / "06-poc/POC-001-reverso-timeout/findings.md",
        f"""# POC-001-reverso-timeout: Findings

{BANNER}

## 1. Result vs hypothesis
**Outcome:** ⚠️ partially

La hipótesis del timeout se sostiene en local. No hay despliegue en OpenShift: el clúster no está definido.

## 2. ✅ What worked
La decisión de 20 s para el emisor A y de 25 s por defecto. El destino del reverso es el adquirente. Las pruebas unittest {passed}.

## 3. ❌ What didn't
No se construyó la imagen ni se aplicaron los manifiestos. La imagen base aprobada por eGlobal sigue vacía en el método original.

## 4. Acceptance test results
| AC | Result | Notes |
|---|---|---|
| AC-001.1 | {passed} | Emisor A, 20 s |
| AC-001.2 | {passed} | Sin configuración, 25 s |
| AC-001.3 | {passed} | Sin configuración, 24 s, no hay reverso |

## 5. Deviations from the architecture
| Deviation | Reason | Recommendation |
|---|---|---|
| Imagen `python:3.12-slim` en vez de una UBI aprobada | `platform-openshift.md` llegó en TBD y este dry run tuvo que elegir una imagen pública | Sustituirla cuando Arquitectura nombre la imagen |
| Route con TLS edge de ejemplo | No hay política de ingress | Ajustarla al clúster real |
| Secret con valor `dry-run-ejemplo` | Hace falta un ejemplo para el manifiesto | No usarlo fuera de este dry run |

## 6. Considerations for the real build
El timeout por emisor sale de ConfigMap. El token del mock sale de Secret. El código legacy no se copió al contenedor: el servicio es nuevo, escrito desde el SDD.

## 7. Risks discovered
Cola manual y reintentos siguen fuera. Si el código real reintenta, este slice no lo muestra.

## 8. Recommendation
**Go** para el slice del timeout, porque las AC pasan en local. No es un go de construcción: el proceso es ficticio y el clúster no se tocó.
""",
    )


def write_status() -> None:
    write(
        BRAIN / "STATUS.md",
        f"""# STATUS

{BANNER}

_Last updated: {DATE} (dry-run 001)_

| Phase | Output | Gate | State |
|---|---|---|---|
| 0 Setup | 00-context/ y validation-process.md | G0 | omitida, corrida por el script |
| 1 Legacy | 01-legacy/output/knowledge/P-REV.md | G1 | omitida |
| 2 As-Is | 02-asis/output/knowledge/P-REV.md | G2 | omitida |
| 3 Code | 03-code/output/knowledge/P-REV.md | G3 | omitida |
| 4 Audit | validated-asis/P-REV.md y audit-report.md | G4 | omitida |
| 5 Spec | 05-spec/CAP-001-reverso-timeout/ | G5a/b | omitida |
| 6 PoC | 06-poc/POC-001-reverso-timeout/ | G6 | pruebas locales; sin despliegue |

**Next step:** ninguno dentro de este dry run. Las compuertas siguen sin firma humana.
""",
    )


if __name__ == "__main__":
    sys.exit(main())
