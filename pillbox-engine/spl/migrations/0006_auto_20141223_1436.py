# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spl', '0005_auto_20141215_1138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pill',
            name='rxtty',
            field=models.TextField(null=True, verbose_name=b'rxtty', blank=True),
            preserve_default=True,
        ),
    ]
