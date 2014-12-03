# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pillbox', '0006_auto_20141202_2029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pillboxdata',
            name='spl_ingredients',
            field=models.TextField(null=True, verbose_name=b'SPL_INGREDIENTS', blank=True),
            preserve_default=True,
        ),
    ]
