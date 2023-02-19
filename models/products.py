from sqlalchemy import Integer, String, Column, ForeignKey
from .recipes import recipes
import sqlalchemy

metadata = sqlalchemy.MetaData()

recipes_and_product = sqlalchemy.Table('recipes_and_product', metadata,
                                       Column('recipes_id', Integer(), ForeignKey(recipes.c.id)),
                                       Column('products_id', Integer(), ForeignKey('product.id'))
                                       )

product = sqlalchemy.Table('product', metadata,
                           Column('id', Integer(), primary_key=True),
                           Column('name', String(100), ForeignKey('product.id')),
                           Column('recipes_id', Integer(), ForeignKey(recipes.c.id)),
                           )
