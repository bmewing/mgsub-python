#!/usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.core import setup

setup(
    name='mgsub',
    version='0.0.1',
    url='https://github.com/bmewing/mgsub-python',
    download_url='https://github.com/bmewing/mgsub-python.git',
    author='Peter Yasi',
    packages=['mgsub'],
    module=['mgsub'],
    description='A safe, multiple, simultaneous string substitution function',
    long_description=open('README.md', 'r').read(),
    keywords=['strings', 'substitution'],
)