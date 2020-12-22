import pandas as pd
import numpy as np
#インポート
df = pd.read_csv('data/gapminder.tsv', sep='\t')
print(df.head())
#ユーザー変数
def my_zscore(x):
    return ((x - x.mean()) / x.std())
#データを変換する
print(df.groupby('year').lifeExp.transform(my_zscore))
