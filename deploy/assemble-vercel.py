#!/usr/bin/env python3
"""Arma public/ para Vercel: la página, los diagramas y los archivos que lista."""

from __future__ import annotations

import json
import os
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PUBLIC = ROOT / "public"
sys.path.insert(0, str(ROOT / "web"))

import server  # noqa: E402


def js_string(value: str) -> str:
    return value.replace("\\", "\\\\").replace('"', '\\"')


def ignore_build_junk(_directory: str, names: list[str]) -> set[str]:
    return {name for name in names if name == "__pycache__" or name.endswith(".pyc")}


def main() -> None:
    if PUBLIC.exists():
        shutil.rmtree(PUBLIC)
    web = PUBLIC / "web"
    web.mkdir(parents=True)

    reverso = os.environ.get("RAILWAY_REVERSO_URL", "").strip().rstrip("/")
    emisor = os.environ.get("RAILWAY_EMISOR_URL", "").strip().rstrip("/")
    (web / "railway-config.js").write_text(
        "window.RAILWAY = {\n"
        f'  reversoUrl: "{js_string(reverso)}",\n'
        f'  emisorUrl: "{js_string(emisor)}"\n'
        "};\n",
        encoding="utf-8",
    )
    (web / "tree.json").write_text(
        json.dumps(server.tree(), ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    shutil.copyfile(ROOT / "web" / "index.html", PUBLIC / "index.html")
    for name in ("dry-run-flow.html", "spike-001-flow.html"):
        source = ROOT / name
        if source.is_file():
            shutil.copyfile(source, PUBLIC / name)
    for folder in ("eglobal-brain", "legacy-readonly"):
        source = ROOT / folder
        if source.is_dir():
            shutil.copytree(source, PUBLIC / folder, ignore=ignore_build_junk)


if __name__ == "__main__":
    main()
