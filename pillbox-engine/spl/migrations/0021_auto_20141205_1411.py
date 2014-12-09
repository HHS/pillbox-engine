# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('spl', '0020_auto_20141205_1351'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='download',
            name='task_id',
        ),
        migrations.AddField(
            model_name='download',
            name='task',
            field=models.ForeignKey(blank=True, to='spl.Task', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='source',
            name='files',
            field=jsonfield.fields.JSONField(help_text=b'Enter in form python list', verbose_name=b'File Names'),
            preserve_default=True,
        ),
    ]
