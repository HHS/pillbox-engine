# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spl', '0010_auto_20141126_1406'),
    ]

    operations = [
        migrations.AlterField(
            model_name='setinfo',
            name='author',
            field=models.CharField(max_length=300, null=True, verbose_name=b'Author (Laberer)', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='setinfo',
            name='author_legal',
            field=models.CharField(max_length=300, null=True, verbose_name=b'Legal Author', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='setinfo',
            name='code',
            field=models.CharField(max_length=250, verbose_name=b'Document Type (Code)'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='setinfo',
            name='filename',
            field=models.CharField(max_length=300, verbose_name=b'File Name'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='setinfo',
            name='source',
            field=models.CharField(max_length=250, verbose_name=b'Source'),
            preserve_default=True,
        ),
    ]
