Welcome to jaspion Docs
=======================

Jaspion is a python library designed to process events received from FreeSwitch
via ESL.

What is FreeSwitch?
-------------------

FreeSWITCH is a free and open-source application server for real-time
communication, WebRTC, telecommunications, video and Voice over Internet
Protocol (VoIP). Multiplatform, it runs on Linux, Windows, macOS and FreeBSD. It
is used to build PBX systems, IVR services, videoconferencing with chat and
screen sharing, wholesale least-cost routing, Session Border Controller (SBC)
and embedded communication appliances. It has full support for encryption, ZRTP,
DTLS, SIPS. It can act as a gateway between PSTN, SIP, WebRTC, and many other
communication protocols. Its core library, libfreeswitch, can be embedded into
other projects. It is licensed under the Mozilla Public License (MPL), a free
software license. `wikipedia`_.

What is ESL?
------------

ESL is a way to communicate with FreeSwitch. See more details `here`_.

How to contribute
-----------------

If you are thinking of contributing in any way to the project, you will be very
welcome.
Whether it's improving existing documentation, suggesting new features or
running existing bugs, it's only by working together that the project will grow.
Do not forget to see our `Contributing Guide`_ and our `Code of Conduct`_ to
always be aligned with the ideas of the project.

.. _here: https://en.wikipedia.org/wiki/FreeSWITCH
.. _wikipedia: https://en.wikipedia.org/wiki/FreeSWITCH
.. _Contributing Guide: https://github.com/Otoru/jaspion/blob/master/CONTRIBUTING.md
.. _Code of Conduct: https://github.com/Otoru/jaspion/blob/master/CODE_OF_CONDUCT.md

.. toctree::
    :caption: Library Documentation
    :maxdepth: 2

    started
    install
    tools
    cli

.. toctree::
    :caption: Examples
    :maxdepth: 2

    examples/monitoring_an_extension
    examples/how_to_use_Sketch
    examples/how_to_use_a_class_handler
    examples/record_registers_in_redis
