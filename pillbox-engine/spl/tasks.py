from __future__ import absolute_import, division
import time
import os
import sys
from django.utils import timezone
from zipfile import BadZipfile
from _celery import app
from spl.sync.controller import Controller
from spl.download import DownloadAndUnzip
from spl.models import Task


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
def download_unzip(self, task_id, download_type, files):

    ## SET START STATUS
    start = time.time()
    task = Task.objects.get(pk=task_id)
    task.status = 'STARTED'
    task.pid = os.getpid()
    task.save()

    # RUN THE TASK
    try:
        dl = DownloadAndUnzip(task.id, download_type, files)
        if dl.run():

            # SET END STATUS ON SUCCESS
            end = time.time()
            spent = end - start

            task.status = 'SUCCESS'
            task.duration = spent
            task.time_ended = timezone.now()
            task.is_active = False
            task.save()
    except BadZipfile:
        end = time.time()
        spent = end - start
        task.status = 'FAILED'
        task.is_active = False
        task.time_ended = timezone.now()
        task.duration = spent
        task.traceback = sys.exc_info()
        task.save()
