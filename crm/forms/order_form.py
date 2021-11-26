from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField
from wtforms.validators import DataRequired
from crm.models import Customer, Product


class OrderForm(FlaskForm):
    customer = SelectField('Customer', choices=[(c.id, c) for c in Customer.query.all()],
                           validators=[DataRequired()])
    product = SelectField('Product', choices=[(c.id, c) for c in Product.query.all()],
                          validators=[DataRequired()])
    submit = SubmitField('Submit')
