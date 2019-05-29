"""
How to use a class to handle events.
"""
from jaspion.abc import AbstractBaseHandler
from jaspion import Jaspion


# Freeswitch data to connection
freeswitch = {
    'host': '127.0.0.1',
    'password': 'ClueCon',
    'port': 8021
}


# Create a subclass of *AbstractBaseHandler*
class SimpleHandler(AbstractBaseHandler):
    def setup(self):
        print('Hello, I am a setup.')

    def handle(self):
        print('event:')
        print(self.event)

    def finish(self):
        print('Finishing the processing.')


# Create a Jaspion App
app = Jaspion(**freeswitch)


# Add Classhandler to event.
app['HEARTBEAT'] = SimpleHandler


# Run Jaspion App
if __name__ == '__main__':
    app.run()