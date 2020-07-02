from jaspion.utils import filtrate

import pytest


class Callback:
    """
    Class used to represent a callback.
    """
    def __init__(self):
        self.control = False

    def __call__(self, *args, **kwargs):
        self.control = True

def test_filtrate_is_a_callable():
    """Verify if 'filtrate' is a callable."""
    assert callable(filtrate)

def test_filtrate_require_a_single_argument():
    """Verify if 'filtrate' is a callable."""
    msg = "filtrate() missing 1 required positional argument: 'key'"
    with pytest.raises(TypeError) as exc:
        filtrate() # pylint: disable=no-value-for-parameter
        assert msg in str(exc)

def test_filtrate_return_a_callable():
    """Ensures that the filtrate returns a callable when invoked correctly."""
    result = filtrate('key')
    assert callable(result)

tests = [
    {'decorator': ['key'], 'response': True, 'event': {'key': 'value'}},
    {
        'decorator': ['key'],
        'response': False,
        'event': {
            'invalid_key': 'value'
        }
    },
    {
        'decorator': ['key', 'value'],
        'response': True,
        'event': {
            'key': 'value'
        }
    },
    {
        'decorator': ['key', 'value'],
        'response': False,
        'event': {
            'key': 'another_value'
        }
    },
    {
        'decorator': ['key', '^[a-z]{5}$', True],
        'response': True,
        'event': {
            'key': 'value'
        }
    },
    {
        'decorator': ['key', '^[a-z]{3}$', True],
        'response': False,
        'event': {
            'key': 'value'
        }
    }
]

@pytest.mark.parametrize('content', tests)
def test_decorator_behavior(content):
    """Validates decorator behavior."""
    handler = Callback()
    decorator = filtrate(*content['decorator'])
    new_handler = decorator(handler)
    event = content['event']

    new_handler(event)

    assert content['response'] == handler.control
