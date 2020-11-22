#ライブラリのインポート
import pymongo

#サーバに接続する
uri = ""
client = pymongo.MongoClient(uri)
#db(sample_mflix)を取得する
mflix = client.sample_mflix
#collection(movies)を取得する
movies = mflix.movies

#条件を指定してを1件読み込む
result = movies.find_one( { "cast": "Salma Hayek" } )

#print(result)
print(result['cast'])

client.close()