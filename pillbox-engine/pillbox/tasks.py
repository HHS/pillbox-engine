from __future__ import absolute_import
import os
import time
from django.utils import timezone
from _celery import app

from pillbox.models import Import
from pillbox.importer import importer
from spl.models import Task
from compare.sync import compare


@app.task(bind=True, ignore_result=True)
def import_task(self, csv_file, task_id, download_id):
    start = time.time()
    task = Task.objects.get(pk=task_id)
    task.status = 'STARTED'
    task.pid = os.getpid()
    task.save()

    importer(csv_file, task.id)

    end = time.time()
    spent = end - start

    task = Task.objects.get(pk=task_id)
    task.status = 'SUCCESS'
    task.duration = round(spent, 2)
    task.time_ended = timezone.now()
    task.is_active = False
    task.save()

    imprt = Import.objects.get(pk=download_id)
    imprt.status = task.status
    imprt.duration = task.duration
    imprt.completed = True
    imprt.added = task.meta['added']
    imprt.updated = task.meta['updated']
    imprt.save()


@app.task(bind=True, ignore_result=True)
def transfer_task(self, task_id):
    start = time.time()
    task = Task.objects.get(pk=task_id)
    task.status = 'STARTED'
    task.pid = os.getpid()
    task.save()

    compare(task.id)

    end = time.time()
    spent = end - start

    task = Task.objects.get(pk=task_id)
    task.status = 'SUCCESS'
    task.duration = round(spent, 2)
    task.time_ended = timezone.now()
    task.is_active = False
    task.save()
