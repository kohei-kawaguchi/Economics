"""Data pipeline module for cleaning raw data and running analysis."""

import csv
from pathlib import Path


# =============================================================================
# Data Loading
# =============================================================================

def load_raw_data(filepath):
    """Load raw data from a CSV file.

    Args:
        filepath: Path to the CSV file.

    Returns:
        List of dictionaries, one per row.
    """
    with open(filepath, "r") as f:
        reader = csv.DictReader(f)
        return list(reader)


def load_cleaned_table(filepath):
    """Load a cleaned table from a CSV file.

    Args:
        filepath: Path to the CSV file.

    Returns:
        List of dictionaries, one per row.
    """
    with open(filepath, "r") as f:
        reader = csv.DictReader(f)
        return list(reader)


# =============================================================================
# Stage 1: Data Cleaning (input/ -> cleaned/)
#
# Purpose: Represent raw data in non-redundant form (3NF)
# This stage is ANALYSIS-AGNOSTIC - the cleaned data supports ANY analysis
# =============================================================================

def extract_customers(raw_data):
    """Extract unique customer records from raw data.

    Args:
        raw_data: List of raw order records.

    Returns:
        List of unique customer dictionaries with keys:
        customer_id, customer_name, customer_city
    """
    # TODO: Implement this function
    # Extract unique customers (no duplicates)
    # Each customer should appear exactly once based on customer_id
    pass


def extract_products(raw_data):
    """Extract unique product records from raw data.

    Args:
        raw_data: List of raw order records.

    Returns:
        List of unique product dictionaries with keys:
        product_id, product_name, product_price
    """
    # TODO: Implement this function
    # Extract unique products (no duplicates)
    # Each product should appear exactly once based on product_id
    pass


def extract_orders(raw_data):
    """Extract order records from raw data.

    Args:
        raw_data: List of raw order records.

    Returns:
        List of order dictionaries with keys:
        order_id, customer_id, product_id, quantity, order_date
    """
    # TODO: Implement this function
    # Extract orders with only the necessary columns
    # Do NOT include customer_name, customer_city, product_name, product_price
    # (those belong in other tables to avoid redundancy)
    pass


# =============================================================================
# Stage 2: Analysis (cleaned/ -> output/)
#
# Purpose: Transform cleaned data for a SPECIFIC analysis question
# This stage is ANALYSIS-SPECIFIC - different questions need different outputs
# =============================================================================

def compute_customer_summary(customers, orders, products):
    """Compute summary statistics per customer.

    This is an ANALYSIS-SPECIFIC transformation. The cleaned tables
    (customers, orders, products) could support many different analyses.
    This function answers one specific question: "What is each customer's
    total spending and order count?"

    Args:
        customers: List of customer records.
        orders: List of order records.
        products: List of product records.

    Returns:
        List of dictionaries with keys:
        customer_id, customer_name, total_orders, total_spending
    """
    # TODO: Implement this function
    # For each customer, compute:
    # - total_orders: number of orders they made
    # - total_spending: sum of (quantity * product_price) across all orders
    pass


# =============================================================================
# Utility Functions
# =============================================================================

def save_table(data, filepath, columns):
    """Save a table to a CSV file.

    Args:
        data: List of dictionaries.
        filepath: Output path.
        columns: List of column names to write.
    """
    Path(filepath).parent.mkdir(parents=True, exist_ok=True)
    with open(filepath, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=columns)
        writer.writeheader()
        for row in data:
            writer.writerow({col: row[col] for col in columns})
