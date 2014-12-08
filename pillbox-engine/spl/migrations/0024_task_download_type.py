# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spl', '0023_task_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='download_type',
            field=models.CharField(max_length=200, null=True, verbose_name=b'Download source name', blank=True),
            preserve_default=True,
        ),
    ]
