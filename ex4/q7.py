import datetime as dt

# 获取当前datetime
now = dt.datetime.now()
print(now)

d = dt.date(2021, 3, 24)
print(d)
# 打印年
print('year:', d.year)
# 打印月
print('month:', d.month)
# 打印日
print('day:', d.day)

