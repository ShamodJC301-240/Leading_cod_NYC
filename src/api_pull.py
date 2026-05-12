import requests
import pandas as pd


# NYC OPEN DATA API ENDPOINT

url = "https://data.cityofnewyork.us/resource/jb7j-dtam.json"

# PAGINATION SETUP

limit = 1000
offset = 0

all_data = []

print("Pulling data from API...\n")


# PAGINATION LOOP

while True:

    params = {
        "$limit": limit,
        "$offset": offset
    }

    response = requests.get(url, params=params)

    data = response.json()

    # stopping condition
    if not data:
        break

    # appending rows into master list
    all_data.extend(data)

    print(f"Pulled {len(data)} rows | Total: {len(all_data)}")

    # moving offset window
    offset += limit


# CREATING DATAFRAME

leading_cause_nyc = pd.DataFrame(all_data)


# SAVING RAW DATA

leading_cause_nyc.to_csv(
    "../Data/raw/NY_leading_cause_of_death.csv",
    index=False
)

print("\nDataset saved successfully.")
print(leading_cause_nyc.shape)