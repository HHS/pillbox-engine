# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pillbox', '0004_auto_20141202_2023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='characteristic',
            name='pillbox_value',
            field=models.CharField(max_length=250, verbose_name=b'Pillbox Value'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='characteristic',
            name='spl_value',
            field=models.CharField(max_length=250, verbose_name=b'SPL Value'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pillboxdata',
            name='application_number',
            field=models.CharField(max_length=250, null=True, verbose_name=b'MARKETING_ACT_CODE', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pillboxdata',
            name='approval_code',
            field=models.CharField(max_length=250, null=True, verbose_name=b'approval_code', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pillboxdata',
            name='author',
            field=models.CharField(max_length=250, null=True, verbose_name=b'author', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pillboxdata',
            name='author_type',
            field=models.CharField(max_length=250, null=True, verbose_name=b'author_type', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pillboxdata',
            name='clinical_setid',
            field=models.CharField(max_length=250, null=True, verbose_name=b'MARKETING_ACT_CODE', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pillboxdata',
            name='dea_schedule_code',
            field=models.CharField(max_length=250, null=True, verbose_name=b'DEA_SCHEDULE_CODE', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pillboxdata',
            name='dea_schedule_name',
            field=models.CharField(max_length=250, null=True, verbose_name=b'DEA_SCHEDULE_NAME', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pillboxdata',
            name='document_type',
            field=models.CharField(max_length=250, null=True, verbose_name=b'document_type', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pillboxdata',
            name='dosage_form',
            field=models.CharField(max_length=250, null=True, verbose_name=b'dosage_form', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pillboxdata',
            name='effective_time',
            field=models.CharField(max_length=250, null=True, verbose_name=b'effective_time', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pillboxdata',
            name='equal_product_code',
            field=models.CharField(max_length=250, null=True, verbose_name=b'equal_product_code', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pillboxdata',
            name='file_name',
            field=models.CharField(max_length=250, null=True, verbose_name=b'file_name', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pillboxdata',
            name='from_sis',
            field=models.CharField(max_length=250, null=True, verbose_name=b'MARKETING_ACT_CODE', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pillboxdata',
            name='has_image',
            field=models.CharField(max_length=250, null=True, verbose_name=b'MARKETING_ACT_CODE', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pillboxdata',
            name='image_id',
            field=models.CharField(max_length=250, null=True, verbose_name=b'MARKETING_ACT_CODE', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pillboxdata',
            name='image_source',
            field=models.CharField(max_length=250, null=True, verbose_name=b'Image Source', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pillboxdata',
            name='laberer_code',
            field=models.CharField(max_length=250, null=True, verbose_name=b'MARKETING_ACT_CODE', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pillboxdata',
            name='marketing_act_code',
            field=models.CharField(max_length=250, null=True, verbose_name=b'MARKETING_ACT_CODE', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pillboxdata',
            name='medicine_name',
            field=models.CharField(max_length=250, null=True, verbose_name=b'medicine_name', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pillboxdata',
            name='ndc9',
            field=models.CharField(max_length=250, null=True, verbose_name=b'ndc9', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pillboxdata',
            name='part_medicine_name',
            field=models.CharField(max_length=250, null=True, verbose_name=b'part_medicine_name', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pillboxdata',
            name='part_num',
            field=models.CharField(max_length=250, null=True, verbose_name=b'part_num', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pillboxdata',
            name='physical_characteristics',
            field=models.CharField(max_length=250, null=True, verbose_name=b'MARKETING_ACT_CODE', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pillboxdata',
            name='produce_code',
            field=models.CharField(max_length=250, null=True, verbose_name=b'produce_code', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pillboxdata',
            name='rxcui',
            field=models.CharField(max_length=250, null=True, verbose_name=b'rxcui', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pillboxdata',
            name='rxstring',
            field=models.CharField(max_length=250, null=True, verbose_name=b'rxttystring', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pillboxdata',
            name='rxtty',
            field=models.CharField(max_length=250, null=True, verbose_name=b'rxtty', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pillboxdata',
            name='setid',
            field=models.CharField(max_length=250, serialize=False, verbose_name=b'setid', primary_key=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pillboxdata',
            name='setid_product',
            field=models.CharField(max_length=250, verbose_name=b'setid_product'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pillboxdata',
            name='source',
            field=models.CharField(max_length=250, null=True, verbose_name=b'source', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pillboxdata',
            name='spl_inactive_ing',
            field=models.CharField(max_length=250, null=True, verbose_name=b'SPL_INACTIVE_ING', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pillboxdata',
            name='spl_ingredients',
            field=models.CharField(max_length=250, null=True, verbose_name=b'SPL_INGREDIENTS', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pillboxdata',
            name='spl_strength',
            field=models.CharField(max_length=250, null=True, verbose_name=b'SPL_STRENGTH', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pillboxdata',
            name='splcolor',
            field=models.CharField(max_length=250, null=True, verbose_name=b'SPLCOLOR', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pillboxdata',
            name='splimprint',
            field=models.CharField(max_length=250, null=True, verbose_name=b'SPLIMPRINT', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pillboxdata',
            name='splscore',
            field=models.CharField(max_length=250, null=True, verbose_name=b'SPLSCORE', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pillboxdata',
            name='splshape',
            field=models.CharField(max_length=250, null=True, verbose_name=b'SPLSHAPE', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pillboxdata',
            name='splsize',
            field=models.CharField(max_length=250, null=True, verbose_name=b'SPLSIZE', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pillboxdata',
            name='unii_code',
            field=models.CharField(max_length=250, null=True, verbose_name=b'MARKETING_ACT_CODE', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pillboxdata',
            name='version_number',
            field=models.CharField(max_length=250, null=True, verbose_name=b'MARKETING_ACT_CODE', blank=True),
            preserve_default=True,
        ),
    ]
