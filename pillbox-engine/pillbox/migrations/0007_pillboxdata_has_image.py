# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pillbox', '0006_auto_20141212_1312'),
    ]

    operations = [
        migrations.AddField(
            model_name='pillboxdata',
            name='has_image',
            field=models.BooleanField(default=False, verbose_name=b'Has Image'),
            preserve_default=True,
        ),
    ]
