
import pandas as pd
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DATA_FILE = ROOT / "data" / "processed" / "hotel_bookings_cleaned.csv"
OUTPUT_FILE = ROOT / "daily-tasks" / "day_10" / "final_summary.txt"

df = pd.read_csv(DATA_FILE)

print("=" * 55)
print(" HOTEL & TOURISM ANALYTICS - FINAL PROJECT ANALYSIS")
print("=" * 55)

# 1. Dataset overview
total_bookings = len(df)
total_columns = len(df.columns)

print("\n1. DATASET OVERVIEW")
print("Total Bookings:", total_bookings)
print("Total Columns:", total_columns)
print("Total Hotels:", df["hotel"].nunique())

# 2. Hotel comparison
print("\n2. HOTEL PERFORMANCE")

hotel_summary = df.groupby("hotel").agg(
    total_bookings=("hotel", "size"),
    cancellation_rate=("is_canceled", "mean"),
    average_adr=("adr", "mean")
)

hotel_summary["cancellation_rate"] *= 100

print(hotel_summary.round(2))

# 3. Booking status
print("\n3. BOOKING STATUS")

canceled = int(df["is_canceled"].sum())
successful = total_bookings - canceled

print("Successful Bookings:", successful)
print("Canceled Bookings:", canceled)
print(
    "Overall Cancellation Rate:",
    round((canceled / total_bookings) * 100, 2),
    "%"
)

# 4. Customer analysis
print("\n4. CUSTOMER INSIGHTS")

print("\nCustomer Types:")
print(df["customer_type"].value_counts())

print("\nRepeat Guests:")
print(df["is_repeated_guest"].value_counts())

# 5. Revenue estimation
print("\n5. REVENUE ANALYSIS")

df["total_nights"] = (
    df["stays_in_weekend_nights"] +
    df["stays_in_week_nights"]
)

valid_bookings = df[df["is_canceled"] == 0].copy()

estimated_revenue = (
    valid_bookings["adr"] *
    valid_bookings["total_nights"]
).sum()

print("Estimated Room Revenue:", round(estimated_revenue, 2))
print("Average ADR:", round(valid_bookings["adr"].mean(), 2))

# 6. Average stay and lead time
print("\n6. BOOKING TRENDS")

print(
    "Average Stay Duration:",
    round(df["total_nights"].mean(), 2),
    "nights"
)

print(
    "Average Booking Lead Time:",
    round(df["lead_time"].mean(), 2),
    "days"
)

# 7. Key findings
city_cancel = hotel_summary.loc["City Hotel", "cancellation_rate"]
resort_cancel = hotel_summary.loc["Resort Hotel", "cancellation_rate"]

print("\n7. KEY FINDINGS")

print("1. City Hotel has the higher booking volume."
      if hotel_summary.loc["City Hotel", "total_bookings"] >
      hotel_summary.loc["Resort Hotel", "total_bookings"]
      else "1. Resort Hotel has the higher booking volume.")

print(
    "2. City Hotel has a higher cancellation rate."
    if city_cancel > resort_cancel
    else "2. Resort Hotel has a higher cancellation rate."
)

print("3. Estimated room revenue is calculated using ADR multiplied by total stay nights.")
print("4. Customer types and repeat guest data help understand customer behaviour.")
print("5. Booking lead time and stay duration help identify booking patterns.")

# 8. Save summary
OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
    file.write("HOTEL & TOURISM ANALYTICS - FINAL SUMMARY\n\n")
    file.write(f"Total Bookings: {total_bookings}\n")
    file.write(f"Total Columns: {total_columns}\n")
    file.write(f"Successful Bookings: {successful}\n")
    file.write(f"Canceled Bookings: {canceled}\n")
    file.write(
        f"Cancellation Rate: {(canceled / total_bookings) * 100:.2f}%\n"
    )
    file.write(f"Estimated Room Revenue: {estimated_revenue:.2f}\n")
    file.write(f"Average ADR: {valid_bookings['adr'].mean():.2f}\n")
    file.write(
        f"Average Stay: {df['total_nights'].mean():.2f} nights\n"
    )
    file.write(
        f"Average Lead Time: {df['lead_time'].mean():.2f} days\n"
    )
    file.write("\nHOTEL PERFORMANCE:\n")
    file.write(hotel_summary.round(2).to_string())
    file.write("\n\nKEY FINDINGS:\n")
    file.write("City Hotel and Resort Hotel performance compared.\n")
    file.write("Cancellation patterns and customer behaviour analysed.\n")
    file.write("Estimated room revenue calculated from ADR and stay nights.\n")

print("\nFinal summary saved to:", OUTPUT_FILE)
print("\nPROJECT ANALYSIS COMPLETED SUCCESSFULLY!")
