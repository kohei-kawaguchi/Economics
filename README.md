# Economics

Description of your project goes here.

## Installation

This project uses Poetry for dependency management. To get started:

1. Install Poetry if you haven't already:
   ```bash
   curl -sSL https://install.python-poetry.org | python3 -
   ```

2. Install dependencies:
   ```bash
   poetry install
   ```

## Usage

You can run the package in several ways:

1. Using Python module syntax:
   ```bash
   poetry run python -m economics.main
   ```

2. Using the CLI command (after adding script entry point):
   ```bash
   poetry run economics
   ```

3. In development, activate the poetry shell first:
   ```bash
   poetry shell
   python -m economics.main  # or just 'economics' if script entry point is added
   ```

## Development

- Run tests: `poetry run pytest`
- Format code: `poetry run black .`
- Sort imports: `poetry run isort .`
- Lint code: `poetry run flake8` 