# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spl', '0004_auto_20141031_1806'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('is_active', models.BooleanField(default=True, verbose_name=b'Enabled?')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id', models.CharField(max_length=100, serialize=False, verbose_name=b'Code', primary_key=True)),
                ('code_system', models.CharField(max_length=200, null=True, verbose_name=b'Code System', blank=True)),
                ('name', models.CharField(max_length=300, verbose_name=b'Name')),
                ('class_code', models.CharField(max_length=100, null=True, verbose_name=b'Class Code', blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
