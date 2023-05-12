import sqlalchemy

from web.database.db_session import SqlAlchemyBase


class User(SqlAlchemyBase):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    email = sqlalchemy.Column(sqlalchemy.Text)
    password = sqlalchemy.Column(sqlalchemy.Text)
    admin = sqlalchemy.Column(sqlalchemy.Boolean)
