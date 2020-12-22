import pandas as pd
import numpy as np
import csv
#インポート
df = pd.read_csv("data/room.csv",encoding="cp932",header = 0)
#先頭の10件を出力する
print('先頭の10件')
print(df.head(10))
#条件で抽出する
print(df.query('家賃 < 70000'))

print(df.query('70000 <= 家賃 <= 80000'))

print(df.query("間取り == '1K'"))

print(df.query("間取り in ['1LDK','2LDK']"))
