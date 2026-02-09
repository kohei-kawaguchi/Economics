"""Tests for src/analysis.py"""

import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.analysis import calculate_trimmed_mean


def test_calculate_trimmed_mean_simple():
    result = calculate_trimmed_mean(numbers=[1, 2, 3, 4, 100], trim_ratio=0.2)
    assert result == 3.0


def test_calculate_trimmed_mean_no_trim():
    result = calculate_trimmed_mean(numbers=[1, 2, 3, 4], trim_ratio=0.0)
    assert result == 2.5


def test_calculate_trimmed_mean_floats():
    result = calculate_trimmed_mean(numbers=[1.0, 1.5, 2.0, 100.0, 101.0], trim_ratio=0.2)
    assert result == 34.5

