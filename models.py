from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,Text,Boolean
from sqlalchemy.orm import sessionmaker,scoped_session


engine = create_engine('sqlite:///app.db',echo=True)
Base = declarative_base()

class English(Base):
    __tablename__ = 'english'
    id = Column(Integer,primary_key=True)
    english_sentence = Column(Text)
    japanese_sentence = Column(Text)
    master_check = Column(Boolean)

Base.metadata.create_all(bind=engine)
session = scoped_session(sessionmaker(engine))

