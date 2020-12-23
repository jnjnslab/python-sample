# カイ２乗検定

# 数値計算に使うライブラリ
import numpy as np
import pandas as pd
import scipy as sp
from scipy import stats
# データの読み込み
click_data = pd.read_csv("data/3-10-1-click_data.csv")
print(click_data)
# 分割表形式に変換
cross = pd.pivot_table(
    data = click_data,
    values = "freq",
    aggfunc = "sum",
    index = "color",
    columns = "click"
)
print(cross)
# 検定の実行
# カイ2乗検定量、p値、自由度、期待度数
print(sp.stats.chi2_contingency(cross, correction = False))
