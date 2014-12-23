# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pillbox', '0018_auto_20141223_1436'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pillboxdata',
            name='new',
            field=models.BooleanField(default=False, verbose_name=b'new'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pillboxdata',
            name='stale',
            field=models.BooleanField(default=False, verbose_name=b'stale'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pillboxdata',
            name='updated',
            field=models.BooleanField(default=False, verbose_name=b'updated'),
            preserve_default=True,
        ),
    ]
