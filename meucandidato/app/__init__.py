# -*- coding: utf-8 -*-

from flask import Flask

from meucandidato import config, ext


def create_app(import_name='meucandidato'):
    app = Flask(import_name)

    # Initialize system with dynamic configurations
    config.configure(app)

    # Load the extensions
    ext.configure(app)

    return app
