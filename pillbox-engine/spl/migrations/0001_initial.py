# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SPLData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_active', models.BooleanField(default=True, verbose_name=b'Enabled?')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('setid', models.CharField(unique=True, max_length=40, verbose_name=b'setid')),
                ('setid_product', models.CharField(max_length=100, verbose_name=b'setid_product')),
                ('splsize', jsonfield.fields.JSONField(verbose_name=b'SPLSIZE')),
                ('splshape', jsonfield.fields.JSONField(verbose_name=b'SPLSHAPE')),
                ('splscore', jsonfield.fields.JSONField(verbose_name=b'SPLSCORE')),
                ('splimprint', jsonfield.fields.JSONField(verbose_name=b'SPLIMPRINT')),
                ('splcolor', jsonfield.fields.JSONField(verbose_name=b'SPLCOLOR')),
                ('spl_strength', models.CharField(max_length=100, null=True, verbose_name=b'SPL_STRENGTH', blank=True)),
                ('spl_ingredients', jsonfield.fields.JSONField(verbose_name=b'SPL_INGREDIENTS')),
                ('spl_inactive_ing', jsonfield.fields.JSONField(verbose_name=b'SPL_INACTIVE_ING')),
                ('source', models.CharField(max_length=100, null=True, verbose_name=b'source', blank=True)),
                ('rxtty', models.CharField(max_length=100, null=True, verbose_name=b'rxtty', blank=True)),
                ('rxstring', models.CharField(max_length=100, null=True, verbose_name=b'rxttystring', blank=True)),
                ('rxcui', models.CharField(max_length=100, null=True, verbose_name=b'rxcui', blank=True)),
                ('produce_code', models.CharField(max_length=100, null=True, verbose_name=b'produce_code', blank=True)),
                ('part_num', models.CharField(max_length=100, null=True, verbose_name=b'part_num', blank=True)),
                ('part_medicine_name', models.CharField(max_length=100, null=True, verbose_name=b'part_medicine_name', blank=True)),
                ('ndc9', models.CharField(max_length=100, null=True, verbose_name=b'ndc9', blank=True)),
                ('medicine_name', models.CharField(max_length=100, null=True, verbose_name=b'medicine_name', blank=True)),
                ('marketing_act_code', models.CharField(max_length=100, null=True, verbose_name=b'MARKETING_ACT_CODE', blank=True)),
                ('effective_time', models.CharField(max_length=100, null=True, verbose_name=b'effective_time', blank=True)),
                ('file_name', models.CharField(max_length=100, null=True, verbose_name=b'file_name', blank=True)),
                ('equal_product_code', models.CharField(max_length=100, null=True, verbose_name=b'equal_product_code', blank=True)),
                ('dosage_form', models.CharField(max_length=100, null=True, verbose_name=b'dosage_form', blank=True)),
                ('document_type', models.CharField(max_length=100, null=True, verbose_name=b'document_type', blank=True)),
                ('dea_schedule_code', models.CharField(max_length=100, null=True, verbose_name=b'DEA_SCHEDULE_CODE', blank=True)),
                ('dea_schedule_name', models.CharField(max_length=100, null=True, verbose_name=b'DEA_SCHEDULE_NAME', blank=True)),
                ('author_type', models.CharField(max_length=100, null=True, verbose_name=b'author', blank=True)),
                ('approval_code', models.CharField(max_length=100, null=True, verbose_name=b'approval_code', blank=True)),
                ('image_source', models.CharField(max_length=100, null=True, verbose_name=b'Image Source', blank=True)),
                ('image_id', models.CharField(max_length=100, null=True, verbose_name=b'MARKETING_ACT_CODE', blank=True)),
                ('has_image', models.CharField(max_length=100, null=True, verbose_name=b'MARKETING_ACT_CODE', blank=True)),
                ('from_sis', models.CharField(max_length=100, null=True, verbose_name=b'MARKETING_ACT_CODE', blank=True)),
                ('version_number', models.CharField(max_length=100, null=True, verbose_name=b'MARKETING_ACT_CODE', blank=True)),
                ('clinical_setid', models.CharField(max_length=100, null=True, verbose_name=b'MARKETING_ACT_CODE', blank=True)),
                ('unii_code', models.CharField(max_length=100, null=True, verbose_name=b'MARKETING_ACT_CODE', blank=True)),
                ('physical_characteristics', models.CharField(max_length=100, null=True, verbose_name=b'MARKETING_ACT_CODE', blank=True)),
                ('laberer_code', models.CharField(max_length=100, null=True, verbose_name=b'MARKETING_ACT_CODE', blank=True)),
                ('application_number', models.CharField(max_length=100, null=True, verbose_name=b'MARKETING_ACT_CODE', blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
