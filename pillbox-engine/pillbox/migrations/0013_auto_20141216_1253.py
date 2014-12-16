# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pillbox', '0012_auto_20141215_1641'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pillboxdata',
            old_name='pillbox_core',
            new_name='pillbox_score',
        ),
    ]
