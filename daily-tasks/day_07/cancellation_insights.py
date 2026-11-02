import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DATA_FILE = ROOT / "data" / "processed" / "hotel_bookings_cleaned.csv"
CHART_DIR = ROOT / "visualizations"

df = pd.read_csv(DATA_FILE)
CHART_DIR.mkdir(parents=True, exist_ok=True)

print("===== DAY 7: CANCELLATION INSIGHTS =====")

# 1. Overall cancellation analysis
total_bookings = len(df)
canceled = df["is_canceled"].sum()
not_canceled = total_bookings - canceled

cancellation_rate = (canceled / total_bookings) * 100

print("\nOVERALL CANCELLATION:")
print("Total bookings:", total_bookings)
print("Canceled bookings:", canceled)
print("Successful bookings:", not_canceled)
print("Cancellation rate:", round(cancellation_rate, 2), "%")

# 2. Cancellation by customer type
customer_cancel = df.groupby("customer_type")["is_canceled"].mean() * 100

print("\nCANCELLATION BY CUSTOMER TYPE:")
print(customer_cancel.round(2))

customer_cancel.plot(
    kind="bar",
    title="Cancellation Rate by Customer Type"
)
plt.xlabel("Customer Type")
plt.ylabel("Cancellation Rate (%)")
plt.tight_layout()
plt.savefig(CHART_DIR / "day-07-customer-cancellations.png")
plt.close()

# 3. Cancellation by lead time
df["lead_time_group"] = pd.cut(
    df["lead_time"],
    bins=[-1, 30, 90, 180, float("inf")],
    labels=["0-30 days", "31-90 days", "91-180 days", "180+ days"]
)

lead_cancel = df.groupby(
    "lead_time_group",
    observed=False
)["is_canceled"].mean() * 100

print("\nCANCELLATION BY LEAD TIME:")
print(lead_cancel.round(2))

lead_cancel.plot(
    kind="bar",
    title="Cancellation Rate by Booking Lead Time"
)
plt.xlabel("Lead Time")
plt.ylabel("Cancellation Rate (%)")
plt.tight_layout()
plt.savefig(CHART_DIR / "day-07-lead-time-cancellations.png")
plt.close()

# 4. Cancellation by hotel
hotel_cancel = df.groupby("hotel")["is_canceled"].mean() * 100

print("\nCANCELLATION BY HOTEL:")
print(hotel_cancel.round(2))

hotel_cancel.plot(
    kind="bar",
    title="Cancellation Rate by Hotel"
)
plt.xlabel("Hotel")
plt.ylabel("Cancellation Rate (%)")
plt.tight_layout()
plt.savefig(CHART_DIR / "day-07-hotel-cancellations.png")
plt.close()

print("\nAll Day 7 charts saved successfully!")
