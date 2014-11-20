# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spl', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SetInfo',
            fields=[
                ('is_active', models.BooleanField(default=True, verbose_name=b'Enabled?')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('setid', models.CharField(max_length=200, serialize=False, verbose_name=b'setid', primary_key=True)),
                ('id_root', models.CharField(max_length=200, verbose_name=b'id root')),
                ('title', models.TextField(null=True, verbose_name=b'Title', blank=True)),
                ('effective_time', models.CharField(max_length=8, verbose_name=b'Effective Time')),
                ('version_number', models.IntegerField(verbose_name=b'Version Number')),
                ('code', models.CharField(max_length=10, verbose_name=b'Document Type (Code)')),
                ('filename', models.CharField(max_length=100, verbose_name=b'File Name')),
                ('source', models.CharField(max_length=20, verbose_name=b'Source')),
                ('author', models.CharField(max_length=200, null=True, verbose_name=b'Author (Laberer)', blank=True)),
                ('author_legal', models.CharField(max_length=200, null=True, verbose_name=b'Legal Author', blank=True)),
                ('is_osdf', models.BooleanField(default=False, verbose_name=b'Is In Oral Solid Dosage Form?')),
                ('discontinued', models.BooleanField(default=False, verbose_name=b'Is Discontinued from SPL?')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
