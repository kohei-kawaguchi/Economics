# Answers

Use `docs/workflow/bash_commands.md` as a reference. Replace every TODO in this file. Then create the files under `sandbox/` and commit them.

## Commands you used

Add a short explanation and an example for each command below. Put the command on its own line in a fenced code block. Use your own words for the explanation.

### Navigation

TODO: Explain what `pwd` does and when you use it.

```bash
TODO
```

TODO: Explain what `ls -la` does and why `-a` matters.

```bash
TODO
```

TODO: Explain what `cd ..` does.

```bash
TODO
```

### File operations

TODO: Explain what `mkdir -p` does and why it is useful.

```bash
TODO
```

TODO: Explain what `touch` does.

```bash
TODO
```

TODO: Explain what `cp` does.

```bash
TODO
```

TODO: Explain what `mv` does.

```bash
TODO
```

TODO: Explain what `rm -r` does and what makes it dangerous.

```bash
TODO
```

### Searching and permissions

TODO: Explain what `grep -n` does.

```bash
TODO
```

TODO: Explain what `chmod +x` does.

```bash
TODO
```

### Vim minimal commands

TODO: Describe how you enter Insert mode, how you return to Normal mode, and how you save and quit.

```text
TODO
```

## Files under sandbox

The repository already contains `sandbox/`. Use bash commands to navigate and inspect it, then edit the files using vim and commit the results.

Edit `sandbox/notes/commands.txt` so that it contains the literal command lines below, exactly once each, in any order:

```text
pwd
ls -la
cd ..
mkdir -p sandbox/notes
touch sandbox/notes/commands.txt
grep -n "TODO" report/answers.md
chmod +x sandbox/scripts/hello.sh
```

Verify that `sandbox/scripts/hello.sh` has the contents below and make it executable.

```bash
#!/usr/bin/env bash
echo "hello"
```

