# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spl', '0003_splsource'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductData',
            fields=[
                ('is_active', models.BooleanField(default=True, verbose_name=b'Enabled?')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id', models.CharField(max_length=200, serialize=False, verbose_name=b'id', primary_key=True)),
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
                ('setid', models.ForeignKey(to='spl.SetInfo')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.RenameModel(
            old_name='SPLSource',
            new_name='Source',
        ),
    ]
