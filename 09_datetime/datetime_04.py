import time
#日付→文字列
t = time.localtime()
print(t)
fmt1 = "%Y/%m/%d (%A) %H:%M:%S"
print(time.strftime(fmt1,t))
#文字列→日付
fmt2 = "%Y-%m-%d"
print(time.strptime("2012-01-29",fmt2))
