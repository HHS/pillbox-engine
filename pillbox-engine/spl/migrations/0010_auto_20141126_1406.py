# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spl', '0009_auto_20141125_1214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='setinfo',
            name='author',
            field=models.CharField(max_length=250, null=True, verbose_name=b'Author (Laberer)', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='setinfo',
            name='author_legal',
            field=models.CharField(max_length=250, null=True, verbose_name=b'Legal Author', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='setinfo',
            name='code',
            field=models.CharField(max_length=120, verbose_name=b'Document Type (Code)'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='setinfo',
            name='effective_time',
            field=models.CharField(max_length=100, verbose_name=b'Effective Time'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='setinfo',
            name='source',
            field=models.CharField(max_length=200, verbose_name=b'Source'),
            preserve_default=True,
        ),
    ]
