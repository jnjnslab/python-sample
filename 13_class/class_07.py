#is演算子  同一のオブジェクトか識別する
class Person:
    def __init__(self,name):
        self.name = name

bob = Person('Bob')
same_bob = bob
print(bob is same_bob)

tom = Person('Tom')
print(bob is tom)