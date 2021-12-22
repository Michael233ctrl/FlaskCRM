from flask import render_template, flash, redirect, abort, request
from flask.views import MethodView

from crm.service.view_service import update, create


class BaseListView(MethodView):

    def __init__(self):
        self.template_name = None
        self.model = None
        self.context = None

    def get(self):
        return render_template(self.template_name, **self.context)

    def post(self):
        form = self.context['form']

        if form.validate_on_submit():
            create(self.model, form.data)
            flash('Success', 'success')
            return redirect(request.path)
        else:
            flash('Wrong entered data', 'danger')


class BaseDetailView(MethodView):
    def __init__(self):
        self.template_name = None

    def get(self, id):
        return render_template(self.template_name, **self.get_context(id))

    def post(self, id):
        data = self.get_context(id)
        item = data.get('customer') or data.get('product')
        if item is None:
            abort(404)

        form = data['form']
        if form.validate_on_submit():
            update(item, form.data)
            flash(f'{item} successfully updated', 'success')
            return redirect(request.path)
        else:
            flash('Wrong entered data', 'danger')


class BaseDeleteView(MethodView):
    def __init__(self):
        self.context = None
        self.template_name = None

    def delete(self):
        pass
