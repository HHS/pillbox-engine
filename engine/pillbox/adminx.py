from django.utils import timezone
from django.db.models import Q
import xadmin
from xadmin.filters import BaseFilter, FieldFilter

from xadmin.views.base import filter_hook
from pillbox.models import PillBoxData, Import, Color, Shape, Export
from pillbox.tasks import import_task, export_task
from spl.models import Task


class PillboxFilter(BaseFilter):

    template = 'xadmin/filters/list.html'

    def __init__(self, request, params, model, admin_view):
        self.title = 'Pillbox Filters'
        self.lookup_exact_name = 'pfilter'
        self.used_params = {}
        super(PillboxFilter, self).__init__(request, params, model, admin_view)

        if self.lookup_exact_name in self.request.GET:
            self.used_params[self.lookup_exact_name] = self.request.GET.get(self.lookup_exact_name, '')

    def has_output(self):
        return True

    def do_filte(self, queryset):

        if self.used_params:
            if self.used_params[self.lookup_exact_name] == '1':
                return queryset.filter(splshape='C48336').exclude(splscore='1')

            elif self.used_params[self.lookup_exact_name] == '2':
                return queryset.filter(splsize='0')

            elif self.used_params[self.lookup_exact_name] == '3':
                queryset = queryset.exclude(splsize='')
                ids = []
                for item in queryset:
                    try:
                        if float(item.splsize) > 30:
                            ids.append(item.id)
                    except ValueError:
                        pass
                return queryset.filter(pk__in=ids)

            elif self.used_params[self.lookup_exact_name] == '4':
                queryset = queryset.exclude(splsize='')
                ids = []
                for item in queryset:
                    try:
                        if float(item.splsize) < 4:
                            ids.append(item.id)
                    except ValueError:
                        pass
                return queryset.filter(pk__in=ids)

            elif self.used_params[self.lookup_exact_name] == '5':
                ids = []
                for item in queryset:
                    try:
                        float(item.splsize)
                    except ValueError:
                        ids.append(item.id)
                return queryset.filter(pk__in=ids)

            elif self.used_params[self.lookup_exact_name] == '6':
                queryset = queryset.exclude(splsize='')
                ids = []
                for item in queryset:
                    try:
                        if not float(item.splsize).is_integer():
                            ids.append(item.id)
                    except ValueError:
                        pass
                return queryset.filter(pk__in=ids)

            elif self.used_params[self.lookup_exact_name] == '7':
                ids = []
                for item in queryset:
                    try:
                        float(item.splscore)
                    except (ValueError, TypeError):
                        ids.append(item.id)
                return queryset.filter(pk__in=ids)

            elif self.used_params[self.lookup_exact_name] == '8':
                queryset = queryset.exclude(Q(splscore='') | Q(splscore__isnull=True))
                ids = []
                for item in queryset:
                    try:
                        if float(item.splscore) > 4:
                            ids.append(item.id)
                    except ValueError:
                        pass
                return queryset.filter(pk__in=ids)

            elif self.used_params[self.lookup_exact_name] == '9':
                return queryset.filter(source='REMAIN')

            elif self.used_params[self.lookup_exact_name] == '10':
                queryset = queryset.exclude(splcolor__isnull=True)
                colors = Color.objects.all().values('code', 'display_name')
                color = {item['code']: item['display_name'] for item in colors}
                ids = []
                for item in queryset:
                    cs = item.splcolor.split(';')
                    cs_text = item.splcolor_text.split(';')
                    for i, c in enumerate(cs):
                        try:
                            if color[c] not in cs_text:
                                ids.append(item.id)
                        except (IndexError, KeyError):
                            ids.append(item.id)
                return queryset.filter(pk__in=ids)

            elif self.used_params[self.lookup_exact_name] == '11':
                queryset = queryset.filter(splshape__isnull=False)
                shapes = Shape.objects.all().values('code', 'display_name')
                shape = {item['code']: item['display_name'] for item in shapes}
                ids = []
                for item in queryset:
                    ss = item.splshape.split(';')
                    ss_text = item.splshape_text.split(';')
                    for i, s in enumerate(ss):
                        try:
                            if shape[s] not in ss_text:
                                ids.append(item.id)
                        except (IndexError, KeyError):
                            ids.append(item.id)
                return queryset.filter(pk__in=ids)

        else:
            return queryset

    @property
    def is_used(self):
        return len(self.used_params.keys()) > 0

    def get_context(self):
        context = super(PillboxFilter, self).get_context()
        context['choices'] = list(self.choices())
        return context

    def choices(self):
        for lookup, title in (
                ('', 'All'),
                ('1', 'Shape is Capsule and Score is not 1'),
                ('2', 'Size is 0'),
                ('3', 'Size > 30'),
                ('4', 'Size < 4'),
                ('5', 'Size contains value other than numeral'),
                ('6', 'Decimal points are not allowed in SPLSIZE specification'),
                ('7', 'Score contain value other than numeral'),
                ('8', 'Score > 4'),
                ('9', 'Source is REMAIN'),
                ('10', 'Color code and cooresponding text value don\'t match'),
                ('11', 'Shape code and cooresponding text value don\'t match'),):
            selected = False
            if self.used_params:
                if self.used_params[self.lookup_exact_name] == lookup:
                    selected = True

            yield {
                'selected': selected,
                'query_string': self.query_string({
                    self.lookup_exact_name: lookup,
                    }, ['p']),
                'display': title,
            }


class PillBoxDataAdmin(object):

    def image_popup(self, image_obj):
        if image_obj:
            return '<a data-toggle="lightbox" data-remote="%s"><img height="90" src="%s" /></a>' % (image_obj.url,
                                                                                                    image_obj.url)
        else:
            return ''

    def pillbox_image(self, instance):
        return self.image_popup(instance.splimage)
    pillbox_image.short_description = "Pillbox"
    pillbox_image.allow_tags = True
    pillbox_image.is_column = True

    list_display = ('medicine_name', 'source', 'new', 'updated', 'stale', 'pillbox_image',)
    list_filter = [PillboxFilter, 'new', 'updated', 'stale', 'has_image']
    list_quick_filter = ['new', 'updated', 'stale', 'has_image']
    search_fields = ['medicine_name', 'part_medicine_name', 'produce_code', 'setid', 'setid_product']
    # reversion_enable = True

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

    fields = ['export_link', 'file_type', 'file_name']
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
