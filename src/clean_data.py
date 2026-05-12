import pandas as pd


# LOADING RAW DATASET

leading_cause_nyc = pd.read_csv(
    "../Data/raw/NY_leading_cause_of_death.csv"
)

# BASIC DATA INSPECTION

print("\nFirst five rows:")
print(leading_cause_nyc.head())

print("\nDataset shape:")
print(leading_cause_nyc.shape)


# DUPLICATE CHECK

num_of_duplicates = leading_cause_nyc.duplicated().sum()

print(f"\nNumber of duplicates: {num_of_duplicates}")

# DROPPING DUPLICATES

leading_cause_nyc = leading_cause_nyc.drop_duplicates()

print("\nShape after duplicates removed:")
print(leading_cause_nyc.shape)


# CLEANING COLUMN NAMES

leading_cause_nyc.columns = (
    leading_cause_nyc.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
)

print("\nCleaned column names:")
print(leading_cause_nyc.columns)


# SAVING CLEANED DATASET

leading_cause_nyc.to_csv(
    "../Data/processed/NY_leading_cause_of_death_cleaned.csv",
    index=False
)

print("\nCleaned dataset saved successfully.")