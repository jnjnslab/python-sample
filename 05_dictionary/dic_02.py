#全件取得する
spam = {'color':'red','age':42}
#辞書からキーを取得する
for k in spam.keys():
    print(k)
#辞書からバリューを取得する
for v in spam.values():
    print(v)
#辞書からキー、バリューのペアを取得する
for i in spam.items():
    print(i)
for k,v in spam.items():
    print('Key:' + k + ' Value:' + str(v))
#キーをリストに変換する
print(list(spam.keys()))
