from __future__ import division

from celery.result import AsyncResult
from rest_framework import viewsets, status
from rest_framework.response import Response
from pillbox.models import Import, PillBoxData


class ImportStatus(viewsets.ViewSet):
    """
    Checks status of import tasks
    """

    def list(self, request):
        import_objs = Import.objects.filter(completed=False)
        if import_objs:
            for import_obj in import_objs:
                task = AsyncResult(import_obj.task_id)
                meta = task.info
                if meta:
                    try:
                        processed = int(meta['added']) + int(meta['updated'])
                    except TypeError:
                        pass

                total = PillBoxData.objects.all().count()
                percent = round((processed / total) * 100, 2)

                output = {
                    'message': 'Importing',
                    'status': task.state,
                    'task_id': task.task_id,
                    'meta': meta,
                    'total_processed': processed,
                    'total': total,
                    'percent': percent
                }
        else:
            output = {
                'message': 'No Pending Import Tasks'
            }

        return Response(output, status=status.HTTP_200_OK)
