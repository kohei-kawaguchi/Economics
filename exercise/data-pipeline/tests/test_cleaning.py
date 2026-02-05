"""Tests for data cleaning (Stage 1: input/ -> cleaned/).

These tests verify that the cleaning functions produce proper 3NF tables:
- No redundant data
- Unique primary keys
- Correct foreign key references
- All original information preserved
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from src.pipeline import (
    extract_customers,
    extract_orders,
    extract_products,
    load_raw_data,
)


# Sample raw data for testing
RAW_DATA = [
    {
        "order_id": "1",
        "customer_id": "101",
        "customer_name": "Alice",
        "customer_city": "Tokyo",
        "product_id": "P1",
        "product_name": "Widget",
        "product_price": "100",
        "quantity": "2",
        "order_date": "2025-01-15",
    },
    {
        "order_id": "2",
        "customer_id": "101",
        "customer_name": "Alice",
        "customer_city": "Tokyo",
        "product_id": "P2",
        "product_name": "Gadget",
        "product_price": "200",
        "quantity": "1",
        "order_date": "2025-01-16",
    },
    {
        "order_id": "3",
        "customer_id": "102",
        "customer_name": "Bob",
        "customer_city": "Osaka",
        "product_id": "P1",
        "product_name": "Widget",
        "product_price": "100",
        "quantity": "3",
        "order_date": "2025-01-17",
    },
]


# =============================================================================
# Tests for extract_customers
# =============================================================================

def test_customers_no_duplicates():
    """Each customer should appear exactly once (no redundancy)."""
    customers = extract_customers(raw_data=RAW_DATA)
    customer_ids = [c["customer_id"] for c in customers]

    assert len(customer_ids) == len(set(customer_ids)), (
        "Duplicate customer_id found. Each customer should appear only once."
    )


def test_customers_correct_count():
    """Should extract correct number of unique customers."""
    customers = extract_customers(raw_data=RAW_DATA)

    # RAW_DATA has 2 unique customers: 101 (Alice) and 102 (Bob)
    assert len(customers) == 2, (
        f"Expected 2 unique customers, got {len(customers)}. "
        "Extract unique customers based on customer_id."
    )


def test_customers_has_required_columns():
    """Customer records should have all required columns."""
    customers = extract_customers(raw_data=RAW_DATA)
    required = {"customer_id", "customer_name", "customer_city"}

    for customer in customers:
        assert required.issubset(customer.keys()), (
            f"Customer missing required columns. "
            f"Required: {required}, Got: {set(customer.keys())}"
        )


def test_customers_no_order_columns():
    """Customer records should NOT contain order-specific columns."""
    customers = extract_customers(raw_data=RAW_DATA)
    forbidden = {"order_id", "product_id", "quantity", "order_date", "product_name", "product_price"}

    for customer in customers:
        found_forbidden = forbidden.intersection(customer.keys())
        assert len(found_forbidden) == 0, (
            f"Customer record contains order/product columns: {found_forbidden}. "
            "These belong in other tables."
        )


# =============================================================================
# Tests for extract_products
# =============================================================================

def test_products_no_duplicates():
    """Each product should appear exactly once (no redundancy)."""
    products = extract_products(raw_data=RAW_DATA)
    product_ids = [p["product_id"] for p in products]

    assert len(product_ids) == len(set(product_ids)), (
        "Duplicate product_id found. Each product should appear only once."
    )


def test_products_correct_count():
    """Should extract correct number of unique products."""
    products = extract_products(raw_data=RAW_DATA)

    # RAW_DATA has 2 unique products: P1 (Widget) and P2 (Gadget)
    assert len(products) == 2, (
        f"Expected 2 unique products, got {len(products)}. "
        "Extract unique products based on product_id."
    )


def test_products_has_required_columns():
    """Product records should have all required columns."""
    products = extract_products(raw_data=RAW_DATA)
    required = {"product_id", "product_name", "product_price"}

    for product in products:
        assert required.issubset(product.keys()), (
            f"Product missing required columns. "
            f"Required: {required}, Got: {set(product.keys())}"
        )


# =============================================================================
# Tests for extract_orders
# =============================================================================

def test_orders_correct_count():
    """Should extract all orders."""
    orders = extract_orders(raw_data=RAW_DATA)

    assert len(orders) == 3, (
        f"Expected 3 orders, got {len(orders)}. "
        "Each raw record is one order."
    )


def test_orders_has_required_columns():
    """Order records should have all required columns."""
    orders = extract_orders(raw_data=RAW_DATA)
    required = {"order_id", "customer_id", "product_id", "quantity", "order_date"}

    for order in orders:
        assert required.issubset(order.keys()), (
            f"Order missing required columns. "
            f"Required: {required}, Got: {set(order.keys())}"
        )


def test_orders_no_redundant_columns():
    """Order records should NOT contain redundant customer/product info."""
    orders = extract_orders(raw_data=RAW_DATA)
    forbidden = {"customer_name", "customer_city", "product_name", "product_price"}

    for order in orders:
        found_forbidden = forbidden.intersection(order.keys())
        assert len(found_forbidden) == 0, (
            f"Order record contains redundant columns: {found_forbidden}. "
            "Customer info belongs in customers table. "
            "Product info belongs in products table. "
            "This is what 3NF (Third Normal Form) means - no redundancy!"
        )


# =============================================================================
# Tests for data integrity
# =============================================================================

def test_can_reconstruct_original():
    """Should be able to reconstruct original data by joining tables."""
    customers = extract_customers(raw_data=RAW_DATA)
    products = extract_products(raw_data=RAW_DATA)
    orders = extract_orders(raw_data=RAW_DATA)

    # Create lookup dictionaries
    customer_lookup = {c["customer_id"]: c for c in customers}
    product_lookup = {p["product_id"]: p for p in products}

    # Verify we can reconstruct each original record
    for original in RAW_DATA:
        order = next(o for o in orders if o["order_id"] == original["order_id"])
        customer = customer_lookup[order["customer_id"]]
        product = product_lookup[order["product_id"]]

        assert customer["customer_name"] == original["customer_name"], (
            "Cannot reconstruct customer_name from cleaned data."
        )
        assert product["product_name"] == original["product_name"], (
            "Cannot reconstruct product_name from cleaned data."
        )
