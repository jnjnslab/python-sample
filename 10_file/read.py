#ファイルをオープンする
f = open('hello.txt', 'r', encoding='UTF-8')
#ファイル全体を読み込む
data = f.read()
print(data)
#ファイルをクローズする
f.close()