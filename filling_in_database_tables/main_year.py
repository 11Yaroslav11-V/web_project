# программа для первоначального заполнения в БД таблицы годов


from data.years import Year
from flask import Flask
from data import db_session


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("../db/games.db")
    session = db_session.create_session()

    years = Year()
    years.name_year = '2010'
    session.add(years)
    session.commit()

    years = Year()
    years.name_year = '2011'
    session.add(years)
    session.commit()

    years = Year()
    years.name_year = '2012'
    session.add(years)
    session.commit()

    years = Year()
    years.name_year = '2013'
    session.add(years)
    session.commit()

    years = Year()
    years.name_year = '2014'
    session.add(years)
    session.commit()

    years = Year()
    years.name_year = '2015'
    session.add(years)
    session.commit()

    years = Year()
    years.name_year = '2016'
    session.add(years)
    session.commit()

    years = Year()
    years.name_year = '2017'
    session.add(years)
    session.commit()

    years = Year()
    years.name_year = '2018'
    session.add(years)
    session.commit()

    years = Year()
    years.name_year = '2019'
    session.add(years)
    session.commit()

    years = Year()
    years.name_year = '2020'
    session.add(years)
    session.commit()

    years = Year()
    years.name_year = '2021'
    session.add(years)
    session.commit()

    years = Year()
    years.name_year = '2022'
    session.add(years)
    session.commit()


if __name__ == '__main__':
    main()
