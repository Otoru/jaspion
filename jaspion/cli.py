import os
import importlib

import click

from jaspion import Jaspion


@click.group()
def cli():
    """Jaspion CLI to manipulate and execute projects."""
    ...


@cli.command()
@click.option('--host', default='127.0.0.1', help='Address of FreeSwitch.')
@click.option('--port', default=8021, type=int, help='Port to ESL connection.')
@click.option('--password', default='ClueCon', help='Password ESL connect.')
def runserver(host, port, password):
    """Connect in freeswitch and start a listner."""
    try:
        click.echo('Try to connect in esl://{}:{}'.format(host, port))
        module = os.environ['JASPION_APP']
        listner = importlib.import_module(module)
        click.echo('Listner: {}'.format(listner))
        app = Jaspion(host, port, password)
        app.update(listner)
        app.run()

    except KeyboardInterrupt:
        click.echo('Stoping...')
        app.stop()

    except ImportError:
        click.echo(click.style('Failed to load listener.', fg='red'))
