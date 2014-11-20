Pillbox Engine
==============================

This is the new Pillbox Engine, A local web-based application for download and management of DailyMed SPL Data.

Getting up and running
----------------------

The steps below will get you up and running with a local development environment. We assume you have the following installed:

* pip
* virtualenv

Production Version Setup
-----------------------

First make sure to create and activate a virtualenv_, then open a terminal at the project root and install the requirements for local development::

    $ pip install -r requirements.txt

.. _virtualenv: http://docs.python-guide.org/en/latest/dev/virtualenvs/

Database Setup
^^^^^^^^^^^^^^

To setup the intital database, run this command::

    $ fab initial_setup

Launch
^^^^^^^^^^^^^^

To run the application run::

    $ fab serve

Sync SPL DailyMed
^^^^^^^^^^^^^^^^^

To sync all xml headers from DailyMed::

    $ python manage.py syncspl products

To sync OSDF information::

    $ python manage.py syncspl pills

To sync everything::

    $ python manage.py syncspl all


Development Version Setup
-------------------------

First make sure to create and activate a virtualenv_, then open a terminal at the project root and install the requirements for local development::

    $ pip install -r requirements/local.txt

.. _virtualenv: http://docs.python-guide.org/en/latest/dev/virtualenvs/

You can now run the usual Django ``runserver`` command::

    $ python pillbox-engine/manage.py runserver

To setup database run::

    $ python manage.py syncdb
    $ python manage.py migrate

.. _issue #39: https://github.com/pydanny/cookiecutter-django/issues/39

**Live reloading and Sass CSS compilation**

If you'd like to take advantage of live reloading and Sass / Compass CSS compilation you can do so with the included Grunt task.

Make sure that nodejs_ is installed. Then in the project root run::

    $ npm install grunt

.. _nodejs: http://nodejs.org/download/

Now you just need::

    $ grunt serve

The base app will now run as it would with the usual ``manage.py runserver`` but with live reloading and Sass compilation enabled.

To get live reloading to work you'll probably need to install an `appropriate browser extension`_

.. _appropriate browser extension: http://feedback.livereload.com/knowledgebase/articles/86242-how-do-i-install-and-use-the-browser-extensions-

It's time to write the code!!!
