import pandas as pd
#インポート
scientists = pd.read_csv('data/scientists.csv')
print(scientists)
#エクスポート
scientists.to_csv('output/scientists_new.csv', index=False)