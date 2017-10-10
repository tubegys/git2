from datetime import datetime, timedelta, timezone # datetime是个模块，该模块还包含datetime类
now = datetime.now()  # 获取当前时间
print(now)
dt = datetime(2017, 2, 3, 21, 23)  # 获取指定日期和时间,dt是datetime类型的
print(dt)
timestamp = dt.timestamp()
print(timestamp)  # 获取时间戳
print(datetime.fromtimestamp(timestamp))  # 将时间戳转换成datetime类型(本地时区-东8区)
print(datetime.utcfromtimestamp(timestamp))  # 将时间戳转换成datetime类型（UTC标准时区）
str_day = datetime.strptime('2017-2-3 21:35', '%Y-%m-%d %H:%M')  # 将字符串转换成datetime类型
print(str_day)
print(dt.strftime('%Y-%m-%d %H:%M:%S'))  # 将datetime格式按指定格式 转化成字符串的形式
print(dt.strftime('%a,%b %d'))
dt_plus3hours = dt + timedelta(hours=3)  # 引入timedelta类，可以进行datetime类型的加减
print(dt_plus3hours)
dt_minus_1day_12hours = dt - timedelta(days=1, hours=12)
print(dt_minus_1day_12hours)
tz_utc_8 = timezone(timedelta(hours=8))  # 创建UTC+8:00 时区
dt = dt.replace(tzinfo=tz_utc_8)  # 强制设置为UTC +8:00
print(dt)

utc_now = datetime.utcnow().replace(tzinfo=timezone.utc)
# utc_now 是datetime类型，先通过datetime类的utcnow方法获得当前utc的时间 ，再用replace方法强制设置时区信息
bj_now = utc_now.astimezone(timezone(timedelta(hours=8)))
print(bj_now)
# 通过astimezone方法，设置时区
# 时区转换的关键在于，拿到一个datetime时，要获知正确的时区，然后强制设置时区，作为基准时间
# 利用带时区的datetime，通过astimezone方法，可以转换到任意时区
# 注：不是必须从UTC+0:00 时区转换到任意时区，任何带时区的datetime都可以转换

