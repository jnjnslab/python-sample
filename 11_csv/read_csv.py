import csv
#CSVファイルを入力用に開く。文字コードはutf_8_sigとする。
fp = open('data/out.csv', 'r',encoding="utf_8_sig") 
#CSVファイルのreaderを取得する。
reader = csv.reader(fp)
#読み込んだ結果の各行の処理を行う
for row in reader:
    #行内の各項目の処理を行う
    for col in row:
        #,を付けて出力する
        print(col, end=',')
    #改行する
    print()
#CSVファイルを閉じる
fp.close()