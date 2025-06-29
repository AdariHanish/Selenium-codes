#writting multiple data
from openpyxl import Workbook
x=Workbook()
a=x.active
data=[["Name","Age"],["Hanish",20],["Kiran",25],["Ashika",24]]
for i in data:
    a.append(i)
x.save("sample.xlsx")