import pandas as pd
#インポート
billboard = pd.read_csv('data/billboard.csv')
print(billboard)
#横持ちを縦持ちにする
billboard_long = pd.melt(
    billboard,
    id_vars=['year', 'artist', 'track', 'time', 'date.entered'],
    var_name='week',
    value_name='rating'
)
print(billboard_long.head())