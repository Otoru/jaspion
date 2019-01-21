import os

# Project Directory
here = os.path.dirname(os.path.realpath(__file__))

# FreeSwitch connection data
freeswitch = {
    'host': '{{cookiecutter.freeswitch_host}}',
    'password': '{{cookiecutter.freeswitch_password}}',
    'port': {{cookiecutter.freeswitch_port}}
}
