#リストの値をソートする
spam = [2,5,3.14,1,-7]
spam.sort()
print(spam)
spam.sort(reverse=True)
print(spam)

spam2 = ['ants','cats','badgers','dogs','elephants']
spam2.sort()
print(spam2)

spam3 = ['a','z','A','Z']
spam3.sort()
print(spam3)
spam3.sort(key=str.lower)
print(spam3)
