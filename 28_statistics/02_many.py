# 数値計算に使うライブラリ
import pandas as pd
import numpy as np
import scipy as sp

#データ
cov_data = pd.read_csv("data/3-2-3-cov.csv")
print(cov_data)
# データの取り出し
x = cov_data["x"]
y = cov_data["y"]
# 標本共分散行列
print(np.cov(x, y, ddof = 0))
# 不偏共分散行列
print(np.cov(x, y, ddof = 1))
# 相関行列
print(np.corrcoef(x, y))

