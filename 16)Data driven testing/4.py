#DDT using the csv file
import csv  # To handle CSV files

# Open the CSV file
with open("data.csv") as file:
    reader = csv.DictReader(file)  # Read as dictionary

    for row in reader:
        username = row["username"]
        password = row["password"]
        print("Testing login with:", username, password)