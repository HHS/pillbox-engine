# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pillbox', '0013_auto_20141216_1253'),
    ]

    operations = [
        migrations.CreateModel(
            name='Export',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_active', models.BooleanField(default=True, verbose_name=b'Enabled?')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('file_name', models.CharField(max_length=200, null=True, verbose_name=b'File Name', blank=True)),
                ('csv_file', models.FileField(upload_to=b'csv', null=True, verbose_name=b'CSV File', blank=True)),
                ('completed', models.BooleanField(default=False, verbose_name=b'Completed?')),
                ('task_id', models.CharField(max_length=200, null=True, verbose_name=b'Task ID', blank=True)),
                ('status', models.CharField(max_length=200, null=True, verbose_name=b'Status', blank=True)),
                ('duration', models.FloatField(null=True, verbose_name=b'Duration (Sec.)', blank=True)),
            ],
            options={
                'verbose_name': 'Export',
                'verbose_name_plural': 'Export',
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='pillboxdata',
            name='pillbox_size',
            field=models.CharField(max_length=250, null=True, verbose_name=b'Pillbox SIZE', blank=True),
            preserve_default=True,
        ),
    ]
