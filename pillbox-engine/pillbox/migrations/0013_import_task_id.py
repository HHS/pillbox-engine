# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pillbox', '0012_import_file_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='import',
            name='task_id',
            field=models.CharField(max_length=200, null=True, verbose_name=b'Task ID', blank=True),
            preserve_default=True,
        ),
    ]
