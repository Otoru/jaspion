import json
from urllib import parse

from jaspion import Jaspion

from gevent import pywsgi  # pylint: disable=import-error
from geventwebsocket import handler  # pylint: disable=import-error


def websocket(environ, response):
    app = Jaspion(host="127.0.0.1", port=8021, password="ClueCon")
    client = (environ["REMOTE_ADDR"], environ["REMOTE_PORT"])
    query = environ["QUERY_STRING"]
    ws = environ["wsgi.websocket"]

    def sendmessage(event):
        msg = json.dumps(event)
        ws.send(msg)

    events = parse.parse_qs(query)
    print('New subscriber: "{}:{}"'.format(*client))

    if "event" in events:
        for item in events["event"]:
            print('Listen event "{}"'.format(item))
            app.setdefault(item, []).append(sendmessage)

    app.run()


server = pywsgi.WSGIServer(
    ("", 8000), websocket, handler_class=handler.WebSocketHandler
)


if __name__ == "__main__":
    server.serve_forever()
