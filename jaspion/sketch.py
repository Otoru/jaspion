from collections.abc import MutableMapping
from collections.abc import MutableSequence
from collections.abc import Callable
import functools
import reprlib


class Sketch(MutableMapping):
    def __init__(self, name: str):
        """Method used to save the Sketch name and create a
        dictionary instance in 'self.event_handlers'.
        """
        self.__name__ = name
        self.event_handlers = {}

    def __contains__(self, key: str):
        """Direct access interface to 'self.handlers'."""
        if key in self.event_handlers:
            return True
        return False

    def __eq__(self, other: object):
        """Direct access interface to 'self.handlers'."""
        if isinstance(other, self.__class__):
            return self.event_handlers == other.event_handlers
        else:
            return False

    def __ne__(self, other: object):
        """Direct access interface to 'self.handlers'."""
        return not self.__eq__(other)

    def __iter__(self):
        """Returns an iterable with the 'event_handlers' keys."""
        return (key for key in self.event_handlers.keys())

    def __len__(self):
        """Direct access interface to 'self.handlers'."""
        return len(self.event_handlers)

    def __getitem__(self, key: str):
        """Direct access interface to 'self.handlers'."""
        if key in self.event_handlers:
            return self.event_handlers[key]
        raise KeyError(key)

    def __setitem__(self, event: str, handler: Callable):
        """Direct access interface to 'self.handlers'."""
        if isinstance(handler, Callable):
            self.event_handlers[event] = [handler]

        elif isinstance(handler, MutableSequence):
            self.event_handlers[event] = handler

        else:
            name = type(handler).__name__
            raise TypeError('"%s" not not is valid object' % name)

    def __delitem__(self, key: str):
        """Direct access interface to 'self.handlers'."""
        if key in self.event_handlers:
            del self.event_handlers[key]

    def keys(self):
        """Direct access interface to 'self.handlers'."""
        return self.event_handlers.keys()

    def values(self):
        """Direct access interface to 'self.handlers'."""
        return self.event_handlers.values()

    def items(self):
        """Direct access interface to 'self.handlers'."""
        return self.event_handlers.items()

    def popitem(self):
        """Direct access interface to 'self.handlers'."""
        if self.event_handlers:
            return self.event_handlers.popitem()
        name = name = type(self).__name__
        raise KeyError('popitem(): %s is empty' % name)

    def update(self, other: object):
        """Method to be used to record Sketch's instance of
        Jaspion or even concatenated Sketch's.

        Parameters
        ----------
        - other: required
            An Sketch instance.

        Raises
        ------
        - TypeError:
            Object provided for update is invalid.
        """
        if not isinstance(other, Sketch):
            name = type(other).__name__
            raise TypeError('%s not is valid object.' % name)

        for event, list in other.event_handlers.items():
            self.event_handlers.setdefault(event, []).extend(list)

    def clear(self):
        """Direct access interface to 'self.handlers'."""
        self.event_handlers.clear()

    def register_handle(self, event: str, function: Callable):
        """Function used to add a function to 'event handlers'
        associated with the event reported.

        Parameters
        ----------
        - event: required
            Name of the event to be parsed.
        - function: required
            Function that will process the event.
        """
        self.event_handlers.setdefault(event, []).append(function)

    def handle(self, event: str) -> Callable:
        """Decorator that allows the registration of new handlers.
        The event will be provided for the function in the form
        of a Dict.

        Parameters
        ----------
        - event: required
            Name of the event to be parsed.
        """
        def decorator(function: Callable):
            self.register_handle(event, function)

            @functools.wraps(function)
            def wrapper(*args, **kwargs):
                result = function(*args, **kwargs)
                return result
            return wrapper
        return decorator

    def __repr__(self):
        """Creates a valid representation for class
        and its subclasses.
        """
        name = self.__name__
        clss = type(self).__name__
        events = '[]'
        if self.event_handlers:
            repre = reprlib.repr(self.event_handlers.keys())
            key = (repre.find('[')+1)
            events = repre[key: -2]

        return '%s(name=%s, events=%s)' % (clss, name, events)
