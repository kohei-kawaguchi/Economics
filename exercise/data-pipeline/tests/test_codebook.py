"""Tests for codebook completeness.

These tests verify that the codebook properly documents all cleaned tables.
"""

import sys
from pathlib import Path

# Import the codebook configuration
# We need to parse the qmd file to extract the TABLES config
import re


def extract_tables_config():
    """Extract TABLES configuration from codebook.qmd."""
    codebook_path = Path(__file__).parent.parent / "report" / "codebook.qmd"
    
    if not codebook_path.exists():
        return None
    
    content = codebook_path.read_text()
    
    # Find the TABLES = { ... } block
    # This is a simplified extraction - in practice, we exec the Python code
    match = re.search(r'TABLES\s*=\s*\{', content)
    if not match:
        return None
    
    # For testing, we'll exec the Python code block
    # Extract the Python code from the qmd
    python_blocks = re.findall(r'```\{python\}(.*?)```', content, re.DOTALL)
    
    if not python_blocks:
        return None
    
    # Execute the first Python block to get TABLES
    code = python_blocks[0]
    
    # Remove Quarto directives
    code = re.sub(r'#\|.*\n', '', code)
    
    local_vars = {}
    exec(code, {"pd": None, "Path": Path}, local_vars)
    
    return local_vars.get("TABLES")


def test_codebook_exists():
    """Codebook file should exist."""
    codebook_path = Path(__file__).parent.parent / "report" / "codebook.qmd"
    assert codebook_path.exists(), (
        "Codebook not found at report/codebook.qmd"
    )


def test_tables_config_exists():
    """TABLES configuration should be defined."""
    tables = extract_tables_config()
    assert tables is not None, (
        "Could not find TABLES configuration in codebook.qmd"
    )


def test_all_tables_have_descriptions():
    """Each table should have a non-TODO description."""
    tables = extract_tables_config()
    if tables is None:
        return
    
    for name, config in tables.items():
        desc = config.get("description", "")
        assert "TODO" not in desc, (
            f"Table '{name}' has TODO in description. "
            "Replace with actual description."
        )
        assert len(desc) > 10, (
            f"Table '{name}' description is too short: '{desc}'"
        )


def test_orders_has_foreign_keys():
    """Orders table should have foreign keys defined."""
    tables = extract_tables_config()
    if tables is None:
        return
    
    orders = tables.get("orders", {})
    fks = orders.get("foreign_keys", {})
    
    assert "customer_id" in fks, (
        "Orders table should have customer_id as foreign key. "
        "Add: 'customer_id': 'customers' to foreign_keys"
    )
    assert "product_id" in fks, (
        "Orders table should have product_id as foreign key. "
        "Add: 'product_id': 'products' to foreign_keys"
    )


def test_all_tables_have_variables():
    """Each table should have variables defined."""
    tables = extract_tables_config()
    if tables is None:
        return
    
    expected_vars = {
        "customers": ["customer_id", "customer_name", "customer_city"],
        "products": ["product_id", "product_name", "product_price"],
        "orders": ["order_id", "customer_id", "product_id", "quantity", "order_date"],
    }
    
    for name, expected in expected_vars.items():
        config = tables.get(name, {})
        variables = config.get("variables", {})
        
        assert len(variables) > 0, (
            f"Table '{name}' has no variables defined. "
            "Add variable definitions to the TABLES configuration."
        )
        
        for var in expected:
            assert var in variables, (
                f"Table '{name}' is missing variable '{var}'. "
                "Add it to the variables configuration."
            )


def test_variables_have_required_fields():
    """Each variable should have type, unit, and desc."""
    tables = extract_tables_config()
    if tables is None:
        return
    
    required_fields = ["type", "unit", "desc"]
    
    for table_name, config in tables.items():
        variables = config.get("variables", {})
        
        for var_name, var_config in variables.items():
            for field in required_fields:
                assert field in var_config, (
                    f"Variable '{var_name}' in '{table_name}' is missing '{field}'. "
                    f"Add: '{field}': '...' to the variable configuration."
                )
                
                value = var_config[field]
                assert value and "TODO" not in str(value), (
                    f"Variable '{var_name}' in '{table_name}' has incomplete '{field}': '{value}'"
                )


def test_numeric_variables_have_units():
    """Numeric variables should have meaningful units."""
    tables = extract_tables_config()
    if tables is None:
        return
    
    numeric_types = ["integer", "float"]
    
    # Variables that should have actual units (not just "-")
    vars_needing_units = {
        ("products", "product_price"): "Should have currency unit (e.g., JPY)",
        ("orders", "quantity"): "Should have unit (e.g., units)",
    }
    
    for (table_name, var_name), message in vars_needing_units.items():
        config = tables.get(table_name, {})
        variables = config.get("variables", {})
        var_config = variables.get(var_name, {})
        
        unit = var_config.get("unit", "-")
        assert unit != "-" and unit != "", (
            f"Variable '{var_name}' in '{table_name}': {message}"
        )
