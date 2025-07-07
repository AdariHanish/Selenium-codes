#entering the fake data into the excel sheet
from openpyxl import Workbook
from faker import Faker
x = Workbook()
a = x.active
f=Faker()
for i in range(1,11):
    a.cell(row=i,column=1,value=f.name())
x.save("fake_data.xlsx")