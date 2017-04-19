from __future__ import absolute_import, unicode_literals
import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR + '/engine')

from celery import Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.production')

from django.conf import settings  # noqa

app = Celery('pillbox')
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))

