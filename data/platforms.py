import sqlalchemy
from sqlalchemy import orm
from data.db_session import SqlAlchemyBase


class Platform(SqlAlchemyBase):
    __tablename__ = 'platforms'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name_platform = sqlalchemy.Column(sqlalchemy.String, nullable=True)

    games = orm.relation("Game", back_populates='platform')

    def __repr__(self):
        return f'{self.id} {self.platform}'
