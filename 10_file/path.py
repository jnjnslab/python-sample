import os
#絶対パスの取得
path1 = os.path.abspath('.')
print(path1)
#絶対パスか判定する
print(os.path.isabs(path1))
#print(os.path.relpath('.','e:/work'))
#パスの連結
path2 = os.path.join(path1,'chdir.py')
print(path2)
#パスの分解
print(os.path.dirname(path2))
print(os.path.basename(path2))
print(os.path.split(path2))
print(path2.split(os.sep))
