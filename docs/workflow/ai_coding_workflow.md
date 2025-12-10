# AI Coding Workflow

This document outlines the workflow for using AI coding assistants (Cursor, OpenAI Codex, Claude Code) as research assistants for economic research and development.

## Overview

AI coding assistants can serve as research assistants (RAs) for data science and economic analysis tasks. When properly supervised, they can:

- **Accelerate iterations** - Rapidly implement and test ideas
- **Parallelize tasks** - Work on multiple components simultaneously
- **Integrate research and implementation** - Translate theoretical models into code
- **Improve implementation quality** - Follow best practices and patterns

However, they require the same level of supervision as human RAs and should be managed using established project management best practices.

## Setting Up AI Coding Tools

### Cursor

Cursor is an AI-powered code editor built on VS Code that provides integrated AI assistance.

1. **Download and Install**
   - Visit [cursor.sh](https://cursor.sh/) and download the installer
   - Install following the platform-specific instructions
   - Cursor works similarly to VS Code but with built-in AI features

2. **Initial Setup**
   - Open Cursor and sign in with your account
   - Configure your preferences in Settings (Ctrl+, or Cmd+,)
   - Install recommended extensions (see IDE Extensions section in README.md)

3. **Using Cursor**
   - Press `Ctrl+K` (Windows/Linux) or `Cmd+K` (Mac) to open the AI chat
   - Use `Ctrl+L` (Windows/Linux) or `Cmd+L` (Mac) for inline editing
   - Select code and use the AI suggestions that appear
   - Configure AI model preferences in Settings → Features → Cursor Tab

### OpenAI Codex CLI

OpenAI Codex provides a command-line interface and VS Code/Cursor extension for AI-assisted coding.

1. **Install the CLI**
   ```bash
   # Install via npm (requires Node.js)
   npm install -g @openai/codex-cli
   ```

2. **Authenticate**
   ```bash
   codex auth
   ```
   Follow the prompts to authenticate with your OpenAI API key.

3. **Install VS Code/Cursor Extension**
   - Open VS Code/Cursor
   - Go to Extensions (Ctrl+Shift+X or Cmd+Shift+X)
   - Search for "OpenAI Codex" and install
   - Configure your API key in the extension settings

4. **Using Codex**
   - Codex is known for being smart and consistent
   - Access via the command palette (Ctrl+Shift+P or Cmd+Shift+P)
   - Use "Codex: Generate" commands
   - Conversation history stored in `~/.codex/sessions/YYYY/MM/DD/*.jsonl`

### Claude Code CLI

Claude Code provides a CLI and VS Code/Cursor extension with a focus on user experience.

1. **Install the CLI**
   - Visit [claude.com/product/claude-code](https://www.claude.com/product/claude-code)
   - Follow the installation instructions for your platform
   - Authenticate using your Anthropic API key

2. **Install VS Code/Cursor Extension**
   - Open VS Code/Cursor
   - Go to Extensions
   - Search for "Claude Code" and install
   - Configure your API key in settings

3. **Using Claude Code**
   - Known for excellent UI/UX and user-friendly interactions
   - Access via command palette or sidebar
   - Conversation history stored in `~/.claude/history.jsonl`

## Core Principles

### Supervise AI Like Human RAs

- Follow the same project management best practices you would use with human RAs
- Provide clear instructions and specifications
- Review and validate all outputs
- If AI doesn't work well, the issue is likely with project management, not the AI itself

### Theory-Driven Approach

Start from documented ground truth:

1. **Model Setting** - Define the mathematical model clearly
2. **Solution Method** - Specify the algorithm or approach
3. **Pseudocode** - Write detailed pseudocode before implementation
4. **Implementation** - Ask AI to implement based on the pseudocode

### Oral Exam Method

Develop ground truth interactively with AI:

1. Explain what you want to achieve
2. Ask AI if it knows how to implement it
3. Ask AI to search relevant sources until it returns a legitimate answer
4. Once a legitimate answer is obtained, ask AI to summarize it

This method is particularly effective for:
- Model-free analysis
- Data cleaning tasks
- Tasks where formal specification is cumbersome

## Workflow: Issue-Driven Development

Follow a structured, issue-driven approach for all AI-assisted development:

### 1. Issue Creation and Planning

1. **Create Documentation**
   - Ask AI to summarize the issue and plan in `docs/issue/`
   - Include problem specification, approach, and expected outcomes

2. **Create GitHub Issue**
   - Make a GitHub issue describing the task
   - Link to the documentation in `docs/issue/`
   - Assign appropriate labels and milestones

3. **Create Branch**
   - Create a separate branch for the issue: `git switch -c feature/issue-description`
   - Branch name should reference the issue number if applicable

### 2. Planning Phase

**For Solving and Simulating Economic Models:**

1. Write down the model setting in a document
2. Ask AI to write down the equilibrium condition (oral exam)
3. Ask AI to write down the pseudocode (oral exam)
4. Ask AI to write down the issue and plan in a markdown file

**Key Practices:**
- Create plan → Show → **WAIT** for "proceed"
- "continue" ≠ "execute" - clarify if you want explanation or execution
- Never let AI automatically execute without explicit approval

### 3. Implementation Phase

1. **Write Functions**
   - Ask AI to write functions in `src/` following the pseudocode
   - Use named arguments (not positional): `f(value=x)` not `f(x)`
   - Follow the project's coding standards

2. **Modular Design**
   - Use verb-based procedure names: `ComputeMeanReward`, `FitNeuralNetwork`, `SolveValueIteration`
   - Break down into testable subroutines
   - Avoid placeholders - implement actual steps

3. **Code Quality**
   - No timestamps in filenames: `file.py` not `file_20250101.py`
   - No version suffixes: `file.py` not `file_v2.py` or `file_old.py`
   - No backward compatibility requirements
   - Delete wrong code (use git for history)

### 4. Verification Phase

1. **Unit Tests**
   - Ask AI to write unit tests in `test/` or `scripts/test/`
   - Test properties (monotonicity, bounds), not exact values
   - Check all tests pass: `./run.sh test` or `pytest test/`

2. **Consistency Check**
   - Ask AI to list any inconsistencies between pseudocode and implementation
   - Verify all function names and APIs exist (grep to verify)
   - Ensure no hardcoded values - use configuration files

### 5. Validation Phase

1. **Execution**
   - Ask AI to write an execution file in `scripts/` or `scripts/pipeline/`
   - Execute and verify results
   - For expensive computations, test on small scale first

2. **Reporting**
   - Ask AI to write a reporting file in `scripts/report/` or `scripts/analyze_data/`
   - Use Quarto (.qmd) or R Markdown (.Rmd) for reproducible reports
   - Render and review: `quarto render report.qmd`

3. **Validation Checks**
   - Generate relevant comparative statics
   - Spot any strange behavior
   - Speculate reasons or let AI investigate root causes
   - **Never ask AI to solve the issue** - you determine the solution

### 6. Commit and Integration

1. **Commit Changes**
   - Explicitly ask AI to commit: "commit these changes"
   - Never let AI automatically git add/commit/pull/push
   - One session = one commit = minimal and complete changes
   - Use descriptive commit messages

2. **Pull Request**
   - Push branch: `git push -u origin branch-name`
   - Create pull request linked to the issue
   - Request review and validation
   - Merge after approval

## Workflow: Debugging

When encountering bugs or issues:

1. **Reproduce the Bug**
   - Create a validation script that reproduces the issue
   - Ensure the bug is consistently reproducible

2. **Document the Issue**
   - Explain the bug to AI
   - Ask AI to summarize the issue in `docs/issue/`

3. **Root Cause Analysis**
   - Ask AI to list discrepancies between pseudocode and implementation
   - Ask AI to inspect code for the root cause
   - Ask AI to set up a git worktree to run a debugger if needed

4. **Fix Implementation**
   - **Never ask AI to solve** - you determine the solution
   - Ask AI to implement your specified fix
   - Verify the fix with tests

## Workflow: Model-Free Analysis

For exploratory data analysis and model-free approaches:

### Dynamic Reporting

1. Ask AI to make a dynamic report loading the data
2. Ask AI to set up a live server to review the report
3. Ask AI to summarize the variables of the datasets

### Oral Exam Process

1. Explain to AI what you want to achieve
2. Ask AI whether it knows how to implement it
3. Ask AI to search relevant sources until it returns a legitimate answer
4. Once a legitimate answer is obtained, ask AI to summarize it in the report

### Implementation and Validation

1. Ask AI to run the analysis in the report
2. Ask AI to refresh the report and verify the result
3. Review results and iterate as needed

## Best Practices

### Project Structure

- **Package-like folder structure** - Organize code in `src/`, `test/`, `scripts/`
- **Git version control** - Track all changes, use branches for features
- **Documentation** - Maintain `README.md`, `AGENTS.md` or `CLAUDE.md` for AI context
- **Command scripts** - Use wrapper scripts like `run.sh` for common tasks

### Scope Management

- **Specify what can be changed** - Clearly define boundaries
- **Specify what cannot be changed** - Protect critical components
- Use configuration files for parameters, not hardcoding

### Multi-Level Validations

- **Consistency checks** - Verify pseudocode matches implementation
- **Unit tests** - Test properties and behaviors
- **Visualized reports** - Generate plots and tables for inspection
- **Minimum code inspection** - Rely on tests and reports rather than line-by-line review

### Reproducibility

- **DRY (Don't Repeat Yourself)** - Single implementation, parameterize differences
- **Config = Data** - Save configurations with models, load automatically
- **Stable paths** - Use `output/eq/` not `output/eq_20250927/`
- **No versions in filenames** - Use `file.py` not `file_v2.py`

### Testing Philosophy

- Test properties (monotonicity, bounds), not exact values
- Test fails → Fix code, not test
- Run tests before claiming "done"
- Test on small scale before expensive computations

## What AI is Good At

- **On-demand data analysis** - Tasks that can be mathematically defined
- **Implementation from specification** - Translating pseudocode to code
- **Repetitive tasks** - Following established patterns
- **Documentation** - Writing clear comments and documentation
- **Code refactoring** - Improving structure while maintaining functionality

## What AI is NOT Good At

### Economics Concepts

AI may not understand domain-specific concepts:
- Equilibrium, endogenous/exogenous variables
- Observable/unobservable distinctions
- Parameters of interest vs nuisance parameters

**Solution:**
- Translate economics concepts into CS/statistical concepts
- Test knowledge with oral exams
- Provide clear mathematical specifications

### Solving Bugs/Problems

AI may make up fake solutions if asked to **solve** a problem.

**Solution:**
- Always ask to find the **root cause** of the problem
- Solution must be determined by the supervisor
- Use AI to investigate, not to decide

## Critical Checklist

Before asking AI to make changes, ensure:

```
□ REPORT THE ISSUE BEFORE FIXING, EDITING, OR EXECUTING ANYTHING
□ NO GIT without explicit "commit" request
□ NO TIMESTAMPS (❌ file_20250101.py → ✅ file.py)
□ NO VERSIONS (❌ file_v2.py, _old.py → ✅ file.py)
□ NO BACKWARD COMPATIBILITY
□ TEMPORARY → scripts/temporary/
□ NAMED ARGUMENTS (❌ f(x) → ✅ f(value=x))
□ EDIT don't CREATE (when possible)
□ PLAN → WAIT → "proceed"
□ TEST → show results → "done"
□ USE run.sh wrapper (or project-specific command scripts)
□ DELETE wrong code (use git for history)
```

## Reviewing Conversation History

To refresh AI's memory or review past instructions:

- **Codex**: `~/.codex/sessions/YYYY/MM/DD/*.jsonl`
- **Claude**: `~/.claude/history.jsonl`
- **Cursor**: Check conversation history in the chat panel

Ask AI to read the conversation history and git history to review your instructions and maintain context.

## Integration with Other Workflows

This AI coding workflow integrates with:

- **Version Control** (see `version_control.md`) - Use git branches and issues
- **Data Pipeline** (see `data_pipeline.md`) - Follow input → cleaned → output structure
- **Reporting Pipeline** (see `reporting_pipeline.md`) - Generate reproducible reports
- **Weekly Iterations** (see `weekly_iterations.md`) - Plan work in weekly cycles

## References

- TestAI Project: [https://github.com/kohei-kawaguchi/TestAI](https://github.com/kohei-kawaguchi/TestAI)
- Cursor: [https://cursor.sh/](https://cursor.sh/)
- OpenAI Codex CLI: [https://developers.openai.com/codex/cli/](https://developers.openai.com/codex/cli/)
- Claude Code: [https://www.claude.com/product/claude-code](https://www.claude.com/product/claude-code)

