from collections import deque

#デフォルトでは右に1個ずつ要素がローテート（スクロール）する
d = deque(['a', 'b', 'c', 'd', 'e'])
print(d)
d.rotate()
print(d)
#引数に整数値を指定すると、その個数ずつ要素が右にローテートする。負の値を指定すると左にローテート。要素数を超える値を指定してもOK。
d = deque(['a', 'b', 'c', 'd', 'e'])
d.rotate(2)
print(d)

d = deque(['a', 'b', 'c', 'd', 'e'])
d.rotate(-1)
print(d)

d = deque(['a', 'b', 'c', 'd', 'e'])
d.rotate(6)
print(d)
