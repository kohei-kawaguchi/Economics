"""Simple data analysis script."""

import csv


def load_data(filepath):
    """Load numbers from a CSV file."""
    numbers = []
    with open(filepath, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            numbers.append(float(row["value"]))
    return numbers


def calculate_mean(numbers):
    """Calculate the mean of a list of numbers.

    Args:
        numbers: List of numeric values.

    Returns:
        The arithmetic mean of the numbers.
    """
    # TODO: Implement this function
    pass


def main():
    data = load_data("data/numbers.csv")
    print(f"Data: {data}")

    mean = calculate_mean(data)
    print(f"Mean: {mean}")


if __name__ == "__main__":
    main()
