**********************
Commnad Line Interface
**********************

Let's imagine a simple project, which is all defined in the file ``vanila.py``.

Let's also imagine that the source code looks like this:

.. code-block:: python
    :linenos:

    from jaspion.sketch import Sketch


    poke = Sketch(__name__)


    @poke.handle('HEARTBEAT')
    def heartbeat(event):
        server = event['FreeSWITCH-Hostname']
        now = event['Event-Date-Local']
        print('[%s] Recived a "heartbeat" from %s' % (now, server))

In cases similar to this (one or more defined and correlated sketches) you can run the project using the Jaspion CLI.

See the example:

.. code-block:: bash
    :linenos:

    export JASPION_APP=vanila:poke
    jaspion runserver
    # Try to connect in esl://127.0.0.1:8021
    # Listner: Sketch(name=vanila, events='HEARTBEAT')
    # [2019-06-04 08:35:12] Recived a "heartbeat" from PABX


Settings
========

To configure the CLI you must use the following environment variables:

+-------------+-------------------------------+-----------+
| Name        | Description                   | Default   |
+-------------+-------------------------------+-----------+
| JASPION_APP | Application to be inspected.  | N/A       |
+-------------+-------------------------------+-----------+
| FSHOST      | Address of freeswitch.        | 127.0.0.1 |
+-------------+-------------------------------+-----------+
| FSPORT      | Port to connect with ESL.     | 8021      |
+-------------+-------------------------------+-----------+
| FSPASSWD    | Password to connect with ESL. | ClueCon   |
+-------------+-------------------------------+-----------+

Special attention should be given to the variable **JASPION_APP**. It identifies the import path of the project master sketch and must be defined using the following syntax:

- ``<package>:<application>``

If application is not defined, its default value will be `app`, that is:

- ``JASPION_APP=vanila``
- ``JASPION_APP=vanila:app``

Are the same thing.

Application Factory
===================

Taking ``vanila:create_app`` as an example, if ``create_app`` is a function, it will be invoked and if its return fosters a ``Sketch``, it will be used.

more about this concept can be seen `here`_.

Example
-------

.. code-block:: python
    :linenos:

    from jaspion.sketch import Sketch


    def create_app():
        poke = Sketch(__name__)
        return poke

Commands
========

The following is a list of available commands and their parameters.

runserver
---------

Command used to start an application.

Parameters
^^^^^^^^^^

+----------+------------------------------+----------+-----------+
| Name     | Description                  | Required | Default   |
+----------+------------------------------+----------+-----------+
| host     | Address of freeswitch        | yes      | $FSHOST   |
+----------+------------------------------+----------+-----------+
| port     | Port to connect with ESL     | yes      | $FSPORT   |
+----------+------------------------------+----------+-----------+
| password | Password to connect with ESL | yes      | $FSPASSWD |
+----------+------------------------------+----------+-----------+

.. _here: https://flask.palletsprojects.com/en/1.1.x/patterns/appfactories/
