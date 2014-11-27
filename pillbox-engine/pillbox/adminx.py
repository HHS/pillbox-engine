from datetime import datetime
from django import forms
from django.db import models

import xadmin
from csvimport.models import CSVImport

from pillbox.models import PillBoxData, Characteristic


class PillBoxDataAdmin(object):

    list_display = ('medicine_name', 'setid', 'has_image')
    # list_filter = ['product_code', 'dosage_form']
    list_quick_filter = ['splcolor', 'splsize', 'splscore']
    search_fields = ['medicine_name', 'part_medicine_name']
    reversion_enable = True


class CharacteristicAdmin(object):

    list_display = ('type', 'spl_value', 'pillbox_value', 'is_different', 'reason')
    # list_filter = ['product_code', 'dosage_form']
    list_quick_filter = ['type', 'is_different']
    search_fields = ['type', 'spl_value', 'pillbox_value']
    reversion_enable = True


class CSVImportAdmin(object):
    ''' Custom model to not have much editable! '''
    readonly_fields = ['file_name',
                       'upload_method',
                       'error_log_html',
                       'import_user']
    fields = [
        'model_name',
        'field_list',
        'upload_file',
        'file_name',
        'encoding',
        'upload_method',
        'error_log_html',
        'import_user'
    ]
    formfield_overrides = {
        models.CharField: {'widget': forms.Textarea(attrs={'rows': '4',
                                                           'cols': '60'})},
        }

    def save_model(self, request, obj, form, change):
        """ Do save and process command - cant commit False
            since then file wont be found for reopening via right charset
        """
        form.save()
        from csvimport.management.commands.importcsv import Command
        cmd = Command()
        if obj.upload_file:
            obj.file_name = obj.upload_file.name
            obj.encoding = ''
            defaults = self.filename_defaults(obj.file_name)
            cmd.setup(mappings=obj.field_list,
                      modelname=obj.model_name,
                      charset=obj.encoding,
                      uploaded=obj.upload_file,
                      defaults=defaults)
        errors = cmd.run(logid=obj.id)
        if errors:
            obj.error_log = '\n'.join(errors)
        obj.import_user = str(request.user)
        obj.import_date = datetime.now()
        obj.save()

    def filename_defaults(self, filename):
        """ Override this method to supply filename based data """
        defaults = []
        splitters = {'/': -1, '.': 0, '_': 0}
        for splitter, index in splitters.items():
            if filename.find(splitter) > -1:
                filename = filename.split(splitter)[index]
        return defaults


xadmin.site.register(PillBoxData, PillBoxDataAdmin)
xadmin.site.register(Characteristic, CharacteristicAdmin)
xadmin.site.register(CSVImport, CSVImportAdmin)
