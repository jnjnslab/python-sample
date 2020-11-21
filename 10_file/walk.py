import os
#ディレクトリツリーを渡り歩く
for foldername,subfolders,filenames in os.walk('.'):
    print('The current folder is ' + foldername)
    for subfolder in subfolders:
        print('subfolder:' + subfolder)
    for filename in filenames:
        print('file:' + filename)