# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pillbox', '0009_auto_20141215_1141'),
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('display_name', models.CharField(max_length=250, verbose_name=b'SPL Display Name')),
                ('code', models.CharField(max_length=250, verbose_name=b'SPL Code')),
                ('hex_value', models.CharField(max_length=250, null=True, verbose_name=b'HEX Value', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Shape',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('display_name', models.CharField(max_length=250, verbose_name=b'SPL Display Name')),
                ('code', models.CharField(max_length=250, verbose_name=b'SPL Code')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
