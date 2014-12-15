# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compare', '0002_auto_20141212_1152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='color',
            name='pillbox_value',
            field=models.CharField(max_length=200, null=True, verbose_name=b'Pillbox Value', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='color',
            name='spl_value',
            field=models.CharField(max_length=200, null=True, verbose_name=b'SPL Value', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='image',
            name='pillbox_value',
            field=models.CharField(max_length=200, null=True, verbose_name=b'Pillbox Value', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='image',
            name='spl_value',
            field=models.CharField(max_length=200, null=True, verbose_name=b'SPL Value', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='imprint',
            name='pillbox_value',
            field=models.CharField(max_length=200, null=True, verbose_name=b'Pillbox Value', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='imprint',
            name='spl_value',
            field=models.CharField(max_length=200, null=True, verbose_name=b'SPL Value', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='score',
            name='pillbox_value',
            field=models.CharField(max_length=200, null=True, verbose_name=b'Pillbox Value', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='score',
            name='spl_value',
            field=models.CharField(max_length=200, null=True, verbose_name=b'SPL Value', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='shape',
            name='pillbox_value',
            field=models.CharField(max_length=200, null=True, verbose_name=b'Pillbox Value', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='shape',
            name='spl_value',
            field=models.CharField(max_length=200, null=True, verbose_name=b'SPL Value', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='size',
            name='pillbox_value',
            field=models.CharField(max_length=200, null=True, verbose_name=b'Pillbox Value', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='size',
            name='spl_value',
            field=models.CharField(max_length=200, null=True, verbose_name=b'SPL Value', blank=True),
            preserve_default=True,
        ),
    ]
