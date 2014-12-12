# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pillbox', '0007_pillboxdata_has_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pillboxdata',
            name='has_image2',
        ),
    ]
