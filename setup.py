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
    author='scisco',
    author_email='alireza@developmentseed.org',
    packages=[
        'pillbox-engine',
    ],
    include_package_data=True,
    install_requires=[
        'Django==1.7.1',
        'django-configurations==0.8',
        'dj-database-url',
        'django-model-utils==2.2',
        'Pillow==2.6.0',
        'Fabric==1.10.0',
        'celery==3.1.16',
        'django-celery==3.1.16',
        'kombu==3.0.24',
        'lxml==3.4.0',
        'django-crispy-forms==1.4.0',
        'django-reversion==1.8.5',
        'jsonfield==1.0.0'
        'djangorestframework==2.4.4',
        'honcho==0.5.0',
        'ftputil==3.2',
        'requests==2.5.0',
        'simplejson==3.6.5',
        'django-queryset-csv==0.2.10',
        'django-debug-toolbar==1.2.1',
        'coverage==3.7.1',
        'gunicorn==19.1.1',
        'gevent==1.0.1'
    ],
    dependency_links=[
        'git+git://github.com/scisco/dj-database-url.git@master',
    ],
    zip_safe=False,
    scripts=['pillbox-engine/manage.py'],
)
