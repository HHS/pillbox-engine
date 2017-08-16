import ntpath
from os.path import join, exists

from django.core import serializers
from django.conf import settings

from djqscsv import write_csv
from pillbox.models import PillBoxData
from spl.download import check_create_folder


def export(filename, export_type, task_id=None):
    """ export pillbox data in json and csv format """

    acccepted_types = ['json', 'yaml', 'xml', 'csv']

    if export_type in acccepted_types:

        pills = PillBoxData.objects.all().values()

        # remove pillbox/ from images path
        for i, pill in enumerate(pills):
            pills[i]['splimage'] = pill['splimage'].replace('pillbox/', '')

        export_path = join(settings.MEDIA_ROOT, 'export')
        check_create_folder(export_path)
        export_file = join(export_path, '%s.%s' % (filename, export_type))

        if exists(export_file):
            i = 0
            while exists(export_file):
                i += 1
                export_file = join(export_path, '%s_%s.%s' % (filename, str(i), export_type))

        e_file = open(export_file, 'w')

        if export_type == 'csv':
            write_csv(pills, e_file)
            e_file.close()

        else:
            data = serializers.serialize(export_type, pills)
            e_file.write(data)
            e_file.close()

        return 'export/' + ntpath.basename(e_file.name)

    else:
        raise Exception("Incorrect Export Type. Accepted types: 'json', 'yaml', 'xml', 'csv'")
