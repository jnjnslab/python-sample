#ライブラリのインポート
from pymongo import MongoClient
import random

#サーバに接続する
uri = ""
client = MongoClient(uri)
#db(lessons)を取得する
lessons = client.lessons
#collection(deletes)を取得する
deletes = lessons.deletes

#collection(deletes)を削除する
deletes.drop()
#テストデータを作成する
random.seed(42)
imr = deletes.insert_many([{'_id': val, 'random_bool': random.choice([True, False])} for val in range(100)])
print(len(imr.inserted_ids))
#先頭の3件を表示する
print(list(deletes.find().limit(3)))

#1件削除する
dr = deletes.delete_one({'random_bool': True})
print(dr.deleted_count)

#_id:99を削除する
print(deletes.find_one({'_id': 99}))
dr2 = deletes.delete_one({'_id': 99})
print(dr2.deleted_count)
print(deletes.find_one({'_id': 99}))

client.close()