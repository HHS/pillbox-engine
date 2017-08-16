from __future__ import division
import datetime

from django.utils import timezone

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import list_route
from spl import tasks
from spl.models import Task, Source


class DownloadViewSet(viewsets.ViewSet):
    """ Download SPL Data """

    def list(self, request):
        try:
            ## Check if there are any active tasks
            task = Task.objects.filter(is_active=True)[:1].get()
            return Response({
                'meta': task.meta,
                'status': task.status,
                'task_id': task.task_id,
                'pid': task.pid
            }, status=status.HTTP_200_OK)

        except Task.DoesNotExist:
            return Response({'message': 'No Active Tasks'}, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        source = Source.objects.get(pk=pk)

        try:
            ## Check if there are any active tasks
            task = Task.objects.filter(is_active=True)[:1].get()

            ## Check if it is download task
            if task.download_type == source.title:
                return Response({'message': 'Downloading',
                                 'meta': task.meta,
                                 'status': task.status,
                                 'task_id': task.task_id,
                                 'pid': task.pid},
                                status=status.HTTP_200_OK)
            else:
                return Response({'message': 'There is another task running.'},
                                status=status.HTTP_200_OK)
        except Task.DoesNotExist:

            try:
                task = Task.objects.filter(
                    download_type=source.title,
                    status='SUCCESS',
                    time_ended__gte=datetime.datetime.today()-datetime.timedelta(days=1)
                )[:1].get()

                return Response({'message': 'Downloaded! Wait 24 hours to redownload the source!'},
                                status=status.HTTP_200_OK)

            except Task.DoesNotExist:

                # Start a new task
                task = Task()
                task.status = 'PENDING'
                task.name = 'download'
                task.download_type = source.title
                task.time_started = timezone.now()
                task.save()

                celery_task = tasks.download_unzip.delay(task.id, source.id)

                task.task_id = celery_task.task_id
                task.save()

                return Response({'message': 'New download started',
                                 'status': task.status,
                                 'meta': task.meta,
                                 'task_id': task.task_id,
                                 'pid': task.pid},
                                status=status.HTTP_200_OK)


class Status(viewsets.ViewSet):

    def list(self, request):
        try:
            ## Check if there are any active tasks
            task = Task.objects.filter(is_active=True)[:1].get()
            return Response({
                'meta': task.meta,
                'status': task.status,
                'task_id': task.task_id,
                'pid': task.pid
            }, status=status.HTTP_200_OK)

        except Task.DoesNotExist:
            return Response({'message': 'No Active Tasks'}, status=status.HTTP_200_OK)


class SyncSpl(viewsets.ViewSet):
    """
    Run SPL Sync
    """

    def list(self, request):
        return Response({'message': 'empty'}, status=status.HTTP_200_OK)

    @list_route()
    def pills(self, request):
        return self.sync('pills')

    @list_route()
    def products(self, request):
        return self.sync('products')

    @list_route()
    def rxnorm(self, request):
        return self.sync('rxnorm')

    def sync(self, action):

        model_map = ['pills', 'products', 'rxnorm']

        if action in model_map:
            try:
                task = Task.objects.filter(is_active=True)[:1].get()

                if task.name == action:
                    output = {
                        'message': 'Syncing',
                        'status': task.status,
                        'task_id': task.task_id,
                        'meta': task.meta,
                        'pid': task.pid,
                        'action': action
                    }

                    return Response(output, status=status.HTTP_200_OK)

                else:
                    return Response({'message': 'There is another task running.'},
                                    status=status.HTTP_200_OK)

            except Task.DoesNotExist:

                try:
                    task = Task.objects.filter(
                        name=action,
                        time_ended__gte=datetime.datetime.today()-datetime.timedelta(days=1)
                    )[:1].get()
                    return Response({'message': 'Sync Done. You can run the sync again in 24 hours.'},
                                    status=status.HTTP_200_OK)

                except Task.DoesNotExist:

                    task = Task()
                    task.name = action
                    task.status = 'PENDING'
                    task.time_started = timezone.now()
                    task.save()

                    if action == 'rxnorm':
                        sync = tasks.rxnorm_task.delay(task.id)
                    else:
                        sync = tasks.sync.delay(action, task.id)

                    task.task_id = sync.task_id
                    task.save()

                    return Response({
                        'message': 'Sync started',
                        'status': task.status,
                        'meta': task.meta,
                        'task_id': task.task_id,
                        'pid': task.pid},
                        status=status.HTTP_200_OK
                    )

        else:
            return Response({'error': 'Action not supported'}, status=status.HTTP_406_NOT_ACCEPTABLE)

