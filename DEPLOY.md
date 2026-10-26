# Despliegue del dry run 001

Un solo repositorio. Vercel publica lo estático. Railway corre los dos contenedores. La página de Vercel llama a las URLs públicas de Railway.

Esta carpeta todavía no es un repositorio git. Créalo y súbelo. Después conecta ese remoto en los dos productos. No hace falta clonar nada más.

## Qué va en cada lado

| Dónde | Qué | URL resultante |
|---|---|---|
| Vercel | Página para ejecutar, diagramas y archivos del dry run | `https://<proyecto>.vercel.app/` |
| Vercel | Diagrama del dry run | `https://<proyecto>.vercel.app/dry-run-flow.html` |
| Vercel | Diagrama del Spike 001 | `https://<proyecto>.vercel.app/spike-001-flow.html` |
| Railway, servicio `reverso` | `poc-001-reverso` | `https://<reverso>.up.railway.app` |
| Railway, servicio `emisor-mock` | `poc-001-emisor-mock` | `https://<emisor>.up.railway.app` |

En `127.0.0.1:8766` el botón sigue corriendo `run-dry-run-001.py`. En Vercel el botón se llama «Ejecutar en Railway» y llama a los dos servicios.

## 1. Railway

Crea un proyecto y dos servicios del mismo repositorio. El mock primero, para que el nombre exista antes de apuntarle el reverso. Los dos servicios tienen que estar en el mismo proyecto: si no, la red privada no resuelve.

### Servicio `emisor-mock`

El nombre del servicio tiene que ser exactamente `emisor-mock`.

- Root Directory: `eglobal-brain/06-poc/POC-001-reverso-timeout/mocks`
- Config file: `railway.toml` (Dockerfile `Containerfile`, health `GET /health`)
- Genera un dominio público.

Variables:

| Variable | Valor |
|---|---|
| `PORT` | `8081` |
| `EMISOR_TOKEN` | `dry-run-ejemplo` |
| `CORS_ORIGIN` | `*` en el primer despliegue. Después, el origen exacto de Vercel, por ejemplo `https://<proyecto>.vercel.app` |

### Servicio `reverso`

- Root Directory: `eglobal-brain/06-poc/POC-001-reverso-timeout`
- Config file: `railway.toml` (Dockerfile `Containerfile`, health `GET /health`)
- Genera un dominio público.

Variables:

| Variable | Valor |
|---|---|
| `PORT` | `8080` |
| `DEFAULT_TIMEOUT_S` | `25` |
| `ISSUER_TIMEOUTS` | `A=20` |
| `EMISOR_TOKEN` | `dry-run-ejemplo` |
| `EMISOR_URL` | `http://emisor-mock.railway.internal:8081` |
| `CORS_ORIGIN` | El mismo valor que en el mock |

`EMISOR_URL` es la red privada de Railway. El navegador no la usa. La página llama a los dominios públicos.

Comprueba, sin barra final:

```bash
curl -sS -D - https://<emisor>.up.railway.app/health
curl -sS -D - https://<reverso>.up.railway.app/health
curl -sS -D - https://<reverso>.up.railway.app/v1/autorizaciones \
  -H 'Content-Type: application/json' \
  -H 'Origin: https://<proyecto>.vercel.app' \
  -d '{"emisor_id":"A","respondio":false,"transcurrido_s":20}'
```

Los dos health deben ser 200 y `{"status": "ok"}`. La autorización debe ser 200 e incluir `Access-Control-Allow-Origin`.

## 2. Vercel

Importa el mismo repositorio. Framework: Other. `vercel.json` ya fija el build y la salida `public/`. No cambies esos comandos.

Variables de entorno (Production). Sin barra final. Son las URLs públicas del paso anterior.

| Variable | Valor |
|---|---|
| `RAILWAY_REVERSO_URL` | `https://<reverso>.up.railway.app` |
| `RAILWAY_EMISOR_URL` | `https://<emisor>.up.railway.app` |

El build (`python3 deploy/assemble-vercel.py`) las escribe en `/web/railway-config.js`. La página las lee y hace `fetch` a esos dominios:

- `GET /health` en los dos
- `POST /v1/autorizaciones` en el reverso, con `{"emisor_id":"A","respondio":false,"transcurrido_s":20}`

Si cambias una URL, vuelve a desplegar Vercel. Si no, el JavaScript sigue apuntando a la anterior.

## 3. Cerrar el círculo del CORS

1. Despliega Railway y copia las dos URLs públicas.
2. Ponlas en Vercel y despliega. Copia el origen (`https://<proyecto>.vercel.app`, sin ruta).
3. En los dos servicios de Railway, cambia `CORS_ORIGIN` de `*` a ese origen y vuelve a desplegar.

`*` deja pasar a cualquier página. El origen exacto deja pasar solo al sitio de Vercel. El valor por defecto del código, si omites la variable, también es `*`.
