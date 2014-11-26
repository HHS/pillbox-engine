Pillbox Engine
==============================

This is the new Pillbox Engine, A local web-based application for downloading and management of DailyMed SPL Data.

Update
------

If PillBox Engine is already installed, run this to update::

    $ fab update


Production Version Setup
-----------------------

If this is the first time you are running the Pillbox Engine, take steps under `Getting Up and Running <#getting-up-and-running>`_ first.

Make sure to create and activate a virtualenv_, then open a terminal at the project root and install the requirements for local development::

    $ git clone https://github.com/developmentseed/pillbox-engine.git
    $ cd pillbox-engine
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

    $ fab spl products

To sync OSDF information::

    $ fab spl pills

To sync everything::

    $ fab spl all


Getting Up and Running
----------------------

Mac OSX
^^^^^^^^

If you use Mac OSX
We assume you have the following installed:

* pip
* virtualenv

If you don't, you can also follow these steps to setup pip and virtualenv::

    $ curl https://bootstrap.pypa.io/ez_setup.py -o - | sudo python
    $ sudo easy_install python-pip
    $ sudo easy_install virtualenv

To start a virtualenv simply run::

    $ virtualenv --no-site-packages name_of_the_environment
    $ source name_of_the_environment/bin/activate

To deactivate run::

    $ deactivate

Ubuntu 14
^^^^^^^^^

If you use Ubuntu 14, to prepare the system run::

    $ sudo apt-get install ruby
    $ sudo apt-get install python-pip libxml2-dev libxslt-dev python-dev lib32z1-dev git


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
