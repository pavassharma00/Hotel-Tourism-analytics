import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DATA_FILE = ROOT / "data" / "processed" / "hotel_bookings_cleaned.csv"
CHART_DIR = ROOT / "visualizations"

df = pd.read_csv(DATA_FILE)
CHART_DIR.mkdir(parents=True, exist_ok=True)

print("===== DAY 6: BOOKING TRENDS ANALYSIS =====")

# 1. Monthly bookings
months = [
    "January", "February", "March", "April",
    "May", "June", "July", "August",
    "September", "October", "November", "December"
]

df["arrival_date_month"] = pd.Categorical(
    df["arrival_date_month"],
    categories=months,
    ordered=True
)

monthly = df["arrival_date_month"].value_counts().sort_index()

print("\nMONTHLY BOOKINGS:")
print(monthly)

monthly.plot(kind="bar", title="Bookings by Arrival Month")
plt.xlabel("Month")
plt.ylabel("Number of Bookings")
plt.tight_layout()
plt.savefig(CHART_DIR / "day-06-monthly-bookings.png")
plt.close()

# 2. Average lead time
print("\nAVERAGE BOOKING LEAD TIME:")
print(round(df["lead_time"].mean(), 2), "days")

# 3. Average stay duration
df["total_nights"] = (
    df["stays_in_weekend_nights"] +
    df["stays_in_week_nights"]
)

print("\nAVERAGE STAY DURATION:")
print(round(df["total_nights"].mean(), 2), "nights")

# 4. Stay duration chart
stay_counts = df["total_nights"].value_counts().sort_index().head(15)

stay_counts.plot(kind="bar", title="Most Common Stay Durations")
plt.xlabel("Number of Nights")
plt.ylabel("Bookings")
plt.tight_layout()
plt.savefig(CHART_DIR / "day-06-stay-duration.png")
plt.close()

print("\nCharts saved successfully!")
