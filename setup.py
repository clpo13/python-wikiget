"""wikiget2
Simple wget clone for downloading files from Wikimedia sites.
Copyright (C) 2018 Cody Logan; licensed GPLv3+
SPDX-License-Identifier: GPL-3.0-or-later
"""

from setuptools import setup, find_packages
from os import path
from io import open

here = path.abspath(path.dirname(__file__))
with open(path.join(here, "README.md"), "r") as fr:
    long_description = fr.read()

version = {}
with open("wikiget/version.py", "r") as fv:
    exec(fv.read(), version)

setup(
    name="wikiget",
    version=version["__version__"],
    author="Cody Logan",
    author_email="clpo13@gmail.com",
    description="Tool for downloading files from MediaWiki sites",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/clpo13/python-wikiget",
    keywords="mediawiki wikimedia wikipedia",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Topic :: Utilities",
    ],
    install_requires=["future", "mwclient", "pytest-runner", "requests", "tqdm"],
    tests_require=["pytest"],
    project_urls={
        "Bug Reports": "https://github.com/clpo13/python-wikiget/issues",
    },
    entry_points={
        "console_scripts": [
            'wikiget=wikiget.wikiget:main',
        ],
    },
)