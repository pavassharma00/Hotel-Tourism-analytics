
import pandas as pd


def main():
    # Load dataset
    df = pd.read_csv("data/hotel_bookings.csv")

    print("===== DATASET OVERVIEW =====")
    print("Dataset loaded successfully!")
    print("Total records:", len(df))
    print("Total columns:", len(df.columns))

    print("\n===== FIRST 5 RECORDS =====")
    print(df.head())

    print("\n===== COLUMN NAMES =====")
    print(df.columns.tolist())

    print("\n===== MISSING VALUES =====")
    missing = df.isnull().sum()
    missing = missing[missing > 0].sort_values(ascending=False)
    print(missing)

    print("\n===== DUPLICATE RECORDS =====")
    print("Duplicate rows:", df.duplicated().sum())

    print("\n===== HOTEL DISTRIBUTION =====")
    print(df["hotel"].value_counts())

    print("\n===== BOOKING STATUS =====")
    print(df["is_canceled"].value_counts())


if __name__ == "__main__":
    main()
