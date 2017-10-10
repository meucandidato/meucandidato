# -*- coding: utf-8 -*-

from dynaconf.contrib.flask_dynaconf import FlaskDynaconf


def configure(app):
    FlaskDynaconf(
        app=app,
        DYNACONF_NAMESPACE='MEUCANDIDATO',
        SETTINGS_MODULE=f'{app.root_path}/settings.yml'
    )
