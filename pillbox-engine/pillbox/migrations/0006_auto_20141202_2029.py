# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pillbox', '0005_auto_20141202_2027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pillboxdata',
            name='spl_inactive_ing',
            field=models.TextField(null=True, verbose_name=b'SPL_INACTIVE_ING', blank=True),
            preserve_default=True,
        ),
    ]
