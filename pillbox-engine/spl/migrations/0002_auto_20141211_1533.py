# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spl', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pill',
            name='spl_inactive_ing',
            field=models.TextField(null=True, verbose_name=b'SPL_INACTIVE_ING', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pill',
            name='spl_ingredients',
            field=models.TextField(null=True, verbose_name=b'SPL_INGREDIENTS', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pill',
            name='spl_strength',
            field=models.TextField(null=True, verbose_name=b'SPL_STRENGTH', blank=True),
            preserve_default=True,
        ),
    ]
