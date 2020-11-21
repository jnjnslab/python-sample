import time
#エポック
now = time.time()
print(now)
print(time.ctime(now))
print(time.localtime(now))
print(time.gmtime(now))

tm = time.localtime(now)
print(time.mktime(tm))

