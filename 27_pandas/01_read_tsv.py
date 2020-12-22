import pandas as pd
#TSVファイルからDataFrameを作成する
df = pd.read_csv('data/gapminder.tsv', sep='\t')
#先頭の5件を表示する
print(df.head())
#行と列の数を表示する
print(df.shape)
#列の名前を表示する
print(df.columns)
#各列のdtypeを表示する
print(df.dtypes)
#詳しい情報を表示する
print(df.info())
