#ddt using the json and yaml file
import json  # To read JSON files

# Load the JSON file
with open('data.json') as file:
    data = json.load(file)  # Parse JSON into Python list of dicts

# Loop through each set of data
for entry in data:
    username = entry["username"]
    password = entry["password"]
    print("Testing login with:", username, password)
