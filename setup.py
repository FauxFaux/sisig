#!/usr/bin/env python3

import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="sisig",
    version="0.0.1",
    author="Chris West (Faux)",
    author_email="solo-wheel@goeswhere.com",
    license="BSD",
    packages=['sisig', 'tests'],
    long_description=read('README.md'),
    python_requires='>=3',
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
)
