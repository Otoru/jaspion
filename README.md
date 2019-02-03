## What is Jaspion?

Jaspion is a python library designed to process events received from FreeSwitch via ESL.

## What is FreeSwitch?

FreeSWITCH is a free and open-source application server for real-time communication, WebRTC, telecommunications, video and Voice over Internet Protocol (VoIP). Multiplatform, it runs on Linux, Windows, macOS and FreeBSD. It is used to build PBX systems, IVR services, videoconferencing with chat and screen sharing, wholesale least-cost routing, Session Border Controller (SBC) and embedded communication appliances. It has full support for encryption, ZRTP, DTLS, SIPS. It can act as a gateway between PSTN, SIP, WebRTC, and many other communication protocols. Its core library, libfreeswitch, can be embedded into other projects. It is licensed under the Mozilla Public License (MPL), a free software license. [wikipedia](https://en.wikipedia.org/wiki/FreeSWITCH)

## What is ESL?

ESL is a way to communicate with FreeSwitch. See more details [here](https://freeswitch.org/confluence/display/FREESWITCH/Event+Socket+Library).

## Docs

The project documentation is in [jaspion.readthedocs.io](https://jaspion.readthedocs.io/)

## How to contribute?

If you want to contribute to the project, you may be taking a look at the list below. Any help is welcome.

### To-Do List
- [X] Create the decorator to handle events.
- [X] Create filter to request only the marked events.
- [ ] Allow handlers to send commands to freeswitch.
- [X] Create a Class Based Handlers.
- [ ] Create a CLI do create and run projects.
- [ ] Create tests to package.

### Documentations to write
- [X] Installation Instructions.
- [X] Get started.
- [X] AbstractBaseHandler.
- [X] Util decorators.

### Suggested Modules
- Integration with SQLAlchemy
- Integration with MongoDB
- Integration with WebSockets
- Integration with RabbitMQ

### Infinite Tasks
- Create the Documentation.
- Create a new examples.
- Correct errors in existing docstrings and documentation.
