# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pillbox', '0010_color_shape'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pillboxdata',
            name='stale',
            field=models.BooleanField(default=False, verbose_name=b'Does not exist on SPL (Stale)'),
            preserve_default=True,
        ),
    ]
