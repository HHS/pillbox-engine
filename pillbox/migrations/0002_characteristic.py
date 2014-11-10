# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pillbox', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Characteristic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_active', models.BooleanField(default=True, verbose_name=b'Enabled?')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('type', models.CharField(max_length=40, verbose_name=b'Type')),
                ('spl_value', models.CharField(max_length=200, verbose_name=b'Type')),
                ('pillbox_value', models.CharField(max_length=200, verbose_name=b'Type')),
                ('is_different', models.BooleanField(default=False, verbose_name=b'Is Different?')),
                ('reason', models.TextField(null=True, verbose_name=b'Reason', blank=True)),
            ],
            options={
                'verbose_name': 'Pillbox Characteristic',
            },
            bases=(models.Model,),
        ),
    ]
