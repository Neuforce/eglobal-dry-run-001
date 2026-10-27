# AGENTS.md: CAP-001-reverso-timeout

> **🟨 ASSUMPTION — dry-run 001.** Generado en automático el 2026-10-24. Las compuertas humanas se omiten a propósito. Esto no es una aprobación.

## Purpose
Decide si un emisor que no respondió ya venció su timeout y, en ese caso, arma el reverso hacia el adquirente.

## Source of truth
- Spec: `./proposal.md`, `./spec.md`, `./design.md`, `./tasks.md`
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
