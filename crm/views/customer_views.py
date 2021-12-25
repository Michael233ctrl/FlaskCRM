"""
This module contains views related to the customers blueprint
"""
# from flask import current_app as app

from crm.models import Customer
from crm.forms.customer_form import CustomerForm
from views.base_view import BaseListView, BaseDetailView


class CustomerListView(BaseListView):

    def __init__(self):
        super().__init__()
        self.model = Customer
        self.template_name = 'customer/customers.html'
        self.context = self.get_context

    def get_context(self):
        customers = self.select_all()
        return {'customers': customers, 'total_customers': len(customers)}


class CustomerCreateView(BaseListView):

    def __init__(self):
        super().__init__()
        self.model = Customer
        self.template_name = 'customer/customer_create.html'
        self.context = self.get_context

    @staticmethod
    def get_context():
        return {'form': CustomerForm()}


class CustomerDetailView(BaseDetailView):

    def __init__(self):
        super().__init__()
        self.model = Customer
        self.template_name = 'customer/customer_detail.html'
        self.context = self.get_context

    def get_context(self, id_):
        customer = self.select_by_id(id_)
        self.model = customer

        form = CustomerForm(
            name=customer.name,
            surname=customer.surname,
            email=customer.email,
            phone=customer.phone
        )
        return {'customer': customer, 'form': form}
