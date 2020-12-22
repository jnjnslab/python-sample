import pandas as pd
import numpy as np
import csv
#インポート
df = pd.read_csv("data/room.csv",encoding="cp932",header = 0)
#指定した列の値によるソート
#df2=df.sort_values(by="家賃",ascending=True,inplace=False)    #昇順
df2=df.sort_values(by="家賃",ascending=False,inplace=False)   #降順
#df2=df.sort_values(by=["間取り","家賃"],ascending=[True,False],inplace=False)
print(df2)