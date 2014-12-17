from django.utils import timezone
import xadmin

from xadmin.views.base import filter_hook
from pillbox.models import PillBoxData, Import, Color, Shape, Export
from pillbox.tasks import import_task, export_task
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


class ExportAdmin(object):

    def export_link(self, instance):
        if instance.export_file:
            return '<a href="%s" download>%s</a>' % (instance.export_file.url, instance.export_file.name)
        else:
            return ''
    export_link.short_description = "Export File"
    export_link.allow_tags = True

    list_display = ('file_name', 'file_type', 'status', 'duration', 'completed')

    fields = ['file_type', 'file_name']
    readonly_fields = ['export_link', 'completed', 'task_id', 'status', 'duration', 'created_at']

    @filter_hook
    def save_models(self):

        self.new_obj.save()

        # create a task object
        task = Task()
        task.name = 'export'
        task.status = 'PENDING'
        task.time_started = timezone.now()
        task.save()

        # Start Celery Task
        celery_task = export_task.delay(self.new_obj.file_name, self.new_obj.file_type, task.id, self.new_obj.id)
        task.task_id = celery_task.task_id
        task.save()

        self.new_obj.task_id = task.id
        self.new_obj.status = task.status
        self.new_obj.save()

    model_icon = 'fa fa-sign-out'


class ColorAdmin(object):

    list_display = ('display_name', 'code')


class ShapeAdmin(ColorAdmin):
    pass

xadmin.site.register(PillBoxData, PillBoxDataAdmin)
xadmin.site.register(Import, ImportAdmin)
xadmin.site.register(Color, ColorAdmin)
xadmin.site.register(Shape, ShapeAdmin)
xadmin.site.register(Export, ExportAdmin)
