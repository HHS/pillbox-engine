# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pillbox', '0017_auto_20141218_1543'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pillboxdata',
            name='application_number',
            field=models.CharField(max_length=250, null=True, verbose_name=b'application_number', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pillboxdata',
            name='dea_schedule_code',
            field=models.CharField(max_length=250, null=True, verbose_name=b'dea_schedule_code', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pillboxdata',
            name='dea_schedule_name',
            field=models.CharField(max_length=250, null=True, verbose_name=b'dea_schedule_name', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pillboxdata',
            name='from_sis',
            field=models.CharField(max_length=250, null=True, verbose_name=b'epc_match', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pillboxdata',
            name='has_image',
            field=models.BooleanField(default=False, verbose_name=b'has_image'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pillboxdata',
            name='image_source',
            field=models.CharField(max_length=250, null=True, verbose_name=b'image_source', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pillboxdata',
            name='laberer_code',
            field=models.CharField(max_length=250, null=True, verbose_name=b'laberer_code', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pillboxdata',
            name='marketing_act_code',
            field=models.CharField(max_length=250, null=True, verbose_name=b'marketing_act_code', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pillboxdata',
            name='pillbox_color_text',
            field=models.CharField(max_length=250, null=True, verbose_name=b'pillbox_color_text', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pillboxdata',
            name='pillbox_imprint',
            field=models.CharField(max_length=250, null=True, verbose_name=b'pillbox_imprint', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pillboxdata',
            name='pillbox_score',
            field=models.CharField(max_length=250, null=True, verbose_name=b'pillbox_score', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pillboxdata',
            name='pillbox_shape_text',
            field=models.CharField(max_length=250, null=True, verbose_name=b'pillbox_shape_text', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pillboxdata',
            name='pillbox_size',
            field=models.CharField(max_length=250, null=True, verbose_name=b'pillbox_size', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pillboxdata',
            name='produce_code',
            field=models.CharField(max_length=250, null=True, verbose_name=b'product_code', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pillboxdata',
            name='rxstring',
            field=models.TextField(null=True, verbose_name=b'rxtty', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pillboxdata',
            name='rxtty',
            field=models.TextField(null=True, verbose_name=b'rxtty', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pillboxdata',
            name='setid',
            field=models.CharField(unique=True, max_length=250, verbose_name=b'spp'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pillboxdata',
            name='setid_product',
            field=models.CharField(max_length=250, verbose_name=b'setid'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pillboxdata',
            name='spl_inactive_ing',
            field=models.TextField(null=True, verbose_name=b'spl_inactive_ing', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pillboxdata',
            name='spl_ingredients',
            field=models.TextField(null=True, verbose_name=b'spl_ingredients', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pillboxdata',
            name='spl_strength',
            field=models.TextField(null=True, verbose_name=b'spl_strength', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pillboxdata',
            name='splcolor',
            field=models.CharField(max_length=250, null=True, verbose_name=b'splcolor', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pillboxdata',
            name='splcolor_text',
            field=models.CharField(max_length=250, null=True, verbose_name=b'splcolor_text', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pillboxdata',
            name='splimage',
            field=models.FileField(max_length=250, upload_to=b'pillbox', null=True, verbose_name=b'splimage', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pillboxdata',
            name='splimprint',
            field=models.CharField(max_length=250, null=True, verbose_name=b'splimprint', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pillboxdata',
            name='splscore',
            field=models.CharField(max_length=250, null=True, verbose_name=b'splscore', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pillboxdata',
            name='splshape',
            field=models.CharField(max_length=250, null=True, verbose_name=b'splshape', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pillboxdata',
            name='splshape_text',
            field=models.CharField(max_length=250, null=True, verbose_name=b'splshape_text', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pillboxdata',
            name='splsize',
            field=models.CharField(max_length=250, null=True, verbose_name=b'splsize', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pillboxdata',
            name='version_number',
            field=models.CharField(max_length=250, null=True, verbose_name=b'version_number', blank=True),
            preserve_default=True,
        ),
    ]
