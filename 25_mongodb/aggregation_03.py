#ライブラリのインポート
import pymongo
from pymongo import DESCENDING, ASCENDING
from bson.json_util import dumps
#サーバに接続する
uri = ""
client = pymongo.MongoClient(uri)
#db(sample_mflix)を取得する
mflix = client.sample_mflix
#collection(movies)を取得する
movies = mflix.movies

#aggregationの例
pipeline = [
    { "$match": { "directors": "Sam Raimi" } },
    { "$project": { "_id": 0, "year": 1, "title": 1, "cast": 1 } },
    { "$sort": { "year": ASCENDING } },
    { "$skip": 10 }
]
sorted_skipped_aggregation = movies.aggregate( pipeline )
for doc in sorted_skipped_aggregation:
    print(doc)

client.close()