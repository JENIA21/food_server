from sqlalchemy import Integer, String, Column, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import sqlalchemy

Base = declarative_base()

recipes_and_product = sqlalchemy.Table('recipes_and_product', Base.metadata,
                                       Column('recipes_id', Integer(), ForeignKey("recipes.id")),
                                       Column('products_id', Integer(), ForeignKey("products.id"))
                                       )


class Products(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String(10000), nullable=False)
    recipes_id = Column(Integer, ForeignKey('recipes.id'))
    recipes = relationship("Recipes", secondary=recipes_and_product, backref="products")
