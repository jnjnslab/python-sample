# sqlite3 標準モジュールをインポート
import sqlite3
 # データベースファイルのパス
dbpath = 'sample.db'
# データベース接続とカーソル生成
connection = sqlite3.connect(dbpath)
# 自動コミットにする場合は下記を指定（コメントアウトを解除のこと）
# connection.isolation_level = None
cursor = connection.cursor()

# UPDATE
cursor.execute('UPDATE sample SET name=? WHERE id=1', ('小林',))
cursor.execute('UPDATE sample SET name=? WHERE id=?', ('加藤', 2))
connection.commit()

# fetchall()
cursor.execute('SELECT * FROM sample ORDER BY id ASC')
for row in cursor.fetchall():
    print(row)
 
# 接続を閉じる
connection.close()
