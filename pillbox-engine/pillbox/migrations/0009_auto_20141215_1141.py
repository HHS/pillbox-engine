# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pillbox', '0008_remove_pillboxdata_has_image2'),
    ]

    operations = [
        migrations.AddField(
            model_name='pillboxdata',
            name='pillbox_color_text',
            field=models.CharField(max_length=250, null=True, verbose_name=b'Pillbox COLOR Display Name', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pillboxdata',
            name='pillbox_shape_text',
            field=models.CharField(max_length=250, null=True, verbose_name=b'Pillbox Shape Display Name', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pillboxdata',
            name='splcolor_text',
            field=models.CharField(max_length=250, null=True, verbose_name=b'SPLCOLOR Display Name', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pillboxdata',
            name='splshape_text',
            field=models.CharField(max_length=250, null=True, verbose_name=b'SPLSHAPE Display Name', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pillboxdata',
            name='splcolor',
            field=models.CharField(max_length=250, null=True, verbose_name=b'SPLCOLOR Code', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pillboxdata',
            name='splshape',
            field=models.CharField(max_length=250, null=True, verbose_name=b'SPLSHAPE Code', blank=True),
            preserve_default=True,
        ),
    ]
