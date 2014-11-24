import subprocess
import time

from fabric.api import local
from fabric.context_managers import shell_env


def initial_setup():
    """ Initial database creation and fixtures creation """
    with shell_env(DJANGO_CONFIGURATION='Production'):
        local('python pillbox-engine/manage.py syncdb')
        local('python pillbox-engine/manage.py migrate')
        local('python pillbox-engine/manage.py collectstatic')

        # Load SPL sources
        local('python pillbox-engine/manage.py syncspl all')


def push():
    """ Push master branch to github """
    local('git push origin master')


def pull():
    """ Pull master branch from github """
    local('git pull origin master')


def serve():
    """ Run the server in production mode """
    print 'Launching Pillbox Engine ...'
    foreman = subprocess.Popen(['foreman', 'start'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Wait for 3 seconds to ensure the process is launched
    time.sleep(3)
    local('open "http://localhost:5000"')
    print 'To exit Pillbox Engine use Control + C'
    print foreman.stdout.read()


def test():
    """ Run the server in development mode """
    local('python pillbox-engine/manage.py runserver')


def migrate():
    """ Migrate database in development mode """
    local('python pillbox-engine/manage.py makemigrations')
    local('python pillbox-engine/manage.py migrate')


def collect():
    """ Collect Static Files """
    with shell_env(DJANGO_CONFIGURATION='Production'):
        local('python pillbox-engine/manage.py collectstatic')


def spl(choice=None):
    """Sync SPL Data. Choices are products | pills | all"""
    if choice is None:
        choice = 'all'

    with shell_env(DJANGO_CONFIGURATION='Production'):
        if choice in ['products', 'pills', 'all']:
            local('python pillbox-engine/manage syncspl %s' % choice)
        else:
            print 'wrong choice'
