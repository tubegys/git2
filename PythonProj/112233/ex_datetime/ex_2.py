from datetime import datetime, date, tzinfo
today = date.today()
tomorrow = today.replace(day=5)  # 指定新的年月日，生成新的date对象
print(today.timetuple())  # 返回一个time.struct_time类对象……
print(today.isocalendar())  # 返回一个元组，里面记录当前对象的日期
print(today.isoweekday())  # 返回当前对象的星期
print(today.isoformat())  # 返回字符串类型的日期
print(datetime.today())
print(datetime.now(tz=tzinfo(8)))