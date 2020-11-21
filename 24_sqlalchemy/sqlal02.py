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

#テーブルに追加する
session = sessionmaker(bind=engine)()
apple = Fruit()
apple.id = 3
apple.name = 'apple'
session.add(instance=apple)

session.add_all(instances=[
    Fruit(id=4, name='orange'),
    Fruit(id=5, name='melon'),
])

session.commit()
#session.rollback()

session.close()