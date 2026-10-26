---
name: start-poc-containers
description: Levanta los dos contenedores ya construidos del PoC dry run 001 (reverso en 8080 y emisor-mock en 8081) y verifica el health. No reconstruye imágenes.
---
# Skill: start-poc-containers

Levanta el PoC dry run 001 con las imágenes que ya existen. No ejecutes `docker build`.

## Preconditions

- El daemon de Docker responde (`docker version`). Si no, arranca OrbStack o Docker Desktop.
- Existen las imágenes `poc-001-reverso:dry-run` y `poc-001-emisor-mock:dry-run`.
- Los puertos 8080 y 8081 del host están libres, o los contenedores `reverso` y `emisor-mock` son de este mismo dry run y se pueden reemplazar.

Si falta una imagen, detente. Este skill no la construye.

## Red

Nombre: `poc-dry-run`. El servicio llama al mock por el nombre de contenedor `emisor-mock` en el puerto 8081.

## Steps

1. Crea la red si no existe y quita contenedores previos de este dry run:

```bash
docker network create poc-dry-run 2>/dev/null || true
docker rm -f reverso emisor-mock >/dev/null 2>&1 || true
```

2. Levanta el mock. Publica `8081` y deja el token del manifiesto de ejemplo.

```bash
docker run -d --name emisor-mock --network poc-dry-run \
  -p 8081:8081 \
  -e PORT=8081 \
  -e EMISOR_TOKEN=dry-run-ejemplo \
  -e DEFAULT_TIMEOUT_S=25 \
  -e ISSUER_TIMEOUTS=A=20 \
  poc-001-emisor-mock:dry-run
```

3. Levanta el servicio. `EMISOR_URL` apunta al mock dentro de la red.

```bash
docker run -d --name reverso --network poc-dry-run \
  -p 8080:8080 \
  -e PORT=8080 \
  -e DEFAULT_TIMEOUT_S=25 \
  -e ISSUER_TIMEOUTS=A=20 \
  -e EMISOR_URL=http://emisor-mock:8081 \
  -e EMISOR_TOKEN=dry-run-ejemplo \
  poc-001-reverso:dry-run
```

4. Espera un segundo y verifica los dos health. Cada uno debe responder **HTTP 200** y el cuerpo `{"status": "ok"}`.

```bash
curl -sS -D - http://127.0.0.1:8081/health
curl -sS -D - http://127.0.0.1:8080/health
```

5. Opcional: una autorización del emisor A. Esperado: HTTP 200, `"reverso": true`, `"destino": "adquirente"`, `"timeout_s": 20`.

```bash
curl -sS -D - http://127.0.0.1:8080/v1/autorizaciones \
  -H 'Content-Type: application/json' \
  -d '{"emisor_id":"A","respondio":false,"transcurrido_s":20}'
```

## Done when

- `reverso` escucha en `0.0.0.0:8080` con la imagen `poc-001-reverso:dry-run`.
- `emisor-mock` escucha en `0.0.0.0:8081` con la imagen `poc-001-emisor-mock:dry-run`.
- Los dos `GET /health` devolvieron 200.

## Parar

```bash
docker rm -f reverso emisor-mock
```
