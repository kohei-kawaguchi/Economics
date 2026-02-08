"""Tests for git workflow compliance."""

import os
import re
import subprocess


def run_git(args):
    """Run a git command and return output."""
    result = subprocess.run(
        ["git"] + args,
        capture_output=True,
        text=True,
    )
    return result.stdout.strip()


def run_gh(args):
    """Run a gh command and return output."""
    result = subprocess.run(
        ["gh"] + args,
        capture_output=True,
        text=True,
    )
    return result.stdout.strip()


def get_commits():
    """Get list of commits (hash, message, files changed)."""
    log = run_git(["log", "--pretty=format:%H|%s", "--name-only"])
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


def test_multiple_commits():
    """Repository should have multiple commits (not everything squashed)."""
    commits = get_commits()
    assert len(commits) >= 2, (
        f"Expected at least 2 commits, found {len(commits)}. "
        "Make separate commits for each logical change."
    )


def test_commit_references_issue():
    """At least one commit should reference an issue (e.g., #1)."""
    commits = get_commits()
    issue_pattern = re.compile(r"#\d+")
    has_issue_reference = any(issue_pattern.search(c["message"]) for c in commits)
    assert has_issue_reference, (
        "No commit references an issue. "
        "Use 'closes #1' or 'fixes #1' in your commit message."
    )


def test_commit_message_starts_with_verb():
    """Commit messages should start with an action verb."""
    commits = get_commits()

    valid_verbs = [
        "add",
        "fix",
        "update",
        "implement",
        "remove",
        "delete",
        "refactor",
        "improve",
        "change",
        "create",
        "modify",
        "correct",
        "resolve",
        "merge",
        "initial",
        "complete",
    ]

    for commit in commits:
        message = commit["message"].lower()
        first_word = message.split()[0] if message.split() else ""
        starts_with_verb = any(first_word.startswith(v) for v in valid_verbs)
        assert starts_with_verb, (
            f"Commit message should start with a verb: '{commit['message']}'. "
            "Use verbs like: Add, Fix, Update, Implement, etc."
        )


def test_commit_message_not_generic():
    """Commit messages should be descriptive, not generic."""
    commits = get_commits()

    generic_messages = [
        "update",
        "fix",
        "changes",
        "wip",
        "work in progress",
        "stuff",
        "misc",
        "temp",
        "test",
        "asdf",
        "commit",
        "save",
        "done",
        "finished",
    ]

    for commit in commits:
        message = commit["message"].lower().strip()
        is_generic = message in generic_messages or len(message) < 10
        assert not is_generic, (
            f"Commit message is too generic: '{commit['message']}'. "
            "Write a descriptive message explaining what and why."
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

