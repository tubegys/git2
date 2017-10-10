# _*_ coding:utf-8 _*_
import sqlite3
import xlrd
data = xlrd.open_workbook('test_excel.xlsx')  # 打开excel文件读取数据
table = data.sheets()[0]  # 通过索引顺序获得当前工作的表
nrows = table.nrows
ncols = table.ncols
print("行数:",table.nrows)
print('列数:',table.ncols)
for i in range(nrows):
    if i == 0: # 跳过表头
        continue
    print('第',i+1,'行：')
    print(table.row_values(i)[:7])
cell_A2 = table.cell(1,0).value
print('A2单元格的值是:',cell_A2)
# ret = table.put_cell(0,0,1,'3',0) # xlrd模块好像不支持对excel文件的操作，只能对其读
