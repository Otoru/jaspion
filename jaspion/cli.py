import os
import sys
import importlib

import click
from greenswitch.esl import NotConnectedError

from jaspion import Jaspion


@click.group()
def main():
    """Jaspion CLI to manipulate and execute projects."""
    ...


@main.command()
@click.option(
    "--host",
    envvar="FSHOST",
    show_default=True,
    default="127.0.0.1",
    help="Address of FreeSwitch.",
)
@click.option(
    "--port",
    type=int,
    default=8021,
    envvar="FSPORT",
    show_default=True,
    help="Port to ESL connect.",
)
@click.option(
    "--password",
    default="ClueCon",
    show_default=True,
    envvar="FSPASSWD",
    help="Password to ESL connect.",
)
@click.option("--debug/--no-debug", default=False)
def runserver(host, port, password, debug):
    """Connect in freeswitch and start a listner."""
    try:
        module = os.environ.get("JASPION_APP", None)
        sketch = "app"

        if ":" in module:
            module, sketch = module.split(":", 1)

        if module:
            path = os.getcwd()
            importlib.invalidate_caches()
            sys.path.append(os.path.abspath(path))
            click.echo("Try to connect in esl://{}:{}".format(host, port))

            if debug:
                click.echo(
                    click.style(f"Read file {path}/{module}.py", fg="blue")
                )

            mod = importlib.import_module(module)
            result = getattr(mod, sketch)

            if debug:
                click.echo(click.style(f"Listner: {result}", fg="blue"))

            app = Jaspion(host, port, password)

            if callable(result):
                listner = result()
            else:
                listner = result

            app.update(listner)
            app.run()

        else:
            click.echo("No application configured.")

    except ImportError:
        click.echo(click.style("Failed to load listener.", fg="red"))

    except (KeyError, TypeError):
        click.echo(click.style("Invalid listener configured.", fg="red"))

    except (NotConnectedError, ConnectionRefusedError):
        click.echo(click.style("Failed to connect with freeswitch.", fg="red"))

    except KeyboardInterrupt:
        click.echo("Stoping...")
        app.stop()
