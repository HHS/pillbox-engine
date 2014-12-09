# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pillbox', '0013_import_task_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='import',
            name='import_status',
        ),
        migrations.AddField(
            model_name='import',
            name='completed',
            field=models.BooleanField(default=False, verbose_name=b'Completed?'),
            preserve_default=True,
        ),
    ]
