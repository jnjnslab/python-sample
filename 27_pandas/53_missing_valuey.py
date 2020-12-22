import pandas as pd
#インポート
ebola = pd.read_csv('data/country_timeseries.csv')
#欠損値のある行を削除する
ebola_dropna = ebola.dropna()
print(ebola_dropna.shape)
