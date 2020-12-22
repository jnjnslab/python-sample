import pandas as pd
#TSVファイルからDataFrameを作成する
df = pd.read_csv('data/gapminder.tsv', sep='\t')
#列で抽出する
subset = df[['country', 'continent', 'year']]
print(subset.head())