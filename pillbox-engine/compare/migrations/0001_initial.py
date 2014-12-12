# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pillbox', '0003_auto_20141211_1532'),
        ('spl', '0004_auto_20141212_1142'),
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('spl_value', models.CharField(max_length=200, verbose_name=b'SPL Value')),
                ('pillbox_value', models.CharField(max_length=200, verbose_name=b'Pillbox Value')),
                ('is_different', models.BooleanField(default=False, verbose_name=b'Is Different?')),
                ('reason', models.TextField(null=True, verbose_name=b'Reason', blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('pillbox', models.ForeignKey(to='pillbox.PillBoxData')),
                ('spl', models.ForeignKey(to='spl.Pill')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('spl_value', models.CharField(max_length=200, verbose_name=b'SPL Value')),
                ('pillbox_value', models.CharField(max_length=200, verbose_name=b'Pillbox Value')),
                ('is_different', models.BooleanField(default=False, verbose_name=b'Is Different?')),
                ('reason', models.TextField(null=True, verbose_name=b'Reason', blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('pillbox', models.ForeignKey(to='pillbox.PillBoxData')),
                ('spl', models.ForeignKey(to='spl.Pill')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Imprint',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('spl_value', models.CharField(max_length=200, verbose_name=b'SPL Value')),
                ('pillbox_value', models.CharField(max_length=200, verbose_name=b'Pillbox Value')),
                ('is_different', models.BooleanField(default=False, verbose_name=b'Is Different?')),
                ('reason', models.TextField(null=True, verbose_name=b'Reason', blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('pillbox', models.ForeignKey(to='pillbox.PillBoxData')),
                ('spl', models.ForeignKey(to='spl.Pill')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('spl_value', models.CharField(max_length=200, verbose_name=b'SPL Value')),
                ('pillbox_value', models.CharField(max_length=200, verbose_name=b'Pillbox Value')),
                ('is_different', models.BooleanField(default=False, verbose_name=b'Is Different?')),
                ('reason', models.TextField(null=True, verbose_name=b'Reason', blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('pillbox', models.ForeignKey(to='pillbox.PillBoxData')),
                ('spl', models.ForeignKey(to='spl.Pill')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Shape',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('spl_value', models.CharField(max_length=200, verbose_name=b'SPL Value')),
                ('pillbox_value', models.CharField(max_length=200, verbose_name=b'Pillbox Value')),
                ('is_different', models.BooleanField(default=False, verbose_name=b'Is Different?')),
                ('reason', models.TextField(null=True, verbose_name=b'Reason', blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('pillbox', models.ForeignKey(to='pillbox.PillBoxData')),
                ('spl', models.ForeignKey(to='spl.Pill')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('spl_value', models.CharField(max_length=200, verbose_name=b'SPL Value')),
                ('pillbox_value', models.CharField(max_length=200, verbose_name=b'Pillbox Value')),
                ('is_different', models.BooleanField(default=False, verbose_name=b'Is Different?')),
                ('reason', models.TextField(null=True, verbose_name=b'Reason', blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('pillbox', models.ForeignKey(to='pillbox.PillBoxData')),
                ('spl', models.ForeignKey(to='spl.Pill')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
