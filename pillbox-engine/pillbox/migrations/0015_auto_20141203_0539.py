# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pillbox', '0014_auto_20141203_0526'),
    ]

    operations = [
        migrations.AddField(
            model_name='import',
            name='duration',
            field=models.FloatField(null=True, verbose_name=b'Duration (Sec.)', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='import',
            name='status',
            field=models.CharField(max_length=200, null=True, verbose_name=b'Status', blank=True),
            preserve_default=True,
        ),
    ]
