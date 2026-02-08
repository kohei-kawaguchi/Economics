# Data Pipeline Exercise

Practice building a data pipeline that transforms raw data through cleaning to analysis.

## Learning Objectives

- Understand the difference between data cleaning and analysis
- Implement data cleaning that produces non-redundant (3NF) tables
- Build analysis that uses cleaned data
- Create a codebook documenting cleaned data
- Follow reproducible code principles

## Key Concept: Two-Stage Pipeline

```
input/          ->      cleaned/        ->      output/
(raw data)              (3NF tables)            (analysis results)

Stage 1: CLEANING           Stage 2: ANALYSIS
- Analysis-AGNOSTIC         - Analysis-SPECIFIC
- Remove redundancy         - Answer specific questions
- Can support ANY analysis  - Uses cleaned tables
```

### Common Mistake

Students often mix up these two stages:

| Cleaning (Stage 1) | Analysis (Stage 2) |
|--------------------|--------------------|
| Remove duplicate customer info | Calculate total spending per customer |
| Normalize into separate tables | Aggregate, filter, join for insights |
| Result: 3NF tables | Result: Analysis output |
| Supports ANY future analysis | Answers ONE specific question |

## Project Structure

```
data-pipeline/
├── input/                  # Raw data (never modify)
│   └── sales.csv
├── cleaned/                # 3NF tables (you create these)
│   ├── customers.csv
│   ├── products.csv
│   └── orders.csv
├── output/                 # Analysis results (you create these)
│   └── customer_summary.csv
├── report/                 # Documentation
│   └── codebook.qmd        # <- Complete the codebook here
├── config/
│   └── pipeline.json
├── src/
│   └── pipeline.py         # <- Implement functions here
├── scripts/
│   └── run_pipeline.py
└── tests/
```

## Setup

1. Accept this assignment on GitHub Classroom
2. Clone your repository:
   ```bash
   git clone <your-repository-url>
   cd <repository-name>
   ```

## Exercise Steps

### Step 1: Create issues for meaningful units

Create separate issues, one per meaningful unit of work. Use titles like these:

- `Implement Stage 1 cleaning functions`
- `Implement Stage 2 analysis function`
- `Complete codebook`
- `Run full pipeline and verify outputs`

### Step 2: Create a Branch

```bash
git fetch origin
git switch -c feature/implement-pipeline
```

### Step 3: Implement Stage 1 - Data Cleaning

Open `src/pipeline.py` and implement:

1. `extract_customers(raw_data)` - Extract unique customers
2. `extract_products(raw_data)` - Extract unique products
3. `extract_orders(raw_data)` - Extract orders (without redundant columns)

**Key requirements:**
- Each customer appears ONCE (no duplicates)
- Each product appears ONCE (no duplicates)
- Orders do NOT contain customer_name, customer_city, product_name, product_price

Test Stage 1:
```bash
uv run pytest tests/test_cleaning.py -v
```

### Step 4: Implement Stage 2 - Analysis

Implement in `src/pipeline.py`:

1. `compute_customer_summary(customers, orders, products)` - Compute spending per customer

Test Stage 2:
```bash
uv run pytest tests/test_analysis.py -v
```

### Step 5: Run the Full Pipeline

```bash
uv run python scripts/run_pipeline.py
```

### Step 6: Complete the Codebook

Open `report/codebook.qmd` and complete the `TABLES` configuration:

1. Add descriptions for each table
2. Define foreign keys for the orders table
3. Define all variables with their type, unit, and description

**Variable types:** `string`, `integer`, `float`, `date`

**Units:** Use `-` for identifiers, actual units for measurements (e.g., `JPY`, `units`)

Render the codebook:
```bash
quarto render report/codebook.qmd
```

Test the codebook:
```bash
uv run pytest tests/test_codebook.py -v
```

### Step 7: Commit and Push

```bash
git add src/pipeline.py report/codebook.qmd
git commit -m "Implement cleaning and analysis, closes #1 closes #2"
git commit -m "Complete codebook, closes #3"
git push -u origin feature/implement-pipeline
```

### Step 8: Create and Merge PR

1. Go to GitHub and create a Pull Request
2. Review your changes
3. Merge the PR

## Grading Criteria

| Component | Points | What is tested |
|-----------|--------|----------------|
| Data Cleaning | 30 | 3NF properties: no duplicates, no redundancy, correct columns |
| Analysis | 20 | Correct calculations: order count, total spending |
| Codebook | 20 | All tables documented, variables defined with types and units |
| Git Workflow | 30 | Multiple commits, issue reference, descriptive messages |

## Verification

```bash
# Test Stage 1: Cleaning
uv run pytest tests/test_cleaning.py -v

# Test Stage 2: Analysis
uv run pytest tests/test_analysis.py -v

# Test Codebook
uv run pytest tests/test_codebook.py -v

# Test Git Workflow
uv run pytest tests/test_workflow.py -v

# Run full pipeline
uv run python scripts/run_pipeline.py

# Render codebook
quarto render report/codebook.qmd
```

## Reference

See [Data Pipeline Documentation](docs/workflow/data_pipeline.md) for detailed explanations of 3NF and the pipeline structure.
