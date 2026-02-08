# Bash Commands and Vim Exercise

Practice essential bash commands and basic vim editing by creating files and directories, making a script executable, and documenting the commands you used. This assignment is designed to be completed with an issue based git workflow.

## Learning Objectives

Learn how to navigate directories, create and edit files, search text, and manage permissions from the terminal. Learn a minimal set of vim commands needed to edit files on a remote machine. Practice creating issues, working on branches, writing descriptive commits, and merging pull requests.

## Project Structure

```
bash-commands/
├── report/
│   └── answers.md         # <- Complete this file
├── tests/
│   ├── test_bash_tasks.py
│   └── test_workflow.py
├── pyproject.toml
└── README.md
```

## Setup

Accept this assignment on GitHub Classroom and clone your repository.

## Exercise Steps

Create an issue on GitHub titled `Complete bash commands exercise`. Create a branch from the issue and check it out locally.

Read `docs/workflow/bash_commands.md` in the Economics repository and use it as a reference. Follow the instructions in `report/answers.md` and complete the exercises by editing the files under `sandbox/`.

Run tests locally:

```bash
uv run pytest -v
```

Commit your changes with a descriptive message that references the issue number, for example `Complete bash commands exercise, closes #1`. Push your branch, open a pull request, and merge it.

## Grading Criteria

Your submission is graded on two components.

Documentation and bash tasks are graded by `tests/test_bash_tasks.py`. Git workflow is graded by `tests/test_workflow.py` and by the presence of a closed issue and a merged pull request on GitHub.

## Verification

Verify that all tests pass locally using `uv run pytest -v`, then verify that GitHub Actions passes on your pull request.

