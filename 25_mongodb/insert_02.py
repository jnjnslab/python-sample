#ライブラリのインポート
import pymongo

#サーバに接続する
uri = ""
client = pymongo.MongoClient(uri)
#db(electronicsDB)を取得する
db = client.electronicsDB
#collection(video_games)を取得する
vg = db.video_games

fortnite_doc = {"title": "Fortnite2", "year": 2019}
#検索条件に該当しない場合に追加する、存在する場合は更新する
upsert_result = vg.update_one( { "title": "Fortnite2" } , { "$set": fortnite_doc }, upsert=True )
#結果を表示する
print(upsert_result.raw_result)

#全件読み込む
cursor = vg.find({})
for doc in cursor:
    print(doc)

client.close()