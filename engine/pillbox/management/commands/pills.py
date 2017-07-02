from __future__ import print_function

import os
import time
from django.utils import timezone
from django.core.management.base import BaseCommand

from spl.models import Task
from compare.sync import transfer_new, compare


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

    task = Task.objects.get(pk=task_id)
    task.completed()


class Command(BaseCommand):
    help = 'Execute RxNorm'
    args = '<export> | <compare> | <transfer>'

    def handle(self, *args, **options):

        task = None
        arguments = ['export', 'compare', 'transfer']

        if args and args[0] in arguments:
            try:
                if args[0] == 'transfer':
                    # create the task for import
                    print('Starting the transfer')
                    task = Task.create('transfer')
                    transfer_task(task.id, 'transfer')

                elif args[0] == 'compare':
                    print('Staring the compare')
                    task = Task.create('compare')
                    transfer_task(task.id, 'compare')

            except KeyboardInterrupt:
                task.refresh_from_db()
                task.cancelled()

