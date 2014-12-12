# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spl', '0002_auto_20141211_1533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pill',
            name='rxstring',
            field=models.TextField(null=True, verbose_name=b'rxttystring', blank=True),
            preserve_default=True,
        ),
    ]
