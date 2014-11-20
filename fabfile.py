from fabric.api import local
from fabric.context_managers import shell_env


def initial_setup():
    with shell_env(DJANGO_CONFIGURATION='Production'):
        local('python pillbox-engine/manage.py syncdb')
        local('python pillbox-engine/manage.py migrate')

        # Load SPL sources
        local('python pillbox-engine/manage.py syncspl all')


def push():
    local('git push origin master')


def pull():
    local('git pull origin master')


def serve():
    with shell_env(DJANGO_CONFIGURATION='Production'):
        local('python pillbox-engine/manage.py runserver')


def test():
    local('python pillbox-engine/manage.py runserver')


def migrate():
    local('python pillbox-engine/manage.py makemigrations')
    local('python pillbox-engine/manage.py migrate')


def collect():
    with shell_env(DJANGO_CONFIGURATION='Production'):
        local('python pillbox-engine/manage.py collectstatic')


