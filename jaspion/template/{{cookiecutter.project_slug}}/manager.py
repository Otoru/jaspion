import click

from {{cookiecutter.project_slug}}.app import app
from {{cookiecutter.project_slug}} import settings


@click.group()
def main(): pass


@main.command('run', help='Start the project.')
def run():
    print('Start "%s" project...' % settings.name)
    print('Server: {host}:{port}'.format(**settings.freeswitch))
    app.run()


@main.option('--version', '-v', help='Show project version.')
def version():
    print('Project: %s' % settings.name)
    print('Description: %s' % settings.description)
    print('Version: %s' % settings.version)


if __name__ == "__main__":
    main()
