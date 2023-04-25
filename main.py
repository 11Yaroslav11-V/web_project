import os
from os import abort

from flask import Flask, render_template, redirect, request, make_response, jsonify
from flask_login import LoginManager, login_user, login_required, logout_user
from data import db_session

from PIL import Image

from data.login_form import LoginForm
from data.register_form import RegisterForm
from data.users import User
from data.games import Game
from data.genre import Genres
from data.companys import Company
from data.order_game import Order
from data.years import Year
from data.platforms import Platform
from data.add_years import AddYearsGameForm
from data.add_platforms import AddPlatformsForm
from data.add_game import AddGameForm
from data.add_order import AddOrderForm
from data.add_genre import AddGenreGameForm
from data.add_company import AddCompanyForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

login_manager = LoginManager()
login_manager.init_app(app)


def main():
    db_session.global_init("db/games.db")
    app.run()


@app.errorhandler(404)
def not_found(_):
    return make_response(jsonify({'error': 'Not found'}), 404)


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


def search_game_all():
    db_sess = db_session.create_session()
    games = db_sess.query(Game).all()
    result = [(gm.img, gm.link, gm.company.name_company, gm.game_name, gm.year.name_year,
               gm.genres.name_genre, gm.platform.name_platform, gm.age_restriction) for gm in games]
    return result


def search_game_genre(name):
    db_sess = db_session.create_session()
    md = db_sess.query(Genres).filter(Genres.name_genre == name).first()
    games = db_sess.query(Game).filter(Game.id_genres == md.id).all()
    return games


@app.route("/sorting_company")
def sorting_author():
    rez = search_game_all()
    rez.sort(key=lambda x: x[2])
    return render_template("game_list.html", rez=rez, title="Отсортированный список игр по компании")


@app.route("/game_genre")
def game_genre():
    db_sess = db_session.create_session()
    games = db_sess.query(Game).all()
    return render_template("game_genre.html", rez=games, title="Список жанров игр")


@app.route("/game_list")
def game_list():
    rez = search_game_all()
    return render_template("game_list.html", rez=rez, title="Список игр")


@app.route("/game_shooters")
def game_shooters():
    return render_template("game_genre.html", rez=search_game_genre('Шутеры'), title="Шутеры")


@app.route("/game_strategi")
def game_strategi():
    return render_template("game_genre.html", rez=search_game_genre("Стратегии"), title="Стратегии")


@app.route("/game_pesok")
def game_pesok():
    return render_template("game_genre.html", rez=search_game_genre("Песочницы"), title="Песочницы")


@app.route("/game_fight")
def game_fight():
    return render_template("game_genre.html", rez=search_game_genre('Файтинги'), title="Файтинги")


@app.route("/game_horror")
def game_horror():
    return render_template("game_genre.html", rez=search_game_genre('Хоррор'), title="Хорорры")


@app.route("/sorting_game_name")
def sorting_book_name():
    rez = search_game_all()
    rez.sort(key=lambda x: x[3])
    return render_template("game_list.html", rez=rez, title="Отсортированный список книг по названию игры")


@app.route("/close")
def close():
    os.system('shutdown -s')
    return render_template("index.html", title="Досвидания")


@app.route("/")
@app.route("/index")
def index():
    return render_template("reg_member.html", title='Главная')


@app.route("/facts")
def facts():
    return render_template("facts.html", title='Факты о играх')


@app.route("/main")
def all_func():
    return render_template("index.html", title='Главная страница')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            if user.email == 'vinograda80@gmail.com' and user.id == 1:
                return redirect('/index_admin')
            else:
                return redirect("/main")
        return render_template('login.html', title="Неверный логин или пароль", form=form)
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/index")


@app.route('/register', methods=['GET', 'POST'])
def reqister():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация', form=form,
                                   message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Регистрация', form=form,
                                   message="Такой пользователь уже есть")
        user = User(
            name=form.name.data,
            email=form.email.data,
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form)


@app.route('/addcompany', methods=['GET', 'POST'])
@login_required
def addcompany():
    db_sess = db_session.create_session()
    company_in_bd = db_sess.query(Company).all()
    add_form = AddCompanyForm()
    if add_form.validate_on_submit():
        company = Company(
            name_company=add_form.name_company.data)
        db_sess.add(company)
        db_sess.commit()
        return redirect('/index_admin')
    return render_template('add_company.html', title='Добавление названия компании', result=company_in_bd,
                           form=add_form)


@app.route('/addgenre', methods=['GET', 'POST'])
@login_required
def addgenre():
    db_sess = db_session.create_session()
    genres_in_bd = db_sess.query(Genres).all()
    add_form = AddGenreGameForm()
    if add_form.validate_on_submit():
        genre = Genres(
            name_genre=add_form.genre.data)
        db_sess.add(genre)
        db_sess.commit()
        return redirect('/index_admin')
    return render_template('add_genre.html', title='Добавление жанра', result=genres_in_bd, form=add_form)


@app.route('/addyear', methods=['GET', 'POST'])
@login_required
def addyear():
    db_sess = db_session.create_session()
    year_in_bd = db_sess.query(Year).all()
    add_form = AddYearsGameForm()
    if add_form.validate_on_submit():
        year = Year(
            year=add_form.name_year.data)
        db_sess.add(year)
        db_sess.commit()
        return redirect('/index_admin')
    return render_template('add_years.html', title='Добавление годов', result=year_in_bd, form=add_form)


@app.route('/addplatforms', methods=['GET', 'POST'])
@login_required
def addplatform():
    db_sess = db_session.create_session()
    platform_in_bd = db_sess.query(Platform).all()
    add_form = AddPlatformsForm()
    if add_form.validate_on_submit():
        platform = Platform(
            platform=add_form.name_platform.data)
        db_sess.add(platform)
        db_sess.commit()
        return redirect('/index_admin')
    return render_template('add_platforms.html', title='Добавление платформ', result=platform_in_bd, form=add_form)


@app.route('/add_game', methods=['GET', 'POST'])
@login_required
def addgame():
    form = AddGameForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        gm = Game()
        gm.id_year = form.id_year.data
        gm.game_name = form.game_name.data
        gm.id_company = form.id_company.data
        gm.id_genres = form.id_genres.data
        gm.age_restriction = form.age_restriction.data
        gm.id_platforms = form.id_platforms.data
        gm.link = form.link.data
        gm.img = form.img.data
        db_sess.add(gm)
        db_sess.commit()
        return redirect('/index_admin')
    return render_template('add_game.html', title='Добавление игры', form=form)


@app.route('/load_files', methods=['POST', 'GET'])
@login_required
def load_files_img():
    if request.method == 'GET':
        return render_template("load_files.html", title="Загрузка файлов изображений")
    elif request.method == 'POST':
        f = request.files['file']
        with open(f'static/img/{f.filename}', 'wb') as file:
            file.write(f.read())
        img = Image.open(f'static/img/{f.filename}')
        width = 300
        height = 280
        resized_img = img.resize((width, height), Image.ANTIALIAS)
        resized_img.save(f'static/img/{f.filename}')
        return render_template("load_files.html", title="Загрузка файлов изображений")


@app.route('/view_game', methods=['GET', 'POST'])
@login_required
def view_game():
    db_sess = db_session.create_session()
    game_in_bd = db_sess.query(Game).all()
    return render_template('view_game.html', title='Просмотр таблицы с играми', result=game_in_bd)


@app.route('/index_admin', methods=['GET', 'POST'])
@login_required
def index_admin():
    return render_template('index_admin.html', title='Страница администратора БД')


@app.route("/avt_order", methods=['GET', 'POST'])
def avt_order():
    return render_template("add_order.html", title="Заказ игры на публикацию")


@app.route("/avt_order_form", methods=['GET', 'POST'])
def avt_order_form():
    db_sess = db_session.create_session()
    order = db_sess.query(Order).filter((Order.status.like('%отказ%')) | (Order.status == 'в процессе')).all()
    form = AddOrderForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        ord = Order(
            company=form.company.data,
            game_name=form.game_name.data,
            status=form.status.data,
        )
        db_sess.add(ord)
        db_sess.commit()
        return redirect('/avt_order')
    return render_template("add_order_form.html", title="Заказ игры на публикацию", result=order, form=form)


@app.route('/edit_game/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_game(id):
    form = AddGameForm()
    if request.method == "GET":
        db_sess = db_session.create_session()
        gm = db_sess.query(Game).filter(Game.id == id).first()
        if gm:
            form.id_year.data = gm.id_year
            form.game_name.data = gm.game_name
            form.id_company.data = gm.id_company
            form.id_genres.data = gm.id_genres
            form.age_restriction.data = gm.age_restriction
            form.id_platforms.data = gm.id_platforms
            form.link.data = gm.link
            form.img.data = gm.img
        else:
            abort(404)
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        gm = db_sess.query(Game).filter(Game.id == id).first()
        if gm:
            form.id_year.data = gm.id_year
            form.game_name.data = gm.game_name
            form.id_company.data = gm.id_company
            form.id_genres.data = gm.id_genres
            form.age_restriction.data = gm.age_restriction
            form.id_platforms.data = gm.id_platforms
            form.link.data = gm.link
            form.img.data = gm.img
            db_sess.commit()
            return redirect('/index_admin')
        else:
            abort(404)
    return render_template('add_game.html', title='Редактирование игр', form=form)


@app.route('/delete_game/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_game(id):
    db_sess = db_session.create_session()
    gm = db_sess.query(Game).filter(Game.id == id).first()
    if gm:
        db_sess.delete(gm)
        db_sess.commit()

    else:
        abort()
    return redirect('/index_admin')


if __name__ == '__main__':
    main()
