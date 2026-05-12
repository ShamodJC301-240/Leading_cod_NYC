import pandas as pd
from pathlib import Path

# Project root

BASE_DIR = Path(__file__).resolve().parent.parent

# Data path

RAW_DATA_PATH = BASE_DIR / "Data" / "raw" / "NY_leading_cause_of_death.csv"
PROCESSED_DATA_DIR = BASE_DIR / "Data" / "processed"

# Create processed folder if it doesn't exist
PROCESSED_DATA_DIR.mkdir(parents=True, exist_ok=True)

# Load raw data

leading_cause_nyc = pd.read_csv(RAW_DATA_PATH)

print("\nRaw dataset loaded successfully.")

# Basic inspection
 
print("\nFirst five rows:")
print(leading_cause_nyc.head())

rows, cols = leading_cause_nyc.shape
print(f"\nDataset shape → {rows} rows, {cols} columns")

# Duplicates
 
num_duplicates = leading_cause_nyc.duplicated().sum()
print(f"\nNumber of duplicates: {num_duplicates}")

leading_cause_nyc = leading_cause_nyc.drop_duplicates()

rows, cols = leading_cause_nyc.shape
print(f"\nShape after removing duplicates → {rows} rows, {cols} columns")

# Column cleaning

leading_cause_nyc.columns = (leading_cause_nyc.columns.str.strip().str.lower().str.replace(" ", "_"))
cleaned_columns = leading_cause_nyc.columns

print("\nCleaned column names:")
for col in cleaned_columns:
    print(f'- {col}')



# Save cleaned data to processed csv

output_path = PROCESSED_DATA_DIR / "NY_leading_cause_of_death_cleaned.csv"

leading_cause_nyc.to_csv(output_path, index=False)

print("\nCleaned dataset saved successfully.")

print(f"Saved to:\n{output_path}")