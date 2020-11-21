from collections import deque

d = deque(['a', 'a', 'b', 'c'])
#全体の要素数をカウントする
print(len(d))
#指定した値と等しい要素の数をカウント
print(d.count('a'))
print(d.count('x'))
#要素が存在するか判定する
print('b' in d)
print('x' in d)

