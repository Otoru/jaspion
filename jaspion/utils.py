import functools
import typing


def filtrate(key: str, value: str = None):
    """Method that allows to filter the events according
    to a set 'key', 'value'.

    Parameters
    ----------
    - key: required
        Key to be searched in the event.
    - value: optional
        Value needed in the last key.
    """
    def decorator(function: typing.Callable):
        @functools.wraps(function)
        def wrapper(message):
            if isinstance(message, dict):
                if key in message:
                    if key is None:
                        return function(message)
                    if message[key] == value:
                        return function(message)

        return wrapper
    return decorator
