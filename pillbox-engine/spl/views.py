from __future__ import division
import datetime

from django.utils import timezone
from django.conf import settings

from celery.result import AsyncResult
from celery import chain
from djcelery_pillbox.models import TaskMeta
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import list_route
from spl import tasks
from spl.models import Task, SetInfo, ProductData, Download


class DownloadViewSet(viewsets.ViewSet):
    """ Download SPL Data """

    def list(self, request):
        download_obj = Download.objects.filter(completed=False).order_by('-started')

        if download_obj:
            obj = download_obj[0]
            current_task = TaskMeta.objects.order_by('-id')[0:1].get()

            progress = 0
            sources = settings.DAILYMED_FILES.keys()
            for source in sources:
                if getattr(obj, source):
                    progress += 1
            if obj.unzipped:
                progress += 1
            percent = round((progress / 6) * 100, 2)

            return Response(self.meta(message='New download started',
                                      id=obj.id,
                                      percent=percent,
                                      meta=current_task.meta,
                                      task_id=current_task.task_id,
                                      status=obj.status), status=status.HTTP_200_OK)
        else:
            download_obj = Download.objects.filter(
                completed=True,
                ended__gte=datetime.datetime.today()-datetime.timedelta(days=1)
            ).order_by('-started')

            if download_obj:
                obj = download_obj[0]
                return Response(self.meta(message='Download and unzip is completed!',
                                          id=obj.id,
                                          task_id=obj.task_id,
                                          duration=obj.duration,
                                          status=obj.status), status=status.HTTP_200_OK)
            else:
                new_download = Download()
                new_download.started = timezone.now()
                new_download.status = 'STARTED'
                new_download.save()

                chained = []
                for key, value in settings.DAILYMED_FILES.iteritems():
                    chained.append(tasks.download_task.si(new_download.id, key, value))

                # ADD UNZIP TASK
                chained.append(tasks.unzip_task.si(new_download.id))
                task = chain(*chained)()

                new_download.task_id = task.task_id
                new_download.save()

                return Response(self.meta(message='New download started',
                                          id=new_download.id,
                                          meta=task.info,
                                          task_id=task.task_id,
                                          status=task.state), status=status.HTTP_200_OK)

    def meta(self, **kwarg):

        return kwarg


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
                    sync = tasks.sync.delay(action)
                    output = {
                        'message': 'Process Started',
                        'task_id': sync.task_id,
                        'status': sync.state
                    }
                    job = Task()
                    job.task_id = sync.task_id
                    job.name = action
                    job.status = 'PENDING'
                    job.save()

            return Response(output, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Action not supported'}, status=status.HTTP_406_NOT_ACCEPTABLE)

