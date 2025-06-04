import requests
import pandas as pd
from pyjstat import pyjstat

print("🚀 Starting API request to Statistics Finland")

# API endpoint for housing prices of new dwellings
url = "https://pxdata.stat.fi:443/PxWeb/api/v1/en/StatFin/ashi/statfin_ashi_pxt_12de.px"

# JSON query: filter by dwelling type, number of rooms, and plot ownership type
query = {
  "query": [
    {
      "code": "Talotyyppi",  # Building type
      "selection": {
        "filter": "item",
        "values": ["0", "1", "3"]  # All types, blocks of flats, terraced houses
      }
    },
    {
      "code": "Huoneluku",  # Number of rooms
      "selection": {
        "filter": "item",
        "values": ["00", "01", "02", "03"]  # All, 1, 2, 3+ rooms
      }
    },
    {
      "code": "Tontin omistusmuoto",  # Form of plot ownership
      "selection": {
        "filter": "item",
        "values": ["0", "1", "2"]  # All forms, own plot, rented plot
      }
    }
  ],
  "response": {
    "format": "json-stat2"
  }
}

# Send POST request to the API
response = requests.post(url, json=query)

# Check server response
print(f"✅ Response status: {response.status_code}")
if response.status_code != 200:
    print("❌ Failed to retrieve data from the API.")
    exit()

# Convert JSON-stat2 to pandas DataFrame
data = response.json()
dataset = pyjstat.from_json_stat(data)[0]

# Save dataset to CSV
dataset.to_csv("finland_housing_api_data.csv", index=False)

print("📁 Data successfully saved as 'finland_housing_api_data.csv'")
print(dataset.head())