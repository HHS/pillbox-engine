from __future__ import division
from django.utils import timezone
from rest_framework import viewsets, status
from rest_framework.response import Response

from pillbox.tasks import transfer_task
from spl.models import Task


class ImportStatus(viewsets.ViewSet):

    """
    Checks status of import tasks
    """

    def list(self, request):

        try:
            task = Task.objects.filter(is_active=True, name='import')[:1].get()
            output = {
                'message': 'Importing',
                'meta': task.meta,
                'status': task.status,
                'task_id': task.task_id,
                'pid': task.pid
            }
        except Task.DoesNotExist:
            output = {
                'message': 'No Pending Import Tasks'
            }

        return Response(output, status=status.HTTP_200_OK)


class Transfer(viewsets.ViewSet):

    """
    Transfer data from SPL to Pillbox
    """

    def list(self, request):

        try:
            task = Task.objects.filter(is_active=True)[:1].get()

            if task.name == 'transfer':

                output = {
                    'message': 'Transfering',
                    'status': task.status,
                    'task_id': task.task_id,
                    'meta': task.meta,
                    'pid': task.pid,
                }

                return Response(output, status=status.HTTP_200_OK)

            else:
                return Response({'message': 'There is another task running.'},
                                status=status.HTTP_200_OK)

        except Task.DoesNotExist:
            task = Task()
            task.name = 'transfer'
            task.status = 'PENDING'
            task.time_started = timezone.now()
            task.save()

            t = transfer_task.delay(task.id)

            task.task_id = t.task_id
            task.save()

            return Response({
                'message': 'Transfer started',
                'status': task.status,
                'meta': task.meta,
                'task_id': task.task_id,
                'pid': task.pid},
                status=status.HTTP_200_OK
            )
