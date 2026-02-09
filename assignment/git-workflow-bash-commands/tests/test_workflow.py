"""Tests for git workflow compliance."""

import os
import subprocess


def run_gh(args: list[str]) -> str:
    """Run a gh command and return output."""
    result = subprocess.run(
        ["gh"] + args,
        capture_output=True,
        text=True,
    )
    return result.stdout.strip()


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

