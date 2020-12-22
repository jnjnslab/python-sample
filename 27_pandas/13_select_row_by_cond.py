import pandas as pd
#CSVファイルからDataFrameを作成する
scientists = pd.read_csv('data/scientists.csv')
#条件で行で抽出する
row1 = scientists[scientists['Age'] > scientists['Age'].mean()]
print(row1)