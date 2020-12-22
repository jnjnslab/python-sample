import pandas as pd
#CSVファイルからDataFrameを作成する
scientists = pd.read_csv('data/scientists.csv')
print(scientists)
#列を追加する
scientists['died_dt'] = pd.to_datetime(scientists['Died'], format='%Y-%m-%d')
print(scientists)
