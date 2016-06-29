# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-17 19:46
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WorldBorder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('pop_est', models.IntegerField(verbose_name='Population estimate')),
                ('fips', models.CharField(max_length=3, verbose_name='FIPS Code')),
                ('iso2', models.CharField(max_length=5, verbose_name='2 Digit ISO')),
                ('iso3', models.CharField(max_length=3, verbose_name='3 Digit ISO')),
                ('un', models.IntegerField(verbose_name='United Nations Code')),
                ('region', models.CharField(max_length=23, verbose_name='Region Code')),
                ('subregion', models.CharField(max_length=25, verbose_name='Sub-Region Code')),
                ('mpoly', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
            ],
        ),
    ]
