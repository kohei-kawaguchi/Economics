"""Run a toy simulation and save outputs.

This script intentionally violates reproducible code principles at first.
Fix it by following docs/workflow/reproducible_code.md.
"""

from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path

from src.reproducible import compute_summary, simulate_integers


def main() -> None:
    repo_root = Path(__file__).parent.parent

    # TODO: Replace hardcoded values with config (config as data).
    seed = 0
    n = 10
    upper = 100

    # TODO: Replace timestamped output directory with a stable path.
    output_dir = repo_root / "output" / f"simulation_{datetime.now():%Y%m%d}"
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / "simulation.json"

    # TODO: Make execution deterministic, use named arguments.
    sample = simulate_integers(seed, n, upper)
    summary = compute_summary(sample=sample)

    output = {
        "config": {
            "seed": seed,
            "n": n,
            "upper": upper,
        },
        "sample": sample,
        "summary": summary,
    }

    output_path.write_text(json.dumps(output, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main()

