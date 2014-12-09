# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spl', '0027_source_last_downloaded'),
    ]

    operations = [
        migrations.AddField(
            model_name='source',
            name='unzip_size',
            field=models.FloatField(null=True, verbose_name=b'Total unzip folder size', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='source',
            name='zip_size',
            field=models.FloatField(null=True, verbose_name=b'Total zip folder size', blank=True),
            preserve_default=True,
        ),
    ]
