# Development Environment Setup

Before working with the project dependencies, ensure you have the following tools installed:

## Essential Tools

### Git

1. Download and install Git from [git-scm.com](https://git-scm.com/downloads)
2. Configure your Git identity:
   ```bash
   git config --global user.name "Your Name"
   git config --global user.email "your.email@example.com"
   ```

### GitHub Account Setup

1. Sign up for a GitHub account at [github.com](https://github.com/signup)
2. Let the project owner know your GitHub username so they can add you as a collaborator
3. Generate and add an SSH key for secure authentication:

   **Generate SSH Key:**
   ```bash
   # Generate a new SSH key (press Enter when prompted for a passphrase or add one for extra security)
   ssh-keygen -t ed25519 -C "your.email@example.com"
   
   # Start the SSH agent
   eval "$(ssh-agent -s)"
   
   # Add your SSH key to the agent
   ssh-add ~/.ssh/id_ed25519
   
   # Copy your public key to clipboard
   # On macOS:
   pbcopy < ~/.ssh/id_ed25519.pub
   # On Windows (Git Bash):
   cat ~/.ssh/id_ed25519.pub | clip
   # On Linux:
   cat ~/.ssh/id_ed25519.pub | xclip -selection clipboard
   ```

   **Add SSH Key to GitHub:**
   1. Log in to GitHub
   2. Click your profile photo in the top right, then click Settings
   3. In the left sidebar, click "SSH and GPG keys"
   4. Click "New SSH key"
   5. Add a descriptive title (e.g., "Work Laptop")
   6. Paste your key into the "Key" field
   7. Click "Add SSH key"

   **Verify your connection:**
   ```bash
   ssh -T git@github.com
   ```
   
   You should see a message like: "Hi username! You've successfully authenticated..."

### VS Code or Cursor

1. Download and install VS Code from [code.visualstudio.com](https://code.visualstudio.com/) or Cursor from [cursor.sh](https://cursor.sh/)
2. Install recommended extensions (see below)

### TeXLive

Install a full TeXLive distribution for LaTeX support:

- **Windows**: Download and install from [tug.org/texlive/acquire-netinstall.html](https://tug.org/texlive/acquire-netinstall.html)
- **macOS**: Install MacTeX from [tug.org/mactex/](https://tug.org/mactex/)
- **Linux**: 
  ```bash
  # Ubuntu/Debian
  sudo apt-get install texlive-full
  
  # Fedora
  sudo dnf install texlive-scheme-full
  ```

## IDE Extensions

Install the following VS Code/Cursor extensions for a better development experience:

### LaTeX Workshop
- Search for "LaTeX Workshop" in the Extensions view or install from [marketplace](https://marketplace.visualstudio.com/items?itemName=James-Yu.latex-workshop)
- Provides LaTeX editing, compilation, and preview support

### Python Extensions
- "Python" by Microsoft: Provides IntelliSense, linting, debugging, etc.
- "Pylance": Enhanced language server for Python
- "Python Indent": Smart indentation for Python files

### R Extensions
- "R" by REditorSupport: R language support
- "R Debugger": Debug R scripts

# Installing Dependencies

## First-time Setup for Collaborators

### Installing uv (Python Dependency Manager)

Before installing project dependencies, you need to install uv:

```bash
# On macOS/Linux/WSL
curl -LsSf https://astral.sh/uv/install.sh | sh

# On Windows (PowerShell)
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Verify installation:

```bash
uv --version
```

### Installing renv (R Dependency Manager)

Before installing R project dependencies, you need to install renv:

```r
# Start R
R

# Install renv from CRAN
install.packages("renv")

# Verify installation
library(renv)
```

## Installing Python Dependencies with uv

This project uses uv for Python dependencies. The project is already initialized.

1. Install all project dependencies:

   ```bash
   uv sync
   ```
   
   This will read the `pyproject.toml` file and install all required packages. Use `uv sync --dev` to include development dependencies.

2. Select the Python interpreter:

   **In VS Code/Cursor:** The IDE will automatically detect the virtual environment and prompt you to select it. When you open a Python file, click on the Python version in the bottom-right corner of the status bar, or use the Command Palette (Ctrl+Shift+P / Cmd+Shift+P) and select "Python: Select Interpreter", then choose `.venv/bin/python` (or `.venv\Scripts\python.exe` on Windows).

   **For terminal work:** If you need to activate the virtual environment manually in your terminal:

   ```bash
   # On macOS/Linux/WSL
   source .venv/bin/activate
   
   # On Windows (PowerShell)
   .venv\Scripts\Activate.ps1
   
   # On Windows (Git Bash)
   source .venv/Scripts/activate
   ```

3. Install the Python package in editable mode:

   ```bash
   # Install the economics package from src/ in editable mode
   uv pip install -e .
   ```
   
   This makes the `economics` module available for import. The package is located in `src/economics/`.

4. If you need to add a new dependency:

   ```bash
   # Add a regular dependency
   uv add package-name
   
   # Add a development dependency
   uv add --dev package-name
   ```

## Using the Python Package

After installing the package in editable mode, you can import and use the `src.economics` module:

```python
from src.economics.simulate import make_equilibrium, simulate_choice

# Create equilibrium structure
equilibrium = make_equilibrium(
    num_simulation=100,
    num_alternative=3,
    num_covariate=2
)

# Simulate choices
equilibrium = simulate_choice(
    seed=10,
    equilibrium=equilibrium
)
```

The Python package is located in `src/economics/` and includes:
- `simulate.py` - Simulation functions for economic models
- `utils/` - Utility functions and helpers

## Installing R Dependencies with renv

This project uses renv for R dependencies. The project is already initialized.

1. Open R in the project directory:

   ```bash
   R
   ```

2. Restore all project dependencies:

   ```r
   renv::restore()
   ```
   
   This will read the `renv.lock` file and install all required packages.

3. If you need to add a new package:

   ```r
   # Install a new package
   install.packages("package-name")
   
   # After installing new packages, save the state
   renv::snapshot()
   ```

## Updating Dependencies

### Python (uv)

```bash
# Update all dependencies
uv lock --upgrade

# Update a specific package
uv add package-name@latest
```

### R (renv)

```r
# Update all packages
renv::update()

# Update a specific package
renv::update("package-name")
```

