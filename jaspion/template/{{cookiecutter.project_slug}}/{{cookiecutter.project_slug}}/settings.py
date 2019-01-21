import os

# Project Data
name = "{{cookiecutter.project_name}}"
description = "{{cookiecutter.description}}"
slug = "{{cookiecutter.project_slug}}"
version = "{{cookiecutter.version}}"

# Project Directory
here = os.path.dirname(os.path.realpath(__file__))

# FreeSwitch connection data
freeswitch = {
    'host': '{{cookiecutter.freeswitch_host}}',
    'password': '{{cookiecutter.freeswitch_password}}',
    'port': {{cookiecutter.freeswitch_port}}
}
