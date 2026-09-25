from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt

base_dir = Path(__file__).resolve().parent
assets_dir = base_dir.parent / "assets"
assets_dir.mkdir(exist_ok=True)
candidate_files = [
    base_dir / "indian_agricultural_market_prices_cleaned.xlsx",
    base_dir / "indian_agricultural_market_prices_cleaned(EXCEL).xlsx",
    base_dir / "indian_agricultural_market_prices_cleaned (EXCEL).xlsx",
]
file_path = next((p for p in candidate_files if p.exists()), candidate_files[0])

if not file_path.exists():
    raise FileNotFoundError(f"Excel file not found. Looked for: {candidate_files}")

df = pd.read_excel(file_path, sheet_name="Cleaned_Data")

df["Arrival_Date"] = pd.to_datetime(df["Arrival_Date"], errors="coerce")

summary = pd.DataFrame({
    "Metric": [
        "Rows",
        "Columns",
        "Missing values",
        "Duplicate rows",
        "States",
        "Districts",
        "Markets",
        "Commodities",
        "Unique dates"
    ],
    "Value": [
        len(df),
        len(df.columns),
        int(df.isna().sum().sum()),
        int(df.duplicated().sum()),
        df["State"].nunique(),
        df["District"].nunique(),
        df["Market"].nunique(),
        df["Commodity"].nunique(),
        df["Arrival_Date"].nunique()
    ]
})

price_stats = df[
    ["Min_Price", "Max_Price", "Modal_Price"]
].describe().round(2)

state_analysis = (
    df.groupby("State")
    .agg(
        Records=("State", "size"),
        Markets=("Market", "nunique"),
        Avg_Modal_Price=("Modal_Price", "mean")
    )
    .sort_values("Records", ascending=False)
    .head(10)
    .round(2)
)

commodity_analysis = (
    df.groupby("Commodity")
    .agg(
        Records=("Commodity", "size"),
        Markets=("Market", "nunique"),
        Avg_Modal_Price=("Modal_Price", "mean"),
        Min_Modal_Price=("Modal_Price", "min"),
        Max_Modal_Price=("Modal_Price", "max")
    )
)

top_commodities = (
    commodity_analysis[
        commodity_analysis["Records"] >= 5
    ]
    .sort_values("Avg_Modal_Price", ascending=False)
    .head(10)
    .round(2)
)

market_analysis = (
    df.groupby("Market")
    .agg(
        Records=("Market", "size"),
        Avg_Price_Range=("Price_Range", "mean"),
        Avg_Modal_Price=("Modal_Price", "mean")
    )
    .sort_values("Avg_Price_Range", ascending=False)
    .head(10)
    .round(2)
)

flags = pd.DataFrame({
    "Flag": [
        "Low modal price (< ₹100)",
        "High modal price (>= ₹50,000)"
    ],
    "Records": [
        int((df["Modal_Price"] < 100).sum()),
        int((df["Modal_Price"] >= 50000).sum())
    ]
})

print("PYTHON EDA SUMMARY")
print(summary.to_string(index=False))

print("\nDESCRIPTIVE STATISTICS")
print(price_stats.to_string())

print("\nTOP 10 STATES")
print(state_analysis.to_string())

print("\nTOP 10 COMMODITIES BY AVERAGE MODAL PRICE")
print(top_commodities.to_string())

print("\nTOP 10 MARKETS BY AVERAGE PRICE RANGE")
print(market_analysis.to_string())

print("\nPRICE FLAGS")
print(flags.to_string(index=False))

plt.figure(figsize=(10, 5))
plt.bar(state_analysis.index, state_analysis["Records"])
plt.title("Top 10 States by Number of Records")
plt.xlabel("State")
plt.ylabel("Number of Records")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig(assets_dir / "top-states-by-records.png", dpi=160)
plt.show()

plt.figure(figsize=(10, 5))
plt.bar(
    top_commodities.index,
    top_commodities["Avg_Modal_Price"]
)
plt.title("Top 10 Commodities by Average Modal Price")
plt.xlabel("Commodity")
plt.ylabel("Average Modal Price")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig(assets_dir / "top-commodities-by-modal-price.png", dpi=160)
plt.show()

plt.figure(figsize=(10, 5))
plt.hist(df["Modal_Price"], bins=40)
plt.title("Distribution of Modal Prices")
plt.xlabel("Modal Price")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig(assets_dir / "modal-price-distribution.png", dpi=160)
plt.show()

plt.figure(figsize=(10, 5))
plt.bar(
    market_analysis.index,
    market_analysis["Avg_Price_Range"]
)
plt.title("Top 10 Markets by Average Price Range")
plt.xlabel("Market")
plt.ylabel("Average Price Range")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig(assets_dir / "top-markets-by-price-range.png", dpi=160)
plt.show()

"""
*Key findings:  
.6,141 records, 18 states, 131 districts, 302 markets, and 132 commodities.
.The dataset contains only one date: 20 September 2026, 
 so there is no valid historical trend analysis yet.
.Average modal price: ₹5,640.92
.Median modal price: ₹4,250
.Modal price range: ₹0.02–₹130,000
.Tamil Nadu has 5,495 records, far more than any other state in this snapshot.
.Among commodities with at least 5 records, Jasmine has the highest average modal price at ₹47,312.50, 
 followed by Kakada at ₹35,428.57.
.15 records have modal prices below ₹100 and 7 records have modal prices of ₹50,000 or more; 
 these remain flagged rather than being automatically removed.
.Palani (Uzhavar Sandhai) has the largest average price range among the markets analyzed: ₹1,927.27.


*What we produced

The Python phase now has:
    Load Data
        ↓
    Data Validation
        ↓
    Descriptive Statistics
        ↓
    State Analysis
        ↓
    Commodity Analysis
        ↓
    Market Analysis
        ↓
    Price Distribution
        ↓
    EDA Visualizations

*The four visualizations generated are:

1. Top 10 States by Number of Records
2. Top 10 Commodities by Average Modal Price
3. Distribution of Modal Prices
4. Top 10 Markets by Average Price Range

One important analytical caution: comparing commodity prices directly can be misleading when commodities 
may be reported under different market/unit conventions. We should mention that limitation rather than treating 
the price ranking as a direct profitability ranking.
"""

