---
marp: true
theme: default
paginate: true
---

# LaTeX Writing Workflow

Creating research papers and presentations using LaTeX templates.

---

# Templates

1. `draft/draft.tex` - Academic papers and research drafts
2. `draft/slide.tex` - Presentations (Beamer)

All documents in `draft/` folder.

---

# Figure and Table Management

All figures/tables in `figuretable/` must be **programmatically generated**. Never manually edit.

Ensures: reproducibility, consistency, version control.

---

# Generation Scripts

Scripts in `report/` folder:
- R: Rmarkdown (.Rmd) or Quarto (.qmd)
- Python: Jupyter (.ipynb) or scripts (.py)

Output directly to `figuretable/`.

---

# Draft Workflow

1. Create file in `draft/` (e.g., `paper_name.tex`)
2. Copy from `draft.tex` template
3. Update title, author, abstract
4. Reference figures: `\includegraphics[width=0.8\textwidth]{figuretable/figure.png}`
5. Citations: update `library.bib`, use `\cite{key}`

---

# Compilation

```
xelatex draft.tex
bibtex draft
xelatex draft.tex
xelatex draft.tex
```

LaTeX Workshop: Ctrl+Alt+B build, Ctrl+Alt+V view.

---

# Presentation Workflow

1. Copy from `draft/slide.tex`
2. Organize with `\section{}`
3. Slides: `\begin{frame}{Title}`
4. Compile: `xelatex slide.tex`

---

# Magic Comments

```latex
% !TEX TS-program = xelatex
% !TEX TS-options = -synctex=1
```

Tells LaTeX Workshop to use XeLaTeX with SyncTeX.

---

# Best Practices

- Version control all documents
- Keep papers/presentations in `draft/`
- Only programmatically generated figures in `figuretable/`
- Single `library.bib`
- TBA for notes; GitHub Issues for discussion
