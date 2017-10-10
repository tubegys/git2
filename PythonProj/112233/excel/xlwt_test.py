import xlwt,os,sqlite3
create_sql = 'CREATE TABLE tb_test(id integer,name varchar2(20))'
select_sql = 'SELECT id,name FROM tb_test'
test_db = sqlite3.connect("test.db")  # 连接数据库
cur = test_db.cursor()  # 获取游标
# cur.execute(create_sql)
insert_sql = "insert into tb_test(id,name)values(?,?)"
Id = 0
for i in range(3):
    name = input('请输入姓名:')
    Id += 1
    student = (Id, name)
    cur.execute(insert_sql, student)
test_db.commit()
# 数据库插入已经完成，接着从数据库中读取内容，存放到excel中
workbook = xlwt.Workbook() # 打开工作簿
sheet1 = workbook.add_sheet('student_info', cell_overwrite_ok=True)  # 添加一个工作表
sheet1.write(0, 0, '学号')
sheet1.write(0, 1, '姓名')
student_info = cur.execute(select_sql)
row = 1
col = 0
for Id, name in student_info:
    sheet1.write(row, col, Id)
    sheet1.write(row, col+1, name)
    row += 1
workbook.save('E:\\PythonProj\\excel\\db_with_excel.xls')  # 保存excel工作簿
test_db.close()  # 关闭数据库连接
