import pandas as pd
#CSVファイルからDataFrameを作成する
df1 = pd.read_csv('data/concat_1.csv')
df2 = pd.read_csv('data/concat_2.csv')
df3 = pd.read_csv('data/concat_3.csv')
print(df1)
print(df2)
print(df3)
#縦に結合する(インデックスを保存)
row_concat = pd.concat([df1, df2, df3])
print(row_concat)
#縦に結合する(インデックスを振りなおす)
row_concat_reset = pd.concat([df1, df2, df3], ignore_index=True)
print(row_concat_reset)
