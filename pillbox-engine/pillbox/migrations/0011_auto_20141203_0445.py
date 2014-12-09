# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pillbox', '0010_auto_20141202_2221'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='import',
            options={'verbose_name': 'Data Import', 'verbose_name_plural': 'Data Import'},
        ),
        migrations.AddField(
            model_name='import',
            name='added',
            field=models.IntegerField(null=True, verbose_name=b'Reocrds Added', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='import',
            name='import_status',
            field=models.CharField(max_length=b'200', null=True, verbose_name=b'Import Status', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='import',
            name='updated',
            field=models.IntegerField(null=True, verbose_name=b'Records Updated', blank=True),
            preserve_default=True,
        ),
    ]
