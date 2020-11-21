#クラスの定義
class SampleClass:
    #コンストラクター
    def __init__(self,p1,p2):
        #インスタンス変数の設定
        self.p1 = p1
        self.p2 = p2
    #メソッドの定義
    def getP1(self):
        return self.p1
    def setP1(self,p1):
        self.p1 = p1
    
    def getP2(self):
        return self.p2
    def setP2(self,p2):
        self.p2 = p2

#インスタンスの生成
h = SampleClass("ABC","123")
#メソッドの呼び出し
print(h.getP1())
print(h.getP2())
h.setP1("DEF")
h.setP2(456)
print(h.getP1())
print(h.getP2())
