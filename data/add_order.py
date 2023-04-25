from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField
from wtforms.validators import DataRequired


class AddOrderForm(FlaskForm):
    company = StringField('Компания', validators=[DataRequired()])
    game_name = StringField('Название игры', validators=[DataRequired()])
    status = StringField('Статус', validators=[DataRequired()])
    submit = SubmitField('Заказать')
