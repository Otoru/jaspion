# Package Tools

Here we will list some methods that may be useful during the development of a Jaspion project.

## jaspion.utils.haskey(key)

This method is a decorator.
When added to a function that will be used as a handler for FreeSwitch events, it ensures that this function will only process events that have the entered **key**.

### Arguments:
- key: string (required)

## jaspion.utils.filtrate(key, value)

This method is a decorator.
When added to a function that will be used as a handler for FreeSwitch events, it ensures that this function will only process events that have the entered **key** and that have the **value** associated with that key.

### Arguments:
- key: string (required)
- value: string (required)
