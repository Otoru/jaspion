import click

from {{cookiecutter.project_slug}}.app import app
from {{cookiecutter.project_slug}} import settings


@click.group(context_settings={'help_option_names': ('-h', '--help')})
def main(): pass


@main.command('run', help='Start the project.')
def run():
    print('Start "%s" project...' % settings.name)
    print('Server: {host}:{port}'.format(**settings.freeswitch))
    app.run()


if __name__ == "__main__":
    main()
