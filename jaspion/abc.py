from abc import abstractmethod
from typing import Dict
from abc import ABC


class AbstractBaseHandler(ABC):
    def __init__(self, event: Dict):
        self.event = event

        try:
            self.setup()
            self.handle()

        finally:
            self.finish()

    def setup(self):
        """Method called to start event processing. Can be overwritten."""
        ...

    @abstractmethod
    def handle(self):
        """Method called to process the event. Must be overwritten."""

    def finish(self):
        """Method to terminate processing. Can be overwritten."""
        ...

    def __repr__(self):
        """Generates representation for debug."""
        name = type(self).__name__

        if self.event["Event-Name"] == "CUSTOM":
            event = self.event["Event-Subclass"]
        else:
            event = self.event["Event-Name"]

        return "%s(%s)" % (name, event)
