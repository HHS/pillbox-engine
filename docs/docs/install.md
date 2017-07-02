
There are two ways to install and run the Pillbox Engine: (1) Using Docker (2) Direct Installation.

We highly recommend using docker for local or web installation of the Pillbox Engine. We have builta special image of the docker engine that has all the requirements for running the engine, which makes the installation and use of the Engine much easier.

## Docker

### Get Docker

Make sure you have the latest version of [docker](https://docs.docker.com/engine/installation/) and [docker-compose](https://docs.docker.com/compose/install/) running on your computer.

To install docker on MacOSX, you can simply, you can simpliy downoad the latest version of docker from [here](https://docs.docker.com/docker-for-mac/install/) and install it.

Docker-compose installation is pretty simple for all platforms as long as you follow instructions [here](https://docs.docker.com/compose/install/).

### Run Engine in Docker

#### First Time

First we have to create the database and the necessary tables:

    $ mkdir -p config/db/postgres
    $ docker-compose run --rm migrate

**Note:** If the above command failed, run it again.

Then create a superuser:

    $ docker-compose run --rm superuser

Then load the preconfigured data:

    $ docker-compose run --rm loaddata

Then copy the staticfiles to the correct folders:

    $ docker-compose run --rm collectstatic

#### All Other Times

To run the Engine locally just execute this command:

    $ docker-compose up web

The site will be accessible at `http://localhost:5000`

To stop the local version press `Ctrl+C`.

## Direct

### Requirement

- RabbitMQ server

### Installation

    $ pip install -r requirements.txt
    $ python manage.py migrate
    $ python manage.py loadata spl_sources
    $ python manage.py loaddata color_shape
    $ python manage.py createsuperuser
    $ python manage.py collectstatic

## Launch

To run the application run:

    $ honcho start

The admin panel is accessible at: http://localhost:5000/


