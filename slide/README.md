---
marp: true
theme: default
paginate: true
---

# Development Environment Setup

Before working with the project dependencies, ensure you have the following tools installed.

---

# Essential Tools

- Git
- GitHub Account
- VS Code or Cursor
- TeXLive

---

# Git

1. Download and install from [git-scm.com](https://git-scm.com/downloads)
2. Configure your identity:

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

---

# GitHub Account Setup

1. Sign up at [github.com](https://github.com/signup)
2. Notify the project owner of your GitHub username
3. Generate and add an SSH key for authentication

---

# Generate SSH Key

```bash
ssh-keygen -t ed25519 -C "your.email@example.com"
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
```

Copy public key to clipboard:
- macOS: `pbcopy < ~/.ssh/id_ed25519.pub`
- Windows (Git Bash): `cat ~/.ssh/id_ed25519.pub | clip`
- Linux: `cat ~/.ssh/id_ed25519.pub | xclip -selection clipboard`

---

# Add SSH Key to GitHub

1. Log in to GitHub
2. Profile photo → Settings
3. SSH and GPG keys → New SSH key
4. Add title and paste key

Verify: `ssh -T git@github.com`

---

# VS Code or Cursor

1. Download from [code.visualstudio.com](https://code.visualstudio.com/) or [cursor.sh](https://cursor.sh/)
2. Install recommended extensions (see next slides)

---

# TeXLive

- Windows: [tug.org/texlive/acquire-netinstall.html](https://tug.org/texlive/acquire-netinstall.html)
- macOS: MacTeX from [tug.org/mactex/](https://tug.org/mactex/)
- Linux: `sudo apt-get install texlive-full` (Ubuntu/Debian) or `sudo dnf install texlive-scheme-full` (Fedora)

---

# IDE Extensions: LaTeX Workshop

- Search "LaTeX Workshop" or install from marketplace
- Provides LaTeX editing, compilation, and preview support

---

# IDE Extensions: Python

- Python (Microsoft): IntelliSense, linting, debugging
- Pylance: Enhanced language server
- Python Indent: Smart indentation

---

# IDE Extensions: R

- R (REditorSupport): R language support
- R Debugger: Debug R scripts

---

# Installing Dependencies

First-time setup for collaborators

---

# Installing uv (Python)

```bash
# macOS/Linux/WSL
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows (PowerShell)
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

uv --version
```

---

# Installing renv (R)

```r
R
install.packages("renv")
library(renv)
```

---

# Python Dependencies with uv

1. Install: `uv sync` (or `uv sync --dev` for dev deps)
2. Select interpreter: Command Palette → Python: Select Interpreter → `.venv/bin/python`
3. Editable install: `uv pip install -e .`
4. Add dependency: `uv add package-name` or `uv add --dev package-name`

---

# Activate Virtual Environment

```bash
# macOS/Linux/WSL
source .venv/bin/activate

# Windows (PowerShell)
.venv\Scripts\Activate.ps1

# Windows (Git Bash)
source .venv/Scripts/activate
```

---

# Using the Python Package

```python
from src.economics.simulate import make_equilibrium, simulate_choice

equilibrium = make_equilibrium(
    num_simulation=100,
    num_alternative=3,
    num_covariate=2
)
equilibrium = simulate_choice(seed=10, equilibrium=equilibrium)
```

Package location: `src/economics/` (simulate.py, utils/)

---

# R Dependencies with renv

1. Open R in project directory
2. Restore: `renv::restore()`
3. Add package: `install.packages("package-name")` then `renv::snapshot()`

---

# Updating Dependencies

**Python (uv):**
```bash
uv lock --upgrade
uv add package-name@latest
```

**R (renv):**
```r
renv::update()
renv::update("package-name")
```

---

# Summary

- Git, GitHub SSH, VS Code/Cursor, TeXLive
- IDE extensions for LaTeX, Python, R
- uv for Python, renv for R
- `uv sync` and `uv pip install -e .` for Python
- `renv::restore()` for R
