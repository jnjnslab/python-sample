#要素を追加する
from collections import deque

#空のキューを作成する
d = deque()
print(d)
print(type(d))

d = deque(['m', 'n'])
print(d)
#末尾に追加する
d.append('o')
print(d)
#先頭に追加する
d.appendleft('l')
print(d)
#末尾にイテラブルオブジェクトの要素をすべて追加する
d.extend(['p', 'q'])
print(d)
#先頭にイテラブルオブジェクトの要素をすべて追加する
d.extendleft(['k', 'j'])
print(d)
#途中に追加する
d.insert(3, 'XXX')
print(d)
d.insert(-1, 'YYY')
print(d)
d.insert(100, 'ZZZ')
print(d)
d.insert(-100, 'XYZ')
print(d)
