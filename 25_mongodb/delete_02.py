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

#Falseの件数
print(len(list(deletes.find({'random_bool': False}))))
#Trueの件数
print(len(list(deletes.find({'random_bool': True}))))

#Falseを削除する
dr = deletes.delete_many({'random_bool': False})
print(dr.deleted_count)

#残件数
print(len(list(deletes.find({}))))

client.close()