# программа для первоначального заполнения в БД таблицы жанров


from data.genre import Genres
from flask import Flask
from data import db_session


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("../db/games.db")
    session = db_session.create_session()

    genre = Genres()
    genre.name_genre = 'Шутеры'
    session.add(genre)
    session.commit()

    genre = Genres()
    genre.name_genre = 'Файтинги'
    session.add(genre)
    session.commit()

    genre = Genres()
    genre.name_genre = 'Выживание'
    session.add(genre)
    session.commit()

    genre = Genres()
    genre.name_genre = 'Хоррор'
    session.add(genre)
    session.commit()

    genre = Genres()
    genre.name_genre = 'Аркады'
    session.add(genre)
    session.commit()

    genre = Genres()
    genre.name_genre = 'MMORPG'
    session.add(genre)
    session.commit()

    genre = Genres()
    genre.name_genre = 'Песочницы'
    session.add(genre)
    session.commit()

    genre = Genres()
    genre.name_genre = 'Симуляторы'
    session.add(genre)
    session.commit()

    genre = Genres()
    genre.name_genre = 'Стратегии'
    session.add(genre)
    session.commit()


if __name__ == '__main__':
    main()
