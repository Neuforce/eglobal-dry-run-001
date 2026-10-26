# POC-001-reverso-timeout

> **🟨 ASSUMPTION — dry-run 001.** Generado en automático el 2026-10-24. Las compuertas humanas se omiten a propósito. Esto no es una aprobación.

Dos contenedores: `reverso` decide, `emisor-mock` simula al emisor.

```bash
python3 -m unittest discover -s tests -v
docker build -f Containerfile -t poc-001-reverso:dry-run .
docker build -f mocks/Containerfile -t poc-001-emisor-mock:dry-run mocks
```

Los manifiestos están en `openshift/`. Este dry run no los aplica a un clúster.
