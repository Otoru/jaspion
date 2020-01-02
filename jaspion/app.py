from typing import Callable
import logging
import pprint

from greenswitch import InboundESL
from greenswitch.esl import ESLEvent

from jaspion.sketch import Sketch


class Jaspion(Sketch, InboundESL):
    def __init__(self, host: str, port: int, password: str):
        """Method created to perform the call of the two __init __ 's
        present in the SuperClasses.
        """
        Sketch.__init__(self, __name__)
        InboundESL.__init__(self, host, int(port), password)

    def _safe_exec_handler(self, handler: Callable, event: ESLEvent):
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
        try:
            data = event.headers
            worker, client = handler

            if client:
                worker(self, data)

            else:
                worker(data)

        except Exception as exc:
            name = handler.__name__
            logging.exception("ESL %s raised exception." % name)
            logging.exception(pprint.pformat(data))
            logging.exception(exc)

    def command(self, command: str, background: bool = False):
        """Send command to freeswitch using api or bgapi.

        Parameters
        ----------
        - command: required
            Command to be forwarded to freeswitch.
        - background: not required
            Defines whether the freeswitch should run the
            background command or not.
        """
        preffix = "bgapi" if background else "api"
        result = super().send(f"{preffix} {command}").data

        return result.split(": ", 1)[-1] if background else result

    def process_events(self):
        """Overridden method to create the filters in the ESL
        before starting the processing of events.
        """
        for event in self.event_handlers.keys():
            if event.isupper():
                self.send("filter Event-Name {}".format(event))
            else:
                self.send("filter Event-Subclass {}".format(event))
        super().process_events()

    def start(self, *args, **kwargs):
        """Method created to be overwritten."""
        ...

    def run(self):
        """Method called to request the events.

        Raises
        ------
        - greenswitch.NotConnectedError:
            Connection failed while attempting to send command
            to FreeSwitch.
        """
        self.start()
        self.connect()
        self.send("events plain ALL")
        self.process_events()
