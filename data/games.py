import sqlalchemy
from sqlalchemy import orm

from data.db_session import SqlAlchemyBase


class Game(SqlAlchemyBase):
    __tablename__ = 'games'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    id_year = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("years.id"))
    year = orm.relation('Year')
    game_name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    id_company = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("companys.id"))
    company = orm.relation('Company')
    id_genres = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("genres.id"))
    genres = orm.relation('Genres')
    age_restriction = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    id_platforms = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("platforms.id"))
    platform = orm.relation('Platform')
    link = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    img = sqlalchemy.Column(sqlalchemy.String, nullable=True)

    def __repr__(self):
        return f'{self.id} {self.game_name}'
