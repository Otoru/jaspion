"""
This example shows how to monitor an extension (1000 in the example).
"""
from jaspion import Jaspion
from jaspion.utils import filtrate


app = Jaspion(host='127.0.0.1', port=8021, password='ClueCon')

@app.handle('sofia::register')
@filtrate('from-user', '1000')
def register(event):
    domain = event['from-host']
    username = event['from-user']
    date = event['Event-Date-Local']

    print(f'[{date}] {username}@{domain} - Registred.')

@app.handle('sofia::unregister')
@filtrate('from-user', '1000')
def unregister(event):
    domain = event['from-host']
    username = event['from-user']
    date = event['Event-Date-Local']

    print(f'[{date}] {username}@{domain} - Unregistred.')


if __name__ == "__main__":
    app.run()