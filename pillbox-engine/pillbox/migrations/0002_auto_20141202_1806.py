# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pillbox', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pillboxdata',
            name='author',
            field=models.CharField(max_length=100, null=True, verbose_name=b'author', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pillboxdata',
            name='author_type',
            field=models.CharField(max_length=100, null=True, verbose_name=b'author_type', blank=True),
            preserve_default=True,
        ),
    ]
