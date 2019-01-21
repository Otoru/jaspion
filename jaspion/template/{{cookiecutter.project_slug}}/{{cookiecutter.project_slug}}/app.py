from jaspion import Jaspion

from {{cookiecutter.project_slug}} import settings


app = Jaspion(__name__, **settings.freeswitch)


@app.handle('HEARTBEAT')
def heartbeat(event):
    print(event)
