# Git Workflow Exercise

Practice the issue-based git workflow by completing a simple coding task.

## Learning Objectives

- Create issues on GitHub
- Create branches from issues
- Write descriptive commit messages
- Create pull requests linked to issues

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
4. Title: `Add mean calculation function`
5. Description: `Implement the calculate_mean function in analysis.py`
6. Click "Submit new issue"
7. Note the issue number (e.g., #1)

### Step 2: Create a Branch from the Issue

1. On the issue page, find "Development" section on the right sidebar
2. Click "Create a branch"
3. Use the suggested branch name or name it `feature/add-mean-calculation`
4. Select "Checkout locally"
5. Run the provided commands in your terminal:
   ```bash
   git fetch origin
   git switch <branch-name>
   ```

### Step 3: Complete the Task

1. Open `analysis.py`
2. Implement the `calculate_mean` function (replace the TODO)
3. Test your code:
   ```bash
   uv run python analysis.py
   ```
4. Run the tests to verify:
   ```bash
   uv run pytest tests/test_analysis.py -v
   ```

### Step 4: Commit Your Changes

```bash
git add analysis.py
git commit -m "Add mean calculation function, closes #1"
```

Note: Using `closes #1` will automatically close the issue when merged.

### Step 5: Push Your Branch

```bash
git push -u origin <branch-name>
```

### Step 6: Create a Pull Request

1. Go to your repository on GitHub
2. Click "Compare & pull request" (or go to "Pull requests" > "New pull request")
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
- Commit messages start with verb (Add, Fix, Update, etc.)
- Commit messages are descriptive (not generic like "update" or "fix")
- Commit messages mention relevant content (e.g., "mean" when implementing mean)
- Implementation commit only modifies `analysis.py` (minimal)
- Issue is closed
- Pull request is merged

## Verification

After completing all steps, verify:

- [ ] Issue #1 is closed
- [ ] Pull request is merged
- [ ] `main` branch contains your changes
- [ ] Code tests pass: `uv run pytest tests/test_analysis.py -v`
- [ ] Workflow tests pass: `uv run pytest tests/test_workflow.py -v`

## Reference

See [Git Workflow Documentation](https://github.com/your-org/docs/workflow/version_control.md) for detailed explanations.
