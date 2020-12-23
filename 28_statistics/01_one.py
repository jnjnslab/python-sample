# 数値計算に使うライブラリ
import numpy as np
import scipy as sp
from scipy import stats

#1変量データ
fish_data = np.array([2,3,3,4,4,4,4,5,5,6])
# サンプルサイズ
print(len(fish_data))
# 合計
print(np.sum(fish_data))
# 平均値
print(np.mean(fish_data))
# 標本分散
print(np.var(fish_data, ddof = 0))
# 不偏分散
print(np.var(fish_data, ddof = 1))
# 標準偏差
print(np.std(fish_data, ddof = 1))
# 最大
print(np.amax(fish_data))
# 最小
print(np.amin(fish_data))
# 中央値
print(np.median(fish_data))
# 四分位点
fish_data_3 = np.array([1,2,3,4,5,6,7,8,9])
print(stats.scoreatpercentile(fish_data_3, 25))
print(stats.scoreatpercentile(fish_data_3, 50))
print(stats.scoreatpercentile(fish_data_3, 75))