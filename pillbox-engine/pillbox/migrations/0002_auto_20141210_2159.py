# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pillbox', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pillboxdata',
            name='new',
            field=models.BooleanField(default=False, verbose_name=b'New Record'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pillboxdata',
            name='stale',
            field=models.BooleanField(default=True, verbose_name=b'Stale record'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pillboxdata',
            name='updated',
            field=models.BooleanField(default=False, verbose_name=b'Updated from SPL'),
            preserve_default=True,
        ),
    ]
