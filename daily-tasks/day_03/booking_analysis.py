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

print("===== DAY 3: BOOKING ANALYTICS =====")
print("Total bookings:", len(df))

# 1. Bookings by hotel type
hotel_bookings = df["hotel"].value_counts()

print("\n===== BOOKINGS BY HOTEL =====")
print(hotel_bookings)

# 2. Cancellation analysis
cancellation = df.groupby("hotel")["is_canceled"].agg(
    total_bookings="count",
    canceled_bookings="sum",
    cancellation_rate="mean"
)

cancellation["cancellation_rate"] *= 100

print("\n===== CANCELLATION ANALYSIS =====")
print(cancellation.round(2))

# 3. Chart: Bookings by hotel type
plt.figure(figsize=(8, 5))
hotel_bookings.plot(kind="bar", color=["steelblue", "orange"])

plt.title("Bookings by Hotel Type")
plt.xlabel("Hotel Type")
plt.ylabel("Number of Bookings")
plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig(CHART_DIR / "day-03-bookings.png", dpi=150)
plt.show()
plt.close()

# 4. Chart: Cancellation rate by hotel type
plt.figure(figsize=(8, 5))
cancellation["cancellation_rate"].plot(
    kind="bar",
    color=["steelblue", "orange"]
)

plt.title("Cancellation Rate by Hotel Type")
plt.xlabel("Hotel Type")
plt.ylabel("Cancellation Rate (%)")
plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig(CHART_DIR / "day-03-cancellations.png", dpi=150)
plt.show()
plt.close()

print("\nCharts saved in:", CHART_DIR)
print("Booking analysis completed successfully!")
