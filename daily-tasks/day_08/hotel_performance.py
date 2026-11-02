
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DATA_FILE = ROOT / "data" / "processed" / "hotel_bookings_cleaned.csv"
CHART_DIR = ROOT / "visualizations"

df = pd.read_csv(DATA_FILE)
CHART_DIR.mkdir(parents=True, exist_ok=True)

print("===== DAY 8: HOTEL PERFORMANCE ANALYSIS =====")

# 1. Total bookings by hotel
hotel_bookings = df["hotel"].value_counts()

print("\nTOTAL BOOKINGS BY HOTEL:")
print(hotel_bookings)

# 2. Average Daily Rate by hotel
hotel_adr = df.groupby("hotel")["adr"].mean()

print("\nAVERAGE DAILY RATE BY HOTEL:")
print(hotel_adr.round(2))

# 3. Average stay duration by hotel
df["total_nights"] = (
    df["stays_in_weekend_nights"] +
    df["stays_in_week_nights"]
)

hotel_stay = df.groupby("hotel")["total_nights"].mean()

print("\nAVERAGE STAY DURATION:")
print(hotel_stay.round(2))

# 4. Repeat guest percentage by hotel
repeat_guests = df.groupby("hotel")["is_repeated_guest"].mean() * 100

print("\nREPEAT GUEST PERCENTAGE:")
print(repeat_guests.round(2))

# 5. Create comparison charts
hotel_bookings.plot(
    kind="bar",
    title="Total Bookings by Hotel"
)
plt.xlabel("Hotel")
plt.ylabel("Bookings")
plt.tight_layout()
plt.savefig(CHART_DIR / "day-08-hotel-bookings.png")
plt.close()

hotel_adr.plot(
    kind="bar",
    title="Average Daily Rate by Hotel"
)
plt.xlabel("Hotel")
plt.ylabel("Average ADR")
plt.tight_layout()
plt.savefig(CHART_DIR / "day-08-hotel-adr.png")
plt.close()

hotel_stay.plot(
    kind="bar",
    title="Average Stay Duration by Hotel"
)
plt.xlabel("Hotel")
plt.ylabel("Average Nights")
plt.tight_layout()
plt.savefig(CHART_DIR / "day-08-hotel-stay.png")
plt.close()

repeat_guests.plot(
    kind="bar",
    title="Repeat Guest Percentage by Hotel"
)
plt.xlabel("Hotel")
plt.ylabel("Repeat Guests (%)")
plt.tight_layout()
plt.savefig(CHART_DIR / "day-08-repeat-guests.png")
plt.close()

print("\nAll Day 8 charts saved successfully!")
