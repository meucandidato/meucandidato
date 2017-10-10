# -*- coding: utf-8 -*-

from flask import Blueprint, render_template


homepage_blueprint = Blueprint(
    'homepage', __name__, template_folder='templates')


@homepage_blueprint.route('/')
def index():
    return render_template('index.html')


def configure(app):
    app.register_blueprint(homepage_blueprint)
