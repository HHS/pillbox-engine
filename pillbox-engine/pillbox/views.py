from __future__ import division

from rest_framework import viewsets, status
from rest_framework.response import Response

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
