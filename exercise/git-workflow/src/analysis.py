"""Analysis module for computing statistics."""

import csv
import json


def load_data(filepath, column_name):
    """Load numeric data from a CSV file.

    Args:
        filepath: Path to the CSV file.
        column_name: Name of the column to extract.

    Returns:
        List of numeric values.
    """
    numbers = []
    with open(filepath, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            numbers.append(float(row[column_name]))
    return numbers


def calculate_mean(numbers):
    """Calculate the arithmetic mean of a list of numbers.

    Args:
        numbers: List of numeric values.

    Returns:
        The arithmetic mean.
    """
    # TODO: Implement this function
    pass


def save_results(results, config, output_path):
    """Save results with configuration to a JSON file.

    Args:
        results: Dictionary of computed results.
        config: Configuration used for the analysis.
        output_path: Path to save the output.
    """
    output = {
        "results": results,
        "config": config,
    }
    with open(output_path, "w") as f:
        json.dump(output, f, indent=2)
