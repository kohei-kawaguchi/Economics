# Bash Commands and Vim Guide

This document provides essential bash commands and a comprehensive guide to using vim for editing files in the terminal.

## Overview

Bash (Bourne Again Shell) is a command-line interface used for interacting with your operating system. On Windows, Git Bash provides a bash environment. Understanding basic bash commands and vim is essential for efficient development workflows, especially when working with remote servers or in terminal-only environments.

## Essential Bash Commands

### Navigation

```bash
# Print current working directory
pwd

# List files and directories
ls              # List current directory
ls -la          # List with details (including hidden files)
ls -lh          # List with human-readable file sizes

# Change directory
cd <directory>  # Change to directory
cd ..           # Go up one directory
cd ~            # Go to home directory
cd -            # Go to previous directory
cd /            # Go to root directory
```

### File Operations

```bash
# Create files and directories
touch <filename>           # Create empty file
mkdir <directory>          # Create directory
mkdir -p path/to/dir       # Create nested directories

# Copy, move, and remove
cp <source> <destination>  # Copy file
cp -r <source> <dest>      # Copy directory recursively
mv <source> <destination>  # Move/rename file
rm <filename>              # Remove file
rm -r <directory>          # Remove directory recursively
rm -rf <directory>         # Force remove directory (use with caution!)

# View file contents
cat <filename>             # Display entire file
head -n 20 <filename>      # Display first 20 lines
tail -n 20 <filename>      # Display last 20 lines
less <filename>            # View file with pagination (q to quit)
```

### File Permissions

```bash
# View permissions
ls -l <filename>

# Change permissions
chmod +x <filename>        # Make file executable
chmod 755 <filename>       # Set specific permissions (rwxr-xr-x)
chmod -R 755 <directory>   # Recursively change permissions

# Change ownership
chown user:group <file>    # Change file owner
```

### Searching and Filtering

```bash
# Search in files
grep "pattern" <filename>           # Search for pattern in file
grep -r "pattern" <directory>       # Recursive search
grep -i "pattern" <file>            # Case-insensitive search
grep -n "pattern" <file>             # Show line numbers

# Find files
find . -name "*.py"                 # Find all Python files
find . -type f -name "*.md"          # Find all markdown files
find . -type d -name "test"          # Find all directories named "test"

# Count lines, words, characters
wc <filename>                       # Count lines, words, characters
wc -l <filename>                    # Count lines only
```

### Process Management

```bash
# View running processes
ps aux                              # List all processes
ps aux | grep python                # Find Python processes

# Kill processes
kill <PID>                          # Kill process by ID
kill -9 <PID>                       # Force kill process
killall <process-name>              # Kill all processes with name

# Run process in background
<command> &                         # Run in background
nohup <command> &                   # Run in background, survive logout
```

### Environment Variables

```bash
# View environment variables
env                                 # List all environment variables
echo $PATH                          # View PATH variable
echo $HOME                          # View home directory

# Set environment variables
export VAR_NAME="value"             # Set for current session
export PATH=$PATH:/new/path         # Append to PATH
```

### Input/Output Redirection

```bash
# Redirect output
command > file.txt                  # Write output to file (overwrite)
command >> file.txt                 # Append output to file
command 2> error.log                # Redirect errors to file
command > output.log 2>&1           # Redirect both stdout and stderr

# Pipes
command1 | command2                # Pipe output of command1 to command2
ls -la | grep ".md"                 # List files, filter markdown files
cat file.txt | wc -l                # Count lines in file
```

### Useful Shortcuts

```bash
# Command history
history                             # View command history
!!                                  # Repeat last command
!<number>                           # Execute command from history
!<string>                           # Execute last command starting with string
Ctrl+R                              # Search command history interactively

# Command editing
Ctrl+A                              # Move to beginning of line
Ctrl+E                              # Move to end of line
Ctrl+U                              # Delete to beginning of line
Ctrl+K                              # Delete to end of line
Ctrl+W                              # Delete previous word
Ctrl+L                              # Clear screen (same as 'clear')
```

## Using Vim

Vim is a powerful text editor available on most Unix-like systems. It's modal, meaning it has different modes for different operations.

### Getting Started

```bash
# Open vim
vim <filename>                      # Open file in vim
vim                                 # Open vim without file

# Exit vim
# In Normal mode, type:
:q                                  # Quit (if no changes)
:q!                                 # Quit without saving (discard changes)
:wq                                 # Write (save) and quit
:x                                  # Save and quit (same as :wq)
ZZ                                  # Save and quit (shortcut)
ZQ                                  # Quit without saving (shortcut)
```

### Vim Modes

Vim has several modes, but the most important are:

1. **Normal Mode** (default) - For navigation and commands
2. **Insert Mode** - For typing text
3. **Visual Mode** - For selecting text
4. **Command Mode** - For entering commands

### Entering and Exiting Modes

```vim
# From Normal mode:
i                                   # Enter Insert mode before cursor
a                                   # Enter Insert mode after cursor
I                                   # Enter Insert mode at beginning of line
A                                   # Enter Insert mode at end of line
o                                   # Open new line below and enter Insert mode
O                                   # Open new line above and enter Insert mode
v                                   # Enter Visual mode (character selection)
V                                   # Enter Visual mode (line selection)
Ctrl+V                              # Enter Visual mode (block selection)
:                                   # Enter Command mode

# From Insert/Visual mode:
Esc                                 # Return to Normal mode
Ctrl+C                              # Return to Normal mode (alternative)
```

### Navigation in Normal Mode

```vim
# Basic movement
h                                   # Move left
j                                   # Move down
k                                   # Move up
l                                   # Move right

# Word movement
w                                   # Move forward one word
b                                   # Move backward one word
e                                   # Move to end of word
W                                   # Move forward one WORD (ignores punctuation)
B                                   # Move backward one WORD

# Line movement
0                                   # Move to beginning of line
$                                   # Move to end of line
^                                   # Move to first non-blank character
g_                                  # Move to last non-blank character

# Screen movement
H                                   # Move to top of screen
M                                   # Move to middle of screen
L                                   # Move to bottom of screen
Ctrl+F                             # Move forward one screen
Ctrl+B                             # Move backward one screen
Ctrl+D                             # Move down half screen
Ctrl+U                             # Move up half screen

# Document movement
gg                                  # Move to beginning of file
G                                   # Move to end of file
<number>G                          # Move to line number (e.g., 42G)
:<number>                          # Move to line number (command mode)
```

### Editing in Normal Mode

```vim
# Delete
x                                   # Delete character under cursor
X                                   # Delete character before cursor
dw                                  # Delete word
dd                                  # Delete line
D                                   # Delete to end of line
d$                                  # Delete to end of line
d0                                  # Delete to beginning of line

# Copy (yank)
yy                                  # Copy (yank) line
yw                                  # Copy word
y$                                  # Copy to end of line
y0                                  # Copy to beginning of line

# Paste
p                                   # Paste after cursor
P                                   # Paste before cursor

# Undo/Redo
u                                   # Undo
Ctrl+R                             # Redo
U                                   # Undo all changes on current line

# Change (delete and enter Insert mode)
cw                                  # Change word
cc                                  # Change line
c$                                  # Change to end of line
C                                   # Change to end of line (same as c$)
```

### Visual Mode

```vim
# Enter Visual mode
v                                   # Character selection
V                                   # Line selection
Ctrl+V                             # Block selection

# In Visual mode:
y                                   # Yank (copy) selection
d                                   # Delete selection
c                                   # Change selection
>                                   # Indent right
<                                   # Indent left
Esc                                 # Exit Visual mode
```

### Search and Replace

```vim
# Search
/pattern                            # Search forward for pattern
?pattern                            # Search backward for pattern
n                                   # Next match
N                                   # Previous match
*                                   # Search for word under cursor forward
#                                   # Search for word under cursor backward

# Replace (Command mode)
:s/old/new                          # Replace first occurrence in current line
:s/old/new/g                        # Replace all occurrences in current line
:%s/old/new/g                       # Replace all occurrences in file
:%s/old/new/gc                      # Replace all with confirmation
:5,10s/old/new/g                    # Replace in lines 5-10
```

### Working with Files

```vim
# Save
:w                                  # Save file
:w <filename>                       # Save as new filename
:wq                                 # Save and quit

# Open files
:e <filename>                       # Open file in current buffer
:sp <filename>                      # Split window and open file
:vsp <filename>                     # Vertical split and open file

# File information
:r <filename>                       # Read file into current buffer
:!command                           # Execute shell command
:r !command                         # Insert command output
```

### Useful Vim Commands

```vim
# Line numbers
:set number                         # Show line numbers
:set nonumber                       # Hide line numbers
:set nu                             # Short form
:set rnu                            # Relative line numbers

# Indentation
>>                                  # Indent line right
<<                                  # Indent line left
=                                   # Auto-indent selection
gg=G                                # Auto-indent entire file

# Join lines
J                                   # Join current line with next line

# Repeat last command
.                                   # Repeat last change

# Marks (bookmarks)
ma                                  # Set mark 'a' at current position
'a                                  # Jump to mark 'a'
``                                  # Jump to previous position
''                                  # Jump to start of line of previous position
```

### Vim Configuration

Create a `.vimrc` file in your home directory to customize vim:

```bash
# Create/edit vimrc
vim ~/.vimrc
```

Example `.vimrc` contents:

```vim
" Basic settings
set number                          " Show line numbers
set relativenumber                  " Relative line numbers
set tabstop=4                       " Tab width
set shiftwidth=4                    " Indent width
set expandtab                       " Use spaces instead of tabs
set autoindent                      " Auto-indent
set smartindent                     " Smart indenting
set hlsearch                        " Highlight search results
set incsearch                       " Incremental search
set ignorecase                      " Case-insensitive search
set smartcase                       " Case-sensitive if uppercase used
syntax on                           " Enable syntax highlighting
set mouse=a                         " Enable mouse support
```

## Common Workflows

### Editing a File

1. Open file: `vim filename.txt`
2. Navigate to location using `h`, `j`, `k`, `l` or search with `/pattern`
3. Press `i` to enter Insert mode
4. Make your edits
5. Press `Esc` to return to Normal mode
6. Type `:wq` and press Enter to save and quit

### Quick Edits

```bash
# Edit file, make change, save and quit
vim file.txt
# (make edits)
:wq

# View file without editing
vim file.txt
# Press 'q' to quit (if in view mode)
# Or type :q to quit
```

### Search and Replace Example

```vim
# In vim:
:%s/old_text/new_text/g            # Replace all occurrences
:%s/old_text/new_text/gc           # Replace with confirmation
```

### Copying Between Files

```vim
# Method 1: Using registers
"ayy                                # Copy line to register 'a'
:e otherfile.txt                    # Open other file
"ap                                 # Paste from register 'a'

# Method 2: Using system clipboard (if available)
"+yy                                # Copy to system clipboard
"+p                                 # Paste from system clipboard
```

## Tips for Beginners

1. **Start in Normal mode** - Most commands work in Normal mode
2. **Use `Esc` frequently** - Return to Normal mode when unsure
3. **Don't use arrow keys** - Use `h`, `j`, `k`, `l` instead (builds muscle memory)
4. **Learn incrementally** - Master basic navigation, then editing, then advanced features
5. **Use `:help`** - Type `:help <topic>` for built-in help (e.g., `:help navigation`)
6. **Practice** - Use vim for simple edits to build familiarity

## Getting Help

```vim
# In vim
:help                               # Open help
:help <topic>                       # Help on specific topic
:q                                  # Quit help

# Common help topics
:help navigation
:help insert
:help visual
:help options
```

## Integration with Git

Vim is often used as the default editor for Git:

```bash
# Set vim as default Git editor
git config --global core.editor "vim"

# When Git opens vim for commit messages:
# 1. Type your commit message
# 2. Press Esc to ensure Normal mode
# 3. Type :wq to save and complete the commit
```

## Alternatives to Vim

If vim is too complex, consider:

- **nano** - Simpler text editor: `nano filename.txt` (Ctrl+X to exit)
- **VS Code/Cursor** - Modern editors with terminal integration
- **emacs** - Another powerful editor (different keybindings)

However, vim is ubiquitous on servers and remote systems, so learning the basics is valuable.

## Quick Reference Card

### Essential Commands

| Action | Command |
|--------|---------|
| Quit | `:q` |
| Quit without saving | `:q!` |
| Save and quit | `:wq` or `ZZ` |
| Enter Insert mode | `i` |
| Return to Normal mode | `Esc` |
| Delete line | `dd` |
| Copy line | `yy` |
| Paste | `p` |
| Undo | `u` |
| Search | `/pattern` |
| Next match | `n` |
| Go to line | `:<number>` or `<number>G` |

### Navigation

| Action | Command |
|--------|---------|
| Left/Down/Up/Right | `h`/`j`/`k`/`l` |
| Word forward/back | `w`/`b` |
| Beginning/End of line | `0`/`$` |
| Top/Bottom of file | `gg`/`G` |

