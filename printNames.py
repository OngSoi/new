import openpyxl
wb = openpyxl.load_workbook("0805.xlsx")
ws0 = wb.worksheets[0]
print(ws0.title)
ws1 = wb.worksheets[1]
print(ws1.title)