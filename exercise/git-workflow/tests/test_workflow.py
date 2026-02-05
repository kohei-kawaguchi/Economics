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


# Test: Multiple commits exist
def test_multiple_commits():
    """Repository should have multiple commits (not everything squashed)."""
    commits = get_commits()
    # At least 2 commits: initial + implementation
    assert len(commits) >= 2, (
        f"Expected at least 2 commits, found {len(commits)}. "
        "Make separate commits for each logical change."
    )


# Test: Commit message references issue
def test_commit_references_issue():
    """At least one commit should reference an issue (e.g., #1)."""
    commits = get_commits()
    issue_pattern = re.compile(r"#\d+")

    has_issue_reference = any(issue_pattern.search(c["message"]) for c in commits)

    assert has_issue_reference, (
        "No commit references an issue. "
        "Use 'closes #1' or 'fixes #1' in your commit message."
    )


# Test: Commit message starts with verb
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
    ]

    for commit in commits:
        message = commit["message"].lower()
        first_word = message.split()[0] if message.split() else ""

        starts_with_verb = any(first_word.startswith(v) for v in valid_verbs)

        assert starts_with_verb, (
            f"Commit message should start with a verb: '{commit['message']}'. "
            f"Use verbs like: Add, Fix, Update, Implement, etc."
        )


# Test: Commit message is not too generic
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
        "complete",
    ]

    for commit in commits:
        message = commit["message"].lower().strip()

        is_generic = message in generic_messages or len(message) < 10

        assert not is_generic, (
            f"Commit message is too generic: '{commit['message']}'. "
            "Write a descriptive message explaining what and why."
        )


# Test: Commit message is relevant to changes
def test_commit_message_relevant():
    """Commit message should mention relevant content for changed files."""
    commits = get_commits()

    file_keywords = {
        "src/analysis.py": [
            "mean",
            "calculate",
            "function",
            "analysis",
            "implement",
        ],
    }

    for commit in commits:
        message = commit["message"].lower()
        files = commit["files"]

        for file, keywords in file_keywords.items():
            if file in files:
                has_relevant_keyword = any(kw in message for kw in keywords)
                assert has_relevant_keyword, (
                    f"Commit modifying '{file}' should mention relevant terms. "
                    f"Message: '{commit['message']}'. "
                    f"Consider using: {', '.join(keywords)}"
                )


# Test: Implementation commit is minimal
def test_implementation_commit_minimal():
    """The commit implementing calculate_mean should only modify src/analysis.py."""
    commits = get_commits()

    for commit in commits:
        message = commit["message"].lower()
        files = commit["files"]

        # Check commits that implement the mean function
        if "mean" in message or "calculate" in message:
            non_analysis_files = [f for f in files if f != "src/analysis.py"]

            assert len(non_analysis_files) == 0, (
                f"Implementation commit should only modify src/analysis.py, "
                f"but also modified: {non_analysis_files}. "
                "Keep commits minimal and focused."
            )


# Test: Closed issue exists
def test_closed_issue_exists():
    """Repository should have at least one closed issue."""
    repo = os.environ.get("GITHUB_REPOSITORY", "")

    if not repo:
        # Running locally, skip this test
        return

    issues = run_gh(["issue", "list", "--state", "closed", "--json", "number"])

    assert issues and issues != "[]", (
        "No closed issues found. "
        "Create an issue and close it via PR or manually."
    )


# Test: Merged PR exists
def test_merged_pr_exists():
    """Repository should have at least one merged pull request."""
    repo = os.environ.get("GITHUB_REPOSITORY", "")

    if not repo:
        # Running locally, skip this test
        return

    prs = run_gh(["pr", "list", "--state", "merged", "--json", "number"])

    assert prs and prs != "[]", (
        "No merged pull requests found. "
        "Create a PR from your feature branch and merge it."
    )
