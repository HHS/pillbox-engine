Pillbox Engine
==============================

This is the new Pillbox Engine, A local web-based application for downloading and management of DailyMed SPL Data.

Update
------

If PillBox Engine is already installed, run this to update::

    $ fab update


Setup
-----------------------

Mac OSX Requirements
^^^^^^^^

If you use Mac OSX
We assume you have the following installed:

* pip
* virtualenv

If you don't, you can follow these steps to setup pip and virtualenv::

    $ curl https://bootstrap.pypa.io/ez_setup.py -o - | sudo python
    $ sudo easy_install python-pip
    $ sudo easy_install virtualenv

To start a virtualenv simply run::

    $ virtualenv --no-site-packages name_of_the_environment
    $ source name_of_the_environment/bin/activate

To deactivate run::

    $ deactivate

You should also consider using a database engine such Postgres or MySQL with this application. Pillbox Engine supports Sqlite3, Postgres and MySQL, however, we highly recommend using Postgres. This program is primarily tested with Postgres.

To setup Postgres on MacOSX, download `postgres.app<http://postgresapp.com>`_.

If you downloaded and installed the Postgres from the link provided above, you should make sure postgres is probably known to your system path. To achieve this, follow these steps::

    $ PATH="/Applications/Postgres.app/Contents/Versions/9.3/bin:$PATH"
    $ export PGHOST=localhost

For best result, add above command to your .bash_profile.

Ubuntu 14 Requirements
^^^^^^^^^

If you use Ubuntu 14, to prepare the system run::

    $ sudo apt-get update
    $ sudo apt-get install ruby
    $ sudo apt-get install python-pip libxml2-dev libxslt-dev python-dev lib32z1-dev git

To install Postgres, run::

    $  sudo apt-get install postgresql


Installation
^^^^^^^^^

Make sure to create and activate a virtualenv_, then open a terminal at the project root and install the requirements for local development::

    $ git clone https://github.com/developmentseed/pillbox-engine.git
    $ cd pillbox-engine
    $ pip install -r requirements.txt

.. _virtualenv: http://docs.python-guide.org/en/latest/dev/virtualenvs/

Database Setup
^^^^^^^^^^^^^^

If you use Postgres or MySql, make sure the database engine is started.

You also need to setup a database for pillbox. For postgres, run these commands::

    $ createdb -h localhost pillbox_db

Replace pillbox_db with your preferred name. If you use Postgres.app, your username will be your system username and the password is blank.

To setup the intital database, run this command::

    $ fab initial_setup

Launch
^^^^^^^^^^^^^^

To run the application run::

    $ fab serve

The admin panel is accessible at: http://localhost:5000/

The default username and password is pillbox/pillbox.

The admin username and password is admin/admin

Pillbox Images
-------------------------

You can download the latest version of Pillbox Images `from here<http://pillbox.nlm.nih.gov/developer.html#images>`_.

You should unzip and copy the content of this image zip file to ``pillbox-engine/media/pillbox/``


Pillbox Existing Data
-------------------------

Download the latest master data `from here<http://pillbox.nlm.nih.gov/developer.html#data>`_. Then use the Graphic Interface to import the data to the system.

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
