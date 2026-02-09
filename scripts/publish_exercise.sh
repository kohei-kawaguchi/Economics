#!/bin/bash
#
# Publish an exercise folder to a standalone GitHub repository
#
# Usage:
#   ./scripts/publish_exercise.sh <exercise-folder> <github-org>
#   ./scripts/publish_exercise.sh --all <github-org>
#
# Example:
#   ./scripts/publish_exercise.sh git-workflow my-org
#   ./scripts/publish_exercise.sh --all my-org
#
# This will:
#   1. Create a new repository 'git-workflow' in 'my-org'
#   2. Push contents of 'exercise/git-workflow/' to that repository
#   3. Mark it as a template repository for GitHub Classroom

set -e

MODE="$1"
EXERCISE_NAME="$1"
GITHUB_ORG="$2"

if [ "$MODE" = "--all" ]; then
    if [ -z "$GITHUB_ORG" ]; then
        echo "Usage: $0 --all <github-org>"
        echo "Example: $0 --all my-org"
        exit 1
    fi
else
    if [ -z "$EXERCISE_NAME" ] || [ -z "$GITHUB_ORG" ]; then
        echo "Usage: $0 <exercise-folder> <github-org>"
        echo "Example: $0 git-workflow my-org"
        echo "Usage: $0 --all <github-org>"
        echo "Example: $0 --all my-org"
        exit 1
    fi
fi

# Find gh command (handle Windows Git Bash PATH issue)
GH_CMD=""
if command -v gh &> /dev/null; then
    GH_CMD="gh"
elif command -v gh.exe &> /dev/null; then
    GH_CMD="gh.exe"
elif [ -f "/c/Program Files/GitHub CLI/gh.exe" ]; then
    GH_CMD="/c/Program Files/GitHub CLI/gh.exe"
elif [ -f "$LOCALAPPDATA/Programs/GitHub CLI/gh.exe" ]; then
    GH_CMD="$LOCALAPPDATA/Programs/GitHub CLI/gh.exe"
else
    echo "Error: GitHub CLI (gh) is not installed or not found"
    echo "Install it from: https://cli.github.com/"
    echo "If installed, add it to Git Bash PATH or run from PowerShell"
    exit 1
fi

echo "Using gh: $GH_CMD"

# Check if authenticated
if ! "$GH_CMD" auth status &> /dev/null; then
    echo "Error: Not authenticated with GitHub CLI"
    echo "Run: gh auth login"
    exit 1
fi

publish_one() {
    local exercise_name="$1"
    local github_org="$2"

    local exercise_dir="exercise/$exercise_name"
    local repo_name="$exercise_name"

    if [ ! -d "$exercise_dir" ]; then
        echo "Error: Exercise directory '$exercise_dir' does not exist"
        exit 1
    fi

    echo "Publishing exercise: $exercise_name"
    echo "  Source: $exercise_dir"
    echo "  Target: $github_org/$repo_name"
    echo ""

    # Create repository on GitHub (skip if already exists)
    if "$GH_CMD" repo view "$github_org/$repo_name" &> /dev/null; then
        echo "Repository $github_org/$repo_name already exists, updating..."
    else
        echo "Creating repository $github_org/$repo_name..."
        "$GH_CMD" repo create "$github_org/$repo_name" \
            --public \
            --description "Exercise: $exercise_name" \
            --clone=false
    fi

    # Initialize git and push
    (
        cd "$exercise_dir"

        # Remove existing .git if present (in case of re-run)
        if [ -d ".git" ]; then
            rm -rf .git
        fi

        git init
        git add .
        git commit -m "Update exercise"
        git branch -M main
        git remote add origin "https://github.com/$github_org/$repo_name.git"
        git push -u origin main --force
    )

    # Mark as template repository (if not already)
    echo ""
    echo "Ensuring repository is marked as template..."
    "$GH_CMD" repo edit "$github_org/$repo_name" --template 2>/dev/null || true

    echo ""
    echo "Done!"
    echo ""
    echo "Repository: https://github.com/$github_org/$repo_name"
    echo ""
    echo "Next steps:"
    echo "  1. Go to GitHub Classroom"
    echo "  2. Create a new assignment"
    echo "  3. Select '$github_org/$repo_name' as the template repository"
}

if [ "$MODE" = "--all" ]; then
    for d in exercise/*/; do
        publish_one "$(basename "$d")" "$GITHUB_ORG"
        echo ""
        echo "----------------------------------------"
        echo ""
    done
else
    publish_one "$EXERCISE_NAME" "$GITHUB_ORG"
fi
