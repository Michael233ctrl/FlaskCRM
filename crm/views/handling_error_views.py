from flask import Blueprint, render_template
from crm import app

bp = Blueprint('bp', __name__)


@bp.app_errorhandler(404)
def page_not_found(e):
    app.logger.error(e)
    return render_template("error_404.html", description=e.description), 404


@bp.app_errorhandler(500)
def server_error(e):
    app.logger.error(e)
    return render_template("error_500.html", description=e.description), 500
