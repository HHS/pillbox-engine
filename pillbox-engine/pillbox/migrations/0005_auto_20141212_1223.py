# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pillbox', '0004_auto_20141212_1157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pillboxdata',
            name='splimage',
            field=models.FileField(max_length=250, upload_to=b'pillbox', null=True, verbose_name=b'Image Name', blank=True),
            preserve_default=True,
        ),
    ]
