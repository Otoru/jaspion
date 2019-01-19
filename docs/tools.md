# Package Tools

Here we will list some methods that may be useful during the development of a Jaspion project.

###### jaspion.utils.haskey(key)
___
This method is a decorator.
When added to a function that will be used as a handler for FreeSwitch events, it ensures that this function will only process events that have the entered **key**.

| Argument | Type | Required | Default |
|:--------:|:----:|:--------:|:-------:|
|    key   |  str |   True   |   N/A   |

##### Example:
```python
...

@app.handle('sofia::register')
@haskey('from-user')
def register(event):
    domain = event['from-host']
    username = event['from-user']
    date = event['Event-Date-Local']

    print(f'[{date}] {username}@{domain} - Registred.')

...
```

###### jaspion.utils.filtrate(key, value)
___
This method is a decorator.
When added to a function that will be used as a handler for FreeSwitch events, it ensures that this function will only process events that have the entered **key** and that have the **value** associated with that key.

| Argument | Type | Required | Default |
|:--------:|:----:|:--------:|:-------:|
|    key   |  str |   True   |   N/A   |
|   value  |  str |   True   |   N/A   |

##### Example:
```python
...

@app.handle('sofia::register')
@filtrate('from-user', '1000')
def register(event):
    domain = event['from-host']
    username = event['from-user']
    date = event['Event-Date-Local']

    print(f'[{date}] {username}@{domain} - Registred.')

...
```
