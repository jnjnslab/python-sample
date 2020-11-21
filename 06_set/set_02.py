#集合の演算
a = {1,2}
b = {2,3}
c = {1,2,3}
#積集合
print(a & b)
print(a.intersection(b))
#和集合
print(a | b)
print(a.union(b))
#差集合
print(a - b)
print(a.difference(b))
#排他的OR
print(a ^ b)
print(a.symmetric_difference(b))
#部分集合
print(a <= b)
print(a.issubset(b))
print(a <= a)
print(a.issubset(a))
print(a < c)
print(c.issuperset(a))
