import sqlalchemy

from web.database.db_session import SqlAlchemyBase


class Product(SqlAlchemyBase):
    __tablename__ = 'product'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.Text)
    price = sqlalchemy.Column(sqlalchemy.Integer)
    category = sqlalchemy.Column(sqlalchemy.Text)
    namefile = sqlalchemy.Column(sqlalchemy.Text)
    new = sqlalchemy.Column(sqlalchemy.Boolean)
    sale = sqlalchemy.Column(sqlalchemy.Integer)
    hit = sqlalchemy.Column(sqlalchemy.Boolean)
