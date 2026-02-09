"""Tests for git workflow compliance."""

import os
import subprocess
from pathlib import Path


def get_git_root() -> Path:
    result = subprocess.run(
        ["git", "rev-parse", "--show-toplevel"],
        capture_output=True,
        text=True,
    )
    return Path(result.stdout.strip())


def run_git(args: list[str]) -> str:
    """Run a git command and return output."""
    git_root = get_git_root()
    result = subprocess.run(
        ["git", "-C", str(git_root)] + args,
        capture_output=True,
        text=True,
    )
    return result.stdout.strip()


def run_gh(args: list[str]) -> str:
    """Run a gh command and return output."""
    result = subprocess.run(
        ["gh"] + args,
        capture_output=True,
        text=True,
    )
    return result.stdout.strip()


def get_assignment_pathspec() -> str:
    git_root = get_git_root()
    assignment_root = Path(__file__).parent.parent.resolve()
    rel = os.path.relpath(assignment_root, start=git_root)
    return rel


def get_commits():
    """Get list of commits (hash, message, files changed)."""
    pathspec = get_assignment_pathspec()
    log = run_git(["log", "--pretty=format:%H|%s", "--name-only", "--", pathspec])
    commits = []
    current_commit = None

    for line in log.split("\n"):
        if "|" in line:
            parts = line.split("|", 1)
            if current_commit:
                commits.append(current_commit)
            current_commit = {
                "hash": parts[0],
                "message": parts[1],
                "files": [],
            }
        elif line and current_commit:
            current_commit["files"].append(line)

    if current_commit:
        commits.append(current_commit)

    return commits


def is_relevant_commit_message(message: str) -> bool:
    normalized = message.strip().lower()
    if not normalized:
        return False

    words = normalized.split()
    generic_single_words = {
        "update",
        "fix",
        "changes",
        "wip",
        "test",
        "misc",
        "temp",
        "commit",
        "save",
        "done",
    }
    if len(words) == 1 and words[0] in generic_single_words:
        return False

    return True


def test_has_commits():
    commits = [c for c in get_commits() if c["files"]]
    assert commits, "No commits found for this assignment."


def test_commit_messages_are_relevant():
    commits = [c for c in get_commits() if c["files"]]

    for commit in commits:
        assert is_relevant_commit_message(message=commit["message"]), (
            "Commit message is too generic. "
            f"Message: '{commit['message']}'. "
            "Use a short but specific message."
        )


def test_closed_issue_exists():
    """Repository should have at least one closed issue."""
    repo = os.environ.get("GITHUB_REPOSITORY", "")
    if not repo:
        return

    issues = run_gh(["issue", "list", "--state", "closed", "--json", "number"])

    assert issues and issues != "[]", (
        "No closed issues found. "
        "Create an issue and close it via PR or manually."
    )


def test_merged_pr_exists():
    """Repository should have at least one merged pull request."""
    repo = os.environ.get("GITHUB_REPOSITORY", "")
    if not repo:
        return

    prs = run_gh(["pr", "list", "--state", "merged", "--json", "number"])

    assert prs and prs != "[]", (
        "No merged pull requests found. "
        "Create a PR from your feature branch and merge it."
    )

