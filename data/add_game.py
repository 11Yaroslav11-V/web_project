from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, IntegerField
from wtforms.validators import DataRequired


class AddGameForm(FlaskForm):
    id_year = IntegerField('id года выпуска', validators=[DataRequired()])
    game_name = StringField('название книги', validators=[DataRequired()])
    id_company = IntegerField('id компании разработчика', validators=[DataRequired()])
    id_genres = IntegerField('id жанра игры', validators=[DataRequired()])
    age_restriction = IntegerField('возрастное ограничение', validators=[DataRequired()])
    id_platforms = IntegerField("id платформ", validators=[DataRequired()])
    link = StringField('ссылка на игру', validators=[DataRequired()])
    img = StringField('название файла', validators=[DataRequired()])

    submit = SubmitField('Сохранить')
