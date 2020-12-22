import pandas as pd
#TSVファイルからDataFrameを作成する
df = pd.read_csv('data/gapminder.tsv', sep='\t')
#インデックスラベルで抽出する
print(df.loc[99])
#行番号で抽出する
print(df.iloc[99])