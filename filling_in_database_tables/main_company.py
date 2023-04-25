# программа для первоначального заполнения в БД таблицы компаний


from data.companys import Company
from flask import Flask
from data import db_session


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("../db/games.db")
    session = db_session.create_session()

    company = Company()
    company.name_company = 'Epic Games'
    session.add(company)
    session.commit()

    company = Company()
    company.name_company = 'Ubisoft'
    session.add(company)
    session.commit()

    company = Company()
    company.name_company = 'Valve'
    session.add(company)
    session.commit()

    company = Company()
    company.name_company = 'Electronic Arts'
    session.add(company)
    session.commit()

    company = Company()
    company.name_company = 'Lesta Games'
    session.add(company)
    session.commit()

    company = Company()
    company.name_company = 'Riot Games'
    session.add(company)
    session.commit()

    company = Company()
    company.name_company = 'Rockstar Games'
    session.add(company)
    session.commit()

    company = Company()
    company.name_company = 'Mojang Studios'
    session.add(company)
    session.commit()

    company = Company()
    company.name_company = '4A STUDIO'
    session.add(company)
    session.commit()


if __name__ == '__main__':
    main()
