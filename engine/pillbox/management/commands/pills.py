from __future__ import print_function

import os
import time
import traceback
from django.utils import timezone
from django.core.management.base import BaseCommand

from pillbox.models import Export
from pillbox.exporter import export
from spl.models import Task
from compare.sync import transfer_new, compare


def export_task(task_id, filename, export_type):
    task = Task.objects.get(pk=task_id)
    task.status = 'STARTED'
    task.pid = os.getpid()
    task.save()

    export_file = export(filename, export_type, task_id)
    task.refresh_from_db()
    task.completed()

    return export_file


def transfer_task(task_id, action):
    task = Task.objects.get(pk=task_id)
    task.status = 'STARTED'
    task.pid = os.getpid()
    task.save()

    if action == 'compare':
        print('this is a compare action')
        compare(task.id)
    elif action == 'transfer':
        print('this is a transfer action')
        transfer_new(task.id)

    task.refresh_from_db()
    task.completed()


class Command(BaseCommand):
    help = 'Execute RxNorm'
    args = '<export> | <compare> | <transfer>'

    def handle(self, *args, **options):

        task = None
        arguments = ['export', 'compare', 'transfer']

        if args and args[0] in arguments:
            try:
                task = Task.create(args[0])
                print('Starting the %s' % args[0])

                if args[0] == 'transfer':
                    # create the task for import
                    transfer_task(task.id, 'transfer')

                elif args[0] == 'compare':
                    transfer_task(task.id, 'compare')

                elif args[0] == 'export':
                    export = Export()
                    export.file_type = 'json'
                    export.file_name = 'pillbox_export.json'
                    export.task_id = task.id
                    export.save()

                    try:
                        export_file = export_task(task.id, export.file_name, export.file_type)
                        task.refresh_from_db()
                        export.export_file = export_file
                    except Exception as e:
                        task.refresh_from_db()
                        task.cancelled('failed', e)
                        traceback.print_exc()

                    task.refresh_from_db()
                    export.status = task.status
                    export.duration = task.duration
                    export.completed = True
                    export.save()


            except KeyboardInterrupt:
                task.refresh_from_db()
                task.cancelled()

