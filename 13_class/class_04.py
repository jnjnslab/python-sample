#特殊なメソッド(__repr__)
class Lion:
    def __init__(self, name):
        self.name = name
    #printで出力する内容
    def __repr__(self):
        return self.name

lion = Lion("Dilbert")
print(lion)