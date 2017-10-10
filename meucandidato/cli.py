# -*- coding: utf-8 -*-

import code
import click

from .app import create_app


app = create_app()


@click.group()
def main():
    pass


@main.command()
def shell():
    """Abre um shell com o objeto app no contexto"""
    with app.app_context():
        try:
            from IPython import start_ipython
            start_ipython(argv=[], user_ns={'app': app})
        except:
            code.interact(banner='Meu Candidato', local={'app': app})


@main.command()
@click.option('--debug/--no-debug', default=True)
@click.option('--reloader/--no-reloader', default=True)
@click.option('--host', default='0.0.0.0')
@click.option('--port', default=5000)
def runserver(debug, reloader, host, port):
    """Inicia o servidor local em modo debug"""
    app.run(debug=debug, use_reloader=reloader, host=host, port=port)
