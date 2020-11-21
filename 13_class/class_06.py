#特殊なメソッド(__eq__)
class Word():
    def __init__(self, text):
        self.text = text
    #==演算子の働きを実装する
    def __eq__(self, word2):
        return self.text.lower() == word2.text.lower()

first = Word('ha')
second = Word('HA')

print(first == second)
