#setdefaultメソッド
# キーが辞書に存在しない場合のみ登録する
spam = {'name':'Pooka','age':5}
print(spam)
spam.setdefault('color','black')
print(spam)
spam.setdefault('color','white')
print(spam)