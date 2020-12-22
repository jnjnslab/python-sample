import pandas as pd
#関数を定義する
def my_sq(x):
    return x ** 2

def my_row(row):
    return row.mean()

#DataFrameの作成
df=pd.DataFrame({'a':[10,20,30],
                 'b':[20,30,40]})
print(df)

#列ごとに関数を適用する
ap1 = df.apply(my_sq, axis=0)
print(ap1)

#行ごとに関数を適用する
ap2 = df.apply(my_row, axis=1)
print(ap2)


