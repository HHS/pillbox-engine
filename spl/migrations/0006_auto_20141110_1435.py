# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spl', '0005_ingredient'),
    ]

    operations = [
        migrations.DeleteModel(
            name='SPLData',
        ),
        migrations.AlterModelOptions(
            name='productdata',
            options={'verbose_name': 'SPL OSDF Pill', 'verbose_name_plural': 'SPL OSDF Pills'},
        ),
        migrations.AlterModelOptions(
            name='setinfo',
            options={'verbose_name': 'SPL Product', 'verbose_name_plural': 'SPL Products'},
        ),
    ]
