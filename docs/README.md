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
