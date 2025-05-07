#!/usr/bin/env python
import os
import sys
from datetime import datetime, timedelta
import subprocess
from pathlib import Path
import re

def get_git_changes(days=7):
    """Get git changes from the last n days."""
    since_date = (datetime.now() - timedelta(days=days)).strftime('%Y-%m-%d')
    cmd = f'git log --since="{since_date}" --pretty=format:"%h - %s (%cr) <%an>"'
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    return result.stdout.split('\n')

def get_changed_files(days=7):
    """Get list of files changed in the last n days."""
    since_date = (datetime.now() - timedelta(days=days)).strftime('%Y-%m-%d')
    cmd = f'git log --since="{since_date}" --name-only --pretty=format:'
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    return list(set(result.stdout.split('\n')))

def categorize_changes(changed_files):
    """Categorize changes into code, docs, and infrastructure."""
    categories = {
        'code': [],
        'docs': [],
        'infra': []
    }
    
    for file in changed_files:
        if not file.strip():
            continue
        if file.endswith('.py'):
            categories['code'].append(file)
        elif file.endswith('.md') or 'docs' in file:
            categories['docs'].append(file)
        elif file in ['pyproject.toml', 'poetry.lock', 'requirements.txt'] or 'config' in file:
            categories['infra'].append(file)
    
    return categories

def generate_weekly_note():
    """Generate a new weekly note based on the template."""
    # Get the template
    template_path = Path('obsidian/templates/weekly-iteration.md')
    with open(template_path, 'r') as f:
        template = f.read()
    
    # Get changes
    commits = get_git_changes()
    changed_files = get_changed_files()
    categories = categorize_changes(changed_files)
    
    # Replace template placeholders
    today = datetime.now()
    note = template.replace('{{date:YYYY-MM-DD}}', today.strftime('%Y-%m-%d'))
    
    # Add changes to the template
    changes_section = "### Code Changes\n"
    for file in categories['code']:
        changes_section += f"- Modified: {file}\n"
    
    changes_section += "\n### Documentation Updates\n"
    for file in categories['docs']:
        changes_section += f"- Updated: {file}\n"
    
    changes_section += "\n### Infrastructure Changes\n"
    for file in categories['infra']:
        changes_section += f"- Changed: {file}\n"
    
    # Replace the changes section in the template
    note = re.sub(
        r'<!-- This section will be automatically populated.*?-->.*?(?=##)',
        changes_section,
        note,
        flags=re.DOTALL
    )
    
    # Save the new note
    output_dir = Path('obsidian/weekly-iterations')
    output_dir.mkdir(exist_ok=True)
    
    output_file = output_dir / f'iteration-{today.strftime("%Y-%m-%d")}.md'
    with open(output_file, 'w') as f:
        f.write(note)
    
    print(f"Generated weekly note: {output_file}")

if __name__ == '__main__':
    generate_weekly_note() 