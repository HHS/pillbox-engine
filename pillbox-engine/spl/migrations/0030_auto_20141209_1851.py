# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('spl', '0029_auto_20141209_1819'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='meta',
            field=jsonfield.fields.JSONField(default={}, verbose_name=b'Meta'),
            preserve_default=True,
        ),
    ]
