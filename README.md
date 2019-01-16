# Jaspion

Python module developed to work with ESL (FreeSwitch).

## Example
This is a simple example:

```python 
from jaspion import Jaspion


app = Jaspion(__name__)

@app.handle('heartbeat')
def heartbeat(message):
    print(data)


if __name__ == "__main__":
    app.run('127.0.0.1', 8021, 'ClueCon')
```

## To-Do List
- [X] Create the decorator to handle events.
- [ ] Create a CLI to run projects.
- [ ] Create filter to request only the marked events.
- [ ] Create the Documentation.