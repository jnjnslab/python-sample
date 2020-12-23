# 数値計算に使うライブラリ
import numpy as np
import pandas as pd
import scipy as sp
from scipy import stats

# グラフを描画するライブラリ
from matplotlib import pyplot as plt
import seaborn as sns
sns.set()
# データの読み込み
fish = pd.read_csv("data/3-7-1-fish_length.csv")["length"]
print(fish)
# 母平均の点推定
mu = np.mean(fish)
print(mu)
# 母分散の点推定
sigma_2 = np.var(fish, ddof = 1)
print(sigma_2)
# 区間推定
# 自由度
df = len(fish) - 1
print(df)
# 標準誤差
sigma = np.std(fish, ddof = 1)
se = sigma / np.lib.scimath.sqrt(len(fish))
print(se)
# 区間推定(95%信頼区間)
interval = stats.t.interval(alpha = 0.95, df = df, loc = mu, scale = se)
print(interval)

# シミュレーション
be_included_array = np.zeros(20000, dtype = "bool")
# 「データを10個選んで95%信頼区間を求める」試行を20000回繰り返す
# 信頼区間が母平均(4)を含んでいればTrue
np.random.seed(1)
norm_dist = stats.norm(loc = 4, scale = 0.8)
for i in range(0, 20000):
    sample = norm_dist.rvs(size = 10)
    df = len(sample) - 1
    mu = np.mean(sample)
    std = np.std(sample, ddof = 1)
    se = std / np.lib.scimath.sqrt(len(sample))
    interval = stats.t.interval(0.95, df, mu, se)
    if(interval[0] <= 4 and interval[1] >= 4):
        be_included_array[i] = True
print(sum(be_included_array) / len(be_included_array))
