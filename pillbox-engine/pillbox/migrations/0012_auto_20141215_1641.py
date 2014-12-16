# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pillbox', '0011_auto_20141215_1500'),
    ]

    operations = [
        migrations.AddField(
            model_name='pillboxdata',
            name='pillbox_core',
            field=models.CharField(max_length=250, null=True, verbose_name=b'Pillbox SCORE', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pillboxdata',
            name='pillbox_imprint',
            field=models.CharField(max_length=250, null=True, verbose_name=b'Pillbox IMPRINT', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pillboxdata',
            name='pillbox_size',
            field=models.CharField(max_length=250, null=True, verbose_name=b'Pillbo SIZE', blank=True),
            preserve_default=True,
        ),
    ]
