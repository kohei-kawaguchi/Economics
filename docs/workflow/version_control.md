# Minimal Git Workflow

This document outlines a simple and effective git workflow for individual and team projects.

## Basic Git Workflow

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   ```

2. **Create a branch**
   ```bash
   git switch -c <branch-name>
   ```
   
   Naming conventions:
   - `feature/<feature-name>` - For new features
   - `fix/<bug-name>` - For bug fixes
   - `docs/<doc-name>` - For documentation changes

3. **Make changes** to your files

4. **Stage changes**
   ```bash
   git add <file-name>  # Stage specific files
   git add .            # Stage all changes
   ```

5. **Commit changes**
   ```bash
   git commit -m "Descriptive commit message"
   ```
   
   Good commit messages:
   - Start with a verb (Add, Fix, Update, etc.)
   - Be specific and concise
   - Reference issue numbers when applicable

6. **Pull latest changes** from the main branch
   ```bash
   git switch main
   git pull
   git switch <your-branch>
   git merge main  # Resolve any conflicts
   ```

7. **Push your branch**
   ```bash
   git push -u origin <branch-name>
   ```

8. **Create Pull Request** in the git hosting service (GitHub, GitLab, etc.)

9. **After approval, merge** your changes into the main branch

## Using GitHub as a Remote Host

### Working with an Existing Repository

1. **Clone the repository created by the project owner**
   ```bash
   git clone https://github.com/project-owner/repository-name.git
   cd repository-name
   ```

2. **Set up tracking of the upstream repository (if you're working with a fork)**
   ```bash
   git remote add upstream https://github.com/project-owner/repository-name.git
   ```

3. **Check remotes to confirm setup**
   ```bash
   git remote -v
   ```
   You should see:
   ```
   origin      https://github.com/your-username/repository-name.git (fetch)
   origin      https://github.com/your-username/repository-name.git (push)
   upstream    https://github.com/project-owner/repository-name.git (fetch)
   upstream    https://github.com/project-owner/repository-name.git (push)
   ```

4. **Keep your local repository in sync with upstream**
   ```bash
   # Fetch changes from upstream
   git fetch upstream
   
   # Switch to your local main branch
   git switch main
   
   # Merge upstream changes into your local main
   git merge upstream/main
   
   # Push the changes to your origin (if you're working with a fork)
   git push origin main
   ```

### Issue-Based Development Workflow

1. **Create an issue on GitHub**
   - Navigate to the project repository on GitHub
   - Click on the "Issues" tab
   - Click "New issue"
   - Add a descriptive title and detailed description of the feature or bug
   - Apply appropriate labels (bug, enhancement, documentation, etc.)
   - Assign the issue to yourself or leave it unassigned
   - Click "Submit new issue"
   - Note the issue number (e.g., #42)

2. **Create a branch directly from the issue**
   - On the issue page, look for the "Development" section on the right sidebar
   - Click "Create a branch" link
   - GitHub will suggest a branch name based on the issue (e.g., `42-fix-login-bug`)
   - Select "Checkout locally" option
   - Follow the provided commands to create and switch to the branch locally:
   ```bash
   git fetch origin
   git switch -c 42-fix-login-bug origin/main
   ```

3. **Make your changes** and commit with issue reference
   ```bash
   # Make your changes to the code
   git add .
   git commit -m "Fix login validation issue, closes #42"
   ```

4. **Push your branch to GitHub**
   ```bash
   git push -u origin 42-fix-login-bug
   ```

5. **Create a pull request linked to the issue**
   - GitHub will often show a prompt to create a PR for your recently pushed branch
   - Click "Compare & pull request"
   - The PR will automatically link to the issue since you referenced it in the commit message
   - Add additional details about your implementation
   - Request reviews from team members
   - Click "Create pull request"

6. **Address review feedback**
   - Make additional commits to your branch as needed
   - Push changes to automatically update the PR
   - Respond to comments

7. **After approval, merge your changes**
   - Choose the merge method (merge, squash, or rebase)
   - The issue will automatically close when the PR is merged if you used the "closes #42" syntax

### GitHub-Specific Features

1. **Issues**
   - Use issues to track bugs, enhancements, and tasks
   - Provide detailed reproduction steps for bugs
   - Use templates if available in the repository
   - Use labels to categorize issues (bug, enhancement, documentation)
   - Assign priority labels if available (high, medium, low)

2. **Pull Requests**
   - Link PRs to issues using keywords (fixes, closes, resolves)
   - Add detailed descriptions of changes
   - Use the PR checklist if available
   - Request reviews from relevant team members
   - Address all review comments

3. **GitHub Actions**
   - Set up automated workflows in the `.github/workflows` directory
   - Automate testing, building, and deployment processes
   - Check the status of CI/CD checks on your PRs

4. **GitHub Pages**
   - Host static websites directly from your repository
   - Enable in repository settings under "Pages"

## Common Commands

| Command | Description |
|---------|-------------|
| `git status` | Check the status of files |
| `git diff` | See changes between commits |
| `git log` | View commit history |
| `git reset HEAD~1` | Undo the last commit (keeping changes) |
| `git stash` | Temporarily store changes |
| `git stash pop` | Retrieve stashed changes |
| `git switch <branch-name>` | Switch to an existing branch |
| `git switch -c <branch-name>` | Create and switch to a new branch |
| `git switch -` | Switch back to the previous branch |

## Best Practices

- Commit often with clear, descriptive messages
- Pull changes regularly to avoid big merge conflicts
- Create focused branches for specific features or fixes
- Write meaningful commit messages
- Review your changes before committing
- Always sync with the upstream repository before starting new work
- Use `git switch` instead of `git checkout` for branch operations (Git 2.23+)
- Always start work by creating an issue first
- Reference issue numbers in commit messages to maintain traceability
