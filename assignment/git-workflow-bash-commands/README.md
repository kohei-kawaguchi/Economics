# Git Workflow and Bash Commands Assignment

Complete a small coding task and a terminal editing task using an issue-based git workflow. This assignment uses the same structure and grading style as the exercises, but the task content is different.

## Learning objectives

Learn an issue-based git workflow: create an issue, branch from the issue, write descriptive commits that reference the issue, open a pull request, and merge it. Practice essential bash commands and minimal vim editing by creating files and editing text precisely.

## Project structure

```
git-workflow-bash-commands/
├── input/
│   └── numbers.csv
├── config/
│   └── analysis.json
├── src/
│   ├── __init__.py
│   └── analysis.py
├── scripts/
│   └── run_analysis.py
├── sandbox/
│   ├── dotfiles/
│   │   ├── .bash_profile
│   │   └── .bashrc
│   ├── notes/
│   │   ├── commands.txt
│   │   └── vim_exercise.txt
│   └── scripts/
│       └── hello.sh
├── output/
│   └── .gitkeep
├── report/
│   └── answers.md
├── tests/
│   ├── test_analysis.py
│   ├── test_bash_tasks.py
│   └── test_workflow.py
├── pyproject.toml
└── README.md
```

## Setup

Accept this assignment on GitHub Classroom and clone your repository.

## Exercise steps

Create an issue on GitHub titled `Complete combined assignment`. Create a branch from the issue and check it out locally.

Complete both parts of the assignment.

For the coding task, implement `calculate_trimmed_mean` in `src/analysis.py`, then run:

```bash
uv run python scripts/run_analysis.py
uv run pytest tests/test_analysis.py -v
```

For the terminal and vim tasks, follow the instructions in `report/answers.md`, edit the files under `sandbox/`, then run:

```bash
uv run pytest tests/test_bash_tasks.py -v
```

Run the full test suite:

```bash
uv run pytest -v
```

Make multiple commits as you work. Use relevant commit messages. Push your branch, open a pull request, and merge it.

## Grading criteria

Your submission is graded on three components.

Code correctness is graded by `tests/test_analysis.py`. Bash tasks are graded by `tests/test_bash_tasks.py`. Git workflow is graded by `tests/test_workflow.py` and by the presence of a closed issue and a merged pull request on GitHub.

## Verification

Verify that all tests pass locally using `uv run pytest -v`, then verify that GitHub Actions passes on your pull request.

