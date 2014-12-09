# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pillbox', '0002_auto_20141202_1806'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pillboxdata',
            name='setid',
            field=models.CharField(max_length=200, serialize=False, verbose_name=b'setid', primary_key=True),
            preserve_default=True,
        ),
    ]
