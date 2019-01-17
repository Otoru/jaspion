# Jaspion

Python module developed to work with ESL (FreeSwitch).

## What is FreeSwitch?

FreeSWITCH is a free and open-source application server for real-time communication, WebRTC, telecommunications, video and Voice over Internet Protocol (VoIP). Multiplatform, it runs on Linux, Windows, macOS and FreeBSD. It is used to build PBX systems, IVR services, videoconferencing with chat and screen sharing, wholesale least-cost routing, Session Border Controller (SBC) and embedded communication appliances. It has full support for encryption, ZRTP, DTLS, SIPS. It can act as a gateway between PSTN, SIP, WebRTC, and many other communication protocols. Its core library, libfreeswitch, can be embedded into other projects. It is licensed under the Mozilla Public License (MPL), a free software license. [wikipedia](https://en.wikipedia.org/wiki/FreeSWITCH)

## What is ESL?

ESL is a way to communicate with FreeSwitch. See more details [here](https://freeswitch.org/confluence/display/FREESWITCH/Event+Socket+Library).

## Installation Instructions

You can install the package in two ways:
```bash
$ pip install jaspion                           # From pypi
$ pip install https://github.com/Otoru/jaspion  # From source code
```

## Where is the documentation?

Click [here](https://otoru.github.io/jaspion/) to view the complete documentation.

## Example
This is a list with example codes:

- [How to monitoring an extension?][1]

[1]:https://github.com/Otoru/jaspion/blob/master/examples/monitoring_an_extension.py

## To-Do List
- [X] Create the decorator to handle events.
- [ ] Create a CLI to run projects.
- [X] Create filter to request only the marked events.
- [ ] Create the Documentation.
- [ ] Create Class to 'lazzy append' handlers.
- [ ] Write new examples.
- [ ] Create a WebSocket server to send events after handle.
