# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spl', '0011_auto_20141202_1227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='duration',
            field=models.CharField(max_length=100, verbose_name=b'Duration'),
            preserve_default=True,
        ),
    ]
