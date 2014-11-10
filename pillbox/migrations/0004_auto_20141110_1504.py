# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pillbox', '0003_auto_20141110_1454'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pillboxdata',
            name='id',
        ),
        migrations.AlterField(
            model_name='pillboxdata',
            name='setid',
            field=models.CharField(max_length=40, serialize=False, verbose_name=b'setid', primary_key=True),
        ),
    ]
