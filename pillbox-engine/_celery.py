from __future__ import absolute_import

import os
import sys

from celery import Celery

from django.conf import settings

# Because of the special way the cookiecutter template is setup,
# we have to add the root app to the python path
BASE_DIR = os.path.dirname(os.path.dirname(__file__)) + '/pillbox-engine'
sys.path.append(BASE_DIR)

# set the default Django settings module for the 'celery' program.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config")
os.environ.setdefault("DJANGO_CONFIGURATION", "Production")

from configurations import importer
importer.install()

app = Celery('pillbox-engine')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
    # return 'Request: {0!r}'.format(self.request)
