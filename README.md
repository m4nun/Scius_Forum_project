# Scius_Forum_project

> **On the Limitations of the Modulo Trick Method in Solving Exponential Diophantine Equations of the form 1 + p^a = q^b + r^c**

A LaTeX scientific paper and Beamer presentation authored by Burapat Suwanprasert and Kawin Chumtong (Naresuan University), advised by Assoc. Prof. Dr. Kijti Rodtes under the SCiUS Forum program.

## Contents

| Directory | Description |
|---|---|
| `full_paper/` | Full LaTeX paper with Thai/English titles, Thai font support (Sarabun), and bibliography |
| `presentation/` | LaTeX Beamer presentation (50 slides, 16:9), modular sections, and a page selector tool |
| `firyn.pdf` | Pre-compiled paper PDF |

## Paper Abstract

The research investigates the limitations of the "modulo trick" method used to solve exponential Diophantine equations of the form $1 + p^a = q^b + r^c$. The paper formally defines what it means for an equation to be solvable (or non-solvable) by the modulo trick, proves foundational lemmas (single modulus lemma, period of exponent residues), and establishes two main theorems:

1. **Theorem 1:** $1 + (pq)^a = p^b + q^c$ is non-solvable by the modulo trick
2. **Theorem 2:** $a^x - a^y = b^z - b^w$ is non-solvable by the modulo trick

## Building

### Paper
```bash
cd full_paper
latexmk -pdf -outdir=build main.tex
```

### Presentation
```bash
cd presentation
./compile.sh
```
Outputs to `presentation/build/main.pdf`.

For the interactive slide selector:
```bash
cd presentation
./run_selector.sh
```
Opens a web UI at `http://127.0.0.1:8123` to visually select/deselect slides.

## Prerequisites

- LaTeX (texlive with beamer, amsmath, amsfonts, tikz)
- or [tectonic](https://tectonic-typesetting.github.io) for automatic dependency handling
- `poppler-utils` (for PDF thumbnails in the page selector)
- Python 3 (for page selector web server)

## License

Academic work produced for the Science Classrooms in University-Affiliated School Project (SCiUS) at Naresuan University Secondary Demonstration School.
