from setuptools import setup, find_packages
from os import path


here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='Jaspion',
    version='0.1.7',
    description='FreeSwitch Event Handler based in Flask.',
    include_package_data=True,
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/Otoru/Jaspion',
    author='Vitor Hugo de Oliveira Vargas',
    author_email='vitor.hugo@sippulse.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Information Technology',
        'Intended Audience :: Telecommunications Industry',
        'Natural Language :: Portuguese (Brazilian)',
        'Operating System :: Unix',
        'Programming Language :: Python :: 3.7',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: System :: Networking'
    ],
    keywords='ESL, FreeSwitch',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    install_requires=[
        'greenswitch',
    ],
    extras_require={
        'dev': [
            'ipython'
        ],
    },
    # Todo: Create a CLI to run projects.
    #entry_points={
    #    'console_scripts': [
    #        'jaspion=jaspion.cli:main',
    #    ],
    #},
    project_urls={
        'Bug Reports': 'https://github.com/Otoru/Jaspion/issues',
        'Source': 'https://github.com/Otoru/Jaspion',
    }
)
