#継承
#親クラスの定義
class Person():
    #コンストラクター
    def __init__(self, name):
        #クラス変数を設定する
        self.name = name
#子クラスの定義
class EmailPerson(Person):
    #コンストラクター
    def __init__(self, name, email):
        #親クラスのコンストラクターを呼ぶ
        super().__init__(name)
        #クラス変数を設定する
        self.email = email

bob = EmailPerson('Bob','bob@example.com')
print(bob.name)
print(bob.email)
