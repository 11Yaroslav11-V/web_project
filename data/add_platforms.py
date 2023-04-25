from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField
from wtforms.validators import DataRequired


class AddPlatformsForm(FlaskForm):
    name_platform = StringField('Название платформы', validators=[DataRequired()])
    submit = SubmitField('Добавить')
