# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spl', '0008_task'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='task_id',
            field=models.CharField(max_length=250, unique=True, null=True, verbose_name=b'Task ID', blank=True),
            preserve_default=True,
        ),
    ]
