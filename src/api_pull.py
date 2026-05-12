import requests
import pandas as pd
from pathlib import Path

# Project root directory. Set for resolving relative path issues
BASE_DIR = Path(__file__).resolve().parent.parent

# Output directory

RAW_DATA_DIR = BASE_DIR / "Data" / "raw"

# create raw folder if it doesnt exist. Removes ambiguity.
RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)

# NYC Open Data API endpoint

url = "https://data.cityofnewyork.us/resource/jb7j-dtam.json"

# Pagination loop for limit handling

limit = 1000
offset = 0

all_data = []

print("Pulling data from API...\n")

# Pagination loop

while True:

    params = {
        "$limit": limit,
        "$offset": offset
    }

    response = requests.get(url, params=params)

    # convert response into json
    data = response.json()

    # stopping condition
    if not data:
        break

    # append rows into master list
    all_data.extend(data)

    print(f"Pulled {len(data)} rows | Total: {len(all_data)}")

    # move pagination window
    offset += limit

# Creating our dataframe

leading_cause_nyc = pd.DataFrame(all_data)

# Save raw data to csv

output_path = (RAW_DATA_DIR/ "NY_leading_cause_of_death.csv")

leading_cause_nyc.to_csv(output_path,index=False)

print("\nDataset saved successfully.")
print(leading_cause_nyc.shape)

print(f"\nSaved to:\n{output_path}")