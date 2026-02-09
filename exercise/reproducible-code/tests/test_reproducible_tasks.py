"""Tests for reproducible code requirements."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).parent.parent
CONFIG_PATH = REPO_ROOT / "config" / "simulation.json"
OUTPUT_DIR = REPO_ROOT / "output"
OUTPUT_PATH = OUTPUT_DIR / "simulation.json"
SCRIPT_PATH = REPO_ROOT / "scripts" / "run_simulation.py"


def read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def run_script() -> None:
    subprocess.run(
        [sys.executable, str(SCRIPT_PATH)],
        cwd=str(REPO_ROOT),
        check=True,
    )


def test_output_path_is_stable():
    """Script should write to output/simulation.json (stable path)."""
    if OUTPUT_PATH.exists():
        OUTPUT_PATH.unlink()

    run_script()
    assert OUTPUT_PATH.exists(), (
        "Expected output at output/simulation.json. "
        "Use a stable path and overwrite on rerun."
    )

    unexpected = []
    for p in OUTPUT_DIR.iterdir():
        if p.name in {".gitkeep", "simulation.json"}:
            continue
        unexpected.append(p.name)

    assert unexpected == [], (
        "Found unexpected entries under output/. "
        "Do not create timestamped directories or extra outputs. "
        f"Unexpected: {unexpected}"
    )


def test_config_is_saved_with_output_and_no_timestamp():
    """Output should contain the config and should not include a timestamp field."""
    run_script()
    out = read_json(path=OUTPUT_PATH)

    assert "config" in out, "Output must include the config used for the run."
    assert "summary" in out, "Output must include computed summary statistics."
    assert "sample" in out, "Output must include the generated sample."

    assert "timestamp" not in out, (
        "Do not store timestamps in the output. "
        "Reproducible outputs should be stable."
    )

    config = read_json(path=CONFIG_PATH)
    assert out["config"] == config, (
        "Output config does not match config/simulation.json. "
        "Load parameters from config and save that config with the output."
    )


def test_deterministic_execution():
    """Two runs with the same config must produce identical output."""
    run_script()
    out1 = read_json(path=OUTPUT_PATH)

    run_script()
    out2 = read_json(path=OUTPUT_PATH)

    assert out1 == out2, (
        "Outputs differ across runs. "
        "Make the simulation deterministic by seeding randomness."
    )


def test_summary_matches_sample_and_config():
    """Summary should be consistent with the sample and config."""
    run_script()
    out = read_json(path=OUTPUT_PATH)
    config = out["config"]
    sample = out["sample"]
    summary = out["summary"]

    assert len(sample) == config["n"], "Sample length must equal config n."
    assert min(sample) == summary["min"], "summary[min] must equal min(sample)."
    assert max(sample) == summary["max"], "summary[max] must equal max(sample)."

    mean = sum(sample) / len(sample)
    assert summary["mean"] == mean, "summary[mean] must equal sum(sample)/len(sample)."

