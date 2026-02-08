from __future__ import annotations

from pathlib import Path


REPO_ROOT = Path(__file__).parent.parent


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def test_commands_txt_contains_required_lines_once_each():
    commands_path = REPO_ROOT / "sandbox" / "notes" / "commands.txt"
    lines = [line.strip() for line in read_text(path=commands_path).splitlines() if line.strip()]

    required = [
        "pwd",
        "ls -la",
        "cd ..",
        "mkdir -p sandbox/notes",
        "touch sandbox/notes/commands.txt",
        "vim sandbox/notes/vim_exercise.txt",
        "mkdir -p sandbox/dotfiles",
        "vim sandbox/dotfiles/.bashrc",
        "vim sandbox/dotfiles/.bash_profile",
        "chmod +x sandbox/scripts/hello.sh",
    ]

    for req in required:
        count = sum(1 for line in lines if line == req)
        assert count == 1, f"Expected '{req}' exactly once in sandbox/notes/commands.txt"


def test_hello_script_content_and_executable():
    script_path = REPO_ROOT / "sandbox" / "scripts" / "hello.sh"
    text = read_text(path=script_path).replace("\r\n", "\n")
    assert text == '#!/usr/bin/env bash\necho "hello"\n' or text == '#!/usr/bin/env bash\necho "hello"', (
        "sandbox/scripts/hello.sh must match the required contents"
    )

    mode = script_path.stat().st_mode
    assert (mode & 0o111) != 0, "Make sandbox/scripts/hello.sh executable with chmod +x"


def test_vim_exercise_file_matches_expected_content():
    exercise_path = REPO_ROOT / "sandbox" / "notes" / "vim_exercise.txt"
    text = read_text(path=exercise_path).replace("\r\n", "\n")
    expected = (
        "i: insert before cursor\n"
        "Esc: normal mode\n"
        ":wq: save and quit\n"
        "/word: search forward\n"
        ":%s/old/new/g: replace all\n"
    )
    assert text == expected, "Edit sandbox/notes/vim_exercise.txt to match the target text in report/answers.md"


def test_bashrc_contains_persistent_path_export_once():
    bashrc_path = REPO_ROOT / "sandbox" / "dotfiles" / ".bashrc"
    text = read_text(path=bashrc_path).replace("\r\n", "\n")
    line = 'export PATH="$HOME/bin:$PATH"'
    assert text.count(line) == 1, "Add export PATH line to sandbox/dotfiles/.bashrc exactly once"


def test_bash_profile_sources_bashrc_once():
    profile_path = REPO_ROOT / "sandbox" / "dotfiles" / ".bash_profile"
    text = read_text(path=profile_path).replace("\r\n", "\n")
    line = 'source "$HOME/.bashrc"'
    assert text.count(line) == 1, "Add source line to sandbox/dotfiles/.bash_profile exactly once"

