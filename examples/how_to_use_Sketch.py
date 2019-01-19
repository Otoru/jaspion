from jaspion import Jaspion
from jaspion.sketch import Sketch


# Freeswitch data to connection
freeswitch = {
    'host': '127.0.0.1',
    'password': 'ClueCon',
    'port': 8021
}

# Create a Sketch instance
default = Sketch('heartbeat')


# Add a handler to Sketch
@default.handle('HEARTBEAT')
def heartbeat(event):
    server = event['FreeSWITCH-Hostname']
    now = event['Event-Date-Local']
    print('[%s] Recived a "heartbeat" from %s' % (now, server))


# Create a Jaspion App
app = Jaspion(__name__, **freeswitch)

# Add new Sketch to App
app.update(default)


if __name__ == "__main__":
    app.run()
