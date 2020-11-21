from collections import deque

#オブジェクト自体を反転
d = deque(['a', 'b', 'c', 'd', 'e'])
d.reverse()
print(d)
#反転したイテレータを返す
d = deque(['a', 'b', 'c', 'd', 'e'])
print(deque(reversed(d)))

for v in d:
    print(v)
