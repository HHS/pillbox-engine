# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spl', '0015_task_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Download',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('started', models.DateTimeField(null=True, verbose_name=b'Time Started', blank=True)),
                ('ended', models.DateTimeField(null=True, verbose_name=b'Time Ended', blank=True)),
                ('duration', models.FloatField(default=0, verbose_name=b'Duration')),
                ('status', models.CharField(max_length=200, null=True, verbose_name=b'Status', blank=True)),
                ('completed', models.BooleanField(default=False, verbose_name=b'Completed?')),
                ('rx', models.BooleanField(default=False, verbose_name=b'RX Downloaded?')),
                ('otc', models.BooleanField(default=False, verbose_name=b'OTC Downloaded?')),
                ('homeopathic', models.BooleanField(default=False, verbose_name=b'Homeopathic Downloaded?')),
                ('animal', models.BooleanField(default=False, verbose_name=b'Animal Downloaded?')),
                ('remainder', models.BooleanField(default=False, verbose_name=b'Remainder Downloaded?')),
                ('unzipped', models.BooleanField(default=False, verbose_name=b'Unzipped?')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
