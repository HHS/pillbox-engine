import subprocess
import time

from fabric.api import local
from fabric.context_managers import shell_env
from fabric.operations import prompt


def initial_setup():
    """ Initial database creation and fixtures creation """
    with shell_env(DJANGO_CONFIGURATION='Production'):
        try:
            choice = int(prompt('What database engine you plan to use? \n' +
                                'If you choose, Mysql or Postgres, you have to make sure they are' +
                                ' installed on your computer before proceeding further \n' +
                                '(1) Sqlite3 \n' +
                                '(2) MySql \n' +
                                '(3) Postgres \n' +
                                ': '))

            if choice == 1:
                _sync_db()
            elif choice == 2:

                response = _db_questions('3306')

                with shell_env(DATABASE_URL=response):
                    _install_mysql()
                    _sync_db()
            elif choice == 3:
                pass

        except ValueError:
            print 'Try again! You should enter a number.'


        # local('export DATABASE_URL=mysql://root:@localhost:3306/pillbox_new')

        # local('python pillbox-engine/manage.py collectstatic')

        # # Load SPL sources
        # local('python pillbox-engine/manage.py syncspl all')


def push():
    """ Push master branch to github """
    local('git push origin master')


def pull():
    """ Pull master branch from github """
    local('git pull origin master')


def serve():
    """ Run the server in production mode """
    print 'Launching Pillbox Engine ...'
    foreman = subprocess.Popen(['honcho', 'start'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Wait for 3 seconds to ensure the process is launched
    time.sleep(3)
    local('open "http://localhost:5000"')
    print 'To exit Pillbox Engine use Control + C'
    print foreman.stdout.read()


def test():
    """ Run the server in development mode """
    local('python pillbox-engine/manage.py runserver')


def shell():
    local('python pillbox-engine/manage.py shell')


def migrate():
    """ Migrate database in development mode """
    local('python pillbox-engine/manage.py makemigrations')
    local('python pillbox-engine/manage.py migrate')


def collect():
    """ Collect Static Files """
    with shell_env(DJANGO_CONFIGURATION='Production'):
        local('python pillbox-engine/manage.py collectstatic')


def update():
    """ Fetch the latest updates from the repo"""
    local('git pull origin master')
    local('pip install -r requirements.txt')
    local('python pillbox-engine/manage.py migrate')


def spl(choice=None):
    """Sync SPL Data. Choices are products | pills | all"""
    if choice is None:
        choice = 'all'

    with shell_env(DJANGO_CONFIGURATION='Production'):
        if choice in ['products', 'pills', 'all']:
            local('python pillbox-engine/manage.py syncspl %s' % choice)
        else:
            print 'wrong choice'


def _install_mysql():
    local('pip install mysql-connector-python --allow-external mysql-connector-python')


def _install_postgres():
    local('')


def _db_questions(port):

    output = {}

    output['username'] = prompt('Database Username: ')
    output['password'] = prompt('Database Password: ')
    output['host'] = prompt('The host (localhost): ')
    output['port'] = prompt('The post (%s): ' % port)
    output['db_name'] = prompt('Database Name: ')

    output['host'] = output['host'] if output['host'] else 'localhost'
    output['port'] = output['port'] if output['port'] else port

    db_url = 'mysql-connector://%s:%s@%s:%s/%s' % (output['username'],
                                                   output['password'],
                                                   output['host'],
                                                   output['port'],
                                                   output['db_name'])

    local('echo "DATABASE_URL=%s" > .env' % db_url)

    return db_url


def _sync_db():
    local('python pillbox-engine/manage.py syncdb')
    local('python pillbox-engine/manage.py migrate')
    local('python pillbox-engine/manage.py loaddata spl_sources')
