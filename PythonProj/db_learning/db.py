import sqlite3
test_db = sqlite3.connect("test.db")  # 连接数据库
cur = test_db.cursor() # 获取游标
print("before insert...")
data = cur.execute("select id,name,gender from tb_test")
for id,name,gender in data:
        print(id,name,gender)

insert_sql = "insert into tb_test(id,name,gender)values(?,?,?)"
for t in [(6,"2222","m"),(7,"ddddddd","m")]:
    cur.execute(insert_sql,t)


data = cur.execute("select id,name,gender from tb_test")
for id,name,gender in data:
        print(id,name,gender)

test_db.close()   # 关闭数据库连接
