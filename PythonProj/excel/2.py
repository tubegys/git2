import xlrd
workbook = xlrd.open_workbook('test_excel.xlsx')
worksheets = workbook.sheet_names()
print(worksheets)
