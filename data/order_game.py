import datetime
import sqlalchemy
from flask_login import UserMixin, current_user
from sqlalchemy_serializer import SerializerMixin

from .db_session import SqlAlchemyBase


class Order(SqlAlchemyBase, UserMixin, SerializerMixin):
    __tablename__ = 'order_game'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    company = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    game_name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    status = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    created_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now)
