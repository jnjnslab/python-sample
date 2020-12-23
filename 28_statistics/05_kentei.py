# 対応のある2群のt検定

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
# 差を計算
diff = after - before
print(diff)
# 平均値が0と異なるか検定
# 帰無仮説　平均が0
# 対立仮設　平均が0でない
print(stats.ttest_1samp(diff, 0))
# 関数で計算した場合
print(stats.ttest_rel(after, before))

