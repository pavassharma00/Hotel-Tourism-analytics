import pandas as pd
from pathlib import Path

# Project paths
ROOT = Path(__file__).resolve().parents[2]
INPUT_FILE = ROOT / "data" / "hotel_bookings.csv"
OUTPUT_FILE = ROOT / "data" / "processed" / "hotel_bookings_cleaned.csv"

# Load original dataset
df = pd.read_csv(INPUT_FILE)

print("===== DAY 2: DATA CLEANING =====")
print("Original dataset shape:", df.shape)

# 1. Check duplicate rows
duplicate_count = df.duplicated().sum()
print("\nDuplicate rows found:", duplicate_count)

# 2. Check missing values
print("\nMissing values before cleaning:")
print(df.isnull().sum()[df.isnull().sum() > 0])

# 3. Remove exact duplicate rows
df = df.drop_duplicates().copy()

# 4. Handle missing values
# Unknown company or agent is kept as missing because
# missing does not necessarily mean that no company/agent exists.
df["country"] = df["country"].fillna("Unknown")

# Only four children values are missing; fill with the median
# of available values and convert back to whole numbers.
children_median = df["children"].median()
df["children"] = df["children"].fillna(children_median).round().astype(int)

# 5. Convert reservation date to datetime
df["reservation_status_date"] = pd.to_datetime(
    df["reservation_status_date"],
    errors="coerce"
)

# 6. Create output directory and save cleaned data
OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(OUTPUT_FILE, index=False)

print("\n===== CLEANING SUMMARY =====")
print("Rows after removing duplicates:", len(df))
print("Columns:", len(df.columns))
print("Remaining duplicate rows:", df.duplicated().sum())
print("Cleaned dataset saved to:", OUTPUT_FILE)

print("\nRemaining missing values:")
print(df.isnull().sum()[df.isnull().sum() > 0])
