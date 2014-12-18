# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pillbox', '0015_auto_20141217_1013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='export',
            name='file_type',
            field=models.CharField(max_length=200, verbose_name=b'File Type', choices=[(b'json', b'JSON'), (b'csv', b'CSV'), (b'yaml', b'YAML'), (b'xml', b'XML')]),
            preserve_default=True,
        ),
    ]
