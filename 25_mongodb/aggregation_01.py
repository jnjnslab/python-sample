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

#filterの例
sam_raimi_cursor = movies.find( { "directors": "Sam Raimi" } )
print(len(list(sam_raimi_cursor)))
#aggregationの例
match_stage = {"$match": { "directors": "Sam Raimi" } }
pipeline = [
    match_stage
]
sam_raimi_aggregation = movies.aggregate( pipeline )
print(len(list(sam_raimi_aggregation)))

#filter,projectionの例
sam_raimi_cursor = movies.find(
    { "directors": "Sam Raimi" },
    { "_id": 0, "title": 1, "cast": 1 }
)
print(dumps(sam_raimi_cursor, indent=2))
#aggregationの例
match_stage = { "$match": { "directors": "Sam Raimi" } }
project_stage = { "$project": { "_id": 0, "title": 1, "cast": 1 } }
pipeline = [
    match_stage,
    project_stage
]
sam_raimi_aggregation = movies.aggregate( pipeline )
print(dumps(sam_raimi_aggregation, indent=2))

#aggregationの例
unwind_stage = { "$unwind": "$directors" }
group_stage = {
    "$group": {
        "_id": {
            "director": "$directors"
        },
        "average_rating": { "$avg": "$imdb.rating" }
    }
}
sort_stage = {
    "$sort": { "average_rating": -1 }
}
limit_stage = { "$limit": 10 }
# create pipeline from four different stages
pipeline = [
    unwind_stage,
    group_stage,
    sort_stage,
    limit_stage
]
# aggregate using pipeline
director_ratings = movies.aggregate(pipeline)
# iterate through the resulting cursor
#print(list(director_ratings))
for ag in director_ratings:
    print(ag)

client.close()