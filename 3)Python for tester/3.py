#how to read data from excel
from openpyxl import load_workbook
x=load_workbook(filename='sample.xlsx')
a=x.active
print(a['A1'].value,end=" ")
print(a['B1'].value)