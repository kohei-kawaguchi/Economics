"""Utilities for a reproducible simulation project."""

from __future__ import annotations

import random
from typing import Any


def simulate_integers(*, seed: int, n: int, upper: int) -> list[int]:
    """Generate a deterministic sample of integers.

    Args:
        seed: Random seed.
        n: Sample size.
        upper: Sample values are in [0, upper).

    Returns:
        List of integers.
    """
    # TODO: Implement deterministic simulation.
    # Requirements:
    # - Must be deterministic for fixed seed
    # - Must use the function arguments (no hardcoding)
    # - Must return exactly n integers in [0, upper)
    pass


def compute_summary(*, sample: list[int]) -> dict[str, Any]:
    """Compute summary statistics for a sample.

    Args:
        sample: List of integers.

    Returns:
        Dictionary with keys:
        - n
        - mean
        - min
        - max
    """
    # TODO: Implement summary computation.
    pass

