import sqlalchemy
from sqlalchemy import orm

from web.database.db_session import SqlAlchemyBase


class Bucket(SqlAlchemyBase):
    __tablename__ = 'bucket'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    user_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("users.id"))
    product_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("product.id"))
    count = sqlalchemy.Column(sqlalchemy.Integer, default=1)

    user = orm.relationship('User', backref="bucket")
    product = orm.relationship('Product', backref="bucket")
