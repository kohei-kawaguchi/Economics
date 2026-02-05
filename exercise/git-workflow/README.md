# Git Workflow Exercise

Practice the issue-based git workflow by completing a simple coding task following reproducible code principles.

## Learning Objectives

- Create issues on GitHub
- Create branches from issues
- Write descriptive commit messages
- Create pull requests linked to issues
- Follow reproducible code project structure

## Project Structure

```
git-workflow/
├── input/              # Raw data (never modify)
│   └── numbers.csv
├── config/             # Configuration files
│   └── analysis.json
├── src/                # Source code modules
│   └── analysis.py     # <- Implement calculate_mean here
├── scripts/            # Execution scripts
│   └── run_analysis.py
├── output/             # Results (generated)
├── tests/              # Tests
├── pyproject.toml      # Dependencies
└── README.md
```

## Setup

1. Accept this assignment on GitHub Classroom
2. Clone your repository:
   ```bash
   git clone <your-repository-url>
   cd <repository-name>
   ```

## Exercise Steps

### Step 1: Create an Issue

1. Go to your repository on GitHub
2. Click "Issues" tab
3. Click "New issue"
4. Title: `Implement calculate_mean function`
5. Description: `Implement the calculate_mean function in src/analysis.py`
6. Click "Submit new issue"
7. Note the issue number (e.g., #1)

### Step 2: Create a Branch from the Issue

1. On the issue page, find "Development" section on the right sidebar
2. Click "Create a branch"
3. Use the suggested branch name
4. Select "Checkout locally"
5. Run the provided commands in your terminal:
   ```bash
   git fetch origin
   git switch <branch-name>
   ```

### Step 3: Complete the Task

1. Open `src/analysis.py`
2. Implement the `calculate_mean` function (replace the TODO)
3. Run the analysis:
   ```bash
   uv run python scripts/run_analysis.py
   ```
4. Run the tests to verify:
   ```bash
   uv run pytest tests/test_analysis.py -v
   ```

### Step 4: Commit Your Changes

```bash
git add src/analysis.py
git commit -m "Implement calculate_mean function, closes #1"
```

Note: Using `closes #1` will automatically close the issue when merged.

### Step 5: Push Your Branch

```bash
git push -u origin <branch-name>
```

### Step 6: Create a Pull Request

1. Go to your repository on GitHub
2. Click "Compare & pull request"
3. Add a description of your changes
4. Click "Create pull request"

### Step 7: Merge the Pull Request

1. Review your changes in the PR
2. Click "Merge pull request"
3. Click "Confirm merge"
4. Check that your issue is now closed

## Grading Criteria

Your submission is graded on two components:

**Code Correctness (50 points)**
- `calculate_mean` function returns correct results

**Git Workflow (50 points)**
- Multiple commits (not everything in one commit)
- Commit message references issue (e.g., `closes #1`)
- Commit messages start with verb (Add, Fix, Update, Implement, etc.)
- Commit messages are descriptive (not generic like "update" or "fix")
- Commit messages mention relevant content (e.g., "mean" when implementing mean)
- Implementation commit only modifies `src/analysis.py` (minimal)
- Issue is closed
- Pull request is merged

## Verification

After completing all steps, verify:

- [ ] Issue is closed
- [ ] Pull request is merged
- [ ] `main` branch contains your changes
- [ ] Code tests pass: `uv run pytest tests/test_analysis.py -v`
- [ ] Workflow tests pass: `uv run pytest tests/test_workflow.py -v`

## Reproducible Code Principles

This exercise follows key reproducibility principles:

1. **Config = Data**: Parameters are in `config/analysis.json`, not hardcoded
2. **Stable Paths**: Input in `input/`, output in `output/`, no timestamps
3. **Named Arguments**: Function calls use keyword arguments
4. **Project Structure**: Separate folders for input, config, src, scripts, output
