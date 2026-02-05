#!/bin/bash
#
# Publish an exercise folder to a standalone GitHub repository
#
# Usage:
#   ./scripts/publish_exercise.sh <exercise-folder> <github-org>
#
# Example:
#   ./scripts/publish_exercise.sh git-workflow my-org
#
# This will:
#   1. Create a new repository 'git-workflow' in 'my-org'
#   2. Push contents of 'exercise/git-workflow/' to that repository
#   3. Mark it as a template repository for GitHub Classroom

set -e

EXERCISE_NAME="$1"
GITHUB_ORG="$2"

if [ -z "$EXERCISE_NAME" ] || [ -z "$GITHUB_ORG" ]; then
    echo "Usage: $0 <exercise-folder> <github-org>"
    echo "Example: $0 git-workflow my-org"
    exit 1
fi

EXERCISE_DIR="exercise/$EXERCISE_NAME"
REPO_NAME="$EXERCISE_NAME"

if [ ! -d "$EXERCISE_DIR" ]; then
    echo "Error: Exercise directory '$EXERCISE_DIR' does not exist"
    exit 1
fi

echo "Publishing exercise: $EXERCISE_NAME"
echo "  Source: $EXERCISE_DIR"
echo "  Target: $GITHUB_ORG/$REPO_NAME"
echo ""

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

# Create repository on GitHub (skip if already exists)
if "$GH_CMD" repo view "$GITHUB_ORG/$REPO_NAME" &> /dev/null; then
    echo "Repository $GITHUB_ORG/$REPO_NAME already exists, updating..."
else
    echo "Creating repository $GITHUB_ORG/$REPO_NAME..."
    "$GH_CMD" repo create "$GITHUB_ORG/$REPO_NAME" \
        --public \
        --description "Exercise: $EXERCISE_NAME" \
        --clone=false
fi

# Initialize git and push
cd "$EXERCISE_DIR"

# Remove existing .git if present (in case of re-run)
if [ -d ".git" ]; then
    rm -rf .git
fi

git init
git add .
git commit -m "Update exercise"
git branch -M main
git remote add origin "https://github.com/$GITHUB_ORG/$REPO_NAME.git"
git push -u origin main --force

# Mark as template repository (if not already)
echo ""
echo "Ensuring repository is marked as template..."
"$GH_CMD" repo edit "$GITHUB_ORG/$REPO_NAME" --template 2>/dev/null || true

echo ""
echo "Done!"
echo ""
echo "Repository: https://github.com/$GITHUB_ORG/$REPO_NAME"
echo ""
echo "Next steps:"
echo "  1. Go to GitHub Classroom"
echo "  2. Create a new assignment"
echo "  3. Select '$GITHUB_ORG/$REPO_NAME' as the template repository"
