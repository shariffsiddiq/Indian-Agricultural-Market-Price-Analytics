# Indian Agricultural Market Price Analytics

An end-to-end data analytics portfolio project exploring agricultural market prices across Indian states, districts, markets, and commodities.

![Project workflow](assets/project-workflow.svg)

## Project Overview

This project moves from raw market data to an analysis-ready dataset, analytical SQL queries, Python exploratory data analysis, and a Power BI report-ready model.

The analysis covers a snapshot containing **6,141 records**, **18 states**, **131 districts**, **302 markets**, and **132 commodities**. The available data represents one arrival date, so this project focuses on cross-sectional comparisons rather than historical price trends.

## Four-Phase Workflow

### Phase 1: Excel - Data Preparation

- Raw and cleaned CSV files
- Cleaned Excel workbook with the `Cleaned_Data` sheet
- Preparation of price fields, dates, and analysis-ready columns

Files: [Phase-1 Excel](Phase-1%20Excel/)

### Phase 2: Python - Exploratory Data Analysis

The Python workflow validates the data, calculates descriptive statistics, and analyzes state, commodity, and market patterns.

- Missing-value and duplicate checks
- Descriptive statistics for minimum, maximum, and modal prices
- State-level record and market coverage analysis
- Commodity price comparison
- Market price-range analysis
- Outlier flagging for unusually low and high modal prices

Files: [Python EDA script](Phase-2%20Python/Python(EDA).py)

### Phase 3: SQL - Structured Analysis

The SQL scripts set up the database and provide reusable analysis queries for data quality, states, commodities, markets, and window-function exercises.

Files: [Phase-3 SQL analysis](Phase-3%20Sql_Analysis/)

### Phase 4: Power BI - Reporting Dataset

The cleaned CSV and Power BI report file provide the foundation for interactive reporting and dashboard development.

Files: [Phase-4 Power BI](Phase-4%20Power%20BI/)

## Visual Analysis

### Top states by record count

![Top 10 states by number of records](assets/top-states-by-records.png)

Tamil Nadu contributes the largest share of records in this snapshot, with 5,495 records.

### Top commodities by average modal price

![Top 10 commodities by average modal price](assets/top-commodities-by-modal-price.png)

Among commodities with at least five records, Jasmine has the highest average modal price, followed by Kakada.

### Modal price distribution

![Distribution of modal prices](assets/modal-price-distribution.png)

The modal prices range from ₹0.02 to ₹130,000. Low and high values are flagged for review rather than removed automatically.

### Markets by average price range

![Top markets by average price range](assets/top-markets-by-price-range.png)

Palani (Uzhavar Sandhai) has the largest average price range among the markets analyzed.

## Key Findings

- Average modal price: **₹5,640.92**
- Median modal price: **₹4,250**
- 15 records have modal prices below ₹100
- 7 records have modal prices of ₹50,000 or more
- The dataset contains only one date, so historical trend conclusions are out of scope
- Direct commodity price comparisons should be interpreted carefully because market and unit conventions may differ

## Tools Used

`Microsoft Excel` `Python` `pandas` `matplotlib` `MySQL` `Power BI`

## Repository Structure

```text
Phase-1 Excel/       Raw and cleaned data files
Phase-2 Python/      Python EDA script and Excel input
Phase-3 Sql_Analysis/SQL setup, validation, and analysis queries
Phase-4 Power BI/    Cleaned CSV and Power BI report
assets/              README screenshots and workflow graphic
```

## How to Reproduce the Python Analysis

1. Install Python with `pandas`, `matplotlib`, and `openpyxl`.
2. Open `Phase-2 Python/Python(EDA).py`.
3. Run the script from the project root.
4. Review the console summary and charts in `assets/`.

## Limitations and Next Steps

- Add multiple arrival dates to support time-series analysis.
- Standardize price units before comparing commodities directly.
- Add a data dictionary and automated validation checks.
- Extend the Power BI report with slicers for state, market, commodity, and date.

## Portfolio Note

This repository demonstrates a complete analytics workflow: preparing data, validating quality, querying structured data, exploring patterns programmatically, and preparing an interactive BI deliverable.
