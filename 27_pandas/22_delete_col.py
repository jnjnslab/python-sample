import pandas as pd
#CSVファイルからDataFrameを作成する
scientists = pd.read_csv('data/scientists.csv')
print(scientists)
#列を削除する
scientists = scientists.drop(['Born', 'Died'], axis=1)
print(scientists)
