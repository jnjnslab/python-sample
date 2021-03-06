import pandas as pd
import numpy as np
import csv
#Excelファイルを読み込み、データフレームとする
df = pd.read_excel("data/ordersList.xlsx", sheet_name="Sheet")
#品名と得意先名で金額をクロス集計する
#index:縦軸
#columns:横軸
#values:集計する項目
#fill_value=0 : 項目が存在しない部分は0とする
#margins=True : 縦横の合計を追加する
#aggfunc:集計方法
#np.mean 平均 np.sum 合計 np.max 最大 np.min 最小
outdata=df.pivot_table(index="品名",columns="得意先名", values="金額", fill_value=0, margins=True , aggfunc=np.sum)
#データフレームをExcelとして出力する
outdata.to_excel("output/out.xlsx", sheet_name = "pivot")
