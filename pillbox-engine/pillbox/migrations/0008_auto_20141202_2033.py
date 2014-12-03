# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pillbox', '0007_auto_20141202_2032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pillboxdata',
            name='spl_strength',
            field=models.TextField(null=True, verbose_name=b'SPL_STRENGTH', blank=True),
            preserve_default=True,
        ),
    ]
