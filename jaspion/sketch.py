class Sketch:
    def __init__(self, name):
        self.name = name
        self.event_handlers = {}

    def __iter__(self):
        """Returns an iterable with the 'event_handlers' keys."""
        return (key for key in self.event_handlers.keys())

    def register_handle(self, event: str, function: callable):
        """Function used to add a function to 'event handlers'
        associated with the event reported.
        
        Parameters
        ----------
        - event: required
            Name of the event to be parsed.
        - function: required
            Function that will process the event.
        """
        if event not in self.event_handlers:
            self.event_handlers[event] = []
        if function not in self.event_handlers[event]:
            self.event_handlers[event].append(function)

    def handle(self, event: str) -> callable:
        """Decorator that allows the registration of new handlers.
        The event will be provided for the function in the form
        of a Dict.

        Parameters
        ----------
        - event: required
            Name of the event to be parsed.
        """
        def decorator(function: callable):
            self.register_handle(event, function)
            @functools.wraps(function)
            def wrapper(*args, **kwargs):
                result = function(*args, **kwargs)
                return result
            return wrapper
        return decorator