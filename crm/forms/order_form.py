from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField
from wtforms.validators import DataRequired


class OrderForm(FlaskForm):
    customer = SelectField('Customer', validators=[DataRequired()])
    product = SelectField('Product', validators=[DataRequired()])
    submit = SubmitField('Submit')
