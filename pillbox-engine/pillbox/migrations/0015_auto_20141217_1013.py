# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pillbox', '0014_auto_20141217_1009'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='export',
            name='csv_file',
        ),
        migrations.AddField(
            model_name='export',
            name='export_file',
            field=models.FileField(upload_to=b'export', null=True, verbose_name=b'Export File', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='export',
            name='file_type',
            field=models.CharField(default=1, max_length=200, verbose_name=b'File Type', choices=[(b'json', b'JSON'), (b'csv', b'CSV')]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='export',
            name='file_name',
            field=models.CharField(default=1, max_length=200, verbose_name=b'File Name'),
            preserve_default=False,
        ),
    ]
