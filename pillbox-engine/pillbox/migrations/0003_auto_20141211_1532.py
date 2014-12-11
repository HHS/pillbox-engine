# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pillbox', '0002_auto_20141210_2159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pillboxdata',
            name='application_number',
            field=models.CharField(max_length=250, null=True, verbose_name=b'Application Number', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pillboxdata',
            name='clinical_setid',
            field=models.CharField(max_length=250, null=True, verbose_name=b'Clinical Set ID', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pillboxdata',
            name='from_sis',
            field=models.CharField(max_length=250, null=True, verbose_name=b'From SIS', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pillboxdata',
            name='image_id',
            field=models.CharField(max_length=250, null=True, verbose_name=b'Image Name', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pillboxdata',
            name='laberer_code',
            field=models.CharField(max_length=250, null=True, verbose_name=b'Laberer Code', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pillboxdata',
            name='new',
            field=models.BooleanField(default=False, verbose_name=b'Just added from SPL (New)'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pillboxdata',
            name='physical_characteristics',
            field=models.CharField(max_length=250, null=True, verbose_name=b'Physical Characteristics', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pillboxdata',
            name='stale',
            field=models.BooleanField(default=True, verbose_name=b'Does not exist on SPL (Stale)'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pillboxdata',
            name='unii_code',
            field=models.CharField(max_length=250, null=True, verbose_name=b'UNII Code', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pillboxdata',
            name='updated',
            field=models.BooleanField(default=False, verbose_name=b'Is updated from SPL?'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pillboxdata',
            name='version_number',
            field=models.CharField(max_length=250, null=True, verbose_name=b'Version Number', blank=True),
            preserve_default=True,
        ),
    ]
