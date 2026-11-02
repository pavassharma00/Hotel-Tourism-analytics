
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DATA_FILE = ROOT / "data" / "processed" / "hotel_bookings_cleaned.csv"
CHART_DIR = ROOT / "visualizations"

df = pd.read_csv(DATA_FILE)
CHART_DIR.mkdir(parents=True, exist_ok=True)

print("===== DAY 9: FINAL ANALYTICS DASHBOARD =====")

# Basic calculations
total_bookings = len(df)
canceled = df["is_canceled"].sum()
successful = total_bookings - canceled
cancellation_rate = (canceled / total_bookings) * 100

df["total_nights"] = (
    df["stays_in_weekend_nights"] +
    df["stays_in_week_nights"]
)

valid_bookings = df[df["is_canceled"] == 0].copy()
estimated_revenue = (
    valid_bookings["adr"] * valid_bookings["total_nights"]
).sum()

average_adr = valid_bookings["adr"].mean()

hotel_bookings = df["hotel"].value_counts()
monthly_bookings = df["arrival_date_month"].value_counts()

# Print dashboard summary
print("\nKEY PERFORMANCE INDICATORS")
print("Total Bookings:", total_bookings)
print("Successful Bookings:", successful)
print("Canceled Bookings:", canceled)
print("Cancellation Rate:", round(cancellation_rate, 2), "%")
print("Estimated Room Revenue:", round(estimated_revenue, 2))
print("Average ADR:", round(average_adr, 2))

# Create dashboard
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle(
    "HOTEL & TOURISM ANALYTICS DASHBOARD",
    fontsize=18,
    fontweight="bold"
)

# Chart 1: Hotel bookings
hotel_bookings.plot(
    kind="bar",
    ax=axes[0, 0],
    title="Bookings by Hotel"
)
axes[0, 0].set_xlabel("Hotel")
axes[0, 0].set_ylabel("Bookings")

# Chart 2: Booking status
axes[0, 1].pie(
    [successful, canceled],
    labels=["Successful", "Canceled"],
    autopct="%1.1f%%",
    startangle=90
)
axes[0, 1].set_title("Booking Status Distribution")

# Chart 3: Monthly bookings
months = [
    "January", "February", "March", "April",
    "May", "June", "July", "August",
    "September", "October", "November", "December"
]

monthly_bookings = (
    df["arrival_date_month"]
    .value_counts()
    .reindex(months)
)

monthly_bookings.plot(
    kind="bar",
    ax=axes[1, 0],
    title="Monthly Booking Trends"
)
axes[1, 0].set_xlabel("Month")
axes[1, 0].set_ylabel("Bookings")

# Chart 4: Revenue by hotel
revenue_by_hotel = valid_bookings.groupby("hotel").apply(
    lambda group: (
        group["adr"] * group["total_nights"]
    ).sum()
)

revenue_by_hotel.plot(
    kind="bar",
    ax=axes[1, 1],
    title="Estimated Room Revenue by Hotel"
)
axes[1, 1].set_xlabel("Hotel")
axes[1, 1].set_ylabel("Estimated Revenue")

plt.tight_layout(rect=[0, 0, 1, 0.95])

dashboard_path = CHART_DIR / "day-09-final-dashboard.png"
plt.savefig(dashboard_path, dpi=300, bbox_inches="tight")
plt.close()

print("\nDashboard saved to:", dashboard_path)
print("\nDay 9 completed successfully!")
