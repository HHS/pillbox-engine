## Mac OSX requirements

If you use Mac OSX We assume you have the following installed:

- pip
- virtualenv

If you don't have these requirements, you can follow below steps to setup pip and virtualenv:

    $ curl https://bootstrap.pypa.io/ez_setup.py -o - | sudo python
    $ sudo easy_install pip
    $ sudo easy_install virtualenv

To start a new virtualenv run:

    $ virtualenv --no-site-packages name_of_the_environment
    $ source name_of_the_environment/bin/activate

To deactivate run:

    $ deactivate


You should also consider using a database engine such Postgres or MySQL with this application. Pillbox Engine supports Sqlite3, Postgres and MySQL, however, we highly recommend using Postgres. This program is primarily tested with Postgres.

To setup Postgres on MacOSX, download [postgres app](http://postgresapp.com/).

If you downloaded and installed the Postgres from the link provided above, you should make sure postgres is known to your system path. To achieve this, follow these steps:

    $ PATH="/Applications/Postgres.app/Contents/Versions/9.3/bin:$PATH"
    $ export PGHOST=localhost

For best result, add above command to your `.bash_profile`.

## Ubuntu 14 Requirements

If using Ubuntu 14, to prepare the system run:

    $ sudo apt-get update
    $ sudo apt-get install ruby
    $ sudo apt-get install python-pip libxml2-dev libxslt-dev python-dev lib32z1-dev git

To install Postgres, run:

    $  sudo apt-get install postgresql


## Installation

Make sure to create and activate a virtualenv, then open a terminal at the project root and install the requirements for local development:

    $ git clone https://github.com/developmentseed/pillbox-engine.git
    $ cd pillbox-engine
    $ pip install -r requirements.txt

## Database Setup

If you use Postgres or MySql, make sure the database engine is started.

You also need to setup a database for pillbox. For postgres, run these commands:

    $ createdb -h localhost pillbox_db

Replace pillbox_db with your preferred name. If you use Postgres.app, your username will be your system username and the password is blank.

To setup the intital database, run this command:

    $ fab initial_setup

And follow the instructions.

During the setup you have answer a few questions including what database backend should be used. Choices are Sqlite3, MySQl and Postgres.

If you choose MySQL or Postgres, you should also provide the username and password, the address, port and the name of the database.

Address and port are set by default, so you can just press enter and skip them.

## Launch

To run the application run:

    $ fab serve

The admin panel is accessible at: http://localhost:5000/

type | username | password
------------ | ------------- | ------------
default | pillbox | pillbox
admin | admin | admin



