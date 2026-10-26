# Target Architecture (To-Be)

> **🟨 ASSUMPTION — dry-run 001.** Generado en automático el 2026-10-24. Las compuertas humanas se omiten a propósito. Esto no es una aprobación.

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
