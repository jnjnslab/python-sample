#特殊なメソッド(__add__)
class AlwaysPositive:
    def __init__(self, number):
        self.n = number
    #+演算子の働きを実装する
    def __add__(self, other):
        return abs(self.n + other.n)

x = AlwaysPositive(-20)
y = AlwaysPositive(10)

print(x + y)
