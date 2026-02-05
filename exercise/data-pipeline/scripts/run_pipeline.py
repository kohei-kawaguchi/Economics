"""Main script to run the full data pipeline."""

import json
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.pipeline import (
    compute_customer_summary,
    extract_customers,
    extract_orders,
    extract_products,
    load_cleaned_table,
    load_raw_data,
    save_table,
)


def run_cleaning(config):
    """Stage 1: Clean raw data into 3NF tables.
    
    This stage is ANALYSIS-AGNOSTIC.
    The cleaned data can support any future analysis.
    """
    print("=" * 60)
    print("Stage 1: Data Cleaning (input/ -> cleaned/)")
    print("Purpose: Non-redundant representation (3NF)")
    print("=" * 60)

    # Load raw data
    raw_data = load_raw_data(filepath=config["input_file"])
    print(f"Loaded {len(raw_data)} raw records")

    # Extract normalized tables
    customers = extract_customers(raw_data=raw_data)
    products = extract_products(raw_data=raw_data)
    orders = extract_orders(raw_data=raw_data)

    print(f"Extracted {len(customers)} unique customers")
    print(f"Extracted {len(products)} unique products")
    print(f"Extracted {len(orders)} orders")

    # Save cleaned tables
    cleaned_dir = config["cleaned_dir"]

    save_table(
        data=customers,
        filepath=f"{cleaned_dir}/{config['tables']['customers']['filename']}",
        columns=config["tables"]["customers"]["columns"],
    )

    save_table(
        data=products,
        filepath=f"{cleaned_dir}/{config['tables']['products']['filename']}",
        columns=config["tables"]["products"]["columns"],
    )

    save_table(
        data=orders,
        filepath=f"{cleaned_dir}/{config['tables']['orders']['filename']}",
        columns=config["tables"]["orders"]["columns"],
    )

    print(f"Saved cleaned tables to {cleaned_dir}/")
    return customers, products, orders


def run_analysis(config, customers, products, orders):
    """Stage 2: Run analysis on cleaned data.
    
    This stage is ANALYSIS-SPECIFIC.
    Different questions require different transformations.
    """
    print()
    print("=" * 60)
    print("Stage 2: Analysis (cleaned/ -> output/)")
    print("Purpose: Answer specific question about customer spending")
    print("=" * 60)

    # Compute customer summary
    summary = compute_customer_summary(
        customers=customers,
        orders=orders,
        products=products,
    )

    print(f"Computed summary for {len(summary)} customers")

    # Save analysis output
    output_dir = config["output_dir"]
    save_table(
        data=summary,
        filepath=f"{output_dir}/{config['analysis']['customer_summary']['filename']}",
        columns=["customer_id", "customer_name", "total_orders", "total_spending"],
    )

    print(f"Saved analysis results to {output_dir}/")
    return summary


def main(config_path="config/pipeline.json"):
    """Run the full data pipeline."""
    # Load configuration
    with open(config_path) as f:
        config = json.load(f)

    # Stage 1: Cleaning
    customers, products, orders = run_cleaning(config=config)

    # Stage 2: Analysis
    summary = run_analysis(
        config=config,
        customers=customers,
        products=products,
        orders=orders,
    )

    print()
    print("Pipeline complete!")


if __name__ == "__main__":
    main()
