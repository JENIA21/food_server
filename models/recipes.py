import sqlalchemy

metadata = sqlalchemy.MetaData()

recipes = sqlalchemy.Table('recipes', metadata,
                           sqlalchemy.Column('id', sqlalchemy.Integer(), primary_key=True),
                           sqlalchemy.Column('name', sqlalchemy.String(100)),
                           sqlalchemy.Column('description', sqlalchemy.Text(), ),
                           sqlalchemy.Column('time', sqlalchemy.Integer()),
                           )
