#空の集合を定義する
s = set()
#集合に要素を追加する
s.add(1)
s.add(2)
s.add(3)
s.add(4)
s.add(5)
s.add(5)
s.add(5)
#集合の要素を取り出す
print(len(s))
for i in s:
    print(i)
#集合の要素を削除する
s.remove(3)
#集合に存在するか調べる
print(5 in s)
#リストに変換する
l = list(s)
print(l)
#集合を空にする
s.clear()
print(len(s))
