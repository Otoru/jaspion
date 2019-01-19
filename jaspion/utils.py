import functools


def filtrate(key: str, value: str):
    """Method that allows to filter the events according
    to a set 'key', 'value'. No need 'haskey' to work.

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


def haskey(key: str):
    """Ensures that only events with the entered key will be
    processed by the function.

    Parameters
    ----------
    - key: required
        Key to be searched in the event.
    """
    def decorator(function: callable):
        @functools.wraps(function)
        def wrapper(message):
            if isinstance(message, dict):
                if key in message:
                    result = function(message)
                    return result
        return wrapper
    return decorator
