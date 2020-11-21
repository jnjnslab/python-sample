#ファイルをオープンする
f = open('hello.txt', 'r', encoding='UTF-8')
#1行ごとのリストとして読み込む
datalist = f.readlines()
for data in datalist:
    print(data,end='')
#ファイルをクローズする
f.close()