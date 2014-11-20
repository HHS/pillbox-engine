# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spl', '0006_auto_20141110_1435'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ingredient',
            options={'verbose_name': 'OSDF Ingredient'},
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='id',
            field=models.CharField(max_length=100, serialize=False, verbose_name=b'Unii Code', primary_key=True),
            preserve_default=True,
        ),
    ]
