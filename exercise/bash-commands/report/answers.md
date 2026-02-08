# Exercises

Use `docs/workflow/bash_commands.md` in the Economics repository as a reference. Complete the exercises below by creating and editing files under `sandbox/`. The autograder checks only the produced files and their contents.

## Terminal exercises

Do these actions from the terminal.

Create `sandbox/notes/commands.txt` so that it contains the literal command lines below, exactly once each, in any order.

```text
pwd
ls -la
cd ..
mkdir -p sandbox/notes
touch sandbox/notes/commands.txt
vim sandbox/notes/vim_exercise.txt
chmod +x sandbox/scripts/hello.sh
```

Verify that `sandbox/scripts/hello.sh` has the contents below and make it executable.

```bash
#!/usr/bin/env bash
echo "hello"
```

## Vim exercises

Open `sandbox/notes/vim_exercise.txt` in vim and edit it so that it matches the content below exactly.

```text
i: insert before cursor
Esc: normal mode
:wq: save and quit
/word: search forward
:%s/old/new/g: replace all
```

