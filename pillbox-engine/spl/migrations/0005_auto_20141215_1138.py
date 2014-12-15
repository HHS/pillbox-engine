# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spl', '0004_auto_20141212_1142'),
    ]

    operations = [
        migrations.AddField(
            model_name='pill',
            name='splcolor_text',
            field=models.CharField(max_length=100, null=True, verbose_name=b'SPL Color Display Name', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pill',
            name='splshape_text',
            field=models.CharField(max_length=100, null=True, verbose_name=b'SPL Shape Display Name', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pill',
            name='splcolor',
            field=models.CharField(max_length=100, null=True, verbose_name=b'SPL Color Code', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pill',
            name='splshape',
            field=models.CharField(max_length=100, null=True, verbose_name=b'SPL Shape Code', blank=True),
            preserve_default=True,
        ),
    ]
