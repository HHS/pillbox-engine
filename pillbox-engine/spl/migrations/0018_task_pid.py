# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spl', '0017_download_task_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='pid',
            field=models.CharField(max_length=100, null=True, verbose_name=b'PID', blank=True),
            preserve_default=True,
        ),
    ]
