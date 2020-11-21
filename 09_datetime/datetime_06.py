import datetime
from dateutil.relativedelta import relativedelta

#日付の加算
next_date = datetime.datetime(2016, 12, 15) + relativedelta(years=1,months=1,days=1)
print(next_date)
print(type(next_date))

#期間を計算する
diff = relativedelta(datetime.datetime(2018, 2, 17),datetime.datetime(2016, 12, 15))
print(diff)
print(diff.years)
print(diff.months)
print(diff.days)
