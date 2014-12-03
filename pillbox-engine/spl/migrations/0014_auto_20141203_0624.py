# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spl', '0013_auto_20141203_0609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='duration',
            field=models.FloatField(default=0, verbose_name=b'Duration'),
            preserve_default=True,
        ),
    ]
