# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_active', models.BooleanField(default=True, verbose_name=b'Enabled?')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('spl_id', models.CharField(unique=True, max_length=100, verbose_name=b'Unii Code')),
                ('code_system', models.CharField(max_length=200, null=True, verbose_name=b'Code System', blank=True)),
                ('name', models.CharField(max_length=300, verbose_name=b'Name')),
                ('class_code', models.CharField(max_length=100, null=True, verbose_name=b'Class Code', blank=True)),
            ],
            options={
                'verbose_name': 'OSDF Ingredient',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Pill',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_active', models.BooleanField(default=True, verbose_name=b'Enabled?')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('ssp', models.CharField(unique=True, max_length=200, verbose_name=b'Pillbox Unique ID')),
                ('dosage_form', models.CharField(max_length=20, verbose_name=b'Dosage Form')),
                ('ndc', models.CharField(max_length=100, null=True, verbose_name=b'NDC9', blank=True)),
                ('ndc9', models.CharField(max_length=100, null=True, verbose_name=b'NDC9', blank=True)),
                ('product_code', models.CharField(max_length=60, null=True, verbose_name=b'Product Code', blank=True)),
                ('equal_product_code', models.CharField(max_length=30, null=True, verbose_name=b'Equal Product Code', blank=True)),
                ('approval_code', models.CharField(max_length=100, null=True, verbose_name=b'approval_code', blank=True)),
                ('medicine_name', models.CharField(max_length=300, verbose_name=b'Medicine Name')),
                ('part_num', models.IntegerField(default=0, verbose_name=b'Part Number')),
                ('part_medicine_name', models.CharField(max_length=200, null=True, verbose_name=b'Part Medicine Name', blank=True)),
                ('rxtty', models.CharField(max_length=100, null=True, verbose_name=b'rxtty', blank=True)),
                ('rxstring', models.CharField(max_length=100, null=True, verbose_name=b'rxttystring', blank=True)),
                ('rxcui', models.CharField(max_length=100, null=True, verbose_name=b'rxcui', blank=True)),
                ('dea_schedule_code', models.CharField(max_length=100, null=True, verbose_name=b'DEA_SCHEDULE_CODE', blank=True)),
                ('dea_schedule_name', models.CharField(max_length=100, null=True, verbose_name=b'DEA_SCHEDULE_NAME', blank=True)),
                ('marketing_act_code', models.CharField(max_length=100, null=True, verbose_name=b'MARKETING_ACT_CODE', blank=True)),
                ('splcolor', models.CharField(max_length=100, null=True, verbose_name=b'SPL Color', blank=True)),
                ('splsize', models.CharField(max_length=100, null=True, verbose_name=b'SPL Size', blank=True)),
                ('splshape', models.CharField(max_length=100, null=True, verbose_name=b'SPL Shape', blank=True)),
                ('splimprint', models.CharField(max_length=100, null=True, verbose_name=b'SPL Imprint', blank=True)),
                ('splimage', models.CharField(max_length=100, null=True, verbose_name=b'SPL Image', blank=True)),
                ('splscore', models.CharField(max_length=100, null=True, verbose_name=b'SPL Score', blank=True)),
            ],
            options={
                'verbose_name': 'SPL OSDF Pill',
                'verbose_name_plural': 'SPL OSDF Pills',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_active', models.BooleanField(default=True, verbose_name=b'Enabled?')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('setid', models.CharField(unique=True, max_length=200, verbose_name=b'setid')),
                ('id_root', models.CharField(max_length=200, verbose_name=b'id root')),
                ('title', models.TextField(null=True, verbose_name=b'Title', blank=True)),
                ('effective_time', models.CharField(max_length=100, verbose_name=b'Effective Time')),
                ('version_number', models.IntegerField(verbose_name=b'Version Number')),
                ('code', models.CharField(max_length=250, verbose_name=b'Document Type (Code)')),
                ('filename', models.CharField(max_length=300, verbose_name=b'File Name')),
                ('source', models.CharField(max_length=250, verbose_name=b'Source')),
                ('author', models.CharField(max_length=300, null=True, verbose_name=b'Author (Laberer)', blank=True)),
                ('author_legal', models.CharField(max_length=300, null=True, verbose_name=b'Legal Author', blank=True)),
                ('is_osdf', models.BooleanField(default=False, verbose_name=b'Is In Oral Solid Dosage Form?')),
                ('discontinued', models.BooleanField(default=False, verbose_name=b'Is Discontinued from SPL?')),
            ],
            options={
                'verbose_name': 'SPL Product',
                'verbose_name_plural': 'SPL Products',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_active', models.BooleanField(default=True, verbose_name=b'Enabled?')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=100, verbose_name=b'Title')),
                ('host', models.CharField(help_text=b'FTP host to download the files from', max_length=200, verbose_name=b'FTP Host')),
                ('path', models.CharField(help_text=b'Path where the files are located on the ftp server', max_length=200, verbose_name=b'PATH')),
                ('files', jsonfield.fields.JSONField(help_text=b'Enter in form python list', verbose_name=b'File Names')),
                ('last_downloaded', models.DateTimeField(null=True, verbose_name=b'Last Downloaded and Unzipped', blank=True)),
                ('zip_size', models.FloatField(null=True, verbose_name=b'Total zip folder size (bytes)', blank=True)),
                ('unzip_size', models.FloatField(null=True, verbose_name=b'Total unzip folder size (bytes)', blank=True)),
                ('xml_count', models.IntegerField(null=True, verbose_name=b'Total xml files', blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250, verbose_name=b'Task Name')),
                ('task_id', models.CharField(max_length=250, unique=True, null=True, verbose_name=b'Task ID', blank=True)),
                ('time_started', models.DateTimeField(auto_now_add=True)),
                ('time_ended', models.DateTimeField(null=True, verbose_name=b'Time Ended', blank=True)),
                ('duration', models.FloatField(default=0, verbose_name=b'Duration')),
                ('status', models.CharField(max_length=200, null=True, verbose_name=b'Status', blank=True)),
                ('meta', jsonfield.fields.JSONField(default={}, verbose_name=b'Meta')),
                ('pid', models.CharField(max_length=100, null=True, verbose_name=b'PID', blank=True)),
                ('is_active', models.BooleanField(default=True, verbose_name=b'Task is active (running)?')),
                ('download_type', models.CharField(max_length=200, null=True, verbose_name=b'Download source name', blank=True)),
                ('traceback', models.TextField(null=True, verbose_name=b'Traceback', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='pill',
            name='setid',
            field=models.ForeignKey(to='spl.Product'),
            preserve_default=True,
        ),
    ]
