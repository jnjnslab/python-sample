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

#テーブルを削除する
session = sessionmaker(bind=engine)()

orange = session.query(Fruit).filter_by(id=4).one()
session.delete(orange)
session.commit()

session.close()