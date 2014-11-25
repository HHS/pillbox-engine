# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spl', '0007_auto_20141120_1513'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250, verbose_name=b'Task Name')),
                ('task_id', models.CharField(max_length=250, null=True, verbose_name=b'Task ID', blank=True)),
                ('time_started', models.DateTimeField(auto_now_add=True)),
                ('time_ended', models.DateTimeField(null=True, verbose_name=b'Time Ended', blank=True)),
                ('duration', models.CharField(max_length=10, verbose_name=b'Duration')),
                ('meta', models.TextField(null=True, verbose_name=b'Meta', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
