#ファイルをオープンする
f = open('bacon.txt', 'w', encoding='UTF-8')
#1行書き込む
f.write('Hello World!\n')
f.write('こんにちは!\n')
#ファイルをクローズする
f.close()
#ファイルをオープンする
f = open('bacon.txt', 'a', encoding='UTF-8')
#1行追加する
f.write('Bacon is not a vegetable.\n')
#ファイルをクローズする
f.close()
#ファイルをオープンする
f = open('bacon.txt', 'r', encoding='UTF-8')
#ファイル全体を読み込む
data = f.read()
print(data,end='')
#ファイルをクローズする
f.close()
