from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length


class CustomerForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(max=120)])
    surname = StringField('Surname', validators=[DataRequired(), Length(max=120)])
    email = StringField('Email', validators=[DataRequired(), Length(max=120)])
    phone = StringField('Phone', validators=[DataRequired(), Length(max=120)])
    submit = SubmitField('Submit')