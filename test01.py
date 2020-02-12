import openpyxl as px
import os

files = os.listdir()
#print(files)
#print(len(files))

for y in files:
    z = y.split(".")
#    print(z[1])

    if z[1] == "xlsx":
#        print("OK xlsx " + y)
        print(y)
        book = px.load_workbook(y)
        name = book.sheetnames
        print(name)
#    else:
#        print("NG xlsx " + y)
# https://net9999.hatenablog.com/
