from __future__ import division
import datetime
from django.utils import timezone
from rest_framework import viewsets, status
from rest_framework.response import Response

from pillbox.tasks import transfer_task
from spl.models import Task
from pillbox.models import Export


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


class ExportStatus(viewsets.ViewSet):

    """
    Checks status of export tasks
    """

    def list(self, request):

        try:
            task = Task.objects.filter(is_active=True, name='export')[:1].get()
            output = {
                'message': 'Exporting',
                'meta': task.meta,
                'status': task.status,
                'task_id': task.task_id,
                'pid': task.pid
            }
        except Task.DoesNotExist:
            try:
                export = Export.objects.filter(completed=True).order_by('-updated_at')[:1].get()

                output = {
                    'message': 'Download: <a id="export-file" href="%s" download>%s</a>' % (export.export_file.url,
                                                                                            export.export_file.name)
                }

            except Export.DoesNotExist:
                output = {
                    'message': 'No Pending Export Tasks'
                }

        return Response(output, status=status.HTTP_200_OK)


class Transfer(viewsets.ViewSet):

    """
    Transfer data from SPL to Pillbox
    """

    def list(self, request):
        return Response({'message': 'empty'}, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):

        actions = ['transfer', 'compare']

        if pk not in actions:
            return Response({'message': 'empty'}, status=status.HTTP_200_OK)

        try:
            task = Task.objects.filter(is_active=True)[:1].get()

            if task.name == pk:

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
            task.name = pk
            task.status = 'PENDING'
            task.time_started = timezone.now()
            task.save()

            t = transfer_task.delay(task.id, pk)

            task.task_id = t.task_id
            task.save()

            return Response({
                'message': '%s started' % pk,
                'status': task.status,
                'meta': task.meta,
                'task_id': task.task_id,
                'pid': task.pid},
                status=status.HTTP_200_OK
            )
