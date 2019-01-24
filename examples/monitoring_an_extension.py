"""
This example shows how to monitor an extension (1000 in the example).
"""
from jaspion import Jaspion
from jaspion.utils import filtrate


# Freeswitch data to connection
freeswitch = {
    'host': '127.0.0.1',
    'password': 'ClueCon',
    'port': 8021
}

# Instance of Jaspion
app = Jaspion(__name__, **freeswitch)


# Handler to 'pre_register' event and filter to extension 1000.
@app.handle('sofia::pre_register')
@filtrate('from-user', '1000')
def pre_register(event):
    domain = event['from-host']
    username = event['from-user']
    date = event['Event-Date-Local']

    print(f'[{date}] {username}@{domain} - Tried to register.')


# Handler to 'register_attempt' event and filter to extension 1000.
@app.handle('sofia::register')
@filtrate('from-user', '1000')
def register(event):
    domain = event['from-host']
    username = event['from-user']
    date = event['Event-Date-Local']

    print(f'[{date}] {username}@{domain} - Register.')


# Handler to 'register_attempt' event and filter to extension 1000.
@app.handle('sofia::register_attempt')
@filtrate('from-user', '1000')
def register_attempt(event):
    domain = event['from-host']
    username = event['from-user']
    date = event['Event-Date-Local']

    print(f'[{date}] {username}@{domain} - Auth operation terminated.')


# Handler to 'register_failure' event and filter to extension 1000.
@app.handle('sofia::register_failure')
@filtrate('from-user', '1000')
def register_failure(event):
    domain = event['from-host']
    username = event['from-user']
    date = event['Event-Date-Local']

    print(f'[{date}] {username}@{domain} - Failed to register.')


# Handler to 'unregister' event and filter to extension 1000.
@app.handle('sofia::unregister')
@filtrate('from-user', '1000')
def unregister(event):
    domain = event['from-host']
    username = event['from-user']
    date = event['Event-Date-Local']

    print(f'[{date}] {username}@{domain} - Unregistred.')


if __name__ == "__main__":
    # Start Jaspion
    app.run()
