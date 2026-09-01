# CLAUDE.md

Guidance for AI assistants (Claude Code) working in this repository.

## What this repository is

This is the working repository for an Indonesian undergraduate thesis (*skripsi*) by
**Muhammad Kholis** (NIM 2022573010098), Teknik Informatika, **Politeknik Negeri
Lhokseumawe**.

Thesis title:

> *Rancang Bangun Aplikasi Point of Sale dengan Fitur Prediksi Penjualan Harian
> Menggunakan Metode Long Short-Term Memory (LSTM)*
> ("Design and Development of a Point of Sale Application with a Daily Sales Prediction
> Feature Using the Long Short-Term Memory (LSTM) Method")

The application studied is a Flutter + Supabase + Isar (offline-first) POS app with an
LSTM-based daily-sales-prediction feature.

> **Most important thing to understand:** this repo holds the **LaTeX/document
> deliverables** of the thesis (report, funding proposal, system-design docs, admin
> letters, coursework) — **not** the POS application's source code. The app is only
> *described* in `Rancangan/`. Work here is authoring and compiling documents, not building
> software. Document content is written in **Bahasa Indonesia**; match the surrounding
> tone and terminology.

The repo started from a UNY LaTeX thesis template (see `README.md`, which is the original
template documentation in Indonesian).

## Repository layout

| Path | Role |
| --- | --- |
| `Project/` | **Main thesis document** (full LaTeX project with build script). Start here. |
| `Pendanaan/` | Standalone LaTeX funding/research proposal (`Pendanaan.tex` → `Pendanaan.pdf`). |
| `Rancangan/` | System design: `PRD.md`, Mermaid diagrams, wireframes, screen mockups. |
| `Dokumen/` | Administrative letters/templates (incl. `Surat Permintaan Data/`, a small LaTeX letter). |
| `Tugas/` | Coursework for *Manajemen Proyek TI* (`Tugas.tex`). Not part of the thesis itself. |
| `referensi/` | Reference PDFs (LSTM sales-forecasting papers). |
| `README.md` | Original LaTeX template docs (Indonesian). `CHANGELOG`, `LICENSE` (MIT). |

## Main document — `Project/`

Entry point: `Project/laporan.tex`. It pulls in modular files by a strict naming scheme:

- `a0`–`a8` — front matter:
  - `a0-identitas.tex` — title, student, advisors, dates (thesis metadata)
  - `a2-abstrak.tex` (Indonesian abstract), `a3-abstract.tex` (English abstract)
  - `a5-katapengantar.tex` (preface), `a7-pustaka.bib` (BibTeX references),
    `a8-lampiran.tex` (appendices)
- `b1-bab1.tex` … `b5-bab5.tex` — chapters (Bab I Pendahuluan → Bab V Kesimpulan dan Saran)
- `untouch/xx-*.tex` — protected template files (preamble, covers, approval/declaration
  pages). **Do not edit these** — they are marked *"DILARANG EDIT BAGIAN INI"*.
- `gambar/` — figures; `kode/` — code listings + utility scripts.

**Proposal vs. final-report mode** is toggled near the top of `laporan.tex`:

```latex
%\newcommand{\Jenis}{Proposal}   % proposal mode
\newcommand{\Jenis}{Laporan}     % final-report mode
```

Enable exactly one. Proposal mode emits cover → approval → TOC → Bab I–III; Laporan mode
adds declaration, preface, abstracts, and Bab IV–V.

## Building / compiling

Main thesis (preferred — uses `Project/compile.sh`, a 4-pass pdflatex+bibtex build with a
7-day dependency cache):

```bash
cd Project
./compile.sh                 # normal build (uses cache) -> laporan.pdf
./compile.sh --quiet         # silent (automation)
./compile.sh --debug         # full diagnostics
./compile.sh --clean         # remove temp files only
./compile.sh --skip-deps     # skip dependency check (faster)
./compile.sh --force-deps-check  # bypass cache, recheck deps
./compile.sh --clear-cache   # reset dependency cache
./compile.sh --help          # all options
```

Other LaTeX documents have **no** compile script — build them manually, e.g.:

```bash
cd Pendanaan && pdflatex Pendanaan.tex && bibtex Pendanaan && pdflatex Pendanaan.tex && pdflatex Pendanaan.tex
```

Requirements: a full TeX Live / MiKTeX install (`pdflatex`, `bibtex`). On Overleaf the
`compile.sh` script does not run — set the main document to `laporan.tex` and compile in the
browser.

## Conventions (read before editing)

- **Never edit `Project/untouch/xx-*.tex`** — protected template internals.
- Add figures to `Project/gambar/` and reference them via the configured graphicspath
  (e.g. `\includegraphics{gambar/foo.png}`). Code listings go in `Project/kode/`.
- Add bibliography entries to `Project/a7-pustaka.bib` (BibTeX); cite with `\cite{key}`.
- Do **not** commit LaTeX build artifacts — `Project/.gitignore` already excludes
  `*.aux`, `*.log`, `*.bbl`, `.latex_deps_cache/`, etc. (Some artifacts in `Pendanaan/`,
  `Tugas/`, `Dokumen/` are currently tracked; avoid adding new ones.)
- Keep document content in Bahasa Indonesia, matching the existing style.
- In `Rancangan/`, the Mermaid `.mmd` files are the source of truth — the paired `.png`/
  `.svg` are exports. Regenerate exports when you change a `.mmd`.

## Utility scripts — `Project/kode/`

- `code_sample.{py,cpp,java,ino}` — demo listings showing code-formatting in the document.
- `extract_docx.py` — extract text from a `.docx`.
- `extract_media.py` — extract embedded media (images) from a `.docx`.
- `image_mapper.py` — map image references inside a `.docx`.

These help migrate content from Word drafts into the LaTeX/asset workflow.

## Git

- Develop on the assigned feature branch; do not push to others without permission.
- Observed commit-message style: `"<Area> - <Change>"`, e.g. `Pendanaan - Update`,
  `Rancangan - Alur Kerja LSTM`. Prefix with the directory/document being changed.
