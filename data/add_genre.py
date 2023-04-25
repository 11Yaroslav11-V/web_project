from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField
from wtforms.validators import DataRequired


class AddGenreGameForm(FlaskForm):
    genre = StringField('Жанр игры', validators=[DataRequired()])
    submit = SubmitField('Добавить')
