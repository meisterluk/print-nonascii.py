#!/usr/bin/env python

"""
    print-nonascii
    ~~~~~~~~~~~~~~

    Print any non-ASCII characters of a file.

    (C) Lukas Prokop, 2015, Public Domain
"""

import os.path

from setuptools import setup

def readfile(fname):
    with open(os.path.join(os.path.dirname(__file__), fname)) as fp:
        return fp.read()

setup(
    name='printnonascii',
    version='0.0.1',
    url='http://lukas-prokop.at/proj/print-nonascii/',
    license='Public Domain',
    author='Lukas Prokop',
    author_email='admin@lukas-prokop.at',
    description='Print all nonascii characters of a file in human-readable form',
    long_description=readfile('README.rst'),
    packages=['printnonascii'],
    platforms='any',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Quality Assurance',
        'Topic :: Software Development :: Testing',
        'Topic :: Software Development :: Debuggers'
    ],
    entry_points = {
        "console_scripts": ['print-nonascii.py = printnonascii.scripts:main']
    }
)

