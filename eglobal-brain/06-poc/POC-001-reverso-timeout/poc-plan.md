# POC-001-reverso-timeout: Plan

> **🟨 ASSUMPTION — dry-run 001.** Generado en automático el 2026-10-24. Las compuertas humanas se omiten a propósito. Esto no es una aprobación.

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
