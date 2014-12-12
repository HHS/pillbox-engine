from __future__ import absolute_import, division
import time
import os
import sys
import Queue

from django.utils import timezone
from django.conf import settings

from zipfile import BadZipfile
from ftputil.error import TemporaryError, FTPOSError

from _celery import app
from spl.sync.controller import Controller
from spl.sync.rxnorm import ThreadXNorm
from spl.download import DownloadAndUnzip
from spl.models import Task, Source, Pill, Product


@app.task(bind=True, ignore_result=True)
def rxnorm_task(self, task_id):
    start = time.time()

    pills = Pill.objects.all().values('id')
    total = pills.count()

    task = Task.objects.get(pk=task_id)
    task.status = 'STARTED'
    task.pid = os.getpid()
    task.meta = {
        'action': 'rxnom sync',
        'processed': 0,
        'total': total,
        'percent': 0
    }
    task.save()

    queue = Queue.Queue()

    print "starting the threads"
    for i in range(20):
        t = ThreadXNorm(queue, task.id)
        t.daemon = True
        t.start()

    print "queuing jobs"
    for pill in pills:
        queue.put(pill['id'])

    queue.join()

    end = time.time()
    spent = end - start

    task = Task.objects.get(pk=task_id)
    task.status = 'SUCCESS'
    task.duration = round(spent, 2)
    task.time_ended = timezone.now()
    task.is_active = False
    task.save()

    return


@app.task(bind=True, ignore_result=True)
def sync(self, action, task_id):
    start = time.time()
    arguments = ['products', 'pills', 'all']

    task = Task.objects.get(pk=task_id)
    task.status = 'STARTED'
    task.pid = os.getpid()
    task.save()

    if action in arguments:
        try:
            controller = Controller(task.id)
            controller.sync(action)
        except Product.DoesNotExist:
            record_error(task, start, sys.exc_info())
            return

    end = time.time()
    spent = end - start

    task = Task.objects.get(pk=task_id)
    task.status = 'SUCCESS'
    task.duration = round(spent, 2)
    task.time_ended = timezone.now()
    task.is_active = False
    task.save()

    return


@app.task(bind=True, ignore_result=True)
def download_unzip(self, task_id, source_id):

    source = Source.objects.get(pk=source_id)

    # SET START STATUS
    start = time.time()
    task = Task.objects.get(pk=task_id)
    task.status = 'STARTED'
    task.pid = os.getpid()
    task.save()

    # RUN THE TASK
    try:
        dl = DownloadAndUnzip(task.id, source.title, source.files,
                              source.host, source.path)
        if dl.run():

            # Calculate folder size for zip and unzip files
            source.zip_size = folder_size_count(settings.DOWNLOAD_PATH + '/' + source.title)['size']
            unzip_count = folder_size_count(settings.SOURCE_PATH + '/' + source.title)
            source.xml_count = unzip_count['count']
            source.unzip_size = unzip_count['size']
            source.save()

            # SET END STATUS ON SUCCESS
            end = time.time()
            spent = end - start

            task = Task.objects.get(pk=task_id)
            task.status = 'SUCCESS'
            task.duration = round(spent, 2)
            task.time_ended = timezone.now()
            task.is_active = False
            task.save()

            source.last_downloaded = task.time_ended
            source.save()

            return

    except BadZipfile:
        record_error(task, start, sys.exc_info())
        return
    except (TemporaryError, FTPOSError) as exc:
        # Retry again if the connection timeout
        raise self.retry(exc=exc)


def folder_size_count(path):
    """ Returns the folder size in Bytes and files count of the give path """
    total = {
        'size': 0,
        'count': 0
    }
    for dirpath, folders, filenames in os.walk(path):
        total['count'] += len(filenames)
        if 'tmp' not in dirpath:
            for filename in filenames:
                _file = os.path.join(dirpath, filename)
                total['size'] += os.path.getsize(_file)

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

