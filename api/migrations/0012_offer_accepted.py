# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-23 20:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_auto_20160421_2046'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='accepted',
            field=models.NullBooleanField(),
        ),
    ]
