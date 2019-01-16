import functools
import logging

from greenswitch import InboundESL
import gevent


class Jaspion(InboundESL):
    def __init__(self, name):
        self.name = name
        self.hands = {}

    def _addhand(self, event, function):
        if event not in self.hands:
            self.hands[event] = []

        if function in self.hands[event]:
            return

        self.hands[event].append(function)

    def handle(self, event):
        def decorator(function):
            self._addhand(event, function)
            @functools.wraps(function)
            def wrapper(*args, **kwargs):
                result = function(*args, **kwargs)
                return result
            return wrapper
        return decorator

    def run(self, host='127.0.0.1', port=8021, password='ClueCon'):
        logging.debug('Try connect with %s:%s' % (host, password))
        super().__init__(host, port, password)
        self.event_handlers.update(self.hands)
        self.connect()
        logging.debug('Requesting events to the server.')
        self.send('events plain ALL')
        self.process_events()
