import pandas as pd
#インポート
pew = pd.read_csv('data/pew.csv')
print(pew.head())
#横持ちを縦持ちにする
pew_long = pd.melt(pew, id_vars='religion')
print(pew_long.head())
#展開した列に名前を付ける
pew_long2 = pd.melt(pew, id_vars='religion', var_name='income', value_name='count')
print(pew_long2.head())
