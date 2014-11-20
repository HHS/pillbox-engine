#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

pillbox = __import__('pillbox-engine')
version = pillbox.__version__

setup(
    name='pillbox-engine',
    version=version,
    author='',
    author_email='alireza@developmentseed.org',
    packages=[
        'pillbox-engine',
    ],
    include_package_data=True,
    install_requires=[
        'Django>=1.7.1',
    ],
    zip_safe=False,
    scripts=['pillbox-engine/manage.py'],
)
