from datetime import date
#日付→文字列
fmt1 = "%Y/%m/%d (%A)"
some_day = date(2020,10,25)
print(some_day.strftime(fmt1))

