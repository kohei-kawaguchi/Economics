---
marp: true
theme: default
paginate: true
---

# Bash Commands and Vim Guide

Essential bash commands and vim for terminal editing. On Windows: Git Bash.

---

# Navigation

```bash
pwd              # Current directory
ls -la           # List with details
cd <dir>         # Change directory
cd ..            # Up one level
cd ~             # Home
cd -             # Previous directory
```

---

# File Operations

```bash
touch <file>     # Create file
mkdir -p a/b/c   # Create nested dirs
cp -r src dest   # Copy recursively
mv src dest      # Move/rename
rm -rf <dir>     # Remove (caution!)
cat, head, tail, less  # View files
```

---

# Permissions and Search

```bash
chmod +x file    # Make executable
chmod 755 file   # rwxr-xr-x
grep "pattern" file    # Search in file
grep -r "pattern" dir  # Recursive
find . -name "*.py"    # Find files
wc -l file       # Line count
```

---

# Process and Environment

```bash
ps aux | grep python
kill -9 <PID>
nohup cmd &      # Background, survive logout

env              # List variables
export VAR="value"
```

---

# Redirection and Pipes

```bash
cmd > file.txt   # Overwrite
cmd >> file.txt  # Append
cmd 2> err.log   # Redirect stderr
cmd > out.log 2>&1
cmd1 | cmd2      # Pipe
```

---

# Useful Shortcuts

```bash
history          # Command history
!!               # Repeat last
!42              # Execute #42 from history
Ctrl+R           # Search history
Ctrl+A/E         # Start/end of line
Ctrl+U/K         # Delete to start/end
Ctrl+L           # Clear screen
```

---

# Vim: Getting Started

```bash
vim file.txt     # Open file
```

Exit (Normal mode):
- `:q` quit (no changes)
- `:q!` quit without saving
- `:wq` or `ZZ` save and quit

---

# Vim Modes

1. Normal (default) - navigation, commands
2. Insert - typing
3. Visual - selection
4. Command - `:` commands

From Normal: `i` insert, `a` append, `v` visual, `:` command. `Esc` return to Normal.

---

# Vim Navigation

```
h/j/k/l     left/down/up/right
w/b         word forward/back
0/$         start/end of line
gg/G        top/bottom of file
42G         go to line 42
```

---

# Vim Editing

```
x, dd       delete char, line
yy, p       copy line, paste
u, Ctrl+R   undo, redo
cw, cc      change word, line
```

---

# Vim Search and Replace

```
/pattern    search forward
n/N         next/previous match
:s/old/new/g      current line
:%s/old/new/g     entire file
:%s/old/new/gc    with confirmation
```

---

# Vim: Line Numbers and Indent

```
:set number      # Show line numbers
:set rnu         # Relative numbers
>>  <<           # Indent right/left
gg=G             # Auto-indent file
```

---

# Vim Tips for Beginners

1. Start in Normal mode
2. Use Esc frequently
3. Use h/j/k/l instead of arrows
4. Learn incrementally
5. `:help <topic>` for help

---

# Vim as Git Editor

```bash
git config --global core.editor "vim"
```

For commit messages: type message, Esc, `:wq`

---

# Quick Reference

| Action | Command |
|--------|---------|
| Quit | `:q` |
| Save and quit | `:wq` or `ZZ` |
| Insert | `i` |
| Normal | `Esc` |
| Delete line | `dd` |
| Copy/Paste | `yy` / `p` |
| Search | `/pattern` |
