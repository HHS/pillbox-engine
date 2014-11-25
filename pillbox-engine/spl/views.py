import datetime

from celery.result import AsyncResult
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import detail_route, list_route
from spl import tasks
from spl.models import Task


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

        jobs = Task.objects.filter(name='sync',
                                   time_started__gte=datetime.datetime.today()-datetime.timedelta(days=1))

        if jobs:
            active_jobs = jobs.filter(time_ended__exact=None)
            if active_jobs:
                job = AsyncResult(active_jobs[0].task_id)
                output = {
                    'status': 'There is a sync process already running',
                    'task_id': job.task_id,
                    'meta': job.info
                }
            else:
                output = {
                    'status': 'The process has been executed at least once in the last 24 hours',
                }
        else:
            sync = tasks.sync.delay(action)
            output = {
                'status': 'Process Started',
                'task_id': sync.task_id
            }
            job = Task()
            job.task_id = sync.task_id
            job.name = 'sync'
            job.save()

        return Response(output, status=status.HTTP_200_OK)
