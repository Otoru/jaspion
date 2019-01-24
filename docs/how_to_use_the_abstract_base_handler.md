# How to use the *AbstractBaseHandler*?

Abstract Base Bandler is an ABC[¹][1] for those who want to create more robust handlers for events.


## Where is?

You can use ABC you should import the same from `jaspion.abc`. See an example below.

## Show me the code

```python

from jaspion.abc import AbstractBaseHandler
from jaspion import Jaspion


class SimpleHandler(AbstractBaseHandler):
    def setup(self):
        print('Hello, I am a setup.')

    def handle(self):
        print('event:')
        print(self.event)

    def finish(self):
        print('Finishing the processing.')

app = Jaspion(__name__, host='127.0.0.1',
                        port=8021,
                        password='ClueCon')


app['HEARTBEAT'] = SimpleHandler


if __name__ == '__main__':
    app.run()

```

## Understanding the example

First of all let's understand the SimpleHandler class:

- It is a subclass of our ABC AbstractBaseHandler.
- Three methods were implemented: setup, handle and finish.
- the SetUp method is called before starting the event processing and is optional.
- The handle method is mandatory and event processing must be contained in it.
- Similar to the setup method, the finish method serves to finalize event processing and is also an optional method.
- Similar to a dictionary, to add a class to a certain event you should use `app[event] = class`.


## Comments

- The event instance to be processed will always be a dictionary referenced in `self.event`.
- To add more than one handler to a given event, you can use the syntax `app[event].append(class)`.

[1]: https://docs.python.org/3/glossary.html#term-abstract-base-class

