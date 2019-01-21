from setuptools import setup, find_packages
from os import path


here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='{{cookiecutter.project_name}}',
    version='{{cookiecutter.version}}',
    description='{{cookiecutter.description}}',
    include_package_data=True,
    license='MIT',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='{{cookiecutter.author}}',
    packages=find_packages(),
    install_requires=[
        'jaspion'
    ],
    extras_require={
        'dev': [
            'ipython',
            'flake8'
        ],
    },
    zip_safe=False
)
