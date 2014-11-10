# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spl', '0006_auto_20141110_1435'),
        ('pillbox', '0002_characteristic'),
    ]

    operations = [
        migrations.AddField(
            model_name='characteristic',
            name='pillbox',
            field=models.ForeignKey(default=1, to='pillbox.PillBoxData'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='characteristic',
            name='spl',
            field=models.ForeignKey(default=1, to='spl.ProductData'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='characteristic',
            name='pillbox_value',
            field=models.CharField(max_length=200, verbose_name=b'Pillbox Value'),
        ),
        migrations.AlterField(
            model_name='characteristic',
            name='spl_value',
            field=models.CharField(max_length=200, verbose_name=b'SPL Value'),
        ),
        migrations.AlterField(
            model_name='characteristic',
            name='type',
            field=models.CharField(max_length=40, verbose_name=b'Type', choices=[(b'splsize', b'SPL Size'), (b'splshape', b'SPL Shape'), (b'splscore', b'SPL Score'), (b'splcolor', b'SPL Color'), (b'splimprint', b'SSPL Imprint')]),
        ),
    ]
