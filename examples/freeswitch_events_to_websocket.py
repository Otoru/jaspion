"""
How to send freeswitch events via websockets
"""
import json

from jaspion import Jaspion

from gevent.pywsgi import WSGIServer
# You need install geventwebsocket
from geventwebsocket.handler import WebSocketHandler


# Freeswitch data to connection
freeswitch = {
    'host': '127.0.0.1',
    'password': 'ClueCon',
    'port': 8021
}

# Websocket address in list
address = ('127.0.0.1', 8000)

# Simple function to connect freeswitch and websocket client
def websocket(environ, response):
    app = Jaspion(**freeswitch)
    path = environ["PATH_INFO"].replace('/','').upper()
    ws = environ["wsgi.websocket"]

    def sendmessage(event):
        msg = json.dumps(event)
        ws.send(msg)
    
    app[path] = sendmessage
    app.run()


if __name__ == '__main__':
    # Connect function to WSGI server
    server = WSGIServer(address, websocket, handler_class=WebSocketHandler)
    server.serve_forever()
