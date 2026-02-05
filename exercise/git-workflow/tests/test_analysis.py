"""Tests for src/analysis.py"""

import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.analysis import calculate_mean


def test_calculate_mean_basic():
    """Test mean calculation with simple integers."""
    result = calculate_mean(numbers=[10, 20, 30, 40, 50])
    assert result == 30.0


def test_calculate_mean_single():
    """Test mean calculation with a single value."""
    result = calculate_mean(numbers=[5])
    assert result == 5.0


def test_calculate_mean_floats():
    """Test mean calculation with floats."""
    result = calculate_mean(numbers=[1.5, 2.5, 3.0])
    assert result == 7.0 / 3
