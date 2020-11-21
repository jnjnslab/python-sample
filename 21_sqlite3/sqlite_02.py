# sqlite3 標準モジュールをインポート
import sqlite3
 # データベースファイルのパス
dbpath = 'sample.db'
# データベース接続とカーソル生成
connection = sqlite3.connect(dbpath)
# 自動コミットにする場合は下記を指定（コメントアウトを解除のこと）
# connection.isolation_level = None
cursor = connection.cursor()

# SELECT
cursor.execute('SELECT * FROM sample ORDER BY id')
 
# 全件取得は cursor.fetchall()
res = cursor.fetchall()
print(res)
print(len(res)) 
print(cursor.rowcount)  
 
# 1件取得 cursor.fetchone()
# fetchone() メソッド実行のたびにカーソル位置が移動します
cursor.execute('SELECT * FROM sample ORDER BY id')
print(cursor.fetchone())  # (1, '佐藤')
print(cursor.fetchone())  # (2, '鈴木')
print(cursor.fetchone())  # (3, '高橋')
 
# WHERE 句の例
cursor.execute('SELECT * FROM sample WHERE name=?', ('佐藤',))
print(cursor.fetchone())  # (1, '佐藤')
 
# WHERE 句で該当なしの場合
cursor.execute('SELECT * FROM sample WHERE name=?', ('SUZUKI',))
print(cursor.fetchall())  # []
print(cursor.fetchone())  # None
 
# 全件ループ表示方法は「イテレータ」と「fetchall()」の2パターン。いずれも同じ結果が得られます。
# イテレータ
for row in cursor.execute('SELECT * FROM sample ORDER BY id ASC'):
    print(row)
 
# fetchall()
cursor.execute('SELECT * FROM sample ORDER BY id ASC')
for row in cursor.fetchall():
    print(row)
 
# 接続を閉じる
connection.close()