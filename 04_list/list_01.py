#インデックスを指定してリストから要素を取り出す
spam = ['cat','bat','rat','elephant']
print(spam[0])
print(spam[1])
print(spam[2])
print(spam[3])

spam2 = [['cat','bat'],[10,20,30,40,50]]
print(spam2[0])
print(spam2[0][1])
print(spam2[1][4])

#負のインデックス
spam3 = ['cat','bat','rat','elephant']
print(spam3[-1])
print(spam3[-3])

#部分リスト
spam4 = ['cat','bat','rat','elephant']
print(spam4[0:4])
print(spam4[1:3])
print(spam4[0:-1])
print(spam4[:2])
print(spam4[1:])
print(spam4[:])
