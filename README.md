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


app = Jaspion(__name__)

@app.handle('sofia::register')
@app.filtrate('from-user', '1000')
def register(event):
    domain = event['from-host']
    username = event['from-user']
    date = event['Event-Date-Local']

    print(f'[{date}] {username}@{domain} - Registred.')

@app.handle('sofia::unregister')
@app.filtrate('from-user', '1000')
def unregister(event):
    domain = event['from-host']
    username = event['from-user']
    date = event['Event-Date-Local']

    print(f'[{date}] {username}@{domain} - Unregistred.')


if __name__ == "__main__":
    app.run('127.0.0.1', 8021, 'ClueCon')
```

## To-Do List
- [X] Create the decorator to handle events.
- [ ] Create a CLI to run projects.
- [ ] Create filter to request only the marked events.
- [ ] Create the Documentation.
