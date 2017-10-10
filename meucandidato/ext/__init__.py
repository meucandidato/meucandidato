# -*- coding: utf-8 -*-

import import_string


def configure(app):
    for extension in app.config.get('EXTENSIONS', []):
        try:
            factory = import_string(extension)
            factory(app)
        except Exception as e:
            app.logger.error(f'Error to load {extension}: {e}')
        else:
            app.logger.debug(f'Extension {extension} loaded successfully.')
