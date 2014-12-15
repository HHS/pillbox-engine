from django.utils import timezone
import xadmin

from xadmin.views.base import filter_hook
from pillbox.models import PillBoxData, Import, Color, Shape
from pillbox.tasks import import_task
from spl.models import Task


class PillBoxDataAdmin(object):

    list_display = ('medicine_name', 'source', 'new', 'updated', 'stale')
    list_filter = ['new', 'updated', 'stale', 'has_image']
    list_quick_filter = ['new', 'updated', 'stale', 'has_image']
    search_fields = ['medicine_name', 'part_medicine_name']
    reversion_enable = True

    model_icon = 'fa fa-briefcase'


class ImportAdmin(object):

    list_display = ('file_name', 'completed', 'status', 'added', 'updated', 'duration', 'created_at')

    fields = ['csv_file', 'file_name', 'completed', 'status', 'added', 'duration', 'updated', 'created_at']
    readonly_fields = ['file_name', 'completed', 'status', 'added', 'updated', 'duration', 'created_at']

    @filter_hook
    def save_models(self):

        self.new_obj.file_name = self.new_obj.csv_file.name
        self.new_obj.save()

        # create a task object
        task = Task()
        task.name = 'import'
        task.status = 'PENDING'
        task.time_started = timezone.now()
        task.save()

        # Start Celery Task
        celery_task = import_task.delay(self.new_obj.csv_file.path, task.id, self.new_obj.id)
        task.task_id = celery_task.task_id
        task.save()

        self.new_obj.task_id = task.id
        self.new_obj.status = task.status
        self.new_obj.save()

    model_icon = 'fa fa-paperclip'


class ColorAdmin(object):

    list_display = ('display_name', 'code')


class ShapeAdmin(ColorAdmin):
    pass

xadmin.site.register(PillBoxData, PillBoxDataAdmin)
xadmin.site.register(Import, ImportAdmin)
xadmin.site.register(Color, ColorAdmin)
xadmin.site.register(Shape, ShapeAdmin)
