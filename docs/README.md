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

### Obsidian for Note-Taking

Obsidian is a powerful knowledge base and note-taking application that works on top of a local folder of plain text Markdown files.

1. **Download and Install Obsidian**:
   - Go to [obsidian.md](https://obsidian.md/) and download the free version for your platform
   - Install the application following the on-screen instructions

2. **Setting Up Obsidian**:
   - Launch Obsidian
   - Choose "Open folder as vault" (A vault is just a folder where Obsidian stores your notes)
   - **Important**: Navigate to and select the `docs` folder in this project
   - This ensures all documentation is kept in the same location and can be version-controlled
   - If prompted, trust the author of the vault

3. **Using Obsidian**:
   - Create new notes with the "New note" button
   - Link between notes using `[[double brackets]]`
   - Organize notes with folders and tags
   - Use Markdown syntax for formatting:
     ```markdown
     # Heading 1
     ## Heading 2
     **Bold text**
     *Italic text*
     - Bullet list
     1. Numbered list
     ```

4. **Recommended Plugins** (Optional):
   - Go to Settings → Community plugins → Turn on Community plugins
   - Browse and install plugins like:
     - Calendar
     - Dataview (for querying your notes)
     - Advanced Tables
     - Citations (for academic references)

5. **Syncing** (Optional):
   - Obsidian's files are just plain text files in your project's `docs` folder
   - They will be included in your Git repository for version control
   - For more advanced sync, consider Obsidian Sync (paid service) or use your own solution like Dropbox/Google Drive

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

### Optional but Recommended
- "Git Graph": Visualize Git history
- "GitLens": Enhanced Git capabilities
- "Markdown All in One": Markdown support for documentation

# Installing Dependencies

## First-time Setup for Collaborators

### Installing Poetry (Python Dependency Manager)

Before installing project dependencies, you need to install Poetry:

```bash
# On macOS/Linux/WSL
curl -sSL https://install.python-poetry.org | python3 -

# On Windows (PowerShell)
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -
```

Verify installation:

```bash
poetry --version
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

## Installing Python Dependencies with Poetry

This project uses Poetry for Python dependencies. The project is already initialized.

1. Install all project dependencies:

   ```bash
   poetry install
   ```
   
   This will read the `pyproject.toml` and `poetry.lock` files and install all required packages.

2. Activate the virtual environment:

   ```bash
   poetry shell
   ```

3. If you need to add a new dependency:

   ```bash
   # Add a regular dependency
   poetry add package-name
   
   # Add a development dependency
   poetry add package-name --group dev
   ```

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

### Python (Poetry)

```bash
# Update all dependencies
poetry update

# Update a specific package
poetry update package-name
```

### R (renv)

```r
# Update all packages
renv::update()

# Update a specific package
renv::update("package-name")
```
