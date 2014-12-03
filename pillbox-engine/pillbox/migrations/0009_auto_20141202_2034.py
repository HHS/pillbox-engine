# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pillbox', '0008_auto_20141202_2033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pillboxdata',
            name='rxstring',
            field=models.TextField(null=True, verbose_name=b'rxttystring', blank=True),
            preserve_default=True,
        ),
    ]
