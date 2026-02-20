#!/bin/bash
#
# Publish hidden pytest suites for one exercise to a private repository,
# and set the corresponding GitHub Actions variables/secrets on the public
# classroom repository.
#
# Usage:
#   ./scripts/publish_hidden_tests.sh <exercise-folder> <public-org> <private-tests-repo>
#
# Example:
#   ./scripts/publish_hidden_tests.sh randomization_inference_variant my-org my-org/private-autograde-tests
#
# Required:
#   - Hidden test source exists at: exercise/<exercise-folder>/tests/
#   - Public classroom repo exists at: <public-org>/<exercise-folder>
#   - GitHub CLI authenticated (`gh auth login`)
#
# Optional environment variable:
#   - HIDDEN_TESTS_TOKEN_VALUE:
#       If set, this script writes it to secret HIDDEN_TESTS_TOKEN
#       in the public classroom repository.
#

set -e

EXERCISE_NAME="$1"
PUBLIC_ORG="$2"
PRIVATE_TEST_REPO="$3"

if [ -z "$EXERCISE_NAME" ] || [ -z "$PUBLIC_ORG" ] || [ -z "$PRIVATE_TEST_REPO" ]; then
    echo "Usage: $0 <exercise-folder> <public-org> <private-tests-repo>"
    echo "Example: $0 randomization_inference_variant my-org my-org/private-autograde-tests"
    exit 1
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
    exit 1
fi

if ! "$GH_CMD" auth status &> /dev/null; then
    echo "Error: Not authenticated with GitHub CLI"
    echo "Run: gh auth login"
    exit 1
fi

SOURCE_TEST_DIR="exercise/$EXERCISE_NAME/tests"
PUBLIC_REPO="$PUBLIC_ORG/$EXERCISE_NAME"
TARGET_SUBDIR="$EXERCISE_NAME"

if [ ! -d "$SOURCE_TEST_DIR" ]; then
    echo "Error: Hidden test source directory does not exist: $SOURCE_TEST_DIR"
    exit 1
fi

if ! "$GH_CMD" repo view "$PUBLIC_REPO" &> /dev/null; then
    echo "Error: Public classroom repository not found: $PUBLIC_REPO"
    echo "Run publish_exercise.sh first."
    exit 1
fi

if "$GH_CMD" repo view "$PRIVATE_TEST_REPO" &> /dev/null; then
    echo "Private test repository exists: $PRIVATE_TEST_REPO"
else
    echo "Creating private test repository: $PRIVATE_TEST_REPO"
    "$GH_CMD" repo create "$PRIVATE_TEST_REPO" --private --description "Hidden autograde tests"
fi

TMP_DIR="$(mktemp -d)"
cleanup() {
    rm -rf "$TMP_DIR"
}
trap cleanup EXIT

echo "Cloning private test repository..."
"$GH_CMD" repo clone "$PRIVATE_TEST_REPO" "$TMP_DIR/private-tests"

mkdir -p "$TMP_DIR/private-tests/$TARGET_SUBDIR"
rm -rf "$TMP_DIR/private-tests/$TARGET_SUBDIR"/*
cp -r "$SOURCE_TEST_DIR"/. "$TMP_DIR/private-tests/$TARGET_SUBDIR"/

(
    cd "$TMP_DIR/private-tests"

    git add "$TARGET_SUBDIR"
    if git diff --cached --quiet; then
        echo "No hidden test changes to push."
    else
        git commit -m "Update hidden tests: $EXERCISE_NAME"
        git push
        echo "Hidden tests pushed to $PRIVATE_TEST_REPO/$TARGET_SUBDIR"
    fi
)

echo "Setting GitHub Actions variables on $PUBLIC_REPO"
"$GH_CMD" variable set HIDDEN_TESTS_REPO --repo "$PUBLIC_REPO" --body "$PRIVATE_TEST_REPO"
"$GH_CMD" variable set HIDDEN_TESTS_REF --repo "$PUBLIC_REPO" --body "main"
"$GH_CMD" variable set HIDDEN_TESTS_PATH --repo "$PUBLIC_REPO" --body ".hidden_tests/$TARGET_SUBDIR"

if [ -n "$HIDDEN_TESTS_TOKEN_VALUE" ]; then
    echo "Setting secret HIDDEN_TESTS_TOKEN on $PUBLIC_REPO"
    printf "%s" "$HIDDEN_TESTS_TOKEN_VALUE" | "$GH_CMD" secret set HIDDEN_TESTS_TOKEN --repo "$PUBLIC_REPO" --body -
else
    echo "HIDDEN_TESTS_TOKEN_VALUE is not set."
    echo "Set secret manually or rerun with:"
    echo "  HIDDEN_TESTS_TOKEN_VALUE=<token> $0 $EXERCISE_NAME $PUBLIC_ORG $PRIVATE_TEST_REPO"
fi

echo "Done."
echo "Public classroom repo: https://github.com/$PUBLIC_REPO"
echo "Private hidden-test repo: https://github.com/$PRIVATE_TEST_REPO"
