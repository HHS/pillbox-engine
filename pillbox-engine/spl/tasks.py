from __future__ import absolute_import, division
import time
import os
import sys

from django.utils import timezone
from django.conf import settings

from zipfile import BadZipfile
from ftputil.error import TemporaryError

from _celery import app
from spl.sync.controller import Controller
from spl.download import DownloadAndUnzip
from spl.models import Task, Source


@app.task()
def add(x, y):
    print '%s' % (x + y)


@app.task(bind=True, ignore_result=True)
def sync(self, action, task_id):

    arguments = ['products', 'pills', 'all']

    if action in arguments:
        controller = Controller(task_id=task_id)
        controller.sync(action)


@app.task(bind=True, ignore_result=True)
def download_unzip(self, task_id, source_id):

    source = Source.objects.get(pk=source_id)

    # SET START STATUS
    start = time.time()
    task = Task.objects.get(pk=task_id)
    task.status = 'STARTED'
    task.pid = os.getpid()
    task.meta = {}
    task.save()

    # RUN THE TASK
    try:
        dl = DownloadAndUnzip(task.id, source.title, source.files,
                              source.host, source.path)
        if dl.run():

            # Calculate folder size for zip and unzip files
            source.zip_size = folder_size(settings.DOWNLOAD_PATH + '/' + source.title)
            source.unzip_size = folder_size(settings.SOURCE_PATH + '/' + source.title)
            source.save()

            # SET END STATUS ON SUCCESS
            end = time.time()
            spent = end - start

            task.status = 'SUCCESS'
            task.duration = spent
            task.time_ended = timezone.now()
            task.is_active = False
            task.save()

            source.last_downloaded = task.time_ended
            source.save()

    except BadZipfile:
        record_error(task, start, sys.exc_info())
        return
    except TemporaryError as exc:
        # Retry again if the connection timeout
        raise self.retry(exc=exc)


def folder_size(path):
    """ Returns the folder size in Bytes of the give path """
    total = 0
    for dirpath, folders, filenames in os.walk(path):
        for filename in filenames:
            _file = os.path.join(dirpath, filename)
            total += os.path.getsize(_file)
            total = total
    return total


def record_error(task, start, traceback, status='FAILED'):
    """ Updates the task model with a FAIL status
    @param

    """
    end = time.time()
    spent = end - start
    task.status = status
    task.is_active = False
    task.time_ended = timezone.now()
    task.duration = spent
    task.traceback = traceback
    task.save()

