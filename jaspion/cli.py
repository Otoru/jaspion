import os

import click
from cookiecutter.main import cookiecutter


here = os.path.dirname(os.path.realpath(__file__))


@click.group()
def main(): pass


@main.command('new', help='Create a new project.')
def new():
    """Command called to create a new Jaspion project."""
    print('Create a new Jaspion project...')
    cookiecutter(os.path.join(here, 'template'))
