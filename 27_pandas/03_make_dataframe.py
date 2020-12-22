import pandas as pd
#DataFrameを作成する
scientists=pd.DataFrame(
data={'Occupation':['Chemist','Statistician'],
'Born':['1920-07-25', '1876-06-13'],
'Died':['1958-04-16', '1937-10-16'],
'Age':[37,61]},
index=['Rosaline Franklin','William Gosset'],
columns=['Occupation', 'Born','Died','Age'])

print(scientists)
