import pandas as pd
import numpy as np
#インポート
df = pd.read_csv('data/gapminder.tsv', sep='\t')
print(df.head())
#キー単位に集約する(平均)
print(df.groupby('year')['lifeExp'].mean())
#キー単位に集約する(合計)
print(df.groupby(['year', 'continent'])['lifeExp'].agg(np.sum))
#ユーザー変数
def my_mean(values):
    n = len(values)
    sum = 0
    for value in values:
        sum += value
    return (sum / n)

print(df.groupby('year')['lifeExp'].agg(my_mean))
