import sqlalchemy
from sqlalchemy import orm
from data.db_session import SqlAlchemyBase


class Year(SqlAlchemyBase):
    __tablename__ = 'years'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name_year = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)

    games = orm.relation("Game", back_populates='year')

    def __repr__(self):
        return f'{self.year}'
