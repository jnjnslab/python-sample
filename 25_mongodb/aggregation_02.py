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

#filter,projectionの例
limited_cursor = movies.find(
    { "directors": "Sam Raimi" },
    { "_id": 0, "title": 1, "cast": 1 } 
).limit(2)
print(dumps(limited_cursor, indent=2))

#aggregationの例
pipeline = [
    { "$match": { "directors": "Sam Raimi" } },
    { "$project": { "_id": 0, "title": 1, "cast": 1 } },
    { "$limit": 2 }
]
limited_aggregation = movies.aggregate( pipeline )
print(dumps(limited_aggregation, indent=2))

client.close()