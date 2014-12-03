# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pillbox', '0011_auto_20141203_0445'),
    ]

    operations = [
        migrations.AddField(
            model_name='import',
            name='file_name',
            field=models.CharField(max_length=200, null=True, verbose_name=b'File Name', blank=True),
            preserve_default=True,
        ),
    ]
