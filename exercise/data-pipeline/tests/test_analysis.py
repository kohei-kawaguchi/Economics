"""Tests for analysis (Stage 2: cleaned/ -> output/).

These tests verify that the analysis functions produce correct results.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from src.pipeline import compute_customer_summary


# Sample cleaned data for testing
CUSTOMERS = [
    {"customer_id": "101", "customer_name": "Alice", "customer_city": "Tokyo"},
    {"customer_id": "102", "customer_name": "Bob", "customer_city": "Osaka"},
]

PRODUCTS = [
    {"product_id": "P1", "product_name": "Widget", "product_price": "100"},
    {"product_id": "P2", "product_name": "Gadget", "product_price": "200"},
]

ORDERS = [
    {"order_id": "1", "customer_id": "101", "product_id": "P1", "quantity": "2", "order_date": "2025-01-15"},
    {"order_id": "2", "customer_id": "101", "product_id": "P2", "quantity": "1", "order_date": "2025-01-16"},
    {"order_id": "3", "customer_id": "102", "product_id": "P1", "quantity": "3", "order_date": "2025-01-17"},
]


def test_customer_summary_count():
    """Should return summary for each customer."""
    summary = compute_customer_summary(
        customers=CUSTOMERS,
        orders=ORDERS,
        products=PRODUCTS,
    )

    assert len(summary) == 2, (
        f"Expected summary for 2 customers, got {len(summary)}."
    )


def test_customer_summary_has_required_columns():
    """Summary should have all required columns."""
    summary = compute_customer_summary(
        customers=CUSTOMERS,
        orders=ORDERS,
        products=PRODUCTS,
    )
    required = {"customer_id", "customer_name", "total_orders", "total_spending"}

    for row in summary:
        assert required.issubset(row.keys()), (
            f"Summary missing required columns. "
            f"Required: {required}, Got: {set(row.keys())}"
        )


def test_customer_summary_order_count():
    """Should correctly count orders per customer."""
    summary = compute_customer_summary(
        customers=CUSTOMERS,
        orders=ORDERS,
        products=PRODUCTS,
    )

    summary_dict = {s["customer_id"]: s for s in summary}

    # Alice (101) has 2 orders
    assert int(summary_dict["101"]["total_orders"]) == 2, (
        f"Alice should have 2 orders, got {summary_dict['101']['total_orders']}."
    )

    # Bob (102) has 1 order
    assert int(summary_dict["102"]["total_orders"]) == 1, (
        f"Bob should have 1 order, got {summary_dict['102']['total_orders']}."
    )


def test_customer_summary_spending():
    """Should correctly calculate total spending per customer."""
    summary = compute_customer_summary(
        customers=CUSTOMERS,
        orders=ORDERS,
        products=PRODUCTS,
    )

    summary_dict = {s["customer_id"]: s for s in summary}

    # Alice (101): 2 * 100 (Widget) + 1 * 200 (Gadget) = 400
    assert float(summary_dict["101"]["total_spending"]) == 400, (
        f"Alice's total spending should be 400 (2*100 + 1*200), "
        f"got {summary_dict['101']['total_spending']}."
    )

    # Bob (102): 3 * 100 (Widget) = 300
    assert float(summary_dict["102"]["total_spending"]) == 300, (
        f"Bob's total spending should be 300 (3*100), "
        f"got {summary_dict['102']['total_spending']}."
    )
