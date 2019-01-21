from jaspion import Jaspion

from {{cookiecutter.project_name}} import settings


app = Jaspion(__name__, **settings.freeswitch)


@app.handle('HEARTBEAT')
def heartbeat(event):
    print(event)
