from datetime import datetime

print(type(datetime.now()))
formatter_date = datetime.strptime('2017-01-01 03:05:58', '%Y-%m-%d %H:%M:%S')
print(type(formatter_date))
print(formatter_date)