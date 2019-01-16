import functools

from greenswitch import InboundESL
from greenswitch.esl import ESLEvent
import gevent


class Jaspion(InboundESL):
    def __init__(self, *args, **kwargs):
        """Method created only to call the superclass method without
        giving valid arguments."""
        host = kwargs.get('host')
        port = kwargs.get('port')
        password = kwargs.get('password')
        super().__init__(host, port, password)

    def _safe_exec_handler(self, handler: callable, event: ESLEvent):
        """Overridden method to ensure that the event passed to
        handlers is actually a dict instance with information
        already processed."""
        event = event.headers
        super()._safe_exec_handler(handler, event)

    def handle(self, event: str) -> callable:
        """Decorator that allows the registration of new handlers."""
        def decorator(function: callable):
            self.register_handle(event, function)
            @functools.wraps(function)
            def wrapper(*args, **kwargs):
                result = function(*args, **kwargs)
                return result
            return wrapper
        return decorator

    def connect(self, host: str, port: int, password: str):
        """Overwritten method to ensure that FreeSwitch information
        is only required at connection time."""
        self.host = host
        self.port = port
        self.password = password
        super().connect()

    def run(self, host='127.0.0.1', port=8021, password='ClueCon'):
        """Method called to perform the connection with the freeswitch
        and request the events."""
        self.connect(host, port, password)
        self.send('events plain ALL')
        self.process_events()