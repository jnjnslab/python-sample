#ライブラリのインポート
import pymongo
from bson.json_util import dumps

#サーバに接続する
uri = ""
client = pymongo.MongoClient(uri)
#db(sample_mflix)を取得する
mflix = client.sample_mflix
#collection(movies)を取得する
movies = mflix.movies

#条件を指定してを件数をカウントする
count = movies.count_documents( { "cast": "Salma Hayek" } )
print(count)

#条件を指定してを全件読み込む
cursor = movies.find( { "cast": "Salma Hayek" } )
#print(dumps(cursor, indent=2))
for doc in cursor:
    print(doc['title'])

client.close()