import pprint
import logging
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
        already processed.

        Parameters
        ----------
        - handler: required
            Callable that will be called to process the event.
            The same should accept only a mandatory filing for
            no exceptions to occur.
        - event: required
            ESLEvent instance with date already parsed.
        """
        data = event.headers
        try:
            handler(data)
        except:
            logging.exception('ESL %s raised exception.' % handler.__name__)
            logging.error(pprint.pformat(event))

    def handle(self, event: str) -> callable:
        """Decorator that allows the registration of new handlers.
        The event will be provided for the function in the form
        of a Dict.

        Parameters
        ----------
        - event: required
            Name of the event to be parsed..
        """
        def decorator(function: callable):
            self.register_handle(event, function)
            @functools.wraps(function)
            def wrapper(*args, **kwargs):
                result = function(*args, **kwargs)
                return result
            return wrapper
        return decorator

    def filtrate(self, key: str, value: str):
        """Method that allows to filter the events according
        to a set 'key', 'value'.
        
        Parameters
        ----------
        - key: required
            Key to be searched in the event.
        - value: required
            Value needed in the last key.
        """
        def decorator(function: callable):
            @functools.wraps(function)
            def wrapper(message):
                if isinstance(message, dict):
                    if key in message:
                        if message[key] == value:
                            result = function(message)
                            return result
            return wrapper
        return decorator

    def connect(self, host: str, port: int, password: str):
        """Overwritten method to ensure that FreeSwitch information
        is only required at connection time.

        Parameters
        ----------
        - host: required
            FreeSwitch IP Address.
        - port: required
            Port where the ESL service is listening..
        - password: required
            Password used for authentication.

        Raises
        ------
        - greenswitch.NotConnectedError:
            Connection failed.
        - ValueError:
            Invalid password.
        """
        self.host = host
        self.port = port
        self.password = password
        super().connect()

    def run(self,
            host: str = '127.0.0.1',
            port: int = 8021,
            password: str = 'ClueCon'):
        """Method called to perform the connection with the freeswitch
        and request the events.
        For more details of the parameters., see the 'connect' method.

        Raises
        ------
        - greenswitch.NotConnectedError:
            Connection failed while attempting to send command
            to FreeSwitch.
        """
        self.connect(host, port, password)
        # TODO: Find a way to request only events that have a handler.
        self.send('events plain ALL')
        self.process_events()
