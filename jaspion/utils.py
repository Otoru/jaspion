import functools
import typing
import re


def filtrate(key: str, value: str = None, regex: bool = False):
    """
    Method that allows to filter the events accordingto a set 'key', 'value'.

    Parameters
    ----------
    - key: required
        Key to be searched in the event.
    - value: optional
        Value needed in the last key.
    - regex: optional
        Tells whether 'value' is a regular expression.
    """

    def decorator(function: typing.Callable):
        @functools.wraps(function)
        def wrapper(message):
            if isinstance(message, dict):
                if key in message:
                    content = message[key]
                    if value is None:
                        return function(message)
                    if not regex and content == value:
                        return function(message)
                    if regex and re.match(value, content):
                        return function(message)

        return wrapper

    return decorator
