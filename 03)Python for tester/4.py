'''
reading custom sheet
in excel sheet we can have multiple sheets and each sheet can have multiple rows and columns
in this python we can read our custom sheet using the openpyxl
'''
from openpyxl import load_workbook
x = load_workbook(filename='sample.xlsx')
sheet = x['Sheet2']
print(sheet['A1'].value)
print(sheet['A2'].value)