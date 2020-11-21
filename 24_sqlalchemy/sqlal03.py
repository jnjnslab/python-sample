import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

engine = sqlalchemy.create_engine('sqlite:///sample.sqlite3', echo=True)

#モデル定義する
Base = declarative_base()
class Fruit(Base):
    id = Column(Integer, primary_key=True)
    name = Column(String(length=255))

    __tablename__ = 'fruit'

#テーブルを読み込む
session = sessionmaker(bind=engine)()
#全件
print('全件')
query_result = session.query(Fruit).all()
for fruit in query_result:
    print(fruit.id, fruit.name)
#抽出条件の指定
print('抽出条件の指定 name==apple')
apples = session.query(Fruit).filter(Fruit.name=='apple')
for apple in apples:
    print(apple.id, apple.name)
print('抽出条件の指定 id>=4')
query_result2 = session.query(Fruit).filter(Fruit.id >= 4)
for fruit in query_result2:
    print(fruit.id, fruit.name)
#1件取得する
print('1件取得する')
apple = session.query(Fruit).filter(Fruit.name=='apple').one()
print(apple.id, apple.name)
#件数を指定する
print('limit(2)')
query_result3 = session.query(Fruit).limit(2)
for fruit in query_result3:
    print(fruit.id, fruit.name)
#降順
print('降順')
query_result4 = session.query(Fruit).order_by(Fruit.id.desc())
for fruit in query_result4:
    print(fruit.id, fruit.name)

session.close()