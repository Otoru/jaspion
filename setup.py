from setuptools import setup, find_packages
from os import path


here = path.abspath(path.dirname(__file__))

with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="Jaspion",
    version="0.3.7.0",
    description="FreeSwitch Event Handler based in Flask.",
    include_package_data=True,
    license="MIT",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Otoru/Jaspion",
    author="Vitor Hugo de Oliveira Vargas",
    author_email="vitor.hugo@sippulse.com",
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Information Technology",
        "Intended Audience :: Telecommunications Industry",
        "Natural Language :: Portuguese (Brazilian)",
        "Operating System :: Unix",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Communications :: Telephony",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords="ESL, FreeSwitch",
    packages=find_packages(exclude=["docs", "examples"]),
    install_requires=["greenswitch", "click"],
    extras_require={"dev": ["ipython", "pylint"]},
    entry_points={"console_scripts": ["jaspion=jaspion.cli:main"]},
    zip_safe=False,
    project_urls={
        "Bug Reports": "https://github.com/Otoru/Jaspion/issues",
        "Source Code": "https://github.com/Otoru/Jaspion",
        "Docs": "https://github.com/Otoru/jaspion/wiki",
    },
)
