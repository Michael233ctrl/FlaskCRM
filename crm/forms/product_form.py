from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length


class ProductForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(max=200)])
    price = StringField('Price', validators=[DataRequired(), Length(max=120)])
    description = StringField('Description', validators=[DataRequired(), Length(max=300)])
    submit = SubmitField('Submit')
