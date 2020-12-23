# 対応のない2群のt検定

# 数値計算に使うライブラリ
import numpy as np
import pandas as pd
import scipy as sp
from scipy import stats
# データの読み込み
paired_test_data = pd.read_csv("data/3-9-1-paired-t-test.csv")
print(paired_test_data)
# 薬を飲む前と飲んだ後の標本に分ける
before = paired_test_data.query('medicine == "before"')["body_temperature"]
after = paired_test_data.query('medicine == "after"')["body_temperature"]
# np.arrayに変換
before = np.array(before)
after = np.array(after)
# 平均値
mean_bef = np.mean(before)
mean_aft = np.mean(after)
# 分散
sigma_bef = np.var(before, ddof = 1)
sigma_aft = np.var(after, ddof = 1)
# サンプルサイズ
m = len(before)
n = len(after)
# t値
t_value = (mean_aft - mean_bef) / np.lib.scimath.sqrt((sigma_bef/m + sigma_aft/n))
print(t_value)
# 関数で計算した場合(等分散を仮定しない)
print(stats.ttest_ind(after, before, equal_var = False))