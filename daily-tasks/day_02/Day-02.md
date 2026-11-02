
# Day 2: Data Cleaning and Preprocessing

## Objective
To clean the hotel booking dataset and prepare it for analysis.

## Tasks Completed
- Checked missing values.
- Identified duplicate records.
- Removed exact duplicate rows.
- Filled missing country values with "Unknown".
- Filled missing children values using the median.
- Converted reservation status date to datetime.
- Saved the cleaned dataset separately.

## Results
- Original records: 119,390
- Duplicate rows removed: 31,994
- Records after cleaning: 87,396
- Columns: 32
- Remaining missing agent values: 12,193
- Remaining missing company values: 82,137

## Output
data/processed/hotel_bookings_cleaned.csv

## Next Steps
Perform booking and cancellation analysis using the cleaned dataset.
