from datetime import time,datetime,date
#時刻を作成する
this_time = time(12,13,14)
print(this_time)
print(this_time.hour)
print(this_time.minute)
print(this_time.second)
#日時を作成する
some_day = datetime(2020,10,25,8,59,12)
print(some_day)
print(some_day.isoformat())
#現在の日時
now = datetime.now()
print(now)
print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)
print(now.microsecond)
#日付と時刻の結合
this_day = date.today()
combined_date = datetime.combine(this_day,this_time)
print(combined_date)
print(combined_date.date())
print(combined_date.time())
