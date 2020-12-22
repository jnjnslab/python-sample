import pandas as pd
import numpy as np

nrows, ncols = 100000, 100
rng = np.random.RandomState(42)
df1, df2, df3, df4 = (pd.DataFrame(rng.rand(nrows, ncols)) for i in range(4))

df5 = pd.eval('df1 + df2 + df3 + df4')

df = pd.DataFrame(rng.rand(1000, 3), columns=['A', 'B', 'C'])
print(df.head())
result = df.eval('(A + B) / (C - 1)')
print(result.head())