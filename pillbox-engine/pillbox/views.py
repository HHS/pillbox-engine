from __future__ import division

from celery.result import AsyncResult
from rest_framework import viewsets, status
from rest_framework.response import Response
from pillbox.models import Import


class ImportStatus(viewsets.ViewSet):
    """
    Checks status of import tasks
    """

    def list(self, request):
        import_objs = Import.objects.filter(completed=False)
        if import_objs:
            for import_obj in import_objs:
                task = AsyncResult(import_obj.task_id)
                output = {
                    'message': 'Importing...',
                    'status': task.state,
                    'task_id': task.task_id,
                    'meta': task.info
                }
        else:
            output = {
                'message': 'No Pending Import Tasks'
            }

        return Response(output, status=status.HTTP_200_OK)
