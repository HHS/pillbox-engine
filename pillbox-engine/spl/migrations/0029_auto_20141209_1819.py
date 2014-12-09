# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spl', '0028_auto_20141209_1551'),
    ]

    operations = [
        migrations.AddField(
            model_name='source',
            name='xml_count',
            field=models.IntegerField(null=True, verbose_name=b'Total xml files', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='source',
            name='unzip_size',
            field=models.FloatField(null=True, verbose_name=b'Total unzip folder size (bytes)', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='source',
            name='zip_size',
            field=models.FloatField(null=True, verbose_name=b'Total zip folder size (bytes)', blank=True),
            preserve_default=True,
        ),
    ]
