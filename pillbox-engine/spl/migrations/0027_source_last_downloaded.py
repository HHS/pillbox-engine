# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spl', '0026_auto_20141208_1719'),
    ]

    operations = [
        migrations.AddField(
            model_name='source',
            name='last_downloaded',
            field=models.DateTimeField(null=True, verbose_name=b'Last Downloaded and Unzipped', blank=True),
            preserve_default=True,
        ),
    ]
