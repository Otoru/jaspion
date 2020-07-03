***********
Get Started
***********

Looking forward to getting started? If you already have Jaspion installed, let's see how to make a minimal application.

Show me the code
================

Every Jaspion application will start with a simple structure like this:

.. code-block:: python
    :linenos:

    from jaspion import Jaspion

    app = Jaspion(host='127.0.0.1', port=8021, password='ClueCon')

    @app.handle('HEARTBEAT')
    def heartbeat(event):
        print(event)

    if __name__ == '__main__':
        app.run()

Understanding Jaspion
=====================

Let's better understand the code:

- To create a jashpion instance, four arguments are required: name, host, port, and password.
    - name: Positional argument that serves to name the instance in its representation.
    - host: The FreeSwitch address.
    - port: The FreeSwitch connection port.
    - password: Password used for ESL authentication.
 - To add functions as handlers for specific events we must use the decorator ``handle``. it receives a string with the name of the event as an argument.
 - Below the decorator we must have a function that receives a single argument (an event) this argument will be a dictionary that will have the same `key: value` scheme of the selected event.
 - The function can apply the logic you want to in the package, such as expand, save to a database, or whatever you prefer.
 - Finally, we can call the `run` method so that app starts receiving the events.

Choosing Events
===============

You can work on any event that FreeSwitch generates via ESL. Just be aware of the fact that if the searched event is a **CUSTOM**, you must enter your **subclass** name. The `FreeSwitch documentation`_ has more information about events.

.. _FreeSwitch documentation: https://freeswitch.org/confluence/display/FREESWITCH/Event+List
