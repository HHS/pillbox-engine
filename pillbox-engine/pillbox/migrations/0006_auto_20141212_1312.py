# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pillbox', '0005_auto_20141212_1223'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pillboxdata',
            old_name='has_image',
            new_name='has_image2',
        ),
    ]
