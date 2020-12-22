import pandas as pd
#CSVファイルからDataFrameを作成する
df1 = pd.read_csv('data/concat_1.csv')
df2 = pd.read_csv('data/concat_2.csv')
df3 = pd.read_csv('data/concat_3.csv')
print(df1)
print(df2)
print(df3)
#横に結合する
col_concat_ignore = pd.concat([df1, df2, df3], axis=1, ignore_index=True)
print(col_concat_ignore)
