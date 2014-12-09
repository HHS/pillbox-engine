import re
import os
import signal

import xadmin
from xadmin import views

from spl.models import Source, Ingredient, SetInfo, ProductData, Task


class GlobalSetting(object):
    global_search_models = [Source]
    # global_models_icon = {
    #     Source: 'fa fa-laptop', Ingredient: 'fa fa-cloud'
    # }
    menu_style = 'default'  # 'accordion'
    site_title = 'Pillbox Engine'
    site_footer = 'Pillbox'
xadmin.site.register(views.CommAdminView, GlobalSetting)


class SourceAdmin(object):

    search_fields = ['title']
    reversion_enable = True

    list_display = ('title', 'host', 'path', 'files', 'last_downloaded')
    readonly_fields = ['last_downloaded', 'zip_size', 'unzip_size']
    model_icon = 'fa fa-download'


class IngredientAdmin(object):

    list_display = ('name', 'code_system', 'class_code')
    list_filter = ['code_system', 'class_code']
    list_quick_filter = ['class_code']
    search_fields = ['name']
    reversion_enable = True

    model_icon = 'fa fa-dot-circle-o'


class SetInfoAdmin(object):
    def name(self, instance):
        if instance.title:
            check = re.match('[a-zA-Z]', instance.title)
            if check:
                return instance.title
        return instance.setid
    name.short_description = "Title"
    name.is_column = True

    list_display = ('name', 'source', 'version_number', 'author', 'is_osdf')
    list_filter = ['version_number', 'is_osdf']
    list_quick_filter = ['is_osdf', 'source']
    search_fields = ['title', 'setid', 'author', 'author_legal', 'filename']
    reversion_enable = True

    model_icon = 'fa fa-stethoscope'

    list_per_page = 10


class ProductDataAdmin(object):

    fields = ['id', 'setid', 'dosage_form', 'ndc', 'ndc9', 'product_code',
              'equal_product_code', 'approval_code', 'medicine_name', 'part_num',
              'part_medicine_name', 'rxtty', 'rxstring', 'rxcui', 'dea_schedule_code',
              'dea_schedule_name', 'marketing_act_code', 'splcolor', 'splsize',
              'splshape', 'splimprint', 'splimage', 'splscore']

    readonly_fields = fields

    list_display = ('medicine_name', 'product_code', 'part_num', 'dosage_form')
    list_filter = ['product_code', 'dosage_form']
    list_quick_filter = ['splcolor', 'splsize', 'splscore']
    search_fields = ['medicine_name', 'part_medicine_name']
    reversion_enable = True

    model_icon = 'fa fa-medkit'
    list_per_page = 10


class TaskAdmin(object):

    def cancel_task(self, request, queryset):
        tasks = queryset.filter(is_active=True)
        for item in tasks:
            try:
                os.kill(int(item.pid), signal.SIGKILL)
            except OSError:
                pass
            item.is_active = False
            item.status = 'CANCELED'
            item.save()
    cancel_task.short_description = "Cancel Running Task"

    def meta_info(self, instance):
        text = ''
        if instance.meta:
            for k, v in instance.meta.iteritems():
                text += '%s: %s |' % (k, v)
        return text
    meta_info.short_description = "Meta"
    meta_info.is_column = True

    def updated(self, instance):
        if instance.meta:
            # return instance.meta['updated']
            return 0
        return 0
    updated.short_description = "Updated"
    updated.is_column = True

    actions = ['cancel_task']

    list_display = ('name', 'status', 'duration', 'meta_info',
                    'time_started', 'time_ended')
    fields = ['is_active', 'task_id', 'name', 'meta', 'status', 'pid',
              'traceback', 'duration', 'time_started', 'time_ended']
    readonly_fields = ['is_active', 'task_id', 'meta', 'name', 'status',
                       'pid', 'traceback', 'duration', 'time_started', 'time_ended']

    model_icon = 'fa fa-tasks'

xadmin.site.register(Source, SourceAdmin)
xadmin.site.register(Ingredient, IngredientAdmin)
xadmin.site.register(SetInfo, SetInfoAdmin)
xadmin.site.register(ProductData, ProductDataAdmin)
xadmin.site.register(Task, TaskAdmin)
