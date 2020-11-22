#ライブラリのインポート
import pymongo
from bson.json_util import dumps
from faker import Faker
import random

#ダミーユーザー作成関数
def make_user(iter_count):
    account_type = "premium" if iter_count % 2 == 0 else "standard"
    return {
        "name": fake.name(),
        "address": fake.address(),
        "email": fake.email(),
        "age": random.randrange(18, 65),
        "favorite_colors": [fake.color_name(), fake.color_name(), fake.color_name()],
        "account_type": account_type
    }

Faker.seed(42)
fake = Faker()
random.seed(42)

#サーバに接続する
uri = ""
client = pymongo.MongoClient(uri)
#db(sample_mflix)を取得する
mflix = client.sample_mflix
#collection(fake_users)を取得する
fake_users = mflix.fake_users
#collection(fake_users)を削除する
fake_users.drop()
#ダミーユーザーを作成する
to_insert = [make_user(i) for i in range(10)]
#ダミーユーザーを追加する
fake_users.insert_many(to_insert)
#先頭の1件を取得する
doc = fake_users.find_one()
print(doc['name'])
print(doc['age'])
print(doc['favorite_colors'])
#インクリメント
user1 = {"name": doc['name']}
fake_users.update_one(user1, { "$inc": { "age": 1 }})
print(dumps(fake_users.find_one(user1), indent=2))

#リストへの追加
fake_users.update_one(user1, {"$push": { "favorite_colors": "Black"}})
print(dumps(fake_users.find_one(user1), indent=2))

#"account_type": "standard"の件数
print(fake_users.count_documents({"account_type": "standard"}))
print(dumps(fake_users.find({"account_type": "standard"}, { "_id": 0, "name": 1, "account_type": 1}), indent=2))
#項目の更新と新規項目の追加
u_r = fake_users.update_many({"account_type": "standard"}, {"$set": { "account_type": "premium", "free_trial": True}})
#更新結果の表示
print(fake_users.count_documents({"account_type": "standard"}))
print(dumps(fake_users.find({"free_trial": True}, { "_id": 0, "name": 1, "account_type": 1}), indent=2))
print(dir(u_r))
print(u_r.acknowledged, u_r.matched_count, u_r.modified_count, u_r.upserted_id)

#upsert
new_or_updated_user = make_user(0)
u_r = fake_users.update_one({"email": new_or_updated_user["email"]}, {"$set": new_or_updated_user}, upsert=True)
print(dumps(fake_users.find_one({"email": new_or_updated_user["email"]}), indent=2))
print(u_r.acknowledged, u_r.matched_count, u_r.modified_count, u_r.upserted_id)

fake_users.drop()

client.close()