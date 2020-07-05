***********************
Monitoring an Extension
***********************

.. code-block:: python
    :linenos:

    from jaspion import Jaspion
    from jaspion.utils import filtrate


    # Freeswitch data to connection
    freeswitch = {"host": "127.0.0.1", "password": "ClueCon", "port": 8021}

    # Instance of Jaspion
    app = Jaspion(**freeswitch)


    # Handler to 'pre_register' event and filter to extension 1000.
    @app.handle("sofia::pre_register")
    @filtrate("from-user", "1000")
    def pre_register(event):
        domain = event["from-host"]
        username = event["from-user"]
        date = event["Event-Date-Local"]

        print("[{}] {}@{} - Tried to register.".format(date, username, domain))


    # Handler to 'register_attempt' event and filter to extension 1000.
    @app.handle("sofia::register")
    @filtrate("from-user", "1000")
    def register(event):
        domain = event["from-host"]
        username = event["from-user"]
        date = event["Event-Date-Local"]

        print("[{}] {}@{} - Register.".format(date, username, domain))


    # Handler to 'register_attempt' event and filter to extension 1000.
    @app.handle("sofia::register_attempt")
    @filtrate("from-user", "1000")
    def register_attempt(event):
        domain = event["from-host"]
        username = event["from-user"]
        date = event["Event-Date-Local"]

        print("[{}] {}@{} - Operation terminated.".format(date, username, domain))


    # Handler to 'register_failure' event and filter to extension 1000.
    @app.handle("sofia::register_failure")
    @filtrate("from-user", "1000")
    def register_failure(event):
        domain = event["from-host"]
        username = event["from-user"]
        date = event["Event-Date-Local"]

        print("[{}] {}@{} - Failed to register.".format(date, username, domain))


    # Handler to 'unregister' and 'expire' event and filter to extension 1000.
    @app.handle("sofia::unregister")
    @app.handle("sofia::expire")
    @filtrate("from-user", "1000")
    def unregister(event):
        domain = event["from-host"]
        username = event["from-user"]
        date = event["Event-Date-Local"]

        print("[{}] {}@{} - Unregistred.".format(date, username, domain))


    if __name__ == "__main__":
        # Start Jaspion
        app.run()
