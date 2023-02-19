import sqlalchemy
from sqlalchemy import Integer, String, Column

metadata = sqlalchemy.MetaData()

recipes = sqlalchemy.Table('recipes', metadata,
                           Column('id', Integer(), primary_key=True),
                           Column('description', String(10000), ),
                           Column('time', Integer()),
                           )
