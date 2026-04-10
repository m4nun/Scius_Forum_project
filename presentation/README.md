# Presentation Documentation

## Overview

This is a **LaTeX Beamer presentation** project for the academic presentation titled:

> **"On the Limitations of the Modulo Trick Method in Solving Exponential Diophantine Equations of the form $1+p^a=q^b+r^c$"**

This presentation was created by:
- **Mr. Burapat Suwanprasert** (ID: 67983443)
- **Mr. Kawin Chumtong** (ID: 67983115)

**Advisor:** Assoc. Prof. Dr. Kijti Rodtes  
**Date:** 31 March 2026

---

## Table of Contents

1. [Project Structure](#project-structure)
2. [Prerequisites](#prerequisites)
3. [Building the Presentation](#building-the-presentation)
4. [Content Structure](#content-structure)
5. [Section Files](#section-files)
6. [Customization](#customization)
7. [Troubleshooting](#troubleshooting)

---

## Project Structure

```
presentation/
├── main.tex                          # Main LaTeX file (entry point)
├── poly.sty                          # Custom Beamer theme/style
├── refs.bib                          # Bibliography file
├── compile.sh                        # Compilation script
├── run_selector.sh                   # Page selector tool launcher
├── image.png                         # Asset image
├── build/                            # Build output directory
│   └── main.pdf                      # Compiled presentation
├── sections/                         # Modular section files
│   ├── 01_introduction.tex
│   ├── 02_example.tex
│   ├── 03_modulo_trick.tex
│   ├── 04_problem.tex
│   ├── 05_objectives.tex
│   ├── 06_results.tex
│   └── 07_conclusion.tex
├── source/                           # Logo and branding assets
│   ├── logo-name.pdf
│   ├── logo-trans.pdf
│   ├── last-frame.pdf
│   └── ...
└── page_selector/                    # Web-based slide selection tool
    ├── app.js
    ├── index.html
    ├── server.py
    ├── styles.css
    └── thumbnails/                   # Generated page thumbnails
```

---

## Prerequisites

### Required Software

1. **LaTeX Compiler** (one of the following):
   - `latexmk` - Recommended, handles multiple compilation passes automatically
   - `tectonic` - Modern LaTeX engine with automatic package downloading
   - `pdflatex` - Standard LaTeX compiler

2. **PDF Utilities**:
   - `pdftoppm` - For generating thumbnails (usually comes with poppler-utils)

3. **Python 3** - For running the page selector web server

### Installation

#### On Fedora/RHEL/CentOS:
```bash
sudo dnf install texlive-latex texlive-beamer texlive-amsfonts \
                 texlive-amsmath texlive-tikz \
                 poppler-utils python3
```

#### On Ubuntu/Debian:
```bash
sudo apt-get install texlive-latex-base texlive-latex-extra \
                     texlive-fonts-recommended texlive-pictures \
                     poppler-utils python3
```

#### Using Tectonic (Alternative):
```bash
curl -fsSL https://drop-sh.fullyjustified.net | sh
mv tectonic /usr/local/bin/
```

---

## Building the Presentation

### Method 1: Using the Compile Script (Recommended)

```bash
./compile.sh [main.tex]
```

This script automatically:
1. Detects available LaTeX compilers (latexmk → tectonic → pdflatex)
2. Creates the `build/` directory if needed
3. Compiles the document
4. Outputs `build/main.pdf`

### Method 2: Direct Compilation

**Using latexmk:**
```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=build main.tex
```

**Using tectonic:**
```bash
tectonic --keep-logs --outdir build main.tex
```

**Using pdflatex:**
```bash
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=build main.tex
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=build main.tex
```

### Output

The compiled PDF will be available at:
```
build/main.pdf
```

**Current statistics:**
- **Pages:** 50
- **Size:** ~4.8 MB
- **Aspect Ratio:** 16:9
- **Font Size:** 10pt

---

## Content Structure

### Presentation Sections

| Order | Section | Description | File |
|-------|---------|-------------|------|
| 1 | **Title Slide** | Presentation title, authors, date | `main.tex` |
| 2 | **Contents** | Outline of presentation | `main.tex` |
| 3 | **PDF Slides 1-9** | Imported external PDF pages | `main.tex` |
| 4 | **Introduction** | Brenner and Foster's paper overview | `sections/01_introduction.tex` |
| 5 | **Example** | Step-by-step solution of $1+5^a=7^b+7^c$ | `sections/02_example.tex` |
| 6 | **Modulo Trick** | Explanation of the modulo trick method | `sections/03_modulo_trick.tex` |
| 7 | **The Problem** | Equations that resist the method | `sections/04_problem.tex` |
| 8 | **Objectives** | Research goals and methodology | `sections/05_objectives.tex` |
| 9 | **Results** | Foundational results and main theorems | `sections/06_results.tex` |
| 10 | **Conclusion** | Summary and future work | `sections/07_conclusion.tex` |

### Mathematical Content

The presentation covers:

1. **Brenner and Foster's Method**
   - Historical context (1982 paper)
   - The "modulo trick" (congruence method)

2. **Example Walkthrough**
   - Solving $1+5^a=7^b+7^c$
   - Steps 1-7 demonstrating the method
   - Final result: only solution is $(0,0,0)$

3. **Theoretical Framework**
   - Definition of "solvable by modulo trick"
   - Definition of "non-solvable by modulo trick"
   - Key lemmas (Single modulus lemma, Period of exponent residues)

4. **Main Theorems**
   - Theorem 1: $1+(pq)^a = p^b+q^c$ is non-solvable
   - Theorem 2: $a^x-a^y = b^z-b^w$ is non-solvable
   - Validation of Brenner and Foster's observations

---

## Section Files

### `sections/01_introduction.tex`
- Brenner and Foster (1982) paper overview
- Introduction to exponential Diophantine equations
- The main equation form: $1+p^a = q^b + r^c$
- The "Modulo trick" (Congruence method)

### `sections/02_example.tex`
- Complete step-by-step solution example
- **Step 1:** Problem setup
- **Step 2:** Modulo 7 analysis
- **Step 3:** Pattern of $5^a$ modulo 7
- **Step 4:** Modulo 9 analysis
- **Step 5:** Computing $5^a$ modulo 9
- **Step 6:** Comparing both sides modulo 9
- **Step 7:** Resolving the contradiction
- Final theorem with solution

### `sections/03_modulo_trick.tex`
- Flowchart of the modulo trick method
- Brenner and Foster's successful applications
- Examples of solved equations

### `sections/04_problem.tex`
- Equations that resist the modulo trick
- Gap in the literature
- Research questions addressed

### `sections/05_objectives.tex`
- Research objectives (Define, Build, Prove, Validate)
- Methodology flowchart
- Research approach

### `sections/06_results.tex`
**Subsections:**
- **Foundational Results:**
  - Proposition 1 (Key insight for computability)
  - Modeling with sets
  - Formal definitions
  - Key Lemma (Single modulus lemma)
- **Main Theorems:**
  - Theorem 1 (Non-solvability)
  - Corollary 1 (Validating Brenner and Foster)
- **Generalization:**
  - Extended framework
  - General definitions
  - Lemma 3 (Period of exponent residues)
  - Theorem 2 and Corollary 2

### `sections/07_conclusion.tex`
- Summary of main results
- Conclusions
- Future work
- Key references
- Acknowledgments

---

## Page Selector Tool

### Overview

The **page selector** is a web-based tool for interactively selecting which slides to keep or delete from the presentation.

### Usage

```bash
./run_selector.sh [PORT]
```

**Default port:** 8123

### How It Works

1. **Compiles** the PDF (if not already built)
2. **Generates thumbnails** from the PDF using `pdftoppm`
3. **Starts a web server** on the specified port
4. Opens a web interface at `http://127.0.0.1:8123`

### Web Interface Features

- **Thumbnail view** of all slides
- **Keep/Delete toggle** for each slide
- **Keep All / Delete All** buttons
- **Save Selection** to `page_selector/selection.json`
- **Open PDF** button to view the full presentation

### API Endpoints

- `GET /api/pages` - List all pages with thumbnails
- `GET /api/selection` - Get current selection
- `POST /api/selection` - Save user selection
- `GET /pdf/main.pdf` - Serve the compiled PDF

---

## Customization

### Changing the Title/Metadata

Edit in `main.tex` (lines 39-45):

```latex
\title{Your Title Here}
\subtitle{Your Subtitle}
\author[Short Names]{Full Names}
\institute{Your Institution}
\date{Your Date}
```

### Adding New Sections

1. Create a new file in `sections/` (e.g., `08_new_section.tex`)
2. Add the section content:
   ```latex
   \section{New Section Name}
   
   \begin{frame}{Frame Title}
       Content here...
   \end{frame}
   ```
3. Include it in `main.tex`:
   ```latex
   \input{sections/08_new_section}
   ```

### Modifying the Theme

The presentation uses the custom `poly.sty` theme. Edit this file to change:
- Colors (line 23-28)
- Fonts (line 59-74)
- Slide layouts (line 117-205)

### Changing Aspect Ratio

Edit in `main.tex` (line 1):
```latex
\documentclass[10pt,aspectratio=169]{beamer}  % 16:9
\documentclass[10pt,aspectratio=43]{beamer}   % 4:3
```

---

## Troubleshooting

### Common Issues

#### "File `beamer.cls` not found"
**Solution:** Install the beamer package:
```bash
# Fedora/RHEL
sudo dnf install texlive-beamer

# Ubuntu/Debian
sudo apt-get install texlive-latex-recommended
```

#### "No LaTeX compiler found"
**Solution:** Install a LaTeX distribution or use tectonic:
```bash
curl -fsSL https://drop-sh.fullyjustified.net | sh
```

#### "Overfull \hbox" or "Overfull \vbox" warnings
**Explanation:** These are cosmetic warnings indicating content slightly exceeds margins. The PDF still compiles correctly.

**Solution:** 
- Reduce content on the affected slide
- Use `\small` or `\footnotesize` for text
- Adjust table column widths

#### Missing thumbnails in page selector
**Solution:** Ensure `pdftoppm` is installed:
```bash
# Fedora/RHEL
sudo dnf install poppler-utils

# Ubuntu/Debian
sudo apt-get install poppler-utils
```

### Compilation Errors

If compilation fails:

1. Check that all section files exist in `sections/`
2. Verify LaTeX syntax in modified files
3. Check the log file: `build/main.log`
4. Try compiling with tectonic for better error messages

### Getting Help

- Check the LaTeX log: `build/main.log`
- Run with `--print` flag for detailed output (tectonic)
- Ensure all dependencies are installed

---

## License

This presentation is created for academic purposes as part of the Science Classrooms in University-Affiliated School Project (SCiUS) at Naresuan University Secondary Demonstration School.

---

## References

1. J. L. Brenner and L. L. Foster, "Exponential Diophantine equations," *Pacific J. Math.*, vol. 101, no. 2, pp. 263-301, 1982.
2. L. Wang and R. Tijdeman, "Exponential Diophantine equations with four terms," *Indag. Math.*, vol. 51, pp. 87-96, 1988.
3. M. Deze and R. Tijdeman, "Exponential Diophantine equations with four terms," *Indagationes Mathematicae*, vol. 3, no. 1, pp. 47-57, 1992.

---

## Acknowledgments

- Assoc. Prof. Dr. Kijti Rodtes (Advisor)
- Science Classrooms in University-Affiliated School Project (SCiUS)
- Naresuan University Secondary Demonstration School

---

*Last Updated: April 9, 2026*
