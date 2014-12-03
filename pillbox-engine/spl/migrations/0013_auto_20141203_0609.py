# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('spl', '0012_auto_20141202_1241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='meta',
            field=jsonfield.fields.JSONField(null=True, verbose_name=b'Meta', blank=True),
            preserve_default=True,
        ),
    ]
