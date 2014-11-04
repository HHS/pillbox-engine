from fabric.api import local


def push():
    local('git push origin master')


def pull():
    local('git pull origin master')


def serve():
    local('python manage.py runserver')


def migrate():
    local('python manage.py makemigrations')
    local('python manage.py migrate')
