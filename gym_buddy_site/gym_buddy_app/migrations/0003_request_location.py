# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-14 06:03
from __future__ import unicode_literals

from django.db import migrations
import geoposition.fields


class Migration(migrations.Migration):

    dependencies = [
        ('gym_buddy_app', '0002_auto_20161214_0048'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='location',
            field=geoposition.fields.GeopositionField(blank=True, max_length=42),
        ),
    ]
