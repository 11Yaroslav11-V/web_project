import sqlalchemy
from sqlalchemy import orm
from data.db_session import SqlAlchemyBase


class Genres(SqlAlchemyBase):
    __tablename__ = 'genres'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name_genre = sqlalchemy.Column(sqlalchemy.String, nullable=True)

    games = orm.relation("Game", back_populates='genres')

    def __repr__(self):
        return f'{self.genre}'
