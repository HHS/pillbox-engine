from __future__ import division
import datetime

from celery.result import AsyncResult
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import list_route
from spl import tasks
from spl.models import Task, SetInfo, ProductData


class SyncSpl(viewsets.ViewSet):
    """
    Run SPL Sync
    """
    # def get(self, request, *args, **kwargs):
        # sync = tasks.sync.delay(kwargs['action'])
        # output = {
        #     'status': 'Process Started',
        #     'task_id': sync.task_id
        # }

        # return Response(output, status=status.HTTP_200_OK)

    def list(self, request):
        return Response({'me': 'Yoohoo'})

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
                    'message': 'Syncing...',
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
                                           time_started__gte=datetime.datetime.today()-datetime.timedelta(days=1))
                if jobs:
                    output = {
                        'message': 'Sync Done. You can run the sync again in 24 hours.'
                    }
                else:
                    sync = tasks.sync.delay(action)
                    output = {
                        'message': 'Process Started',
                        'task_id': sync.task_id,
                        'status': sync.state
                    }
                    job = Task()
                    job.task_id = sync.task_id
                    job.name = action
                    job.save()

            return Response(output, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Action not supported'}, status=status.HTTP_406_NOT_ACCEPTABLE)

