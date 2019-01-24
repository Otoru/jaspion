# How to use the 'Abstract Base Handler'?

Abstract Base Bandler is an ABC[¹][1] for those who want to create more robust handlers for events.


## Where is?

You can use ABC you should import the same from `jaspion.abh`. See an example below.

## Show me the code

```python

from jaspion.abh import BaseHandler
from jaspion import Jaspion


class SimpleHandler(BaseHandler):
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

[1]: https://docs.python.org/3/glossary.html#term-abstract-base-class

