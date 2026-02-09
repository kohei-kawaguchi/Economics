# Exercises

Use `docs/workflow/bash_commands.md` in the Economics repository as a reference. Complete the exercises below by creating and editing files under `sandbox/`. The autograder checks only the produced files and their contents.

## Terminal exercises

Do these actions from the terminal.

Create `sandbox/notes/commands.txt` so that it contains the literal command lines below, exactly once each, in any order.

```text
pwd
ls -1
mkdir -p sandbox/notes
touch sandbox/notes/commands.txt
printf "done\n" > sandbox/notes/marker.txt
vim sandbox/notes/vim_exercise.txt
mkdir -p sandbox/dotfiles
vim sandbox/dotfiles/.bashrc
vim sandbox/dotfiles/.bash_profile
chmod +x sandbox/scripts/hello.sh
bash sandbox/scripts/hello.sh
```

Verify that `sandbox/scripts/hello.sh` has the contents below and make it executable.

```bash
#!/usr/bin/env bash
echo "hello economics"
```

## Vim exercises

Open `sandbox/notes/vim_exercise.txt` in vim and edit it so that it matches the content below exactly.

```text
gg: go to first line
G: go to last line
dd: delete line
yy: copy line
p: paste after cursor
```

## Persistent PATH exercise

Edit `sandbox/dotfiles/.bashrc` so that it contains the line below exactly once.

```bash
export PATH="$HOME/.local/bin:$PATH"
```

Edit `sandbox/dotfiles/.bash_profile` so that it sources `.bashrc` using the line below exactly once.

```bash
. "$HOME/.bashrc"
```

