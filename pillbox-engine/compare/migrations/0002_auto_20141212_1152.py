# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compare', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='color',
            name='verified',
            field=models.BooleanField(default=False, verbose_name=b'Verified?'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='image',
            name='verified',
            field=models.BooleanField(default=False, verbose_name=b'Verified?'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='imprint',
            name='verified',
            field=models.BooleanField(default=False, verbose_name=b'Verified?'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='score',
            name='verified',
            field=models.BooleanField(default=False, verbose_name=b'Verified?'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='shape',
            name='verified',
            field=models.BooleanField(default=False, verbose_name=b'Verified?'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='size',
            name='verified',
            field=models.BooleanField(default=False, verbose_name=b'Verified?'),
            preserve_default=True,
        ),
    ]
