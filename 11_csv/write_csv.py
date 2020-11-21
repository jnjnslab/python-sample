import csv
#CSVファイルを出力用に開く。文字コードはutf_8_sigとする。
fp = open('data/out.csv', 'w',encoding="utf_8_sig") 
#CSVファイルのwriterを取得する。
#quoting=csv.QUOTE_ALL             すべてクォーテーションを付ける
#quoting=csv.QUOTE_NONNUMERIC      数値以外にクォーテーションを付ける
#quoting=csv.QUOTE_NONE            すべてクォーテーションを付けない
#delimiter=                        区切り文字
#lineterminator="\n"               改行コードの指定
writer = csv.writer(fp, quoting=csv.QUOTE_NONE,lineterminator="\n")
#リストからCSVファイルを1行分出力する。
writer.writerow(["青森","apple",120])
writer.writerow(["山形","cherry",50])
writer.writerow(["栃木","strawberry",90])
#CSVファイルを閉じる
fp.close()