# 統計的仮説検定
# 帰無仮説　平均は50
# 対立仮設　平均は50と異なる

# 数値計算に使うライブラリ
import numpy as np
import pandas as pd
import scipy as sp
from scipy import stats
# データの読み込み
junk_food = pd.read_csv("data/3-8-1-junk-food-weight.csv")["weight"]
print(junk_food.head())
# t値の計算
mu = np.mean(junk_food)  # 標本平均
df = len(junk_food) - 1  # 自由度
sigma = np.std(junk_food, ddof = 1)
se = sigma / np.lib.scimath.sqrt(len(junk_food))  # 標準誤差
t_value = (mu - 50) / se  # t値
print(t_value)
# p値の計算
alpha = stats.t.cdf(t_value, df = df)
print((1 - alpha) * 2)
# 関数によるp値の計算
print(stats.ttest_1samp(junk_food, 50))

#シミュレーション
# 標本の情報
size = len(junk_food)
sigma = np.std(junk_food, ddof = 1)
# t値を格納する変数
t_value_array = np.zeros(50000)
# 母平均が50(帰無仮説が正しい)と仮定してt値を計算することを50000回繰り返す
np.random.seed(1)
norm_dist = stats.norm(loc = 50, scale = sigma)
for i in range(0, 50000):
    sample = norm_dist.rvs(size = size)
    sample_mean = np.mean(sample)
    sample_std = np.std(sample, ddof = 1)
    sample_se = sample_std / np.lib.scimath.sqrt(size)
    t_value_array[i] = (sample_mean - 50) / sample_se
# シミュレーションによるp値
print((sum(t_value_array > t_value) / 50000) * 2)
