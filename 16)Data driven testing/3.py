#DDT using the excel file
import openpyxl  # To work with Excel files

# Load Excel workbook
wb = openpyxl.load_workbook("data.xlsx")

# Select sheet
sheet = wb["Sheet1"]

# Iterate over rows starting from 2nd row (skip header)
for row in sheet.iter_rows(min_row=2, values_only=True):
    username, password = row  # Unpack row values
    print("Testing login with:", username, password)
