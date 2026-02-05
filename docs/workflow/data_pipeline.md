# Data Pipeline

This document outlines the data pipeline structure for our economics project.

## Overview

Our data pipeline follows a three-stage workflow designed to maintain data integrity and analysis reproducibility:

1. **Input Folder** - Raw Data Storage
2. **Cleaned Folder** - 3NF Data Storage
3. **Output Folder** - Analysis Results

## Input Folder

The `input` folder contains raw, unprocessed data files:
- Original data sources (surveys, economic indicators, market data)
- Serves as the single source of truth for all analyses
- May contain inconsistencies, redundancies, or complex formats
- Should be preserved in its original state

## Cleaned Folder

The `cleaned` folder houses data transformed into Third Normal Form (3NF):
- Represents an intermediary stage between raw data and analysis
- Standardized, structured, and optimized for analytical use
- Enables consistent access across different analyses
- Follows database normalization principles to ensure data integrity

## Output Folder

The `output` folder is organized by analysis type:
- Each analysis has its own subdirectory (e.g., "simulate")
- Contains final results, models, and visualizations
- Stores processed data in appropriate formats (.pkl for Python, .rds for R)
- Facilitates reproducibility by isolating analysis results

## Third Normal Form (3NF) Definition

Third Normal Form (3NF) is a database normalization principle that ensures data is organized efficiently by:

1. Meeting all requirements of First Normal Form (1NF):
   - Each table has a primary key
   - Each column contains atomic (indivisible) values
   - No repeating groups

2. Meeting all requirements of Second Normal Form (2NF):
   - Satisfies 1NF
   - All non-key attributes are fully functionally dependent on the primary key

3. Additionally satisfying the 3NF requirement:
   - No transitive dependencies exist
   - Every non-key attribute depends directly on the primary key, not on other non-key attributes

### Benefits of 3NF in our Data Pipeline

- Eliminates data redundancy
- Reduces inconsistencies
- Improves data integrity
- Facilitates easier data updates and maintenance
- Creates a reliable foundation for analysis

In our project, transforming raw data to 3NF in the "cleaned" folder ensures analysts work with structured, consistent data that accurately represents the economic phenomena being studied.

## Programmatic Codebook Generation with Quarto

Generate the codebook using Quarto dynamic reporting to ensure it always reflects the actual data. Store the codebook source in the `report/` folder.

**File structure:**
```
report/
├── codebook.qmd          # Quarto source
├── codebook.html         # Generated codebook
└── codebook_files/       # Generated assets

cleaned/
├── customers.csv
├── products.csv
└── orders.csv
```

**Example `report/codebook.qmd`:**

````markdown
---
title: "Codebook: Cleaned Data"
format: html
---

```{python}
#| echo: false
import pandas as pd
from pathlib import Path

# Configuration: define tables and their metadata
TABLES = {
    "customers": {
        "file": "customers.csv",
        "description": "Customer demographic and contact information",
        "primary_key": ["customer_id"],
        "foreign_keys": {},
        "variables": {
            "customer_id": {"type": "string", "unit": "-", "desc": "Unique customer identifier"},
            "customer_name": {"type": "string", "unit": "-", "desc": "Full name of customer"},
            "customer_city": {"type": "string", "unit": "-", "desc": "City of residence"},
            "credit_limit": {"type": "float", "unit": "JPY", "desc": "Maximum credit amount"},
        }
    },
    "products": {
        "file": "products.csv",
        "description": "Product catalog with pricing",
        "primary_key": ["product_id"],
        "foreign_keys": {},
        "variables": {
            "product_id": {"type": "string", "unit": "-", "desc": "Unique product identifier"},
            "product_name": {"type": "string", "unit": "-", "desc": "Product display name"},
            "product_price": {"type": "float", "unit": "JPY", "desc": "Unit price"},
        }
    },
    "orders": {
        "file": "orders.csv",
        "description": "Order transaction records",
        "primary_key": ["order_id"],
        "foreign_keys": {
            "customer_id": "customers",
            "product_id": "products",
        },
        "variables": {
            "order_id": {"type": "integer", "unit": "-", "desc": "Unique order identifier"},
            "customer_id": {"type": "string", "unit": "-", "desc": "Reference to customers table"},
            "product_id": {"type": "string", "unit": "-", "desc": "Reference to products table"},
            "quantity": {"type": "integer", "unit": "units", "desc": "Number of items ordered"},
            "order_date": {"type": "date", "unit": "YYYY-MM-DD", "desc": "Date of order placement"},
        }
    },
}


CLEANED_DIR = Path("../cleaned")


def load_table(filename):
    """Load a CSV table from the cleaned directory."""
    return pd.read_csv(CLEANED_DIR / filename)


def compute_summary(df, var_config):
    """Compute summary statistics for a dataframe."""
    summary = []
    for col in df.columns:
        stats = {
            "Variable": col,
            "N": len(df),
            "Missing": df[col].isna().sum(),
            "Unique": df[col].nunique(),
        }
        if pd.api.types.is_numeric_dtype(df[col]):
            stats["Mean"] = f"{df[col].mean():.2f}"
            stats["Std"] = f"{df[col].std():.2f}"
            stats["Min"] = f"{df[col].min():.2f}"
            stats["Max"] = f"{df[col].max():.2f}"
        else:
            stats["Mean"] = "-"
            stats["Std"] = "-"
            stats["Min"] = "-"
            stats["Max"] = "-"
        summary.append(stats)
    return pd.DataFrame(summary)
```

## Table Overview

```{python}
#| echo: false
overview = []
for name, config in TABLES.items():
    df = load_table(config["file"])
    overview.append({
        "Table": f"`{config['file']}`",
        "Description": config["description"],
        "Primary Key": ", ".join(f"`{k}`" for k in config["primary_key"]),
        "Rows": len(df),
    })
pd.DataFrame(overview)
```

```{python}
#| echo: false
#| output: asis
from IPython.display import Markdown

for name, config in TABLES.items():
    df = load_table(config["file"])
    
    # Section header
    print(f"\n## {config['file']}\n")
    print(f"{config['description']}\n")
    
    # Keys
    print("### Keys\n")
    print(f"- **Primary Key:** {', '.join(f'`{k}`' for k in config['primary_key'])}")
    if config["foreign_keys"]:
        print("- **Foreign Keys:**")
        for fk, ref in config["foreign_keys"].items():
            print(f"  - `{fk}` → `{ref}.csv`")
    else:
        print("- **Foreign Keys:** None")
    
    # Variables
    print("\n### Variables\n")
    print("| Variable | Type | Unit | Description |")
    print("|----------|------|------|-------------|")
    for var, meta in config["variables"].items():
        print(f"| `{var}` | {meta['type']} | {meta['unit']} | {meta['desc']} |")
    
    # Summary statistics
    print("\n### Summary Statistics\n")
    summary_df = compute_summary(df, config["variables"])
    print(summary_df.to_markdown(index=False))
    print("\n---\n")
```
````

**Render the codebook:**

```bash
quarto render report/codebook.qmd
```

**Benefits of Quarto codebook:**
- Summary statistics computed from actual data
- Automatically updates when data changes
- Single source of truth for variable definitions
- Can render to HTML, PDF, or Word
