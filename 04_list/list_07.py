#removeメソッドで削除する
spam = ['cat','bat','rat','elephant']
spam.remove('bat')
print(spam)

spam2 = ['cat','bat','rat','cat','bat','hat']
spam2.remove('cat')
print(spam2)

#popメソッドで末尾の要素を取り出す
spam3 = ['cat','bat','rat','elephant']
print(spam3.pop())
print(spam3)
