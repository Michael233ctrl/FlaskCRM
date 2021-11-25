from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired, Length


class ProductForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(max=200)])
    price = FloatField('Price', validators=[DataRequired()])
    description = StringField('Description', validators=[Length(max=300)])
    submit = SubmitField('Submit')
