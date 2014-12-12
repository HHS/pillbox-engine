# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pillbox', '0003_auto_20141211_1532'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pillboxdata',
            old_name='image_id',
            new_name='splimage',
        ),
    ]
