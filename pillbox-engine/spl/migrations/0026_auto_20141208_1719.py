# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spl', '0025_task_traceback'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='download',
            name='task',
        ),
        migrations.DeleteModel(
            name='Download',
        ),
    ]
