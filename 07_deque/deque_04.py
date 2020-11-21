from collections import deque
#要素を取り出す
d = deque(['a', 'b', 'c', 'c', 'd'])
print(d[0])

print(d[-1])
#要素を更新する
d[2] = 'X'
print(d)
#位置を検索する
print(d.index('c'))