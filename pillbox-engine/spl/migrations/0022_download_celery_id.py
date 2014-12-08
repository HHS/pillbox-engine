# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spl', '0021_auto_20141205_1411'),
    ]

    operations = [
        migrations.AddField(
            model_name='download',
            name='celery_id',
            field=models.CharField(max_length=200, null=True, verbose_name=b'Celery ID', blank=True),
            preserve_default=True,
        ),
    ]
