#!/usr/bin/env python3
"""Interfaz local del dry run 001. Solo biblioteca estándar.

    python3 web/server.py
    http://127.0.0.1:8766/
"""

from __future__ import annotations

import json
import subprocess
import sys
import threading
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlparse

ROOT = Path(__file__).resolve().parent.parent
WEB = Path(__file__).resolve().parent
LAST_RUN = WEB / "last-run.json"
PORT = 8766
HOST = "127.0.0.1"
SCRIPT = ROOT / "run-dry-run-001.py"
LOCK = threading.Lock()

ALLOWED_SUFFIXES = {".md", ".py", ".csv", ".yaml", ".yml", ".txt", ".json"}
ALLOWED_NAMES = {"Containerfile"}
SKIP_DIRS = {".git", "__pycache__", "web"}

INPUT_DOCS = [
    "eglobal-brain/01-legacy/input/raw/LEG-REV-proceso-reverso.md",
    "eglobal-brain/02-asis/input/raw/ASIS-REV-proceso-reverso.md",
]
INPUT_CODE = [
    "legacy-readonly/switch_core/reversal.py",
]


def safe_path(raw: str) -> Path:
    candidate = (ROOT / raw).resolve()
    if not candidate.is_relative_to(ROOT):
        raise ValueError("ruta fuera del dry run")
    if not candidate.is_file():
        raise ValueError("no es un archivo")
    if candidate.name not in ALLOWED_NAMES and candidate.suffix not in ALLOWED_SUFFIXES:
        raise ValueError("tipo de archivo no permitido")
    if any(part in SKIP_DIRS for part in candidate.relative_to(ROOT).parts):
        raise ValueError("carpeta no disponible")
    return candidate


def list_dir(relative: str) -> list[str]:
    base = (ROOT / relative).resolve()
    if not base.is_dir() or not base.is_relative_to(ROOT):
        return []
    found = []
    for path in sorted(base.rglob("*")):
        if not path.is_file():
            continue
        if any(part in SKIP_DIRS for part in path.relative_to(ROOT).parts):
            continue
        if path.name not in ALLOWED_NAMES and path.suffix not in ALLOWED_SUFFIXES:
            continue
        found.append(path.relative_to(ROOT).as_posix())
    return found


def tree() -> dict:
    return {
        "inputs": {
            "documentos": [path for path in INPUT_DOCS if (ROOT / path).is_file()],
            "codigo": [path for path in INPUT_CODE if (ROOT / path).is_file()],
            "contexto": list_dir("eglobal-brain/00-context"),
        },
        "outputs": {
            "contexto": list_dir("eglobal-brain/00-context"),
            "conocimiento": (
                list_dir("eglobal-brain/01-legacy/output")
                + list_dir("eglobal-brain/02-asis/output")
                + list_dir("eglobal-brain/03-code/output")
            ),
            "auditoria": list_dir("eglobal-brain/04-audit"),
            "spec": list_dir("eglobal-brain/05-spec"),
            "poc": list_dir("eglobal-brain/06-poc"),
            "estado": ["eglobal-brain/STATUS.md"] if (ROOT / "eglobal-brain/STATUS.md").is_file() else [],
        },
    }


def read_file(raw: str) -> dict:
    path = safe_path(raw)
    text = path.read_text(encoding="utf-8", errors="replace")
    if len(text) > 200_000:
        text = text[:200_000] + "\n\n… recortado …"
    return {"path": path.relative_to(ROOT).as_posix(), "text": text}


def read_last_run() -> dict:
    if not LAST_RUN.is_file():
        return {"exit_code": None, "stdout": "", "stderr": "", "duration_s": None}
    return json.loads(LAST_RUN.read_text(encoding="utf-8"))


def run_script() -> dict:
    if not LOCK.acquire(blocking=False):
        return {"error": "ya hay una ejecución en curso", "status": 409}
    started = time.monotonic()
    try:
        result = subprocess.run(
            [sys.executable, str(SCRIPT)],
            cwd=ROOT,
            capture_output=True,
            text=True,
            timeout=180,
            check=False,
        )
        payload = {
            "exit_code": result.returncode,
            "stdout": result.stdout,
            "stderr": result.stderr,
            "duration_s": round(time.monotonic() - started, 2),
        }
        LAST_RUN.write_text(json.dumps(payload, ensure_ascii=False), encoding="utf-8")
        payload["status"] = 200
        return payload
    except subprocess.TimeoutExpired as error:
        payload = {
            "exit_code": None,
            "stdout": error.stdout or "",
            "stderr": (error.stderr or "") + "\nTiempo agotado (180 s).",
            "duration_s": round(time.monotonic() - started, 2),
            "status": 504,
        }
        LAST_RUN.write_text(json.dumps(payload, ensure_ascii=False), encoding="utf-8")
        return payload
    finally:
        LOCK.release()


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed = urlparse(self.path)
        if parsed.path == "/":
            body = (WEB / "index.html").read_bytes()
            self._send(200, body, "text/html; charset=utf-8", "no-store")
            return
        if parsed.path == "/api/tree":
            self._json(200, tree())
            return
        if parsed.path == "/api/file":
            raw = parse_qs(parsed.query).get("path", [""])[0]
            try:
                self._json(200, read_file(raw))
            except ValueError as error:
                self._json(400, {"error": str(error)})
            return
        if parsed.path == "/api/last-run":
            self._json(200, read_last_run())
            return
        self._json(404, {"error": "no existe"})

    def do_POST(self):
        if urlparse(self.path).path != "/api/run":
            self._json(404, {"error": "no existe"})
            return
        payload = run_script()
        status = payload.pop("status")
        self._json(status, payload)

    def _json(self, status, payload):
        body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        self._send(status, body, "application/json; charset=utf-8")

    def _send(self, status, body: bytes, content_type: str, cache_control: str = ""):
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(body)))
        if cache_control:
            self.send_header("Cache-Control", cache_control)
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, fmt, *args):
        print(f"level=INFO msg={self.address_string()} {fmt % args}", flush=True)


if __name__ == "__main__":
    server = ThreadingHTTPServer((HOST, PORT), Handler)
    print(f"level=INFO msg=interfaz http://{HOST}:{PORT}/", flush=True)
    server.serve_forever()
