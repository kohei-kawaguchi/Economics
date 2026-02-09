"""Main script to run the analysis."""

import json
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.analysis import calculate_trimmed_mean, load_data, save_results


def main(config_path="config/analysis.json"):
    """Run the analysis using configuration file."""
    # Load configuration
    with open(config_path) as f:
        config = json.load(f)

    # Load data using named arguments
    data = load_data(
        filepath=config["input_file"],
        column_name=config["column_name"],
    )
    print(f"Loaded {len(data)} values: {data}")

    # Compute statistics
    trimmed_mean = calculate_trimmed_mean(
        numbers=data,
        trim_ratio=config["trim_ratio"],
    )
    print(f"Trimmed mean: {trimmed_mean}")

    # Save results with config
    results = {"trimmed_mean": trimmed_mean}
    save_results(
        results=results,
        config=config,
        output_path=config["output_file"],
    )
    print(f"Results saved to {config['output_file']}")


if __name__ == "__main__":
    main()

