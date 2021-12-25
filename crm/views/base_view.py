from flask import render_template, flash, redirect, request, jsonify
from flask.views import MethodView

from crm.service.view_service import ServiceDB


class BaseListView(ServiceDB, MethodView):

    def __init__(self):
        super().__init__()
        self.template_name = None
        self.context = None

    def get(self):
        return render_template(self.template_name, **self.context())

    def post(self):
        data = self.context()
        form = data.get('form')

        if form.validate_on_submit():
            self.create(form.data)
            flash('Item was successfully created', 'success')
            return redirect(request.path)
        else:
            flash('Wrong entered data', 'danger')


class BaseDetailView(ServiceDB, MethodView):

    def __init__(self):
        super().__init__()
        self.template_name = None
        self.context = None

    def get(self, id):
        return render_template(self.template_name, **self.context(id))

    def post(self, id):
        data = self.context(id)
        form = data.get('form')

        if form.validate_on_submit():
            self.update(form.data)
            flash(f'Successfully updated', 'success')
            return redirect(request.path)
        else:
            flash('Wrong entered data', 'danger')

    def delete(self, id):
        item = self.delete_item(id)
        return jsonify(f'{item} was deleted')
