import sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = sqlalchemy.orm.declarative_base()

class Students(Base):
    __tablename__ = "students"  # Corrected __tablename__ with double underscores
    id = Column(Integer, primary_key=True)
    name = Column(String(50))  # Specified max length for the String column
    age = Column(Integer)

engine = create_engine("sqlite:///mydbdbd.db")
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
s = Session()
