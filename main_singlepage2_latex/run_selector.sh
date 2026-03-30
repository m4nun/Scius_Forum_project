#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

PORT="${1:-8123}"
THUMB_DPI="${THUMB_DPI:-144}"

if [ ! -f "build/main.pdf" ]; then
    ./compile.sh
fi

mkdir -p page_selector/thumbnails
pdftoppm -png -r "$THUMB_DPI" build/main.pdf page_selector/thumbnails/page >/dev/null 2>&1

exec python3 page_selector/server.py --port "$PORT"
