# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('spl', '0019_auto_20141205_1348'),
    ]

    operations = [
        migrations.AddField(
            model_name='source',
            name='files',
            field=jsonfield.fields.JSONField(default=1, help_text=b'Json format', verbose_name=b'File Names'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='source',
            name='host',
            field=models.CharField(default=1, help_text=b'FTP host to download the files from', max_length=200, verbose_name=b'FTP Host'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='source',
            name='path',
            field=models.CharField(default=1, help_text=b'Path where the files are located on the ftp server', max_length=200, verbose_name=b'PATH'),
            preserve_default=False,
        ),
    ]
