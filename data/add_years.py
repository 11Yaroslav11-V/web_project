from flask_wtf import FlaskForm
from wtforms import SubmitField, IntegerField
from wtforms.validators import DataRequired


class AddYearsGameForm(FlaskForm):
    name_year = IntegerField('Год игры', validators=[DataRequired()])
    submit = SubmitField('Добавить')
