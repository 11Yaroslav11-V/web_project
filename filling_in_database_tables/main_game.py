from data.games import Game
from flask import Flask
from data import db_session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("../db/games.db")
    session = db_session.create_session()

    game = Game()
    game.id_year = 9
    game.game_name = 'Red Dead Redemption 2'
    game.id_company = 7
    game.id_genres = 1
    game.age_restriction = '18+'
    game.id_platforms = 6
    game.link = 'https://store.steampowered.com/app/1174180/Red_Dead_Redemption_2/'
    game.img = '1.jpg'
    session.add(game)
    session.commit()

    db_session.global_init("db/book.db")
    session = db_session.create_session()
    game = Game()
    game.id_year = 5
    game.game_name = 'Grand Theft Auto V'
    game.id_company = 7
    game.id_genres = 1
    game.age_restriction = '18+'
    game.id_platforms = 6
    game.link = 'https://store.steampowered.com/app/271590/Grand_Theft_Auto_V/'
    game.img = '2.jpg'
    session.add(game)
    session.commit()

    db_session.global_init("db/book.db")
    session = db_session.create_session()
    game = Game()
    game.id_year = 4
    game.game_name = 'Dota 2'
    game.id_company = 3
    game.id_genres = 9
    game.age_restriction = '18+'
    game.id_platforms = 1
    game.link = 'https://store.steampowered.com/app/570/Dota_2/'
    game.img = '3.jpg'
    session.add(game)
    session.commit()

    db_session.global_init("db/book.db")
    session = db_session.create_session()
    game = Game()
    game.id_year = 2
    game.game_name = 'Minecraft'
    game.id_company = 8
    game.id_genres = 7
    game.age_restriction = '12+'
    game.id_platforms = 9
    game.link = 'https://www.minecraft.net/ru-ru/get-minecraft'
    game.img = '4.jpg'
    session.add(game)
    session.commit()

    db_session.global_init("db/book.db")
    session = db_session.create_session()
    game = Game()
    game.id_year = 3
    game.game_name = 'Far Cry 3'
    game.id_company = 2
    game.id_genres = 1
    game.age_restriction = '18+'
    game.id_platforms = 6
    game.link = 'https://store.steampowered.com/app/220240/Far_Cry_3/'
    game.img = '5.jpg'
    session.add(game)
    session.commit()

    db_session.global_init("db/book.db")
    session = db_session.create_session()
    game = Game()
    game.id_year = 3
    game.game_name = 'Counter-Strike: Global Offensive'
    game.id_company = 3
    game.id_genres = 1
    game.age_restriction = '17+'
    game.id_platforms = 6
    game.link = 'https://store.steampowered.com/app/730/CounterStrike_Global_Offensive/'
    game.img = '6.jpg'
    session.add(game)
    session.commit()

    db_session.global_init("db/book.db")
    session = db_session.create_session()
    game = Game()
    game.id_year = 4
    game.game_name = 'BioShock Infinite'
    game.id_company = 2
    game.id_genres = 1
    game.age_restriction = '17+'
    game.id_platforms = 6
    game.link = 'https://store.steampowered.com/app/8870/BioShock_Infinite/'
    game.img = '7.jpg'
    session.add(game)
    session.commit()

    db_session.global_init("db/book.db")
    session = db_session.create_session()
    game = Game()
    game.id_year = 10
    game.game_name = 'METRO EXODUS'
    game.id_company = 9
    game.id_genres = 4
    game.age_restriction = '18+'
    game.id_platforms = 1
    game.link = 'https://store.steampowered.com/app/412020/Metro_Exodus/'
    game.img = '8.jpg'
    session.add(game)
    session.commit()

    db_session.global_init("db/book.db")
    session = db_session.create_session()
    game = Game()
    game.id_year = 10
    game.game_name = "Tom Clancy's The Division 2"
    game.id_company = 2
    game.id_genres = 1
    game.age_restriction = '17+'
    game.id_platforms = 6
    game.link = 'https://store.steampowered.com/app/2221490/Tom_Clancys_The_Division_2/'
    game.img = '9.jpg'
    session.add(game)
    session.commit()

    db_session.global_init("db/book.db")
    session = db_session.create_session()
    game = Game()
    game.id_year = 10
    game.game_name = 'Mortal Kombat 11'
    game.id_company = 7
    game.id_genres = 2
    game.age_restriction = '17+'
    game.id_platforms = 6
    game.link = 'https://store.steampowered.com/app/976310/Mortal_Kombat11/'
    game.img = '10.jpg'
    session.add(game)
    session.commit()


if __name__ == '__main__':
    main()
