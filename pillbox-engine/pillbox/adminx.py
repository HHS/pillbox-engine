import xadmin

from xadmin.views.base import filter_hook
from pillbox.models import PillBoxData, Import
from pillbox.tasks import import_task


class PillBoxDataAdmin(object):

    list_display = ('medicine_name', 'setid', 'has_image')
    # list_filter = ['product_code', 'dosage_form']
    list_quick_filter = ['splcolor', 'splsize', 'splscore']
    search_fields = ['medicine_name', 'part_medicine_name']
    reversion_enable = True


class ImportAdmin(object):

    list_display = ('file_name', 'completed', 'status', 'added', 'updated', 'duration', 'created_at')

    fields = ['csv_file', 'file_name', 'completed', 'status', 'added', 'duration', 'updated', 'created_at']
    readonly_fields = ['file_name', 'completed', 'status', 'added', 'updated', 'duration', 'created_at']

    @filter_hook
    def save_models(self):

        self.new_obj.file_name = self.new_obj.csv_file.name
        self.new_obj.save()

        # Start Celery Task
        task = import_task.delay(self.new_obj.csv_file.path, self.new_obj.id)
        self.new_obj.task_id = task.task_id
        self.new_obj.status = 'PENDING'
        self.new_obj.save()

xadmin.site.register(PillBoxData, PillBoxDataAdmin)
xadmin.site.register(Import, ImportAdmin)
