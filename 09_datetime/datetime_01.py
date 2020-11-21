from datetime import date,timedelta
#日付の作成
halloween = date(2020,10,31)
print(halloween)
print(halloween.year)
print(halloween.month)
print(halloween.day)
print(halloween.isoformat())
#当日の日付
now = date.today()
print(now)
#日付の加算
one_day = timedelta(days=1)
tomorrow = now + one_day
print(tomorrow)
yesterday = now - one_day
print(yesterday)
print(now + 17*one_day)
#最大日付
print(date.min)
#最小日付
print(date.max)




