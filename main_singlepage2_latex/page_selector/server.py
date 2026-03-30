#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from datetime import datetime, timezone
from http import HTTPStatus
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlparse

WEB_ROOT = Path(__file__).resolve().parent
PROJECT_ROOT = WEB_ROOT.parent
PDF_PATH = PROJECT_ROOT / "build" / "main.pdf"
THUMB_DIR = WEB_ROOT / "thumbnails"
SELECTION_PATH = WEB_ROOT / "selection.json"


def list_pages() -> list[dict[str, object]]:
    pages = []
    for path in sorted(
        THUMB_DIR.glob("page-*.png"),
        key=lambda p: int(re.search(r"page-(\d+)\.png$", p.name).group(1)),
    ):
        match = re.search(r"page-(\d+)\.png$", path.name)
        if not match:
            continue
        page = int(match.group(1))
        pages.append({"page": page, "image": f"/thumbnails/{path.name}"})
    return pages


def load_selection() -> dict[str, object]:
    if not SELECTION_PATH.exists():
        return {}
    try:
        return json.loads(SELECTION_PATH.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return {}


class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(WEB_ROOT), **kwargs)

    def _send_json(self, payload: dict[str, object], status: int = HTTPStatus.OK) -> None:
        body = json.dumps(payload, indent=2).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self) -> None:
        parsed = urlparse(self.path)
        if parsed.path == "/api/pages":
            payload = {
                "pages": list_pages(),
                "selection": load_selection(),
                "pdf_url": "/pdf/main.pdf",
            }
            self._send_json(payload)
            return
        if parsed.path == "/api/selection":
            self._send_json(load_selection())
            return
        if parsed.path == "/pdf/main.pdf":
            if not PDF_PATH.exists():
                self.send_error(HTTPStatus.NOT_FOUND, "PDF not found")
                return
            data = PDF_PATH.read_bytes()
            self.send_response(HTTPStatus.OK)
            self.send_header("Content-Type", "application/pdf")
            self.send_header("Content-Length", str(len(data)))
            self.end_headers()
            self.wfile.write(data)
            return
        super().do_GET()

    def do_POST(self) -> None:
        parsed = urlparse(self.path)
        if parsed.path != "/api/selection":
            self.send_error(HTTPStatus.NOT_FOUND, "Unknown endpoint")
            return

        length = int(self.headers.get("Content-Length", "0"))
        raw = self.rfile.read(length)
        try:
            payload = json.loads(raw.decode("utf-8"))
        except json.JSONDecodeError:
            self._send_json({"error": "Invalid JSON payload"}, status=HTTPStatus.BAD_REQUEST)
            return

        payload["saved_at"] = datetime.now(timezone.utc).isoformat()
        SELECTION_PATH.write_text(json.dumps(payload, indent=2), encoding="utf-8")
        self._send_json({"ok": True, "selection_path": str(SELECTION_PATH), "selection": payload})


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", type=int, default=8123)
    args = parser.parse_args()

    server = ThreadingHTTPServer(("127.0.0.1", args.port), Handler)
    print(f"Serving selector on http://127.0.0.1:{args.port}")
    server.serve_forever()


if __name__ == "__main__":
    main()
