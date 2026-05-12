import pandas as pd
from pathlib import Path

# Project root directory. Basically clean_data.py.absolute_path().parent(src).parent(New_York_Leading_Cause_Of_Death)

BASE_DIR = Path(__file__).resolve().parent.parent

# Our data paths

raw_data_path = (BASE_DIR/ "Data"/ "raw"/ "NY_leading_cause_of_death.csv")

processed_data_dir = (BASE_DIR/ "Data"/ "processed")

# creates processed folder if it doesnt exist
processed_data_dir.mkdir(parents=True,exist_ok=True)

# Load raw dataset

leading_cause_nyc = pd.read_csv(raw_data_path)

# Basic data inspection

print("\nFirst five rows:")
print(leading_cause_nyc.head())

print("\nDataset shape:")
print(leading_cause_nyc.shape)

# Duplicate check

num_of_duplicates = (leading_cause_nyc.duplicated().sum())

print(f"\nNumber of duplicates: {num_of_duplicates}")

# Drop duplicates

leading_cause_nyc = (leading_cause_nyc.drop_duplicates())

print("\nShape after duplicates removed:")
print(leading_cause_nyc.shape)

# Clean cloumn names

leading_cause_nyc.columns = (leading_cause_nyc.columns.str.strip().str.lower().str.replace(" ", "_"))

print("\nCleaned column names:")
print(leading_cause_nyc.columns)

# Save clean dataset

output_path = (processed_data_dir/ "NY_leading_cause_of_death_cleaned.csv")

leading_cause_nyc.to_csv(output_path,index=False)

print("\nCleaned dataset saved successfully.")

print(f"\nSaved to:\n{output_path}")