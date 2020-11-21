import os

path1 = os.path.abspath('.')
path2 = os.path.join(path1,'chdir.py')
#存在するか
print(os.path.exists(path2))
#ディレクトリか判定する
print(os.path.isdir(path1))
print(os.path.isdir(path2))
#ファイルが判定する
print(os.path.isfile(path1))
print(os.path.isfile(path2))
