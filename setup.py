#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This code is distributed under the two-clause BSD license.
# Copyright (c) 2013 Raphaël Barrois

from setuptools import setup
import os
import re

root_dir = os.path.abspath(os.path.dirname(__file__))


def get_version(package_name):
    version_re = re.compile(r"^__version__ = [\"']([\w_.-]+)[\"']$")
    package_components = package_name.split('.')
    path_components = package_components + ['__init__.py']
    with open(os.path.join(root_dir, *path_components)) as f:
        for line in f:
            match = version_re.match(line[:-1])
            if match:
                return match.groups()[0]
    return '0.1.0'


PACKAGE = 'fire'


setup(
    name="fire",
    version='0.1.0',
    author="Raphaël Barrois",
    author_email="raphael.barrois+fire@polytechnique.org",
    description="Advanced remote code execution for Python.",
    license="BSD",
    keywords=['pyro', 'remote', 'tests'],
    url="http://github.com/rbarrois/fire",
    download_url="http://pypi.python.org/pypi/fire/",
    packages=['fire'],
    setup_requires=[
        'setuptools>=0.8',
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    test_suite='tests',
)

