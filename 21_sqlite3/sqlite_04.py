# sqlite3 標準モジュールをインポート
import sqlite3
 # データベースファイルのパス
dbpath = 'sample.db'
# データベース接続とカーソル生成
connection = sqlite3.connect(dbpath)
# 自動コミットにする場合は下記を指定（コメントアウトを解除のこと）
# connection.isolation_level = None
cursor = connection.cursor()
 
# DELETE
cursor.execute('DELETE FROM sample WHERE id > 3')
connection.commit()

# fetchall()
cursor.execute('SELECT * FROM sample ORDER BY id ASC')
for row in cursor.fetchall():
    print(row)
 
# 接続を閉じる
connection.close()
