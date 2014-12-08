# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spl', '0018_task_pid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='download',
            old_name='homeopathic',
            new_name='homeo',
        ),
        migrations.RenameField(
            model_name='download',
            old_name='otc',
            new_name='hotc',
        ),
        migrations.RenameField(
            model_name='download',
            old_name='rx',
            new_name='hrx',
        ),
        migrations.RenameField(
            model_name='download',
            old_name='remainder',
            new_name='remain',
        ),
    ]
