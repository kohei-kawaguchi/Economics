from __future__ import annotations

from pathlib import Path


REPO_ROOT = Path(__file__).parent.parent


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def test_answers_has_no_todo():
    answers_path = REPO_ROOT / "report" / "answers.md"
    text = read_text(path=answers_path)
    assert "TODO" not in text, "Replace every TODO in report/answers.md"


def test_commands_txt_contains_required_lines_once_each():
    commands_path = REPO_ROOT / "sandbox" / "notes" / "commands.txt"
    lines = [line.strip() for line in read_text(path=commands_path).splitlines() if line.strip()]

    required = [
        "pwd",
        "ls -la",
        "cd ..",
        "mkdir -p sandbox/notes",
        "touch sandbox/notes/commands.txt",
        'grep -n "TODO" report/answers.md',
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

