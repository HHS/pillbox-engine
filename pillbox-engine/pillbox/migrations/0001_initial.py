# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Import',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_active', models.BooleanField(default=True, verbose_name=b'Enabled?')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('file_name', models.CharField(max_length=200, null=True, verbose_name=b'File Name', blank=True)),
                ('csv_file', models.FileField(upload_to=b'csv', verbose_name=b'CSV File')),
                ('completed', models.BooleanField(default=False, verbose_name=b'Completed?')),
                ('added', models.IntegerField(null=True, verbose_name=b'Reocrds Added', blank=True)),
                ('updated', models.IntegerField(null=True, verbose_name=b'Records Updated', blank=True)),
                ('task_id', models.CharField(max_length=200, null=True, verbose_name=b'Task ID', blank=True)),
                ('status', models.CharField(max_length=200, null=True, verbose_name=b'Status', blank=True)),
                ('duration', models.FloatField(null=True, verbose_name=b'Duration (Sec.)', blank=True)),
            ],
            options={
                'verbose_name': 'Data Import',
                'verbose_name_plural': 'Data Import',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PillBoxData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_active', models.BooleanField(default=True, verbose_name=b'Enabled?')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('setid', models.CharField(unique=True, max_length=250, verbose_name=b'setid')),
                ('setid_product', models.CharField(max_length=250, verbose_name=b'setid_product')),
                ('splsize', models.CharField(max_length=250, null=True, verbose_name=b'SPLSIZE', blank=True)),
                ('splshape', models.CharField(max_length=250, null=True, verbose_name=b'SPLSHAPE', blank=True)),
                ('splscore', models.CharField(max_length=250, null=True, verbose_name=b'SPLSCORE', blank=True)),
                ('splimprint', models.CharField(max_length=250, null=True, verbose_name=b'SPLIMPRINT', blank=True)),
                ('splcolor', models.CharField(max_length=250, null=True, verbose_name=b'SPLCOLOR', blank=True)),
                ('spl_strength', models.TextField(null=True, verbose_name=b'SPL_STRENGTH', blank=True)),
                ('spl_ingredients', models.TextField(null=True, verbose_name=b'SPL_INGREDIENTS', blank=True)),
                ('spl_inactive_ing', models.TextField(null=True, verbose_name=b'SPL_INACTIVE_ING', blank=True)),
                ('source', models.CharField(max_length=250, null=True, verbose_name=b'source', blank=True)),
                ('rxtty', models.CharField(max_length=250, null=True, verbose_name=b'rxtty', blank=True)),
                ('rxstring', models.TextField(null=True, verbose_name=b'rxttystring', blank=True)),
                ('rxcui', models.CharField(max_length=250, null=True, verbose_name=b'rxcui', blank=True)),
                ('produce_code', models.CharField(max_length=250, null=True, verbose_name=b'produce_code', blank=True)),
                ('part_num', models.CharField(max_length=250, null=True, verbose_name=b'part_num', blank=True)),
                ('part_medicine_name', models.CharField(max_length=250, null=True, verbose_name=b'part_medicine_name', blank=True)),
                ('ndc9', models.CharField(max_length=250, null=True, verbose_name=b'ndc9', blank=True)),
                ('medicine_name', models.CharField(max_length=250, null=True, verbose_name=b'medicine_name', blank=True)),
                ('marketing_act_code', models.CharField(max_length=250, null=True, verbose_name=b'MARKETING_ACT_CODE', blank=True)),
                ('effective_time', models.CharField(max_length=250, null=True, verbose_name=b'effective_time', blank=True)),
                ('file_name', models.CharField(max_length=250, null=True, verbose_name=b'file_name', blank=True)),
                ('equal_product_code', models.CharField(max_length=250, null=True, verbose_name=b'equal_product_code', blank=True)),
                ('dosage_form', models.CharField(max_length=250, null=True, verbose_name=b'dosage_form', blank=True)),
                ('document_type', models.CharField(max_length=250, null=True, verbose_name=b'document_type', blank=True)),
                ('dea_schedule_code', models.CharField(max_length=250, null=True, verbose_name=b'DEA_SCHEDULE_CODE', blank=True)),
                ('dea_schedule_name', models.CharField(max_length=250, null=True, verbose_name=b'DEA_SCHEDULE_NAME', blank=True)),
                ('author_type', models.CharField(max_length=250, null=True, verbose_name=b'author_type', blank=True)),
                ('author', models.CharField(max_length=250, null=True, verbose_name=b'author', blank=True)),
                ('approval_code', models.CharField(max_length=250, null=True, verbose_name=b'approval_code', blank=True)),
                ('image_source', models.CharField(max_length=250, null=True, verbose_name=b'Image Source', blank=True)),
                ('image_id', models.CharField(max_length=250, null=True, verbose_name=b'MARKETING_ACT_CODE', blank=True)),
                ('has_image', models.CharField(max_length=250, null=True, verbose_name=b'MARKETING_ACT_CODE', blank=True)),
                ('from_sis', models.CharField(max_length=250, null=True, verbose_name=b'MARKETING_ACT_CODE', blank=True)),
                ('version_number', models.CharField(max_length=250, null=True, verbose_name=b'MARKETING_ACT_CODE', blank=True)),
                ('clinical_setid', models.CharField(max_length=250, null=True, verbose_name=b'MARKETING_ACT_CODE', blank=True)),
                ('unii_code', models.CharField(max_length=250, null=True, verbose_name=b'MARKETING_ACT_CODE', blank=True)),
                ('physical_characteristics', models.CharField(max_length=250, null=True, verbose_name=b'MARKETING_ACT_CODE', blank=True)),
                ('laberer_code', models.CharField(max_length=250, null=True, verbose_name=b'MARKETING_ACT_CODE', blank=True)),
                ('application_number', models.CharField(max_length=250, null=True, verbose_name=b'MARKETING_ACT_CODE', blank=True)),
            ],
            options={
                'verbose_name': 'Pillbox Data',
                'verbose_name_plural': 'Pillbox Data',
            },
            bases=(models.Model,),
        ),
    ]
