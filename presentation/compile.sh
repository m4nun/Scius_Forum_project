#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

MAIN_TEX="${1:-main.tex}"
BUILD_DIR="${BUILD_DIR:-build}"

mkdir -p "$BUILD_DIR"

if command -v latexmk >/dev/null 2>&1; then
    latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir="$BUILD_DIR" "$MAIN_TEX"
elif command -v tectonic >/dev/null 2>&1; then
    tectonic --keep-logs --outdir "$BUILD_DIR" "$MAIN_TEX"
elif command -v pdflatex >/dev/null 2>&1; then
    pdflatex -interaction=nonstopmode -halt-on-error -output-directory="$BUILD_DIR" "$MAIN_TEX"
    pdflatex -interaction=nonstopmode -halt-on-error -output-directory="$BUILD_DIR" "$MAIN_TEX"
else
    echo "No LaTeX compiler found. Install latexmk, tectonic, or pdflatex, then rerun ./compile.sh." >&2
    exit 1
fi

echo "Built PDF: $BUILD_DIR/${MAIN_TEX%.tex}.pdf"
