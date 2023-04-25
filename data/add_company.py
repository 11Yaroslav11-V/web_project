from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField
from wtforms.validators import DataRequired


class AddCompanyForm(FlaskForm):
    name_company = StringField('Название компании', validators=[DataRequired()])
    submit = SubmitField('Добавить')
