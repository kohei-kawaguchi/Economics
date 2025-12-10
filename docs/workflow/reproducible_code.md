# Principles for Reproducible Code

This document outlines the principles and practices for writing reproducible code in economic research. Reproducibility ensures that analyses can be recreated, verified, and extended by others (including your future self).

## Overview

Reproducible code means that anyone (including yourself in the future) can:
- Run your code and obtain the same results
- Understand what the code does and why
- Modify parameters and configurations easily
- Verify the correctness of the implementation

## Core Principles

### 1. DRY (Don't Repeat Yourself)

**Principle:** Single implementation, parameterize differences.

**Why:** Duplicated code leads to inconsistencies, bugs, and maintenance nightmares. When you need to change logic, you should only change it in one place.

**How:**
- Write functions for repeated operations
- Use configuration files for parameters
- Create reusable modules and libraries
- Avoid copying and pasting code blocks

**Example:**
```python
# ❌ Bad: Repeated code
def analyze_dataset_1():
    data = load_data("input/dataset1.csv")
    cleaned = clean_data(data, method="standard")
    results = run_analysis(cleaned, alpha=0.05)
    save_results(results, "output/analysis1.pkl")

def analyze_dataset_2():
    data = load_data("input/dataset2.csv")
    cleaned = clean_data(data, method="standard")
    results = run_analysis(cleaned, alpha=0.05)
    save_results(results, "output/analysis2.pkl")

# ✅ Good: Parameterized function
def analyze_dataset(dataset_name, output_name):
    data = load_data(f"input/{dataset_name}.csv")
    cleaned = clean_data(data, method="standard")
    results = run_analysis(cleaned, alpha=0.05)
    save_results(results, f"output/{output_name}.pkl")

analyze_dataset("dataset1", "analysis1")
analyze_dataset("dataset2", "analysis2")
```

### 2. Config = Data

**Principle:** Save configurations with models, load automatically, no hardcoding.

**Why:** Hardcoded values make it impossible to reproduce results or understand what parameters were used. Configuration files serve as documentation and enable easy experimentation.

**How:**
- Store all parameters in configuration files (JSON, YAML, or code-based configs)
- Save configuration alongside model outputs
- Load configurations at runtime
- Never hardcode magic numbers or file paths

**Example:**
```python
# ❌ Bad: Hardcoded values
def solve_model():
    beta = 0.95
    gamma = 0.1
    max_iter = 1000
    tolerance = 1e-6
    # ... model solving code ...

# ✅ Good: Configuration file
# config.json
{
    "beta": 0.95,
    "gamma": 0.1,
    "max_iter": 1000,
    "tolerance": 1e-6
}

# solve_model.py
import json

def solve_model(config_path="config.json"):
    with open(config_path) as f:
        config = json.load(f)
    
    # Save config with output
    output = run_solver(config)
    save_output(output, config, "output/model_results.pkl")

def save_output(output, config, path):
    import pickle
    data = {
        "output": output,
        "config": config,
        "timestamp": datetime.now().isoformat()
    }
    with open(path, "wb") as f:
        pickle.dump(data, f)
```

### 3. Stable Paths

**Principle:** Use stable, semantic paths. Never use timestamps or versions in filenames.

**Why:** Timestamped or versioned paths make it impossible to reference outputs consistently. Other code, documentation, and collaborators will break when paths change.

**How:**
- Use semantic names: `output/eq/` not `output/eq_20250927/`
- Use `file.py` not `file_v2.py` or `file_old.py`
- Overwrite outputs when rerunning (use git for history)
- Use descriptive, stable directory structures

**Example:**
```python
# ❌ Bad: Timestamped paths
output_dir = f"output/results_{datetime.now().strftime('%Y%m%d')}"
save_results(results, f"{output_dir}/analysis.pkl")

# ❌ Bad: Versioned files
save_results(results, "output/analysis_v2.pkl")

# ✅ Good: Stable paths
output_dir = "output/equilibrium"
save_results(results, f"{output_dir}/analysis.pkl")
# Overwrite on rerun - use git to track history
```

### 4. Named Arguments

**Principle:** Always use named arguments for function calls.

**Why:** Named arguments make code self-documenting and prevent errors from argument order mistakes.

**How:**
- Define functions with clear parameter names
- Call functions with named arguments: `f(value=x)` not `f(x)`
- Use keyword-only arguments for critical parameters

**Example:**
```python
# ❌ Bad: Positional arguments
result = estimate_model(data, 0.05, 1000, True)

# ✅ Good: Named arguments
result = estimate_model(
    data=data,
    alpha=0.05,
    max_iter=1000,
    verbose=True
)
```

### 5. Version Control Everything

**Principle:** Track all code, configurations, and documentation in version control.

**Why:** Version control provides a complete history of changes, enables collaboration, and allows you to revert to previous working states.

**How:**
- Commit code frequently with descriptive messages
- Track configuration files
- Use `.gitignore` appropriately (exclude data, large outputs, but track code)
- Tag important versions/releases

**What to Track:**
- ✅ All source code (`src/`, `scripts/`, `R/`)
- ✅ Configuration files (`config.json`, `pyproject.toml`, `renv.lock`)
- ✅ Documentation (`docs/`, `README.md`)
- ✅ Tests (`test/`)
- ✅ Build scripts (`run.sh`, `Makefile`)

**What NOT to Track:**
- ❌ Large data files (use DVC or external storage)
- ❌ Generated outputs (unless small and necessary)
- ❌ Environment-specific files (`.env` with secrets)
- ❌ Temporary files

### 6. Explicit Dependencies

**Principle:** Explicitly declare all dependencies with versions.

**Why:** Different versions of packages can produce different results. Explicit dependencies ensure everyone uses the same environment.

**How:**
- Use dependency management tools:
  - **Python**: `pyproject.toml` with `uv` or `requirements.txt` with `pip`
  - **R**: `renv.lock` with `renv`
- Pin package versions
- Document system requirements

**Example:**
```toml
# pyproject.toml
[project]
dependencies = [
    "numpy>=1.24.0,<2.0.0",
    "pandas>=2.0.0,<3.0.0",
    "scipy>=1.10.0,<2.0.0",
]

[project.optional-dependencies]
dev = [
    "pytest>=7.0.0",
    "black>=23.0.0",
]
```

### 7. Deterministic Execution

**Principle:** Code should produce the same results when run multiple times.

**Why:** Non-deterministic code makes it impossible to verify correctness or debug issues.

**How:**
- Set random seeds explicitly
- Avoid time-dependent behavior
- Use deterministic algorithms when possible
- Document any necessary randomness

**Example:**
```python
# ❌ Bad: No seed
import numpy as np
data = np.random.normal(0, 1, 1000)

# ✅ Good: Explicit seed
import numpy as np
np.random.seed(42)  # Or use np.random.default_rng(42) for newer NumPy
data = np.random.normal(0, 1, 1000)

# ✅ Better: Seed in config
config = load_config("config.json")
np.random.seed(config["random_seed"])
```

### 8. Specification as Single Source of Truth

**Principle:** Maintain specifications as external documents. Code should implement the specification naturally, with functionality evident from structure.

**Why:** Comments become outdated and create maintenance burden. Specifications serve as the authoritative source for intent and design decisions. Code structure should make functionality obvious without relying on comments.

**How:**
- Write specifications in external documents (markdown, LaTeX, or structured formats)
- Code should directly implement the specification
- Use descriptive variable and function names that reflect the specification
- Structure code so its functionality is self-evident
- Avoid comments that explain intent (that's in the spec) or functionality (should be obvious)
- Keep specifications synchronized with code changes

**Example:**
```python
# ❌ Bad: Unclear names, relies on comments
def calc(x, y):
    # Multiply x and y, then add x
    return x * y + x

# ❌ Bad: Comments duplicate specification
def compute_present_value(future_value, discount_rate):
    """
    Compute present value using continuous discounting.
    Formula: PV = FV * exp(-r * t)
    For t=1: PV = FV * exp(-r)
    """
    return future_value * np.exp(-discount_rate)

# ✅ Good: Clear structure, specification in external doc
# Specification (docs/spec/present_value.md):
# "Compute present value using continuous discounting: PV = FV * exp(-r)"

def compute_present_value(future_value, discount_rate):
    return future_value * np.exp(-discount_rate)

# ✅ Better: Structure makes functionality obvious
def compute_present_value(future_value, discount_rate):
    discount_factor = np.exp(-discount_rate)
    present_value = future_value * discount_factor
    return present_value
```

**Specification Structure:**
- Model definitions and mathematical formulations
- Algorithm descriptions and pseudocode
- Design decisions and assumptions
- API contracts and interfaces
- Examples and use cases

### 9. Testable Code

**Principle:** Write code that can be tested, and write tests.

**Why:** Tests verify correctness, prevent regressions, and serve as documentation of expected behavior.

**How:**
- Write modular, testable functions
- Test properties (monotonicity, bounds), not exact values
- Use unit tests for individual functions
- Use integration tests for workflows
- Test on small, dummy data before expensive computations

**Example:**
```python
# ✅ Good: Testable function (specification in external doc)
def compute_equilibrium(price, demand_params, supply_params):
    equilibrium_price = solve_equilibrium_condition(price, demand_params, supply_params)
    equilibrium_quantity = compute_quantity_at_price(equilibrium_price, demand_params)
    return equilibrium_price, equilibrium_quantity

# ✅ Good: Property-based test (property defined in specification)
def test_equilibrium_monotonicity():
    base_price = 10.0
    low_demand = {"shift": 0.5}
    high_demand = {"shift": 1.5}
    
    p1, _ = compute_equilibrium(base_price, low_demand, {})
    p2, _ = compute_equilibrium(base_price, high_demand, {})
    
    assert p2 > p1
```

### 10. Programmatic Generation

**Principle:** Generate all outputs programmatically. Never manually edit generated files.

**Why:** Manual edits break reproducibility and create inconsistencies.

**How:**
- Generate figures and tables from code
- Use scripts to create all outputs
- Regenerate outputs when inputs change
- Store generation scripts in version control

**Example:**
```r
# ✅ Good: Programmatic figure generation
# report/generate_figures.Rmd
library(ggplot2)
library(dplyr)

# Load data
data <- readRDS("../cleaned/analysis_data.rds")

# Generate figure
p <- ggplot(data, aes(x = x_var, y = y_var)) +
  geom_point() +
  theme_classic() +
  labs(title = "Analysis Results")

# Save figure
ggsave("../figuretable/analysis_plot.png", p, width = 8, height = 6)
```

## Project Structure for Reproducibility

Follow a consistent project structure:

```
project/
├── input/              # Raw data (never modify)
├── cleaned/            # Processed data (3NF)
├── output/             # Analysis results (stable paths)
│   ├── eq/            # Equilibrium results
│   ├── simulate/      # Simulation results
│   └── estimate/      # Estimation results
├── src/                # Source code (packages)
├── scripts/            # Execution scripts
│   ├── pipeline/      # Pipeline scripts
│   ├── report/        # Report generation
│   └── temporary/     # Temporary scripts
├── test/               # Tests
├── config/             # Configuration files
├── docs/               # Documentation
├── pyproject.toml      # Python dependencies
├── renv.lock          # R dependencies
└── README.md          # Project documentation
```

## Workflow for Reproducible Analysis

1. **Plan** - Document the analysis plan and approach
2. **Implement** - Write code following reproducibility principles
3. **Test** - Test on small data, verify properties
4. **Configure** - Store parameters in configuration files
5. **Execute** - Run analysis with saved configurations
6. **Validate** - Check results against theoretical expectations
7. **Document** - Update documentation with findings
8. **Commit** - Save all code, configs, and docs to version control

## Common Anti-Patterns to Avoid

### ❌ Hardcoded Values
```python
# Don't do this
results = model.fit(data, lr=0.001, epochs=100)
```

### ❌ Timestamped Outputs
```python
# Don't do this
save_path = f"output/results_{datetime.now():%Y%m%d}.pkl"
```

### ❌ Versioned Files
```python
# Don't do this
save_path = "output/analysis_v2_final.pkl"
```

### ❌ Manual Edits to Generated Files
```bash
# Don't manually edit generated figures/tables
# Instead, fix the generation script
```

### ❌ Missing Dependencies
```python
# Don't assume packages are installed
# Always declare in pyproject.toml or requirements.txt
```

### ❌ Non-Deterministic Code
```python
# Don't forget to set seeds
data = np.random.normal(0, 1, 1000)  # Different each run!
```

### ❌ Relying on Comments for Intent or Functionality
```python
# Don't do this - intent should be in specification
def solve_model():
    # This function solves the equilibrium model using value iteration
    # It implements the Bellman equation from the paper
    # The algorithm converges when the value function stops changing
    # ... implementation ...

# Don't do this - functionality should be obvious from structure
def compute_price(demand, supply):
    # Multiply demand by supply, then divide by 2
    return demand * supply / 2
```

## Integration with Other Workflows

These reproducibility principles integrate with:

- **Data Pipeline** (see `data_pipeline.md`) - Stable paths for data storage
- **Version Control** (see `version_control.md`) - Track all code and configs
- **Reporting Pipeline** (see `reporting_pipeline.md`) - Programmatic figure generation
- **AI Coding Workflow** (see `ai_coding_workflow.md`) - Follow principles when using AI assistants

## Checklist for Reproducible Code

Before considering code complete, verify:

- [ ] All parameters are in configuration files (no hardcoding)
- [ ] All paths are stable (no timestamps or versions)
- [ ] Random seeds are set explicitly
- [ ] Dependencies are declared with versions
- [ ] Code is tested (at least property-based tests)
- [ ] Specification exists as external document and is up to date
- [ ] Code structure makes functionality self-evident (no reliance on comments)
- [ ] All code and configs are in version control
- [ ] Outputs are generated programmatically
- [ ] Code follows DRY principles (no duplication)
- [ ] Functions use named arguments

## References

- Sandve, G. K., Nekrutenko, A., Taylor, J., & Hovig, E. (2013). Ten simple rules for reproducible computational research. *PLoS computational biology*, 9(10), e1003285.
- Wilson, G., et al. (2014). Best practices for scientific computing. *PLoS biology*, 12(1), e1001745.
- Project-specific guidelines: See `.cursorrules` for additional reproducibility principles

