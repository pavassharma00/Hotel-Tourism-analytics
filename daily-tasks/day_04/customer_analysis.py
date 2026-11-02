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

print("===== DAY 4: CUSTOMER ANALYTICS =====")
print("Total customer records:", len(df))


# 1. Customer type analysis
print("\n===== CUSTOMER TYPES =====")

customer_types = df["customer_type"].value_counts()
print(customer_types)


# 2. Repeat customer analysis
print("\n===== REPEAT CUSTOMER ANALYSIS =====")

repeat_customers = df["is_repeated_guest"].value_counts()

print("New customers:", repeat_customers.get(0, 0))
print("Repeat customers:", repeat_customers.get(1, 0))


# 3. Market segment analysis
print("\n===== MARKET SEGMENT ANALYSIS =====")

market_segments = df["market_segment"].value_counts()
print(market_segments)


# 4. Top 10 customer countries
print("\n===== TOP 10 CUSTOMER COUNTRIES =====")

top_countries = df["country"].value_counts()
top_countries = top_countries.drop("Unknown", errors="ignore").head(10)

print(top_countries)


# 5. Chart: Customer types
plt.figure(figsize=(8, 5))

customer_types.plot(
    kind="bar",
    color="steelblue"
)

plt.title("Bookings by Customer Type")
plt.xlabel("Customer Type")
plt.ylabel("Number of Bookings")
plt.xticks(rotation=30)
plt.tight_layout()

plt.savefig(CHART_DIR / "day-04-customer-types.png", dpi=150)
plt.show()
plt.close()


# 6. Chart: Repeat customers
plt.figure(figsize=(7, 5))

repeat_customers.rename({
    0: "New Customers",
    1: "Repeat Customers"
}).plot(
    kind="bar",
    color=["orange", "seagreen"]
)

plt.title("New vs Repeat Customers")
plt.xlabel("Customer Category")
plt.ylabel("Number of Bookings")
plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig(CHART_DIR / "day-04-repeat-customers.png", dpi=150)
plt.show()
plt.close()


# 7. Chart: Market segments
plt.figure(figsize=(9, 5))

market_segments.plot(
    kind="bar",
    color="mediumpurple"
)

plt.title("Bookings by Market Segment")
plt.xlabel("Market Segment")
plt.ylabel("Number of Bookings")
plt.xticks(rotation=30)
plt.tight_layout()

plt.savefig(CHART_DIR / "day-04-market-segments.png", dpi=150)
plt.show()
plt.close()


print("\nCharts saved successfully!")
print("Customer analytics completed successfully!")
