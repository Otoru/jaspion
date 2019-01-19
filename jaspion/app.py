import pprint
import logging
import functools

from greenswitch import InboundESL
from greenswitch.esl import ESLEvent
import gevent

from jaspion.sketch import Sketch

class Jaspion(Sketch, InboundESL):
    def __init__(self, name: str, *args, **kwargs):
        """Method created to perform the call of the two __init __ 's
        present in the SuperClasses.
        """
        Sketch.__init__(self, name)
        InboundESL.__init__(self, *args, **kwargs)

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
            logging.debug('ESL %s raised exception.' % handler.__name__)
            logging.debug(pprint.pformat(event))

    def run(self):
        """Method called to request the events.
        
        Raises
        ------
        - greenswitch.NotConnectedError:
            Connection failed while attempting to send command
            to FreeSwitch.
        """
        self.connect()
        # TODO: Find a way to request only events that have a handler.
        self.send('events plain ALL')
        self.process_events()
