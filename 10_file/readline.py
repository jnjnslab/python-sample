#ファイルをオープンする
f = open('hello.txt', 'r', encoding='UTF-8')
#1行ずつ読み込む
while True:
    data = f.readline()
    if data == '':
        break
    print (data.rstrip('\n'))
#ファイルをクローズする
f.close()