# Jaspion

Python module developed to work with ESL (FreeSwitch).

## Installation Instructions

You can install the package in two ways:
```bash
$ pip install jaspion                           # From pypi
$ pip install https://github.com/Otoru/jaspion  # From source code
```

## Example
This is a simple example:

```python 
from jaspion import Jaspion
from jaspion.utils import filtrate


app = Jaspion('127.0.0.1', 8021, 'ClueCon')

@app.handle('sofia::register')
@filtrate('from-user', '1000')
def register(event):
    domain = event['from-host']
    username = event['from-user']
    date = event['Event-Date-Local']

    print(f'[{date}] {username}@{domain} - Registred.')

@app.handle('sofia::unregister')
@filtrate('from-user', '1000')
def unregister(event):
    domain = event['from-host']
    username = event['from-user']
    date = event['Event-Date-Local']

    print(f'[{date}] {username}@{domain} - Unregistred.')


if __name__ == "__main__":
    app.run()
```

## To-Do List
- [X] Create the decorator to handle events.
- [ ] Create a CLI to run projects.
- [X] Create filter to request only the marked events.
- [ ] Create the Documentation.
- [ ] Create Class to 'lazzy append' handlers.
