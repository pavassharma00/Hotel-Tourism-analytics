import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Project paths
ROOT = Path(__file__).resolve().parents[2]

DATA_FILE = ROOT / "data" / "processed" / "hotel_bookings_cleaned.csv"
CHART_DIR = ROOT / "visualizations"

CHART_DIR.mkdir(parents=True, exist_ok=True)

# Load cleaned dataset
df = pd.read_csv(DATA_FILE)

print("===== DAY 5: REVENUE ANALYTICS =====")

# Keep bookings that were not canceled
completed = df[df["is_canceled"] == 0].copy()

# Calculate total nights
completed["total_nights"] = (
    completed["stays_in_weekend_nights"]
    + completed["stays_in_week_nights"]
)

# Calculate estimated room revenue
completed["estimated_revenue"] = (
    completed["adr"] * completed["total_nights"]
)

print("\n===== HOTEL-WISE REVENUE =====")

hotel_revenue = completed.groupby("hotel")[
    "estimated_revenue"
].sum()

print(hotel_revenue.round(2))

print("\nTotal estimated room revenue:",
      round(hotel_revenue.sum(), 2))


# Average Daily Rate by hotel
print("\n===== AVERAGE DAILY RATE =====")

adr_analysis = completed.groupby("hotel")["adr"].mean()

print(adr_analysis.round(2))


# Monthly revenue analysis
print("\n===== MONTHLY REVENUE =====")

month_order = [
    "January", "February", "March", "April",
    "May", "June", "July", "August",
    "September", "October", "November", "December"
]

completed["arrival_date_month"] = pd.Categorical(
    completed["arrival_date_month"],
    categories=month_order,
    ordered=True
)

monthly_revenue = completed.groupby(
    "arrival_date_month",
    observed=True
)["estimated_revenue"].sum()

print(monthly_revenue.round(2))

if not monthly_revenue.empty:
    print("\nHighest revenue month:", monthly_revenue.idxmax())
    print("Revenue:", round(monthly_revenue.max(), 2))


# Chart 1: Hotel-wise revenue
plt.figure(figsize=(8, 5))

hotel_revenue.plot(kind="bar", color=["steelblue", "orange"])

plt.title("Estimated Revenue by Hotel Type")
plt.xlabel("Hotel Type")
plt.ylabel("Estimated Revenue")
plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig(CHART_DIR / "day-05-hotel-revenue.png", dpi=150)
plt.show()
plt.close()


# Chart 2: Monthly revenue
plt.figure(figsize=(10, 5))

monthly_revenue.plot(kind="line", marker="o", color="green")

plt.title("Monthly Estimated Revenue")
plt.xlabel("Month")
plt.ylabel("Estimated Revenue")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()

plt.savefig(CHART_DIR / "day-05-monthly-revenue.png", dpi=150)
plt.show()
plt.close()


# Chart 3: Average Daily Rate
plt.figure(figsize=(8, 5))

adr_analysis.plot(kind="bar", color=["mediumpurple", "teal"])

plt.title("Average Daily Rate by Hotel")
plt.xlabel("Hotel Type")
plt.ylabel("Average Daily Rate")
plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig(CHART_DIR / "day-05-average-daily-rate.png", dpi=150)
plt.show()
plt.close()

print("\nCharts saved successfully!")
print("Revenue analysis completed successfully!")
