# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spl', '0016_download'),
    ]

    operations = [
        migrations.AddField(
            model_name='download',
            name='task_id',
            field=models.CharField(max_length=250, null=True, verbose_name=b'Task ID', blank=True),
            preserve_default=True,
        ),
    ]
