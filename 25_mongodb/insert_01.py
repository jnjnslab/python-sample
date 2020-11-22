#ライブラリのインポート
import pymongo

#サーバに接続する
uri = ""
client = pymongo.MongoClient(uri)
#db(electronicsDB)を取得する
db = client.electronicsDB
#electronicsDB無いのcollectionの一覧を取得する
print(db.list_collection_names())
#collection(video_games)を取得する
vg = db.video_games

#documentを1件追加する
insert_result = vg.insert_one({"title": "Fortnite", "year": 2018})
#追加が成功したか確認する
print(insert_result.acknowledged)
#追加したdocumentの"_id"を取得する
print(insert_result.inserted_id)
#追加したdocumentを読み込む
doc = vg.find_one( { "_id": insert_result.inserted_id } )
print(doc)

client.close()