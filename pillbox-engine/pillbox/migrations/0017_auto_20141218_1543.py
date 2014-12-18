# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pillbox', '0016_auto_20141218_1541'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pillboxdata',
            name='clinical_setid',
        ),
        migrations.RemoveField(
            model_name='pillboxdata',
            name='physical_characteristics',
        ),
        migrations.RemoveField(
            model_name='pillboxdata',
            name='unii_code',
        ),
    ]
