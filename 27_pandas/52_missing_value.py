import pandas as pd
#インポート
ebola = pd.read_csv('data/country_timeseries.csv')
#欠損値を置き換える
print(ebola.fillna(0).iloc[:10, :5])
#欠損値を前方の値で置き換える
print(ebola.fillna(method='ffill').iloc[:10, :5])
#欠損値を後方の値で置き換える
print(ebola.fillna(method='bfill').iloc[:10, :5])
#欠損値を補間する
#https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.interpolate.html
print(ebola.interpolate(method='linear').iloc[:10, :5])


