# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-08 16:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0016_auto_20160504_1509'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='about',
            field=models.TextField(blank=True, max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='address',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
    ]
