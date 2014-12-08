from __future__ import division
import datetime

from django.utils import timezone

from celery.result import AsyncResult
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import list_route
from spl import tasks
from spl.models import Task, SetInfo, ProductData, Source


class DownloadViewSet(viewsets.ViewSet):
    """ Download SPL Data """

    def list(self, request):
        return Response({'message': 'empty'}, status=status.HTTP_200_OK)

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

            # Start a new task
            task = Task()
            task.name = 'Download/Unzip'
            task.download_type = source.title
            task.time_started = timezone.now()
            task.save()

            celery_task = tasks.download_unzip.delay(task.id, source.title, source.files)

            task.task_id = celery_task.task_id
            task.save()

            return Response({'message': 'New download started',
                             'status': task.status,
                             'meta': task.meta,
                             'task_id': task.task_id,
                             'pid': task.pid},
                            status=status.HTTP_200_OK)


class SyncSpl(viewsets.ViewSet):
    """
    Run SPL Sync
    """

    def list(self, request):
        return Response({'message': 'It\'s working'})

    @list_route()
    def pills(self, request):
        return self.sync('pills')

    @list_route()
    def products(self, request):
        return self.sync('products')

    @list_route()
    def all(self, request):
        return self.sync('all')

    def sync(self, action):

        model_map = {
            'pills': ProductData,
            'products': SetInfo
        }

        try:
            job = Task.objects.filter(time_ended__exact=None)[0]
        except IndexError:
            job = None

        processed = 0

        if action in model_map.keys():
            if job:
                if job.name != action:
                    return Response({'message': 'Another task is running'}, status=status.HTTP_406_NOT_ACCEPTABLE)

                task = AsyncResult(job.task_id)
                meta = task.info
                if meta:
                    try:
                        processed = int(meta['added']) + int(meta['updated'])
                    except TypeError:
                        pass

                total = model_map[action].objects.all().count()
                percent = round((processed / total) * 100, 2)

                if percent > 100:
                    percent = 99

                output = {
                    'message': 'Syncing',
                    'status': task.state,
                    'task_id': task.task_id,
                    'meta': meta,
                    'total_processed': processed,
                    'total': total,
                    'percent': percent,
                    'action': action
                }
            else:
                jobs = Task.objects.filter(name=action,
                                           time_ended__gte=datetime.datetime.today()-datetime.timedelta(days=1))
                if jobs:
                    output = {
                        'message': 'Sync Done. You can run the sync again in 24 hours.'
                    }
                else:
                    job = Task()
                    job.name = action
                    job.status = 'PENDING'
                    job.save()
                    sync = tasks.sync.delay(action, job.id)
                    output = {
                        'message': 'Process Started',
                        'task_id': sync.task_id,
                        'status': sync.state
                    }

            return Response(output, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Action not supported'}, status=status.HTTP_406_NOT_ACCEPTABLE)

