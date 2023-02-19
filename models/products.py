from .recipes import recipes
import sqlalchemy

metadata = sqlalchemy.MetaData()

recipes_and_product = sqlalchemy.Table('recipes_and_product', metadata,
                                       sqlalchemy.Column('recipes_id', sqlalchemy.Integer(),
                                                         sqlalchemy.ForeignKey(recipes.c.id)),
                                       sqlalchemy.Column('products_id', sqlalchemy.Integer(),
                                                         sqlalchemy.ForeignKey('product.id'))
                                       )

product = sqlalchemy.Table('product', metadata,
                           sqlalchemy.Column('id', sqlalchemy.Integer(), primary_key=True),
                           sqlalchemy.Column('name', sqlalchemy.String(100)),
                           sqlalchemy.Column('recipes_id', sqlalchemy.Integer(), sqlalchemy.ForeignKey(recipes.c.id)),
                           )
