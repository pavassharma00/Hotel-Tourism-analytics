
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent

tasks = [
    ("Day 1: Dataset Inspection",
     "daily-tasks/day_01/dataset_inspection.py"),

    ("Day 2: Data Cleaning",
     "daily-tasks/day_02/data_cleaning.py"),

    ("Day 3: Booking Analysis",
     "daily-tasks/day_03/booking_analysis.py"),

    ("Day 4: Customer Analysis",
     "daily-tasks/day_04/customer_analysis.py"),

    ("Day 5: Revenue Analytics",
     "daily-tasks/day_05/revenue_analysis.py"),

    ("Day 6: Booking Trends",
     "daily-tasks/day_06/booking_trends.py"),

    ("Day 7: Cancellation Insights",
     "daily-tasks/day_07/cancellation_insights.py"),

    ("Day 8: Hotel Performance",
     "daily-tasks/day_08/hotel_performance.py"),

    ("Day 9: Final Dashboard",
     "daily-tasks/day_09/final_dashboard.py"),

    ("Day 10: Final Analysis",
     "daily-tasks/day_10/final_analysis.py"),
]

print("\n====================================")
print(" HOTEL & TOURISM ANALYTICS PLATFORM")
print("====================================")

for title, file_path in tasks:
    script = ROOT / file_path

    print(f"\n\n========== {title} ==========")

    if not script.exists():
        print(f"Not created yet: {file_path}")
        continue

    result = subprocess.run(
        [sys.executable, str(script)],
        cwd=ROOT
    )

    if result.returncode != 0:
        print(f"\nError while running {title}")
        break

print("\n====================================")
print(" PROJECT EXECUTION FINISHED")
print("====================================")
