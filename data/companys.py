import sqlalchemy
from sqlalchemy import orm
from data.db_session import SqlAlchemyBase


class Company(SqlAlchemyBase):
    __tablename__ = 'companys'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name_company = sqlalchemy.Column(sqlalchemy.String, nullable=True)

    games = orm.relation("Game", back_populates='company')

    def __repr__(self):
        return f'{self.id} {self.name_company}'
