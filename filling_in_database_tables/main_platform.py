# программа для первоначального заполнения в БД таблицы платформ на которых можно играть


from data.platforms import Platform
from flask import Flask
from data import db_session


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("../db/games.db")
    session = db_session.create_session()

    platform = Platform()
    platform.name_platform = 'PC'
    session.add(platform)
    session.commit()

    platform = Platform()
    platform.name_platform = 'PS4, PS5'
    session.add(platform)
    session.commit()

    platform = Platform()
    platform.name_platform = 'ANDROID, IOS'
    session.add(platform)
    session.commit()

    platform = Platform()
    platform.name_platform = 'NINTENDO SWITCH'
    session.add(platform)
    session.commit()

    platform = Platform()
    platform.name_platform = 'XBOX'
    session.add(platform)
    session.commit()

    platform = Platform()
    platform.name_platform = 'PC, PS4, PS5, XBOX'
    session.add(platform)
    session.commit()

    platform = Platform()
    platform.name_platform = 'PC, ANDROID, IOS'
    session.add(platform)
    session.commit()

    platform = Platform()
    platform.name_platform = 'PS4, PS5, XBOX'
    session.add(platform)
    session.commit()

    platform = Platform()
    platform.name_platform = 'PS4, PS5, XBOX, PC, ANDROID, IOS'
    session.add(platform)
    session.commit()


if __name__ == '__main__':
    main()
