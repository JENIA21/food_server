from sqlalchemy import Integer, String, Column
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Recipes(Base):
    __tablename__ = 'recipes'
    id = Column(Integer, primary_key=True)
    description = Column(String(10000), nullable=False)
    time = Column(Integer, nullable=False)
