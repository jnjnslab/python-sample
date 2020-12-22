import pandas as pd
#インポート
ebola = pd.read_csv('data/country_timeseries.csv')
print(ebola.head())
#欠損値の有無を確認する
print(ebola.isnull().any(axis=0))
