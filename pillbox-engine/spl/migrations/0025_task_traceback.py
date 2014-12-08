# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spl', '0024_task_download_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='traceback',
            field=models.TextField(null=True, verbose_name=b'Traceback', blank=True),
            preserve_default=True,
        ),
    ]
