#リスト内包表記
#1から10
l1 = [i for i in range(1,11)]
print(l1)
#3の倍数
l2 = [i for i in range(1,31) if i % 3 == 0]
print(l2)
l3 = [i * 3  for i in range(1,11)]
print(l3)
