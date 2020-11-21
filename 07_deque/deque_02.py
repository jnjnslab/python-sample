from collections import deque

d = deque(['a', 'b', 'c', 'b', 'd'])
print(d)
#末尾の要素を取り出して削除する
print(d.pop())
print(d)
#先頭の要素を取り出して削除する
print(d.popleft())
print(d)
#引数に指定した値と等しい最初の要素を削除する
d.remove('b')
print(d)
#すべての要素を削除する
d.clear()
print(d)
