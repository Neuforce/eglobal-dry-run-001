# POC-001-reverso-timeout: Findings

> **🟨 ASSUMPTION — dry-run 001.** Generado en automático el 2026-10-24. Las compuertas humanas se omiten a propósito. Esto no es una aprobación.

## 1. Result vs hypothesis
**Outcome:** ⚠️ partially

La hipótesis del timeout se sostiene en local. No hay despliegue en OpenShift: el clúster no está definido.

## 2. ✅ What worked
La decisión de 20 s para el emisor A y de 25 s por defecto. El destino del reverso es el adquirente. Las pruebas unittest pasa.

## 3. ❌ What didn't
No se construyó la imagen ni se aplicaron los manifiestos. La imagen base aprobada por eGlobal sigue vacía en el método original.

## 4. Acceptance test results
| AC | Result | Notes |
|---|---|---|
| AC-001.1 | pasa | Emisor A, 20 s |
| AC-001.2 | pasa | Sin configuración, 25 s |
| AC-001.3 | pasa | Sin configuración, 24 s, no hay reverso |

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
