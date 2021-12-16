"""
This module contains views related to the bp blueprint
"""
from flask import Blueprint, render_template
from flask import current_app as app

bp = Blueprint('bp', __name__)


@bp.app_errorhandler(404)
def page_not_found(e):
    """
    Called when a 404(not found) error occurs,
    and write an error to a log file.

    :param e: error
    :return: rendered `error_404.html` template
    """
    print(e)
    app.logger.error(e)
    return render_template("error_404.html", description=e.description), 404


@bp.app_errorhandler(500)
def server_error(e):
    """
    Called when a 500(internal server error) error occurs,
    and write an error to a log file.

    :param e: error
    :return: rendered `error_500.html` template
    """
    app.logger.error(e)
    return render_template("error_500.html", description=e.description), 500
