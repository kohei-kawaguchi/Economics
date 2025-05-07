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
