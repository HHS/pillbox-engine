# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spl', '0003_auto_20141211_1651'),
    ]

    operations = [
        migrations.AddField(
            model_name='pill',
            name='produce_code',
            field=models.CharField(max_length=60, null=True, verbose_name=b'Produce Code', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pill',
            name='splimage',
            field=models.FileField(upload_to=b'spl', null=True, verbose_name=b'SPL Image', blank=True),
            preserve_default=True,
        ),
    ]
